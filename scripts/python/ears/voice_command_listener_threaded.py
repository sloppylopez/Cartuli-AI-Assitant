#!/usr/bin/env python3
import sys

# NOTE: this example requires PyAudio because it uses the Microphone class
import keyboard
import time
from threading import Thread
from queue import Queue

import speech_recognition as sr

from scripts.python.hands.get_image import get_file_from_path
from scripts.python.mouth.cartuli_says import cartuli_says
from scripts.python.mouth.show_ai_avatar import display_image

r = sr.Recognizer()
audio_queue = Queue()


def recognize_worker():
    # this runs in a background thread
    while True:
        audio = audio_queue.get()  # retrieve the next audio processing job from the main thread
        if audio is None:
            break  # stop processing if the main thread is done
        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            cartuli_says("GSR thinks you said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            cartuli_says("GSR could not understand audio")
        except sr.RequestError as e:
            cartuli_says("Could not request results from Google Speech Recognition service; {0}".format(e))
        audio_queue.task_done()  # mark the audio processing job as completed in the queue


# start a new thread to recognize audio, while this thread focuses on listening
recognize_thread = Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()

with sr.Microphone() as source:
    is_f19_pressed = False
    once = True
    try:
        while True:
            if keyboard.is_pressed('F19'):
                keyboard.add_hotkey("F19", lambda: display_image(
                    get_file_from_path("../../../images/cartuli-logo-master.png"), keyboard))
                if once:
                    cartuli_says('Say something, I\'m all ears...')
                    once = False
                if not is_f19_pressed:
                    audio_queue.put(r.listen(source))
                    is_f19_pressed = True
            else:
                keyboard.remove_all_hotkeys()
                is_f19_pressed = False
            # time.sleep(0.05)  # Add a small delay to reduce CPU usage
    except KeyboardInterrupt:
        pass

recognize_thread.join()  # wait for the recognize_thread to actually stop

if __name__ == "__main__":
    recognize_worker()
