import openai
import speech_recognition as sr
import os
import pyperclip

from scripts.python.brain.text_classificator import classify_command
from scripts.python.mouth.display_notification import display_notification


def asker():
    # Set up OpenAI API key
    openai.api_key = getOpenAIKey()
    audio, r = getAudio()
    try:
        getChatGptResponse(audio, r)
    except sr.UnknownValueError:
        # TODO add fadeout animation
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


def getOpenAIKey():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is not None:
        print("API key found.")
    else:
        print("OPENAI_API_KEY environment variable is not set.")
        exit()
    return api_key


def getChatGptResponse(audio, r):
    # Convert speech to text
    text = r.recognize_google(audio)
    print(f"You said: {text}")
    # Write question text to clipboard
    write_to_clipboard(text)
    classify_command(text)
    # Generate response from OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=60
    )
    if 'choices' in response and len(response['choices']) > 0:
        generated_text = response['choices'][0]['text'].strip()
        # Display the recognized text as a notification
        display_notification(generated_text)
        # Write response text to clipboard
        write_to_clipboard(generated_text)
        print("Generated response:", generated_text)
    else:
        print("No response received from the API.")

def write_to_clipboard(text):
    pyperclip.copy(text)
    print("copied to clipboard:", text)


def getAudio():
    # Set up speech recognition
    r = sr.Recognizer()
    # Listen to user's voice
    with sr.Microphone() as source:
        print("Cartuli: Speak something...")
        audio = r.listen(source)
    return audio, r
