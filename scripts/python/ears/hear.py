from spinners import Spinners

from halo import Halo

from mouth.sayer import sayer
import speech_recognition as sr


def get_audio():
    # Set up speech recognition
    r = sr.Recognizer()
    # Listen to user's voice
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            sayer("Speak something...")
            spinner = Halo(text='', spinner=Spinners.growVertical.value, color='white', animation='bounce')
            spinner.start()
            audio = r.listen(source, timeout=5, phrase_time_limit=15)
        spinner.stop()
    except Exception as e:
        spinner.fail(e)
        spinner.stop()
    spinner.stop()
    return audio, r
