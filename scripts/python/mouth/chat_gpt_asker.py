import os

import openai
import speech_recognition as sr

from ears.hear import get_audio
from mouth.cartuli_says import cartuli_says
# from mouth.display_notification import display_notification
from tools.clipboard_copier import copy_to_clipboard
from tools.typewriter import typewriter_print


def asker(text):
    audio = None
    r = None
    # Set up OpenAI API key
    openai.api_key = get_open_ai_key()
    if text is None:
        audio, r = get_audio()
    try:
        # Convert speech to text
        if text is None:
            text = r.recognize_google(audio)
            cartuli_says("")
            typewriter_print(f"You said: {text}")

        get_chat_gpt_response(text)
    except sr.UnknownValueError:
        # TODO add fadeout animation
        cartuli_says("Could not understand audio")
    except sr.RequestError as e:
        cartuli_says(f"Could not request results; {e}")


def get_open_ai_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        cartuli_says("OPENAI_API_KEY environment variable is not set.")
        exit()
    return api_key


def get_chat_gpt_response(text):
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
        copy_to_clipboard(generated_text, "Response: ")
        # Display the recognized text as a notification (Ditching notifications in favour of terminal)
        # display_notification(generated_text)
        typewriter_print(generated_text)
    else:
        cartuli_says("")
        typewriter_print("No response received from the API.")
