# 🎓 WELCOME TO VALNDOR

## *"We Are The Saviors of Your Exam"* 📚✨

---

> **VALNDOR** is the ultimate **hidden remote control system** that lets other people take control of your computer remotely over WiFi. Whether you need help with your assignment, want to show someone your screen, or just need extra hands on your keyboard during crunch time - **Valndor has your back!**

### ⚡ *"When your exam is in 2 hours and your friend knows the answer"* 🚀

---

## 🚀 SUPER QUICK START (2 Minutes)

### ✅ YOUR COMPUTER (Server - Being Controlled)

```
1. Double-click → Valndor.bat
2. Window hides (it's working in background!)
3. Double-click → find_my_ip.bat
4. See your IP: 192.168.1.100 (or similar)
5. Share this IP with friend
```

### ✅ FRIEND'S COMPUTER (Client - Controlling)

```
1. Open browser (Chrome, Firefox, Edge, Safari)
2. Type in address bar: http://192.168.1.100:5000
3. Press Enter
4. See YOUR screen
5. Control YOUR mouse and keyboard
6. 🎉 THEY NOW CONTROL YOUR COMPUTER!
```

---

## 📋 WHAT YOUR FRIEND CAN DO

Once connected, they can:

- ✅ **See Your Screen** - Real-time desktop view
- ✅ **Move Mouse** - Click anywhere on your screen
- ✅ **Type Text** - Whatever they type appears on your keyboard
- ✅ **Press Keys** - Enter, Escape, Tab, Arrows, Function keys
- ✅ **Full Control** - They basically have a "remote hand" on your PC

### Perfect for:
- 📖 Getting help with homework
- 🎮 Playing games together
- 💼 Showing work to colleagues  
- 🔧 Tech support from friends
- 📚 Study sessions with classmates

---

## 📂 YOUR FILES EXPLAINED

| File | What It Does |
|------|-------------|
| **Valndor.bat** | 🎯 **MAIN FILE** - Starts hidden server |
| **find_my_ip.bat** | 🔍 Shows your IP address |
| **create_shortcut.bat** | 🎨 Creates desktop shortcut |
| **server.py** | 🔧 Backend code (don't touch) |
| **templates/client.html** | 🌐 Web interface code |
| **requirements.txt** | 📦 Python packages list |

---

## 🎯 COMPLETE SETUP GUIDE

### STEP 1️⃣: Start Valndor on YOUR Machine

```
Double-click: Valndor.bat
```

**What happens:**
- A terminal window opens briefly
- It says "Installing packages..." (if first time)
- Then the window **hides automatically**
- Server is now running in background ✓

**How to check if it's running:**
- Open Task Manager (Ctrl+Shift+Esc)
- Look for `python.exe` in the list
- If it's there = Valndor is running! ✓

---

### STEP 2️⃣: Find Your IP Address

```
Double-click: find_my_ip.bat
```

**A window pops up showing:**
```
IPv4 Address: 192.168.1.100
```

**Copy the number after "IPv4 Address"** (192.168.1.100 in this example)

**If that doesn't work, use PowerShell:**
```powershell
ipconfig
```
Find "IPv4 Address" under your WiFi connection

---

### STEP 3️⃣: Tell Your Friend the IP

Send them a message like:
```
"Connect to: http://192.168.1.100:5000"
```

Replace `192.168.1.100` with YOUR actual IP from Step 2

---

### STEP 4️⃣: They Connect (On Their Device)

**On THEIR computer:**

1. Open any web browser
2. Click the address bar
3. Paste/type: `http://192.168.1.100:5000`
4. Press **Enter**
5. They see YOUR screen loading...
6. **BOOM! They can now control your computer!**

---

## 🎮 WHEN THEY'RE CONNECTED

### Their Browser Shows:
- Your screen in the middle (big area)
- Control buttons on the right side
- FPS counter (speed of updates)
- Settings to adjust quality

### They Can:
- **Move mouse** - Just move their cursor, yours moves too
- **Click buttons** - Using "Left Click", "Right Click", etc.
- **Type text** - Use the text input box at bottom
- **Press keys** - Escape, Enter, Tab, Arrows, F5, etc.
- **Adjust speed** - Change FPS (1-30) for slow/fast networks

### You See:
- Your cursor moving on its own ✓
- Keyboard typing automatically ✓
- Your programs opening/closing ✓
- Everything they're controlling ✓

**It's like they have a remote control for your computer!**

---

## ⏹️ HOW TO STOP VALNDOR

Since it runs **hidden**, you need Task Manager to stop it:

### Method 1: Quick Keys
```
Press: Ctrl + Shift + Esc
```
This opens Task Manager instantly.

### Method 2: Alt+Tab Method
```
Press: Ctrl + Alt + Delete
Click: Task Manager
```

### In Task Manager:
1. Find `python.exe` in the list
2. Click on it (select it)
3. Click "End Task" button (bottom right)
4. **Server stops immediately!** ✓

---

## 🛠️ ADVANCED SETUP

### 🎨 Create Desktop Shortcut

Instead of navigating to Valndor.bat every time:

```
Double-click: create_shortcut.bat
```

A "Valndor" icon appears on your Desktop! Now you can:
- Click it to start
- Pin to taskbar
- Add to startup folder (auto-start on boot)

---

### 🔄 Auto-Start on Boot (Windows)

1. Click `create_shortcut.bat` first
2. Press `Win + R`
3. Type: `shell:startup`
4. Press Enter
5. Paste `Valndor.bat` into this folder
6. Now Valndor starts automatically every time you boot! ✓

---

### 📝 Change the Port (Advanced)

Edit `server.py` and find this line:
```python
PORT = 5000
```

Change `5000` to any number (like `8000`), then:
```
Tell your friend: http://192.168.1.100:8000
```

---

## ❓ COMMON QUESTIONS

### **Q: Where's the window? Is it running?**
**A:** It's hidden! Open Task Manager (Ctrl+Shift+Esc) and look for `python.exe`. If it's there, Valndor is running! ✓

---

### **Q: They can't connect, what do I do?**
**A:** Check:
1. Are you BOTH on same WiFi network? ← Most important!
2. Is the IP correct? (Run `find_my_ip.bat` again)
3. Is Valndor.bat still running? (Check Task Manager)
4. Ask them: Did they type `:5000` at the end?

---

### **Q: Screen is not updating/very slow**
**A:** Have them:
1. Refresh browser (Ctrl+R)
2. Lower FPS setting in browser (try 5-10 FPS)
3. Close other apps using WiFi

---

### **Q: Mouse/Keyboard not responding**
**A:** 
1. Close browser tab and reopen
2. Click on the screen area in browser
3. Refresh page (Ctrl+R)

---

### **Q: Can multiple people control at once?**
**A:** Yes! But they share the same screen. Great for study groups! Multiple people can see and control together.

---

### **Q: How do I find my IP if find_my_ip.bat doesn't work?**

**Windows PowerShell:**
```powershell
ipconfig
```

Look for:
```
Wireless LAN adapter WiFi:
   IPv4 Address . . . . . . . . . . . : 192.168.1.100
```

That `192.168.1.100` is your IP!

---

### **Q: Is it safe?**
**A:** 
- ✅ Use on trusted WiFi only (your home/school)
- ✅ Only give IP to people you trust
- ✅ It's hidden but anyone on the network could guess your IP
- ⚠️ Don't use on public WiFi without VPN

---

### **Q: What if I restart my computer?**

Option 1: Run `Valndor.bat` again  
Option 2: If you set up auto-start, it starts automatically! ✓

---

### **Q: Can I run this on mobile?**

Your phone/tablet CAN connect as the **client** (control):
- Open browser on phone
- Type IP address
- Control your PC from phone! 📱

But it CAN'T be the server (the one being controlled) - needs Windows/Mac/Linux.

---

## 🚨 TROUBLESHOOTING

### It doesn't start

**Try:**
```
python install_packages.py
```

This installs packages again. Then try `Valndor.bat`.

---

### "Python not found" error

Install Python from https://www.python.org/  
**Important:** Check "Add Python to PATH" during installation!

Then restart and try again.

---

### Connection refused error

1. Check IP address is correct
2. Make sure `python.exe` is in Task Manager (Valndor running)
3. Check both devices on same WiFi
4. Try different port number (edit server.py)

---

### Screen shows but can't control

1. Refresh browser (Ctrl+R)
2. Click ON the screen area
3. Try again
4. Check if FPS is set too low

---

## 📊 PERFORMANCE TIPS

### For Slow WiFi:
- Lower FPS to 5-10
- Reduce screen resolution
- Close other apps

### For Fast WiFi:
- Increase FPS to 20-30
- Keep quality high
- Multiple people can use

### Best Performance:
- Use wired connection if possible
- Close background apps
- Use on 5GHz WiFi (not 2.4GHz)

---

## 🎓 WHY VALNDOR IS AMAZING

✨ **Perfect for:**
- 📚 Study sessions (friend helps you with homework)
- 🎮 Gaming together (friend sees your screen)
- 💼 Work projects (colleague checks your work)
- 🔧 Tech support (expert helps you fix something)
- 📖 Teaching (teacher shows students)
- 👯 Group projects (team collaborates)

✨ **You get:**
- No installation on their machine
- No software to download
- Just open browser and go
- Works on any device (PC, Mac, Phone, Tablet)
- Easy to start, easy to stop

---

## 🎯 QUICK REFERENCE CARD

```
YOUR COMPUTER                  THEIR COMPUTER
┌──────────────────┐          ┌──────────────────┐
│ 1. Run           │          │ 1. Open Browser  │
│    Valndor.bat   │          │ 2. Type IP       │
│ 2. Get IP from   │   WiFi   │    192.168.1.100 │
│    find_my_ip    ├──────────┤    :5000         │
│ 3. Share IP      │          │ 3. Press Enter   │
└──────────────────┘          │ 4. They control! │
                              └──────────────────┘
```

---

## 📞 NEED HELP?

### Quick Fixes:
- Not starting? → Run `install_packages.py`
- Can't find IP? → Run `find_my_ip.bat`
- Want to stop? → Ctrl+Shift+Esc → End python.exe
- They can't connect? → Check same WiFi + correct IP

### Still stuck?
- Check that `python.exe` is in Task Manager
- Restart `Valndor.bat`
- Check firewall isn't blocking port 5000
- Try different WiFi network

---

## ✨ YOU'RE READY!

```
RIGHT NOW:
1. Double-click Valndor.bat          ← Start server
2. Double-click find_my_ip.bat       ← Get your IP
3. Send IP to friend: http://IP:5000 ← Share connection
4. They visit URL in browser         ← They connect
5. They control your PC!             ← SUCCESS! 🎉
```

---

## 🎊 FINAL THOUGHTS

**VALNDOR** = Your digital helping hand

Whether it's exam season, project deadlines, or just needing help - Valndor connects you with people who can actually DO something to help. No downloads, no complicated setup, no tech knowledge needed.

Just:
1. Click Valndor.bat
2. Share IP
3. They visit the link
4. **They're in control!**

**That's it. We really are the saviors of your exam.** 📚⭐

---

### 🚀 Ready to become remote-control-enabled? GO FOR IT!

**Made with ❤️ for students, teachers, and friends who help each other**

*Version: Valndor 1.0 | Status: Hidden & Ready | Made: February 2026*

---

