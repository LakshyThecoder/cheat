

# Vanldor Remote Access Application

Valndor is a lightweight, browser-based remote access tool for controlling a computer over a local WiFi network.
Designed for simplicity, low latency, and ease of deployment using Python and a web interface.

---

## Table of Contents

* Overview
* Architecture
* System Requirements
* Installation
* Usage

  * Server Setup
  * Client Access
* Features
* Performance Optimization
* Troubleshooting
* Security Considerations
* Running as a Background Service (Windows)
* Configuration
* Stopping the Application
* License

---

## Overview

This application enables remote screen viewing and input control (mouse and keyboard) between two machines connected to the same local network.

* **Server**: The machine being controlled
* **Client**: Any device with a modern web browser

No client-side installation is required beyond a browser.

---

## Architecture

* Python-based backend server
* Web-based client interface
* Real-time screen streaming
* Event-driven mouse and keyboard input forwarding
* Local network (LAN) communication only

---

## System Requirements

* Python **3.7+**
* Windows, macOS, or Linux
* Both devices connected to the **same WiFi or LAN**
* Modern web browser (Chrome, Firefox, Edge, Safari)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/remote-access-app.git
cd remote-access-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Server Setup (Controlled Machine)

1. Open a terminal or command prompt
2. Navigate to the project directory
3. Start the server:

```bash
python server.py
```

4. The server will display connection details:

```
============================================================
REMOTE ACCESS SERVER STARTED
============================================================
Local IP: 192.168.x.x
Port: 5000
URL: http://192.168.x.x:5000
Hostname: YOUR-PC-NAME
============================================================
```

Make a note of the **Local IP address**.

---

### Client Access (Controlling Machine)

1. Open a web browser
2. Enter the server URL:

```
http://192.168.x.x:5000
```

3. The remote control interface will load automatically

From here, you can view the remote screen and control the system in real time.

---

## Features

### Screen Sharing

* Live screen capture
* Adjustable frame rate (1–30 FPS)
* Pause and resume streaming
* FPS and latency indicators

### Mouse Control

* Real-time cursor movement
* Left, right, middle, and double click support

### Keyboard Control

* Remote text input
* Special keys:

  * Enter, Escape, Tab
  * Backspace, Delete
  * Arrow keys
  * Home, End, Page Up, Page Down

### Connection Information

* Connected hostname
* Operating system detection
* Live connection status

---

## Performance Optimization

### Slower Networks

* Reduce FPS to 5–10
* Lower server screen resolution
* Close bandwidth-heavy applications

### Faster Networks

* Increase FPS up to 30
* Keep auto-refresh enabled
* Use wired Ethernet when possible

---

## Troubleshooting

### Connection Refused

* Ensure the server is running
* Confirm both devices are on the same network
* Verify the IP address and port
* Check firewall rules for port `5000`

### Cannot Find Server

* Ping the server IP from the client machine
* Restart the server and retry
* Double-check network isolation settings on the router

### Screen Not Updating

* Lower FPS
* Refresh the browser page
* Verify auto-refresh is enabled

### Input Not Responding

* Reload the web interface
* Restart the server
* Check browser console for errors

---

## Security Considerations

This application is intended **only for trusted local networks**.

* No authentication is enabled by default
* Do not expose the server directly to the internet
* Use a VPN if remote access outside the LAN is required
* Add authentication and encryption before production use

---

## Running as a Background Service (Windows)

### 1. Create a Startup Script

Create a file named `start_server.bat`:

```batch
@echo off
python server.py
pause
```

### 2. Add to Startup Folder

Place a shortcut to the batch file in:

```
C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

The server will start automatically on login.

---

## Configuration

Edit `server.py` to customize:

* `HOST` – Bind to a specific IP address
* `PORT` – Change the default port (5000)
* `fps` – Default frame rate
* `screen_quality` – JPEG compression quality (1–95)

---

## Stopping the Application

### Server

Press `Ctrl + C` in the terminal

### Client

Close the browser tab

---

## License

MIT License
Free to use, modify, and distribute.

---

