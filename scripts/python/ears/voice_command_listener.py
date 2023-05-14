import speech_recognition as sr

from scripts.python.brain.text_classificator import classify_command
from scripts.python.hands.copy_to_clipboard import copy_to_clipboard
from scripts.python.mouth.cartuli_says import cartuli_says


def voice_command_listener():
    audio, r = get_audio()
    try:
        # Convert speech to text
        text = r.recognize_google(audio)
        cartuli_says(f"You said: {text}")
        # Write question text to clipboard
        copy_to_clipboard(text)
        # Classify command text
        classify_command(text)
    except sr.UnknownValueError:
        # TODO add fadeout animation
        cartuli_says("Could not understand audio")
    except sr.RequestError as e:
        cartuli_says(f"Could not request results; {e}")


def get_audio():
    # Set up speech recognition
    r = sr.Recognizer()
    # Listen to user's voice
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        cartuli_says("Speak something...")
        audio = r.listen(source, timeout=10000, phrase_time_limit=20000)
    return audio, r
