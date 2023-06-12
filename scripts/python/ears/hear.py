import time

from spinners import Spinners

from halo import Halo

from tools.logger import logger
import speech_recognition as sr

from tools.typewriter import typewrite


def get_audio():
    audio = None
    spinner = None
    # Set up speech recognition
    r = sr.Recognizer()
    # Listen to user's voice
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            spinner = Halo(text='', spinner=Spinners.growVertical.value, color='cyan', animation='bounce')
            # time.sleep(0.2)  # if we don't do this, we will speak too soon
            typewrite("Speak something...", 0.02, "\033[35;40m")
            spinner.start()
            audio = r.listen(source, timeout=None, phrase_time_limit=None)

    except Exception as e:
        if spinner is not None:
            stop_and_clear(spinner)
        spinner.fail("\033[31;40m Exception: {0}".format(e) + "\033[0m")
    stop_and_clear(spinner)
    return audio, r


def stop_and_clear(spinner):
    spinner.stop()
    spinner.clear()


if __name__ == '__main__':
    get_audio()
