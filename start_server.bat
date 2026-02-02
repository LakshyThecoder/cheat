@echo off
setlocal enabledelayedexpansion

REM Remote Access App - Server Launcher for Windows
REM Robust installation with multiple retry attempts

title Remote Access Application - Server Setup

echo.
echo ============================================================
echo  REMOTE ACCESS APPLICATION - SETUP
echo ============================================================
echo.

REM Check if Python is installed
echo [STEP 1] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo SOLUTION: 
    echo 1. Download Python from: https://www.python.org/downloads/
    echo 2. Run the installer
    echo 3. CHECK "Add Python to PATH" during installation
    echo 4. Restart this script
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo [OK] Python found: %PYTHON_VERSION%
echo.

REM Upgrade pip with retries
echo [STEP 2] Upgrading pip (this helps with installation)...
setlocal enabledelayedexpansion
set RETRY_COUNT=0
set MAX_RETRIES=3

:pip_upgrade_retry
echo [Processing] Please wait... (this may take 30-60 seconds)
echo.
python -m pip install --upgrade pip --default-timeout=1000 --retries 5 2>&1 | findstr /V "^$"
if errorlevel 1 (
    set /a RETRY_COUNT=!RETRY_COUNT! + 1
    if !RETRY_COUNT! leq !MAX_RETRIES! (
        echo.
        echo [RETRY] Attempt !RETRY_COUNT! of !MAX_RETRIES!...
        echo Waiting 5 seconds...
        for /L %%N in (1,1,5) do (
            echo   . %%N seconds
            timeout /t 1 /nobreak >nul
        )
        goto pip_upgrade_retry
    ) else (
        echo [WARNING] Pip upgrade failed, continuing with default pip...
    )
) else (
    echo.
    echo [OK] Pip upgraded successfully
)
echo.

REM Install Flask
echo [STEP 3] Installing Flask (this is the main framework)...
set RETRY_COUNT=0
:flask_retry
echo   Downloading Flask... Please wait
echo.
python -m pip install flask==2.3.3 --default-timeout=1000 --retries 5 2>&1 | findstr /V "^$"
if errorlevel 1 (
    set /a RETRY_COUNT=!RETRY_COUNT! + 1
    if !RETRY_COUNT! leq 2 (
        echo.
        echo   [RETRY] Waiting before retry...
        for /L %%N in (1,1,5) do (
            echo      . %%N seconds
            timeout /t 1 /nobreak >nul
        )
        goto flask_retry
    ) else (
        echo.
        echo ERROR: Could not install Flask after multiple attempts
        echo TROUBLESHOOTING:
        echo - Check internet connection
        echo - Try: pip install flask==2.3.3 -i https://mirrors.aliyun.com/pypi/simple/
        echo.
        pause
        exit /b 1
    )
) else (
    echo.
    echo [OK] Flask installed successfully
)
echo.

REM Install Flask-CORS
echo [STEP 4] Installing Flask-CORS (cross-origin support)...
set RETRY_COUNT=0
:cors_retry
echo   Downloading Flask-CORS... Please wait
echo.
python -m pip install flask-cors==4.0.0 --default-timeout=1000 --retries 5 2>&1 | findstr /V "^$"
if errorlevel 1 (
    set /a RETRY_COUNT=!RETRY_COUNT! + 1
    if !RETRY_COUNT! leq 2 (
        echo.
        echo   [RETRY] Waiting before retry...
        for /L %%N in (1,1,5) do (
            echo      . %%N seconds
            timeout /t 1 /nobreak >nul
        )
        goto cors_retry
    ) else (
        echo [WARNING] Flask-CORS failed, trying to continue...
    )
) else (
    echo.
    echo [OK] Flask-CORS installed successfully
)
echo.

REM Install Pillow
echo [STEP 5] Installing Pillow (image processing - critical)...
set RETRY_COUNT=0
:pillow_retry
echo   Downloading Pillow... Please wait
echo.
python -m pip install Pillow==12.0.0 --default-timeout=1000 --retries 5 --only-binary :all: 2>&1 | findstr /V "^$"
if errorlevel 1 (
    set /a RETRY_COUNT=!RETRY_COUNT! + 1
    if !RETRY_COUNT! leq 2 (
        echo.
        echo   [RETRY] Waiting before retry...
        for /L %%N in (1,1,5) do (
            echo      . %%N seconds
            timeout /t 1 /nobreak >nul
        )
        goto pillow_retry
    ) else (
        echo [WARNING] Pillow installation failed. Screen capture may not work...
    )
) else (
    echo.
    echo [OK] Pillow installed successfully
)
echo.

REM Install pynput
echo [STEP 6] Installing pynput (mouse/keyboard control)...
set RETRY_COUNT=0
:pynput_retry
echo   Downloading pynput... Please wait
echo.
python -m pip install pynput==1.7.6 --default-timeout=1000 --retries 5 2>&1 | findstr /V "^$"
if errorlevel 1 (
    set /a RETRY_COUNT=!RETRY_COUNT! + 1
    if !RETRY_COUNT! leq 2 (
        echo.
        echo   [RETRY] Waiting before retry...
        for /L %%N in (1,1,5) do (
            echo      . %%N seconds
            timeout /t 1 /nobreak >nul
        )
        goto pynput_retry
    ) else (
        echo [WARNING] pynput failed. Will use Windows fallback...
    )
) else (
    echo.
    echo [OK] pynput installed successfully
)
echo.

echo.
echo ============================================================
echo  INSTALLATION COMPLETE - STARTING SERVER
echo ============================================================
echo.
echo.

timeout /t 2 /nobreak >nul

REM Start the server
python server.py

pause
