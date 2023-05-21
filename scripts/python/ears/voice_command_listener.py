import speech_recognition as sr
from halo import Halo
from spinners import Spinners

recognizer = sr.Recognizer()


def convert_speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Speech:", text)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service:", e)

    return ""


# def voice_command_listener():
#     try:
#         audio, r = get_audio()
#         # Convert speech to text
#         text = r.recognize_google(audio)
#         # typewriter_print("You said: " + text, 0.02, "\033[35;40m")
#         print("\033[35;40mYou said: \033[0m" + f"\033[37;40m{text}\033[0m")
#         # Write question text to clipboard
#         copy_to_clipboard(text, "Question: ")
#         # Classify command text
#         classify_command(text)
#     except Exception as e:
#         stop_spinner(e)
#         get_input_text()
#

def stop_spinner(e):
    spinner = Halo(text='', spinner=Spinners.growVertical.value, color='cyan')
    spinner.fail("\033[31;40m" + "Unknown exception:" + " {0}".format(e) + "\033[0m")
    spinner.stop()
    spinner.clear()
