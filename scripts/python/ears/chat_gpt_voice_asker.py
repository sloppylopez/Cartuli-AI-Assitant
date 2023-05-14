import os
import sys

import openai
import speech_recognition as sr

from scripts.python.brain.text_classificator import classify_command
from scripts.python.hands.write_to_clipboard import write_to_clipboard
from scripts.python.mouth.cartuli_says import cartuli_says
from scripts.python.mouth.display_notification import display_notification


def asker():
    # Set up OpenAI API key
    openai.api_key = get_open_ai_key()
    audio, r = get_audio()
    try:
        get_chat_gpt_response(audio, r)
    except sr.UnknownValueError:
        # TODO add fadeout animation
        cartuli_says("Could not understand audio")
    except sr.RequestError as e:
        cartuli_says(f"Could not request results; {e}")


def get_open_ai_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is not None:
        cartuli_says("API key found.")
    else:
        cartuli_says("OPENAI_API_KEY environment variable is not set.")
        exit()
    return api_key


def get_chat_gpt_response(audio, r):
    # Convert speech to text
    text = r.recognize_google(audio)
    cartuli_says(f"You said: {text}")
    # Write question text to clipboard
    write_to_clipboard(text)
    # Classify command text
    classify_command(text)
    # Generate response from OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=60,
        # 💀 Number of tokens(group of words), this is sensitive since the budget depends on this, use with caution!!
        temperature=0,  # Controls the precision of the response, don't improvise
        n=1  # number of responses generated per question, we just one the most precise
    )
    if 'choices' in response and len(response['choices']) > 0:
        generated_text = response['choices'][0]['text'].strip()
        # Write response text to clipboard
        write_to_clipboard(generated_text)
        # Display the recognized text as a notification
        display_notification(generated_text)
        cartuli_says("ChatGPT told me this-> \n" + generated_text)
        sys.exit(0)
    else:
        cartuli_says("No response received from the API.")


def get_audio():
    # Set up speech recognition
    r = sr.Recognizer()
    # Listen to user's voice
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        cartuli_says("Speak something...")
        audio = r.listen(source, timeout=10000, phrase_time_limit=20000)
    return audio, r
