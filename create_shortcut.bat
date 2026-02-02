@echo off
REM Create Valndor Shortcut

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo  Valndor - Shortcut Creator
echo ============================================================
echo.

REM Get current directory
set "CURRENT_DIR=%cd%"
set "VALNDOR_BAT=%CURRENT_DIR%\Valndor.bat"

REM Check if Valndor.bat exists
if not exist "%VALNDOR_BAT%" (
    echo ERROR: Valndor.bat not found in current directory
    echo Please run this script from the Valndor folder
    pause
    exit /b 1
)

REM Create shortcut on Desktop
set "DESKTOP=%USERPROFILE%\Desktop\Valndor.lnk"

REM Use PowerShell to create shortcut
powershell -Command ^
  "$WshShell = New-Object -ComObject WScript.Shell; " ^
  "$Shortcut = $WshShell.CreateShortcut('%DESKTOP%'); " ^
  "$Shortcut.TargetPath = '%VALNDOR_BAT%'; " ^
  "$Shortcut.WorkingDirectory = '%CURRENT_DIR%'; " ^
  "$Shortcut.WindowStyle = 7; " ^
  "$Shortcut.Save()"

if errorlevel 1 (
    echo ERROR: Could not create shortcut
    pause
    exit /b 1
)

echo.
echo ============================================================
echo SUCCESS! Valndor shortcut created on Desktop
echo ============================================================
echo.
echo You can now:
echo 1. Double-click the Valndor icon on your Desktop
echo 2. The server will start hidden
echo 3. Share your IP with others to control your machine
echo.
echo To find your IP, run PowerShell and type: ipconfig
echo.
pause
