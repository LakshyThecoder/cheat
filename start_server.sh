#!/bin/bash
# Remote Access App - Server Launcher for macOS/Linux

echo ""
echo "============================================================"
echo "Remote Access Application - Server Setup"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo ""
    echo "Please install Python 3 using:"
    echo "  macOS: brew install python3"
    echo "  Linux: sudo apt-get install python3 python3-pip"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "[1/3] Checking Python installation... OK"
echo ""

# Check if requirements are installed
echo "[2/3] Installing dependencies..."
python3 -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    read -p "Press Enter to exit..."
    exit 1
fi
echo ""

# Start the server
echo "[3/3] Starting server..."
echo ""
python3 server.py

read -p "Press Enter to exit..."
