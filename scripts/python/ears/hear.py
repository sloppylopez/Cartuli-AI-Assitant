from scripts.python.mouth.cartuli_says import cartuli_says
import speech_recognition as sr


def get_audio():
    # Set up speech recognition
    r = sr.Recognizer()
    # Listen to user's voice
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        cartuli_says("Speak something...")
        audio = r.listen(source, timeout=10000, phrase_time_limit=20000)
    return audio, r
