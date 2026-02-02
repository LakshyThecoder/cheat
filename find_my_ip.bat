@echo off
REM Valndor - Find Your IP Address

title Valndor - IP Finder

cls
echo.
echo ============================================================
echo  VALNDOR - FIND YOUR IP ADDRESS
echo ============================================================
echo.
echo Your network information:
echo.
ipconfig | findstr /R "IPv4 Address"
echo.
echo ============================================================
echo.
echo Copy the IPv4 Address (looks like 192.168.x.x)
echo Share this with the person who wants to control your PC
echo They should visit: http://YOUR_IP:5000 in their browser
echo.
echo ============================================================
echo.
pause
