"""
Remote Access Server - Runs on the machine to be controlled
Captures screen and receives remote input commands
"""

import socket
import threading
import time
import io
import os
import json
import subprocess
import platform
import base64
import ipaddress
import sys
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Check if this is the hidden subprocess
is_hidden = "--hidden" in sys.argv

if not is_hidden:
    # Ask user if they want to hide
    print("\n" + "="*60)
    print("VALNDOR - REMOTE ACCESS SERVER")
    print("="*60)
    print("\nDo you want to run HIDDEN?")
    print("\nY = Yes, hide from taskbar (run in background)")
    print("N = No, show the window")
    print()
    choice = input("Enter your choice (Y/N): ").strip().upper()

    if choice == "Y":
        print("\nStarting in HIDDEN mode...")
        print("To stop: Ctrl+Shift+Esc → End pythonw.exe\n")
        
        # Relaunch this script using pythonw.exe (no console) with --hidden flag
        script_path = os.path.abspath(__file__)
        subprocess.Popen([sys.executable.replace("python.exe", "pythonw.exe"), script_path, "--hidden"])
        sys.exit(0)
    
    elif choice == "N":
        print("\nStarting in VISIBLE mode...\n")
    else:
        print("\nInvalid choice. Starting in VISIBLE mode...\n")

try:
    from PIL import ImageGrab
except ImportError:
    print("WARNING: Pillow not installed. Screen capture will be limited.")
    ImageGrab = None

try:
    from pynput.mouse import Controller as MouseController, Button
    from pynput.keyboard import Controller as KeyboardController, Key
    PYNPUT_AVAILABLE = True
except ImportError:
    print("WARNING: pynput not installed. Using ctypes fallback.")
    PYNPUT_AVAILABLE = False
    import ctypes
    import time as pynput_time

app = Flask(__name__, template_folder='ValndorClientSide')
CORS(app)

# Configuration
HOST = '0.0.0.0'
PORT = 5000
screen_quality = 60  # JPEG quality (1-95)
fps = 10  # Frames per second

# Global variables
server_active = True
client_connected = False
last_screenshot = None

def get_ipv4_candidates():
    candidates = []

    # UDP socket trick (gets primary route IP)
    for target in [("8.8.8.8", 80), ("1.1.1.1", 80)]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(target)
            candidates.append(s.getsockname()[0])
        except Exception:
            pass
        finally:
            try:
                s.close()
            except Exception:
                pass

    # Hostname resolution
    try:
        hostname = socket.gethostname()
        for info in socket.getaddrinfo(hostname, None):
            candidates.append(info[4][0])
    except Exception:
        pass

    # Windows ipconfig fallback
    if platform.system().lower().startswith('win'):
        try:
            output = subprocess.check_output(["ipconfig"], text=True, encoding="utf-8", errors="ignore")
            for line in output.splitlines():
                if "IPv4 Address" in line or "IPv4 Address." in line:
                    parts = line.split(":")
                    if len(parts) > 1:
                        ip = parts[-1].strip()
                        candidates.append(ip)
        except Exception:
            pass

    # De-duplicate while preserving order
    seen = set()
    uniq = []
    for ip in candidates:
        if ip not in seen:
            seen.add(ip)
            uniq.append(ip)
    return uniq

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        def is_preferred(ip_str):
            try:
                ip = ipaddress.ip_address(ip_str)
            except ValueError:
                return False
            if ip.version != 4:
                return False
            # Prefer RFC1918 private ranges, exclude CGNAT 100.64.0.0/10
            if ip.is_private and not ipaddress.ip_network("100.64.0.0/10").supernet_of(ipaddress.ip_network(f"{ip}/32")):
                return True
            return False

        candidates = get_ipv4_candidates()

        # Choose best candidate
        for ip in candidates:
            if is_preferred(ip):
                return ip

        # Fallback: first non-loopback IPv4
        for ip in candidates:
            try:
                addr = ipaddress.ip_address(ip)
                if addr.version == 4 and not addr.is_loopback:
                    return ip
            except ValueError:
                continue

        return "127.0.0.1"
    except Exception:
        return "127.0.0.1"

def capture_screen():
    """Capture current screen as JPEG bytes"""
    try:
        # Capture the screen
        screenshot = ImageGrab.grab()
        
        # Reduce size for faster transmission (optional)
        # Uncomment to reduce by 50%
        # screenshot = screenshot.resize((screenshot.width // 2, screenshot.height // 2))
        
        # Convert to JPEG bytes
        img_io = io.BytesIO()
        screenshot.save(img_io, format='JPEG', quality=screen_quality)
        img_io.seek(0)
        return img_io.getvalue()
    except Exception as e:
        print(f"Screenshot error: {e}")
        return None

def mouse_move(x, y):
    """Move mouse to coordinates"""
    try:
        if PYNPUT_AVAILABLE:
            mouse = MouseController()
            mouse.position = (x, y)
        else:
            # Windows ctypes fallback
            ctypes.windll.user32.SetCursorPos(int(x), int(y))
    except Exception as e:
        print(f"Mouse move error: {e}")

def mouse_click(button='left'):
    """Click mouse"""
    try:
        if PYNPUT_AVAILABLE:
            mouse = MouseController()
            if button == 'left':
                mouse.click(Button.left)
            elif button == 'right':
                mouse.click(Button.right)
            elif button == 'middle':
                mouse.click(Button.middle)
            elif button == 'double':
                mouse.click(Button.left, 2)
        else:
            # Windows ctypes fallback
            if button == 'left':
                ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # LEFT DOWN
                ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # LEFT UP
            elif button == 'right':
                ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0)  # RIGHT DOWN
                ctypes.windll.user32.mouse_event(16, 0, 0, 0, 0)  # RIGHT UP
            elif button == 'double':
                ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
                ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
                pynput_time.sleep(0.05)
                ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
                ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    except Exception as e:
        print(f"Mouse click error: {e}")

def type_text(text):
    """Type text"""
    try:
        if PYNPUT_AVAILABLE:
            keyboard = KeyboardController()
            keyboard.type(text)
        else:
            # ctypes fallback - limited support
            for char in text:
                if char.isalnum() or char in ' .,!?':
                    # Windows VK codes for basic characters
                    pass
    except Exception as e:
        print(f"Type text error: {e}")

def key_press(key):
    """Press a key"""
    try:
        if PYNPUT_AVAILABLE:
            keyboard = KeyboardController()
            key_map = {
                'escape': Key.esc,
                'return': Key.enter,
                'enter': Key.enter,
                'tab': Key.tab,
                'backspace': Key.backspace,
                'delete': Key.delete,
                'home': Key.home,
                'end': Key.end,
                'pageup': Key.page_up,
                'pagedown': Key.page_down,
                'up': Key.up,
                'down': Key.down,
                'left': Key.left,
                'right': Key.right,
                'f5': Key.f5,
                'space': Key.space,
            }
            if key in key_map:
                keyboard.press(key_map[key])
                keyboard.release(key_map[key])
    except Exception as e:
        print(f"Key press error: {e}")

@app.route('/')
def index():
    """Serve the web interface"""
    return render_template('client.html')

@app.route('/api/screen', methods=['GET'])
def get_screen():
    """Stream screen capture as base64 image"""
    try:
        screenshot_bytes = capture_screen()
        if screenshot_bytes:
            screenshot_b64 = base64.b64encode(screenshot_bytes).decode('utf-8')
            return jsonify({'image': screenshot_b64, 'success': True})
        return jsonify({'success': False, 'error': 'Screenshot failed'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/mouse/move', methods=['POST'])
def handle_mouse_move():
    """Handle mouse movement"""
    try:
        data = request.json
        x, y = data.get('x'), data.get('y')
        mouse_move(int(x), int(y))
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/mouse/click', methods=['POST'])
def handle_mouse_click():
    """Handle mouse click"""
    try:
        data = request.json
        button = data.get('button', 'left')
        mouse_click(button)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/keyboard/type', methods=['POST'])
def handle_type():
    """Handle keyboard typing"""
    try:
        data = request.json
        text = data.get('text', '')
        type_text(text)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/keyboard/key', methods=['POST'])
def handle_key():
    """Handle keyboard key press"""
    try:
        data = request.json
        key = data.get('key', '')
        key_press(key)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/info', methods=['GET'])
def get_info():
    """Get server information"""
    try:
        local_ip = get_local_ip()
        hostname = socket.gethostname()
        system = platform.system()
        return jsonify({
            'ip': local_ip,
            'port': PORT,
            'hostname': hostname,
            'system': system,
            'connected': True
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def print_server_info():
    """Print server connection info"""
    local_ip = get_local_ip()
    all_ips = get_ipv4_candidates()
    print("\n" + "="*60)
    print("🖥️  VALNDOR - REMOTE ACCESS SERVER STARTED")
    print("="*60)
    print(f"Local IP: {local_ip}")
    if all_ips:
        print(f"All IPv4: {', '.join(all_ips)}")
    print(f"Port: {PORT}")
    print(f"URL: http://{local_ip}:{PORT}")
    print(f"Hostname: {socket.gethostname()}")
    print("\nInstructions:")
    print(f"1. On the client machine, visit: http://{local_ip}:{PORT}")
    print("2. Make sure both machines are on the same WiFi network")
    print("3. To stop the server, use Task Manager (Ctrl+Shift+Esc)")
    print("   and end the Python process")
    print("="*60 + "\n")

if __name__ == '__main__':
    try:
        print_server_info()
        app.run(host=HOST, port=PORT, debug=False, threaded=True)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Error: {e}")
