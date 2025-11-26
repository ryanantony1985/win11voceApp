import customtkinter as ctk
from core.speech_handler import SpeechEngine
from core.text_injector import type_text

class VoiceTypingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        # Window configuration
        self.title("VoiKy")
        
        # Calculate center bottom position
        window_width = 280
        window_height = 60
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Bottom Right position
        x_pos = screen_width - window_width - 50 # 50px padding from right
        y_pos = screen_height - window_height - 50 # 50px padding from bottom
        
        self.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
        self.resizable(False, False)
        
        # Remove title bar for overlay look
        self.overrideredirect(True)
        
        # Always on top
        self.attributes('-topmost', True)
        
        # Theme
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Prevent window from stealing focus (WS_EX_NOACTIVATE)
        self.after(100, self.apply_window_styles)

        # Core Logic
        self.speech_engine = SpeechEngine()
        self.is_listening = False

        # Dragging functionality
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)
        self.x = 0
        self.y = 0

        # UI Layout
        self.grid_columnconfigure(0, weight=0) # Icon
        self.grid_columnconfigure(1, weight=1) # Status Text
        self.grid_columnconfigure(2, weight=0) # Close Button
        self.grid_rowconfigure(0, weight=1)

        # Main Frame to hold everything (for border/background)
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#2b2b2b", border_width=1, border_color="#444")
        self.main_frame.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=0, pady=0)
        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=0)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Microphone Button (Icon style)
        self.mic_button = ctk.CTkButton(
            self.main_frame, 
            text="🎤", 
            command=self.toggle_listening,
            font=("Segoe UI Emoji", 20),
            width=40,
            height=40,
            corner_radius=20,
            fg_color="#3B8ED0",
            hover_color="#36719F"
        )
        self.mic_button.grid(row=0, column=0, padx=(10, 5), pady=10)

        # Status Label
        self.status_label = ctk.CTkLabel(
            self.main_frame, 
            text="Ready to listen", 
            font=("Segoe UI", 14),
            anchor="w"
        )
        self.status_label.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        # Close Button
        self.close_button = ctk.CTkButton(
            self.main_frame,
            text="✕",
            command=self.quit_app,
            font=("Segoe UI", 12),
            width=30,
            height=30,
            corner_radius=15,
            fg_color="transparent",
            hover_color="#c0392b",
            text_color="#aaa"
        )
        self.close_button.grid(row=0, column=2, padx=(5, 10), pady=10)

    def apply_window_styles(self):
        try:
            from ctypes import windll
            GWL_EXSTYLE = -20
            WS_EX_NOACTIVATE = 0x08000000
            WS_EX_TOPMOST = 0x00000008
            
            # Get the window handle (HWND)
            hwnd = windll.user32.GetParent(self.winfo_id())
            
            # If GetParent returns 0, try winfo_id directly
            if hwnd == 0:
                hwnd = self.winfo_id()

            # Get current style
            style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            
            # Set new style
            windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_NOACTIVATE | WS_EX_TOPMOST)
            print("Window styles applied: NOACTIVATE | TOPMOST")
        except Exception as e:
            print(f"Could not set window style: {e}")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def toggle_listening(self):
        if self.is_listening:
            self.stop_listening()
        else:
            self.start_listening()

    def start_listening(self):
        self.is_listening = True
        self.mic_button.configure(fg_color="#e74c3c", hover_color="#c0392b") # Red when listening
        self.status_label.configure(text="Listening...")
        
        # Start speech engine
        self.speech_engine.start_listening(
            on_text_callback=self.on_text_recognized,
            on_error_callback=self.on_error
        )

    def stop_listening(self):
        self.is_listening = False
        self.mic_button.configure(fg_color="#3B8ED0", hover_color="#36719F") # Blue when idle
        self.status_label.configure(text="Ready")
        
        # Stop speech engine
        self.speech_engine.stop_listening()

    def on_text_recognized(self, text):
        print(f"Recognized: {text}")
        self.status_label.configure(text="Typing...")
        type_text(text)
        # Reset status after a short delay
        self.after(1000, lambda: self.status_label.configure(text="Listening..." if self.is_listening else "Ready"))

    def on_error(self, error_msg):
        print(error_msg)
        self.status_label.configure(text="Error")
        self.stop_listening()

    def quit_app(self):
        self.stop_listening()
        self.destroy()
