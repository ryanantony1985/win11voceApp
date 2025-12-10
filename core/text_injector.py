import keyboard
import pyperclip

def type_text(text):
    """
    Simulates typing the given text using clipboard paste for speed.
    """
    if not text:
        return

    try:
        # Save current clipboard
        old_clipboard = pyperclip.paste()
        
        # Copy new text (without trailing space, we'll inject it manually)
        pyperclip.copy(text)
        
        # Paste
        keyboard.send('ctrl+v')
        
        # Inject space explicitly to ensure separation
        # This bypasses potential clipboard trimming or smart paste issues
        keyboard.write(" ")
        
        # Restore clipboard (optional, might cause race condition if paste is slow)
        # For now, let's leave the text in clipboard or wait a bit
        
    except Exception as e:
        print(f"Error injecting text: {e}")
        # Fallback to typing
        try:
            keyboard.write(text + " ")
        except:
            pass
