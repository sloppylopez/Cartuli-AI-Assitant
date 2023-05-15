import speech_recognition as sr
from speech_recognition import WaitTimeoutError

from brain.text_classificator import classify_command
from mouth.cartuli_says import cartuli_says
from ears.hear import get_audio
from tools.clipboard_copier import copy_to_clipboard
from tools.typewriter import typewriter_print


def voice_command_listener():
    try:
        audio, r = get_audio()
        # Convert speech to text
        text = r.recognize_google(audio)
        cartuli_says("")
        typewriter_print("Your said: " + r.recognize_google(audio))
        # Write question text to clipboard
        copy_to_clipboard(text)
        # Classify command text
        classify_command(text)
    except sr.UnknownValueError:
        cartuli_says("GSR could not understand audio")
        voice_command_listener()
    except sr.RequestError as e:
        cartuli_says("Could not request results from GSR service; {0}".format(e))
        voice_command_listener()
    except WaitTimeoutError as e:
        cartuli_says("Try to increase wait timeout time; {0}".format(e))
        voice_command_listener()
    except Exception as e:
        cartuli_says("Uncontrolled exception; {0}".format(e))
        voice_command_listener()
