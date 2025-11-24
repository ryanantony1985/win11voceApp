import speech_recognition as sr
import threading

class SpeechEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.stop_listening_func = None
        self.is_listening = False
        
        # Adjust for ambient noise on startup once
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
        except Exception as e:
            print(f"Warning: Could not adjust for ambient noise: {e}")

    def start_listening(self, on_text_callback, on_error_callback=None):
        """
        Starts listening in the background.
        on_text_callback: function(text) called when speech is recognized.
        on_error_callback: function(error_msg) called on error.
        """
        if self.is_listening:
            return

        self.is_listening = True
        
        # Create a new microphone instance to avoid context manager conflicts
        microphone = sr.Microphone()
        
        # Removed blocking adjust_for_ambient_noise here for speed

        def callback(recognizer, audio):
            try:
                # Recognize speech using Google Web Speech API
                text = recognizer.recognize_google(audio)
                if text:
                    on_text_callback(text)
            except sr.UnknownValueError:
                # Speech was unintelligible
                pass 
            except sr.RequestError as e:
                if on_error_callback:
                    on_error_callback(f"Could not request results; {e}")
                else:
                    print(f"Speech recognition error: {e}")

        self.stop_listening_func = self.recognizer.listen_in_background(microphone, callback)

    def stop_listening(self):
        """
        Stops the background listener.
        """
        if self.stop_listening_func:
            self.stop_listening_func(wait_for_stop=False)
            self.stop_listening_func = None
        self.is_listening = False
