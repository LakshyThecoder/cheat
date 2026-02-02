# VALNDOR - QUICK START GUIDE

## 🎯 What is Valndor?

**Valndor** is a hidden remote control system that lets other people control your computer from theirs - even if they're in another room or building (as long as you're on the same WiFi).

---

## ⚡ 3-STEP SETUP

### STEP 1: Start Valndor on Your Machine
```
Double-click → Valndor.bat
↓
Window hides automatically
↓
Server is now running in background
```

### STEP 2: Find Your IP Address
```
Double-click → find_my_ip.bat
↓
It shows your IP (like 192.168.1.100)
↓
Copy and share this IP with other person
```

### STEP 3: They Connect From Their Machine
```
Open Browser (Chrome, Firefox, etc)
↓
Type: http://192.168.1.100:5000
↓
Press Enter
↓
They can now control your computer!
```

---

## 📋 File Guide

| File | Purpose |
|------|---------|
| **Valndor.bat** | Run this! Starts hidden server |
| **find_my_ip.bat** | Click to find your IP address |
| **create_shortcut.bat** | Creates desktop shortcut |
| **start_server.bat** | Old launcher (shows window) |

---

## 🎮 What They Can Do

Once connected, they can:
- ✅ See your screen
- ✅ Move your mouse
- ✅ Click buttons
- ✅ Type text
- ✅ Press keyboard keys

---

## ⏹️ How to Stop It

Press these keys together:
```
Ctrl + Shift + Esc
```

This opens **Task Manager**:
1. Find `python.exe`
2. Click it
3. Click "End Task"

Done! Server stops.

---

## 🔍 Example Usage

**Your Situation:**
```
Your PC at Home (Server)
    ↓
    ↓ WiFi
    ↓
Friend's Phone/Laptop (Client)
```

**What Happens:**
1. You run `Valndor.bat` → Server starts hidden
2. You tell friend: "Connect to 192.168.1.100:5000"
3. Friend opens browser on their device → Types that address
4. Friend sees YOUR screen
5. Friend controls YOUR mouse & keyboard
6. You see friend moving your cursor! 

---

## ❓ Common Questions

**Q: Where's the window?**  
A: It's hidden! That's the whole point. It runs silently in background.

**Q: How do I see the IP?**  
A: Click `find_my_ip.bat`

**Q: Is it safe?**  
A: Only give the IP to people you trust. Use on your home/work WiFi only.

**Q: Can multiple people control it?**  
A: Yes, but one at a time (they'll see the same screen).

**Q: What if I lose the IP?**  
A: Click `find_my_ip.bat` again to find it.

---

## 🚀 Pro Tips

**Make it start automatically:**
1. Click `create_shortcut.bat`
2. A Valndor icon appears on your Desktop
3. You can also move it to Startup folder for auto-start on boot

**Find IP from PowerShell:**
```powershell
ipconfig
```
Look for "IPv4 Address" under your WiFi

**Change the port (advanced):**
Edit `server.py` and change `PORT = 5000` to another number

---

## 🆘 Quick Troubleshooting

| Issue | Fix |
|-------|-----|
| They can't connect | Check IP is correct, both on same WiFi |
| Screen not showing | Have them refresh browser (Ctrl+R) |
| Mouse/keyboard slow | Lower FPS in browser settings (1-10) |
| Can't stop it | Ctrl+Shift+Esc → Task Manager → End python.exe |
| Doesn't start | Make sure Python is installed |

---

## 📞 Support

For detailed help, see:
- `VALNDOR_GUIDE.md` - Full documentation
- `README.md` - Technical details

---

**Version:** Valndor 1.0  
**Status:** Silent & Running  
**Made:** February 2026
