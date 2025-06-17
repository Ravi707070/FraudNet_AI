@echo off
title FraudNet AI - Advanced Fraud Detection Suite
color 0A

echo.
echo  ========================================
echo   FraudNet AI - Fraud Detection Suite
echo  ========================================
echo.

echo [INFO] Starting FraudNet AI...
echo [INFO] Please wait while we set up the environment...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo [INFO] Please install Python 3.7+ and try again.
    pause
    exit /b 1
)

echo [INFO] Python found. Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    echo [INFO] Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo [INFO] Starting FraudNet AI server...
echo [INFO] The application will open in your default browser.
echo [INFO] Server URL: http://localhost:5000
echo.
echo [INFO] Press Ctrl+C to stop the server.
echo.

REM Start the Flask application
python app.py

pause
