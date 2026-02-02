# Quick Start Guide

## 🚀 Quick Setup (2 minutes)

### On SERVER Machine (The one you want to control):

**Windows - Method 1 (Easiest):**
1. Double-click `start_server.bat`
2. It will automatically install packages and start
3. Note the IP address: `http://192.168.x.x:5000`

**Windows - Method 2 (If Method 1 fails):**
1. Right-click `install_packages.py`
2. Select "Open with Python"
3. Wait for it to finish
4. Then run `start_server.bat`

**macOS/Linux:**
1. Open Terminal in this folder
2. Run: `bash start_server.sh`
3. Note the IP address shown

### On CLIENT Machine (The one controlling):

1. Open any web browser (Chrome, Firefox, Edge, Safari)
2. Type the URL from server (e.g., `http://192.168.1.100:5000`)
3. Press Enter
4. You should see the remote screen!
5. Use mouse, keyboard buttons, and text input to control

---

## What You Can Do

✅ See the remote screen in real-time  
✅ Move the mouse  
✅ Click (left, right, middle, double-click)  
✅ Type text  
✅ Press any keyboard key  
✅ Adjust refresh rate for performance  
✅ Pause and resume streaming  

---

## Common Issues & Quick Fixes

| Problem | Solution |
|---------|----------|
| "Cannot find server" | Check IP address, verify WiFi connection |
| "Connection refused" | Make sure server is running on port 5000 |
| Screen not updating | Refresh browser (Ctrl+R), lower FPS setting |
| Mouse/keyboard not working | Close and reopen browser tab |
| Installation stuck | Use `install_packages.py` instead of batch file |
| Python not found | Install Python from python.org |
| Permission denied on macOS/Linux | Run: `chmod +x start_server.sh` |

---

## Installation Fails? Try These:

### Option 1: Use Alternative Installer (Recommended)
```
python install_packages.py
```
This is more robust and better at retrying failed installations.

### Option 2: Manual Installation in PowerShell
```powershell
pip install flask==2.3.3
pip install flask-cors==4.0.0
pip install Pillow==10.0.0
pip install pynput==1.7.6
```

### Option 3: Use Alternative PyPI Mirror
If downloads are slow/failing, use Alibaba's mirror:
```
pip install -i https://mirrors.aliyun.com/pypi/simple/ flask==2.3.3
pip install -i https://mirrors.aliyun.com/pypi/simple/ flask-cors==4.0.0
pip install -i https://mirrors.aliyun.com/pypi/simple/ Pillow==10.0.0
pip install -i https://mirrors.aliyun.com/pypi/simple/ pynput==1.7.6
```

---

## File Structure

```
remote-access-app/
├── server.py                  # Main server application
├── install_packages.py        # Alternative installer
├── requirements.txt           # Python dependencies list
├── start_server.bat           # Windows launcher (UPDATED)
├── start_server.sh            # macOS/Linux launcher
├── README.md                  # Full documentation
├── QUICKSTART.md              # This file
└── templates/
    └── client.html            # Web client interface
```

---

## Advanced Usage

### Run on Custom Port
Edit `server.py` and change:
```python
PORT = 5000  # Change this number
```

### Adjust Screen Quality
Edit `server.py` and change:
```python
screen_quality = 60  # 1-95 (higher = better but slower)
```

### Find Your Server IP

**Windows:**
```bash
ipconfig
```
Look for "IPv4 Address" under your WiFi connection

**macOS/Linux:**
```bash
ifconfig
```
Look for "inet" under your WiFi interface

---

## Security Reminder

⚠️ This app is for **local network only**  
- Use on trusted WiFi only
- Don't expose to the internet without proper security
- No password protection by default - add if needed for production

---

**Questions?** See README.md for detailed documentation
