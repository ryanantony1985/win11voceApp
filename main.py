from ui.window import VoiceTypingApp
import keyboard
import threading

def main():
    app = VoiceTypingApp()
    
    # Global Hotkey to toggle listening
    # Using 'ctrl+alt+h' to avoid conflict with system 'win+h' during development
    # In a real clone, we might want to override or use a different key.
    def on_hotkey():
        # We need to use app.after to be thread-safe with tkinter
        app.after(0, app.toggle_listening)

    try:
        keyboard.add_hotkey('ctrl+alt+h', on_hotkey)
    except Exception as e:
        print(f"Failed to register hotkey: {e}")

    app.mainloop()

if __name__ == "__main__":
    main()
