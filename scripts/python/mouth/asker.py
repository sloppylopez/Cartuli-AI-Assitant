import os
import openai
from spinners import Spinners
from ears.hear import get_audio
from halo import Halo
from tools.logger import logger
from tools.clipboard_copier import copy_to_clipboard
from tools.typewriter import typewriter_print

system_message = "You are Cartuli, a LLM trained by OpenAI similar to ChatGPT, but with the wisdom and personality of Steve Urkel but named Cartuli, the character of the popular TV show. and you will always answer like him\n"

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
            typewriter_print("\033[35;40mYou said: \033[0m" + f"\033[37;40m{text}\033[0m")

        get_chat_gpt_response(text)
    except Exception as e:
        spinner = Halo(text='', spinner=Spinners['growVertical'], color='cyan')
        spinner.fail(f"Could not request results; {e}")
        spinner.stop()
        spinner.clear()


def get_open_ai_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        logger("OPENAI_API_KEY environment variable is not set.")
        exit()
    return api_key


def get_chat_gpt_response(text):
    spinner = Halo(text='', spinner=Spinners['growVertical'], color='cyan')
    spinner.start()
    # Generate response from OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=system_message + text + "?",
        # We add a question mark at the end to avoid ChatGpt trying to autocomplete our questions, and then returning wrong response, example, "Who was Elvis Presley", and it answers "'manager, Elvis Presley's manager was blablabla, which is wrong!!
        max_tokens=60,
        # top_p=0.2,
        temperature=0,
        n=1
    )
    if 'choices' in response and len(response['choices']) > 0:
        generated_text = response['choices'][0]['text'].strip()
        # Write response text to clipboard
        copy_to_clipboard(generated_text, "Response: ")
        spinner.stop()
        spinner.clear()
        typewriter_print(generated_text)
    else:
        spinner.stop()
        typewriter_print("No response received from the API.")

