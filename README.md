# VoiKy - Voice Typing App

**VoiKy** is a professional voice typing overlay designed for Windows. It provides a modern, dark-themed, draggable overlay that works with ANY application (Word, Notepad, Browser, etc.) without stealing focus.

<a href="https://apps.microsoft.com/detail/9nxq7cbghzdl?referrer=appbadge&mode=direct">
	<img src="https://get.microsoft.com/images/en-us%20dark.svg" width="200"/>
</a>

## Features

- **Modern UI**: Compact, dark-themed, draggable overlay (Windows 11 style).
- **Universal Compatibility**: Works with any application.
- **Instant Typing**: Uses clipboard injection for zero-latency text appearance.
- **Smart Positioning**: Starts automatically at the bottom-right of your screen.

## Prerequisites

- **OS**: Windows 10 or 11.
- **Python**: Python 3.8 or higher.
- **Microphone**: A working microphone set as the default recording device.

## Installation

1. **Clone/Download** the repository.
2. **Run Setup**:
    Double-click `run_app.bat`. This will automatically set up the virtual environment and install dependencies if needed, then launch the app.

    *Alternatively, manually:*

    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

## Usage

1. **Launch**: Run `run_app.bat`. The app appears at the bottom-right.
2. **Start Listening**:
    - Click the **Microphone Icon**.
    - OR press `Ctrl + Alt + H` (Global Hotkey).
3. **Dictate**: Speak clearly. Text appears instantly in your active window.
4. **Move Window**: Drag anywhere on the background.
5. **Stop**: Click the icon or press the hotkey.
6. **Close**: Click the `X` button.

## Building Executable

To create a standalone `.exe`:

1. Double-click `build_app.bat`.
2. Find `VoiKy.exe` in the `dist` folder.

## Troubleshooting

- **Focus Stealing**: Run as Administrator if the app steals focus.
- **Microphone**: Check Windows Privacy settings.
