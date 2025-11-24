# Windows 11 Voice Typing Clone - Setup & Usage Guide

## Overview
This application is a professional clone of the Windows 11 Voice Typing overlay. It features:
-   **Modern UI**: Compact, dark-themed, draggable overlay (Windows 11 style).
-   **Universal Compatibility**: Works with ANY application (Word, Notepad, Browser, etc.) without stealing focus.
-   **Instant Typing**: Uses clipboard injection for zero-latency text appearance.
-   **Smart Positioning**: Starts automatically at the bottom-right of your screen.

## Prerequisites
-   **OS**: Windows 10 or 11.
-   **Python**: Python 3.8 or higher installed.
-   **Microphone**: A working microphone set as the default recording device.

## Installation (New Environment)
Follow these steps to set up the application on a new machine:

1.  **Copy Files**: Ensure you have the project folder containing `main.py`, `requirements.txt`, and the `core/` and `ui/` directories.

2.  **Open Terminal**: Open Command Prompt or PowerShell in the project directory.

3.  **Create Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    ```

4.  **Activate Virtual Environment**:
    ```bash
    venv\Scripts\activate
    ```

5.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: This will install `customtkinter`, `SpeechRecognition`, `pyaudio`, `keyboard`, `Pillow`, and `pyperclip`.*

## Running the Application
You can run the application in two ways:

### Option 1: One-Click Launch (Recommended)
Double-click the included `run.bat` file. This handles the virtual environment activation automatically.

### Option 2: Manual Launch
In your terminal (with venv activated):
```bash
python main.py
```

## How to Use
1.  **Launch**: The app will appear at the bottom-right of your screen.
2.  **Start Listening**:
    -   Click the **Microphone Icon**.
    -   OR press `Ctrl + Alt + H` (Global Hotkey).
3.  **Dictate**: Speak clearly. The text will appear instantly in your active window.
4.  **Move Window**: You can drag the window by clicking and holding anywhere on the background.
5.  **Stop**: Click the icon again or press the hotkey.
6.  **Close**: Click the small `X` button on the right.

## Troubleshooting
-   **"Focus Stealing"**: If clicking the app takes focus away from your document, try running the app as **Administrator** (Right-click `run.bat` -> Run as Administrator). This is sometimes needed for the "No Activate" style to work perfectly on restricted systems.
-   **Microphone Issues**: Ensure your privacy settings allow apps to access the microphone.
