# 🚀 HOW TO RUN VALNDOR - COMPLETE SETUP GUIDE

## *"Get Valndor Running in 10 Minutes - Step by Step"*

---

## ⚠️ IMPORTANT: FIRST TIME SETUP ONLY

**The first time you run Valndor, you MUST install Python packages.** After that, you can just run `Valndor.bat` directly!

---

## 📋 WHAT YOU NEED BEFORE STARTING

✅ **Python installed** on your computer  
✅ **Valndor folder** with all files  
✅ **Internet connection** (for downloading packages)  
✅ **5-10 minutes** of patience

### ❌ If Python is NOT installed:

1. Go to: https://www.python.org/downloads/
2. Download the latest Python
3. Run the installer
4. **IMPORTANT:** Check the box "Add Python to PATH"
5. Click Install
6. Restart your computer
7. Then come back to this guide

---

## 🎯 COMPLETE FIRST-TIME SETUP (10 MINUTES)

---

## STEP 1️⃣: Install Python Packages

This is a ONE-TIME setup. After this, you never need to do it again!

### Option A: The Easy Way (Recommended) 🌟

**Right-click on `install_packages.py`**

Look in your Valndor folder and find the file named `install_packages.py`

Right-click it:

```
install_packages.py
├─ Open
├─ Open with
├─ Edit with Python
├─ Properties
└─ ...
```

Click: **"Open with Python"**

---

**A black window will open. You'll see:**

```
============================================================
  REMOTE ACCESS APP - PACKAGE INSTALLER
============================================================

Python version: 3.14.2 (or similar)

Upgrading pip...
✓ Pip upgraded

[1/3] Installing: flask==2.3.3
Attempt: 1/3

====== Installing ======
Downloading flask...
Processing dependencies...
✓ flask==2.3.3 installed successfully!

[2/3] Installing: flask-cors==4.0.0
... (more packages installing) ...

✓ All packages installed successfully!

You can now run: python server.py

Press Enter to exit...
```

**Just wait!** Don't close it. It might take 2-5 minutes.

---

### Option B: If Option A Doesn't Work

Open PowerShell and run manually:

1. Press: `Win + R`
2. Type: `powershell`
3. Press Enter
4. Copy and paste this:

```powershell
cd "e:\Cheating"
python install_packages.py
```

5. Press Enter
6. Wait for packages to install
7. When done, it says "Press Enter to exit..."
8. Press Enter

---

## ✅ WHAT YOU'LL SEE

**As packages install, you'll see progress:**

```
[1/3] Installing: flask==2.3.3
  Downloading... 100%
  ✓ Flask installed

[2/3] Installing: flask-cors==4.0.0
  Downloading... 100%
  ✓ Flask-CORS installed

[3/3] Installing: Pillow==12.0.0
  Downloading... 100%
  ✓ Pillow installed

[4/4] Installing: pynput==1.7.6
  Downloading... 100%
  ✓ pynput installed

============================================================
  INSTALLATION COMPLETE
============================================================
✓ All packages installed successfully!
```

**When you see this = Everything is ready! ✓**

Press Enter to close.

---

## STEP 2️⃣: Test the Server (OPTIONAL but Recommended)

Before running hidden, let's test it works:

**Double-click: `start_server.bat`**

This runs the server WITH a visible window so you can see what's happening.

### You'll see:

```
============================================================
VALNDOR - REMOTE ACCESS SERVER STARTED
============================================================
Local IP: 192.168.1.100
Port: 5000
URL: http://192.168.1.100:5000
Hostname: YOUR-PC-NAME
```

**Copy that IP address!**

---

### Test the connection:

1. Open a web browser on the **same computer**
2. Type: `http://127.0.0.1:5000`
3. Press Enter
4. You should see the Valndor control interface ✓

---

### Stop the test server:

Press: **Ctrl + C** in the command window

The window will close.

---

## STEP 3️⃣: Run Valndor (The Hidden Version)

Now you're ready to run Valndor for real!

**Double-click: `Valndor.bat`**

---

### What happens:

1. A window opens briefly (shows "Installing...")
2. Packages load (because you already installed them, this is fast)
3. Window **hides automatically** ✓
4. **Valndor is now running in the background!**

---

### How to check if it's running:

Press: **Ctrl + Shift + Esc**

This opens Task Manager.

Look for: **`python.exe`** in the list

If it's there = **Valndor is running!** ✓

---

## STEP 4️⃣: Get Your IP Address

**Double-click: `find_my_ip.bat`**

A window shows:

```
============================================================
  VALNDOR - FIND YOUR IP ADDRESS
============================================================

Your network information:

IPv4 Address: 192.168.1.100

============================================================

Copy the IPv4 Address
Share this with the person who wants to control your PC
They should visit: http://YOUR_IP:5000 in their browser

============================================================
```

**Copy the IP address** (the number like 192.168.1.100)

---

## STEP 5️⃣: Share With Your Friend

Send your friend a message:

```
"Visit this link to control my computer:
http://192.168.1.100:5000"
```

**Replace 192.168.1.100 with YOUR actual IP from Step 4**

---

## STEP 6️⃣: They Connect (On Their Device)

**On THEIR computer:**

1. Open web browser (Chrome, Firefox, Edge, Safari)
2. Click the address bar
3. Paste: `http://192.168.1.100:5000`
4. Press Enter
5. They see YOUR screen loading...
6. **THEY NOW CONTROL YOUR COMPUTER!** 🎉

---

---

# 🔄 AFTER FIRST TIME: RUNNING VALNDOR AGAIN

Once you've done the first-time setup, running Valndor is super easy:

## Simply:

1. **Double-click `Valndor.bat`**
2. Window hides
3. Server runs in background
4. **That's it!** ✓

---

You don't need to install packages again. Just run `Valndor.bat` every time you want to use it!

---

---

# ⏹️ HOW TO STOP VALNDOR

Since Valndor runs hidden, stop it using Task Manager:

## Method 1: Fast Way 🚀

Press: **Ctrl + Shift + Esc**

This opens Task Manager directly.

---

## Method 2: Classic Way

1. Press: **Ctrl + Alt + Delete**
2. Click: **Task Manager**

---

## In Task Manager:

1. Look for: **`python.exe`**
2. Click on it (select it)
3. Click: **"End Task"** button (bottom right)
4. Confirm deletion
5. **Server stops!** ✓

---

---

# 📋 QUICK REFERENCE FLOWCHART

```
FIRST TIME SETUP:
┌─────────────────────────────────────────────────────┐
│ 1. Right-click install_packages.py                  │
│    ↓                                                │
│ 2. Select "Open with Python"                        │
│    ↓                                                │
│ 3. WAIT for packages to install (2-5 minutes)      │
│    ↓                                                │
│ 4. Press Enter when done                            │
│    ↓                                                │
│ 5. Done! Packages installed ✓                       │
└─────────────────────────────────────────────────────┘

OPTIONAL - TEST IT FIRST:
┌─────────────────────────────────────────────────────┐
│ 1. Double-click start_server.bat                    │
│    ↓                                                │
│ 2. See the window with IP shown                     │
│    ↓                                                │
│ 3. Test connection in browser                       │
│    ↓                                                │
│ 4. Press Ctrl+C to stop                             │
└─────────────────────────────────────────────────────┘

RUN VALNDOR (HIDDEN):
┌─────────────────────────────────────────────────────┐
│ 1. Double-click Valndor.bat                         │
│    ↓                                                │
│ 2. Window hides (IT'S WORKING!)                     │
│    ↓                                                │
│ 3. Double-click find_my_ip.bat                      │
│    ↓                                                │
│ 4. See your IP                                      │
│    ↓                                                │
│ 5. Share IP with friend                             │
│    ↓                                                │
│ 6. They visit http://IP:5000                        │
│    ↓                                                │
│ 7. They control your computer! 🎉                   │
└─────────────────────────────────────────────────────┘

TO STOP:
┌─────────────────────────────────────────────────────┐
│ Ctrl+Shift+Esc → Find python.exe → End Task         │
└─────────────────────────────────────────────────────┘
```

---

---

# ❓ COMMON PROBLEMS & FIXES

---

## ❌ "Python is not recognized"

**Problem:** When you try to run `install_packages.py`, you get:
```
'python' is not recognized as an internal or external command
```

**Fix:**

1. Install Python again from https://www.python.org/
2. **IMPORTANT:** When installing, CHECK "Add Python to PATH"
3. Complete installation
4. **Restart your computer**
5. Try again

---

## ❌ "Install packages window closes immediately"

**Problem:** The installation window opens and closes too fast

**Fix:**

Open PowerShell and run manually:

1. Press: `Win + R`
2. Type: `powershell`
3. Press Enter
4. Type: `cd e:\Cheating`
5. Press Enter
6. Type: `python install_packages.py`
7. Press Enter
8. Now you can see what's happening!

---

## ❌ Packages fail to download

**Problem:** Installation gets stuck or fails on a package

**Fix:**

Use alternative PyPI mirror:

```powershell
pip install -i https://mirrors.aliyun.com/pypi/simple/ flask==2.3.3
pip install -i https://mirrors.aliyun.com/pypi/simple/ flask-cors==4.0.0
pip install -i https://mirrors.aliyun.com/pypi/simple/ Pillow==12.0.0
pip install -i https://mirrors.aliyun.com/pypi/simple/ pynput==1.7.6
```

Then try `Valndor.bat` again.

---

## ❌ "Cannot find python.exe in Task Manager"

**Problem:** After running Valndor.bat, you can't find the server in Task Manager

**Fix:**

Try these in order:

1. Open PowerShell
2. Type: `Get-Process python`
3. If you see output = Python is running somewhere ✓
4. If nothing = Python didn't start (try again)
5. Make sure Valndor.bat is in correct folder
6. Double-click it again

---

## ❌ Friend can't connect

**Problem:** They get "Cannot find server" error

**Fix:**

Check in order:

1. **Are you both on same WiFi?** ← Most important!
2. **Is Valndor still running?** (Check Task Manager)
3. **Is the IP correct?** (Run find_my_ip.bat again)
4. **Did they type `:5000`?** (The port number at end)
5. **Firewall issue?** Try disabling firewall temporarily

---

---

# 📝 SUMMARY: THE EASY WAY

### FIRST TIME (ONE-TIME):
```
1. Right-click install_packages.py
2. Select "Open with Python"
3. Wait 2-5 minutes
4. Press Enter when done
```

### EVERY TIME YOU USE VALNDOR:
```
1. Double-click Valndor.bat
2. Double-click find_my_ip.bat
3. Share IP with friend
4. They visit http://IP:5000
5. DONE! They control you!
```

### TO STOP:
```
Ctrl+Shift+Esc → Kill python.exe
```

---

---

# 🎉 YOU'RE READY!

**You now know everything to:**
- ✅ Install packages (first time)
- ✅ Run Valndor (every time)
- ✅ Share with friends
- ✅ Let them control you
- ✅ Stop Valndor when done

**Go forth and conquer!** 🚀

---

*Made with ❤️ for Exam Saviors*  
*Valndor v1.0 | February 2026*

