@echo off
cd /d "%~dp0"

echo Checking Python availability...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Attempting to install Python 3.11 via Winget...
    winget install -e --id Python.Python.3.11
    if %errorlevel% neq 0 (
        echo Failed to install Python. Please install Python 3.11 manually from python.org.
        pause
        exit /b 1
    )
    echo Python installed successfully.
    echo Please restart this script to apply changes to PATH.
    pause
    exit /b 0
)

echo Checking Python environment...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

echo Checking dependencies...
pip install -r requirements.txt

echo Starting VoiKy...
python main.py
pause
