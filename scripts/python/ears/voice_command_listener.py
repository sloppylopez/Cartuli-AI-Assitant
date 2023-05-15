from spinners import Spinners

from brain.text_classificator import classify_command
from ears.hear import get_audio
from halo import Halo
from hands.input_text import get_input_text
from tools.clipboard_copier import copy_to_clipboard
from tools.typewriter import typewriter_print

MAX_ATTEMPTS = 1


def voice_command_listener(attempts):
    try:
        audio, r = get_audio()
        # Convert speech to text
        text = r.recognize_google(audio)
        typewriter_print("You said: " + r.recognize_google(audio))
        # Write question text to clipboard
        copy_to_clipboard(text, "Question: ")
        # Classify command text
        classify_command(text)
    except Exception as e:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        handle_exception(attempts, "Unknown exception:", message)


def handle_exception(attempts, message, e):
    spinner = Halo(text='', spinner=Spinners.growVertical.value, color='white')
    spinner.fail(message + " {0}".format(e))
    spinner.stop()
    if attempts < MAX_ATTEMPTS:
        voice_command_listener(attempts + 1)
    else:
        spinner.info("Max attempts reached. Listening stopped.")
        get_input_text()
