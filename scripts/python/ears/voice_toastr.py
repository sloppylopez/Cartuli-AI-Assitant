import speech_recognition as sr
from plyer import notification
import keyboard
import sys
import time

def display_notification(message):
    notification.notify(
        title="Reconocimiento de Voz",
        message=message,
        timeout=0
    )

# Create a recognizer instance
recognizer = sr.Recognizer()

# Set the language to Spanish
language = "es-ES"

# Flag to indicate if speech recognition is active
listening = False

def start_listening():
    global listening
    listening = True
    print("Escuchando...")

def stop_listening():
    global listening
    listening = False

def exit_program():
    print("Programa terminado")
    sys.exit(0)

# Register the F19 key press event to start listening
keyboard.on_press_key("F19", lambda _: start_listening())

# Register the F19 key release event to stop listening
keyboard.on_release_key("F19", lambda _: stop_listening())

# # Register the F18 key press event to stop listening and exit the program
keyboard.on_press_key("F18", lambda _: exit_program())

# Use the default microphone as the audio source
with sr.Microphone() as source:
    exit_flag = False  # Flag to indicate when to exit the loop

    while not exit_flag:
        try:
            if listening:
                # Adjust the ambient noise threshold for speech recognition
                recognizer.adjust_for_ambient_noise(source)

                # Listen for audio input
                audio = recognizer.listen(source)

                # Recognize speech using Google Speech Recognition in Spanish
                text = recognizer.recognize_google(audio, language=language)

                # Display the recognized text as a notification
                display_notification(text)

                print("Reconocido:", text)

        except sr.UnknownValueError:
            print("El reconocimiento de voz no pudo entender el audio")

        except sr.RequestError as e:
            print("No se pudieron obtener resultados del servicio de reconocimiento de voz de Google; {0}".format(e))

        except KeyboardInterrupt:
            exit_flag = True  # Set the exit flag to exit the loop

        time.sleep(1)  # Add a 1-second delay to reduce resource consumption

    exit_program()
