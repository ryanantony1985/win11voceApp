@echo off
setlocal

set "VENV_DIR=venv"
set "REQUIREMENTS=requirements.txt"

:: Check if python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    pause
    exit /b 1
)

:: Check if venv exists
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

:: Activate venv
call "%VENV_DIR%\Scripts\activate.bat"

:: Install dependencies
if exist "%REQUIREMENTS%" (
    echo Installing/Updating dependencies...
    pip install -r "%REQUIREMENTS%"
) else (
    echo Warning: %REQUIREMENTS% not found.
)

:: Ensure PyInstaller is installed
pip install pyinstaller

:: Build the application
echo Building VoiKy...
pyinstaller --clean VoiKy.spec

if %errorlevel% equ 0 (
    echo.
    echo ==========================================
    echo Build successful! 
    echo Executable is located in: dist\VoiKy.exe
    echo ==========================================
) else (
    echo.
    echo ==========================================
    echo Build failed!
    echo ==========================================
)

pause
