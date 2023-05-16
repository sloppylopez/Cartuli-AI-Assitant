from spinners import Spinners

from halo import Halo

from tools.logger import logger
import speech_recognition as sr


def get_audio():
    # Set up speech recognition
    r = sr.Recognizer()
    # Listen to user's voice
    try:
        spinner = Halo(text='', spinner=Spinners.growVertical.value, color='cyan', animation='bounce')
        spinner.start()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            logger("Speak something...")
            audio = r.listen(source, timeout=5, phrase_time_limit=15)
        stop_and_clear(spinner)
    except Exception as e:
        stop_and_clear(spinner)
        spinner.fail("\033[31;40m Exception: {0}".format(e) + "\033[0m")
    stop_and_clear(spinner)
    return audio, r


def stop_and_clear(spinner):
    spinner.stop()
    spinner.clear()
