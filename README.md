# VoiKy - Free AI Voice Typing & Dictation Assistant for Windows

**VoiKy** is a professional, **free, and open-source voice typing overlay** for Windows 10 and 11. Convert speech to text with zero latency in **ANY application**—Word, Notepad, Chrome, Discord, VS Code, and more.

Designed for productivity, accessibility, and speed, VoiKy provides a modern, dark-themed interface that floats over your work without stealing focus.

<a href="https://apps.microsoft.com/detail/9nxq7cbghzdl?referrer=appbadge&mode=direct">
 <img src="https://get.microsoft.com/images/en-us%20dark.svg" width="200" alt="Get VoiKy from the Microsoft Store"/>
</a>

## Key Features

- **🚀 Zero-Latency Typing**: Uses advanced clipboard injection to ensure text appears instantly as you speak.
- **🤖 Powered by Google**: Utilizes **Google Speech Recognition** for industry-leading accuracy (requires internet).
- **🎨 Modern Windows 11 Design**: Sleek, dark-themed, and draggable overlay that blends perfectly with your desktop.
- **🔓 Universal Compatibility**: Works with **every** Windows application. If you can type in it, you can dictate in it.
- **🎙️ Global Hotkey**: Toggle listening instantly with `Ctrl + Alt + H` from anywhere.
- **🧠 Smart Positioning**: Automatically positions itself unobtrusively at the bottom-right, but you can drag it anywhere.
- **🔒 Privacy Note**: Audio is processed via Google's Web Speech API. No data is stored endlessly by VoiKy itself, but an internet connection is required.

## Why VoiKy?

Unlike built-in Windows dictation or heavy commercial software, VoiKy is:

- **Lightweight**: Minimal background resource usage.
- **Non-Intrusive**: Doesn't take focus away from your active window.
- **Open Source**: Transparent code, free to use and modify.

## Prerequisites

- **OS**: Windows 10 or Windows 11.
- **Python**: Python 3.8 or higher (for source version).
- **Microphone**: A working microphone set as the default recording device.

## Installation

### Option 1: Microsoft Store (Recommended)

[Download VoiKy significantly easily from the Microsoft Store](https://apps.microsoft.com/detail/9nxq7cbghzdl?referrer=appbadge&mode=direct). Changes update automatically.

### Option 2: Run from Source

1. **Clone/Download** this repository.
2. **Run Setup**:
    Double-click `run_app.bat`. This script automatically:
    - Creates a virtual environment.
    - Installs dependencies from `requirements.txt`.
    - Launches the application.

    *Manual Setup:*

    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python main.py
    ```

## Usage Guide

1. **Launch**: Open `VoiKy` (or run `run_app.bat`). The overlay appears.
2. **Start Dictating**:
    - Click the **Microphone Icon** on the overlay.
    - OR press `Ctrl + Alt + H` (Global Hotkey).
3. **Speak**: Speak clearly into your microphone. Watch text appear instantly in your active window.
4. **Move**: Drag the overlay background to reposition it.
5. **Stop**: Click the icon or press the hotkey again.
6. **Exit**: Click the `X` button to close entirely.

## Building Executable

To create a standalone `.exe` for distribution:

1. Double-click `build_app.bat`.
2. Find the portable `VoiKy.exe` in the `dist` folder.

## Troubleshooting

- **Focus Stealing**: If the app takes focus (preventing typing), try running as Administrator.
- **Microphone Issues**: Ensure your microphone is allowed in Windows **Privacy & Security > Microphone** settings.

---
*Keywords: Voice Typing, Speech to Text, Dictation Software, Windows Automation, Accessibility, Open Source, Python, Productivity Tool, Overlay*
