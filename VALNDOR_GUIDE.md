# Valndor - Remote Access Application

**The Hidden Remote Desktop Control System**

## 🚀 Quick Start (30 seconds)

### On Your Machine (Server):

1. **Double-click** `Valndor.bat`
2. The window will **hide automatically**
3. Look at system tray or use the IP finder below to get your IP
4. **Share the IP** with the person who wants to control your machine

### On Their Machine (Client):

1. Open any web browser
2. Type: `http://YOUR_IP:5000`
3. They can now **control your computer!**

---

## 📍 Finding Your IP Address

Since the server hides, use this to find your IP:

**Option 1: PowerShell**
```powershell
ipconfig
```
Look for "IPv4 Address" under your WiFi connection (192.168.x.x)

**Option 2: Check Files Created**
When Valndor starts, it creates a log file with your IP

---

## ⏹️ Stopping Valndor

Since it runs hidden, stop it using **Task Manager**:

1. Press: `Ctrl + Shift + Esc` (or `Ctrl + Alt + Delete`)
2. Look for `python.exe` or `Valndor`
3. Right-click → **End Task**

---

## 🔧 How It Works

- **Valndor.bat** → Installs packages silently → Starts server hidden
- Server runs in background listening for connections
- Other users visit `http://YOUR_IP:5000` in their browser
- They can control your mouse, keyboard, and see your screen
- Only stops when you kill it in Task Manager

---

## 📱 What They Can Control

✅ **Mouse:** Move, click, double-click, right-click  
✅ **Keyboard:** Type text, press any key  
✅ **Screen:** See your desktop in real-time  
✅ **Adjustable Speed:** 1-30 FPS based on connection  

---

## 🔒 Security Notes

⚠️ **HIDDEN MODE WARNING:**
- The server runs silently - only you/admin can stop it via Task Manager
- Make sure you trust the people you give the IP to
- Use on trusted WiFi networks only

---

## 📝 Troubleshooting

| Problem | Solution |
|---------|----------|
| They can't connect | Check IP address is correct, verify same WiFi |
| Can't stop it | Open Task Manager (Ctrl+Shift+Esc), find python.exe, End Task |
| Doesn't start | Check Python is installed, try `Valndor.bat` again |
| Screen not updating | Have them refresh browser (Ctrl+R) |

---

## 🎯 Advanced: Make It Start on Boot

To have Valndor start automatically when you log in:

1. Press `Win + R`
2. Type: `shell:startup`
3. Press Enter
4. Copy `Valndor.bat` into this folder
5. Now it starts hidden every time you boot!

---

## 📂 Files Included

```
Valndor/
├── Valndor.bat              ← Run this (HIDDEN)
├── server.py                ← Server code
├── start_server.bat         ← Regular launcher (shows window)
├── install_packages.py      ← Alternative installer
├── requirements.txt         ← Python packages
└── templates/
    └── client.html          ← Web interface
```

---

## ✨ Version Info

**Valndor v1.0** - The Silent Remote Control  
Created: February 2026  
Status: Hidden & Running

---

**Questions?** Check README.md for full documentation
