from spinners import Spinners

from brain.text_classificator import classify_command
from ears.hear import get_audio
from halo import Halo
from hands.input_text import get_input_text
from tools.clipboard_copier import copy_to_clipboard


def voice_command_listener():
    try:
        audio, r = get_audio()
        # Convert speech to text
        text = r.recognize_google(audio)
        # typewriter_print("You said: " + text, 0.02, "\033[35;40m")
        print("\033[35;40mYou said: \033[0m" + f"\033[37;40m{text}\033[0m")
        # Write question text to clipboard
        copy_to_clipboard(text, "Question: ")
        # Classify command text
        classify_command(text)
    except Exception as e:
        stop_spinner(e)
        get_input_text()


def stop_spinner(e):
    spinner = Halo(text='', spinner=Spinners.growVertical.value, color='cyan')
    spinner.fail("\033[31;40m" + "Unknown exception:" + " {0}".format(e) + "\033[0m")
    spinner.stop()
    spinner.clear()
