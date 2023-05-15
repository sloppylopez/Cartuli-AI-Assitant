import os

import openai
from spinners import Spinners

from ears.hear import get_audio
from halo import Halo
from mouth.sayer import sayer
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
            typewriter_print(f"You said: {text}")

        get_chat_gpt_response(text)
    except Exception as e:
        sayer(f"Could not request results; {e}")


def get_open_ai_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        sayer("OPENAI_API_KEY environment variable is not set.")
        exit()
    return api_key


def get_chat_gpt_response(text):
    spinner = Halo(text='', spinner=Spinners.growVertical.value, color='white')
    spinner.start()
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
        spinner.stop()  # Type-writing does not play along with animated spinners
        typewriter_print(generated_text)
    else:
        spinner.stop()
        typewriter_print("No response received from the API.")
