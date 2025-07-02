#importing all libraries
import speech_recognition as sr
import tempfile
import subprocess
import time
import os

recognizer = sr.Recognizer()

#writing function for speech
def listen_to_microphone(timeout=10) -> str:
    """Captures voice input from the microphone and converts to text."""
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            print("🔍 Transcribing...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "Timeout: No speech detected."
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError as e:
            return f"API error: {e}"

def speak_text(text: str):
    """Uses Windows native voice with VBScript file (safe escaping)."""
    import html

    print(f"🔊 Speaking: {text[:80]}{'...' if len(text) > 80 else ''}")
    time.sleep(0.3)

    # Escape double quotes for VBScript
    safe_text = text.replace('"', "'")  # Replace quotes
    safe_text = safe_text.replace('\n', ' ')  # Remove newlines (VBScript doesn't like them)
    safe_text = safe_text.replace('\r', '')

    vbs_code = f'''
Dim sapi
Set sapi = CreateObject("SAPI.SpVoice")
sapi.Speak "{safe_text}"
'''

    # Save and run VBS
    with tempfile.NamedTemporaryFile(delete=False, suffix=".vbs", mode="w", encoding="utf-8") as vbs_file:
        vbs_file.write(vbs_code)
        vbs_path = vbs_file.name

    try:
        subprocess.run(["cscript", "//nologo", vbs_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error speaking text: {e}")
    finally:
        os.remove(vbs_path)