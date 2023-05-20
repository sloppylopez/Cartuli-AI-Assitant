import sys
import time

import clipboard as clipboard
import openai
import spacy
import speech_recognition as sr
from halo import Halo
from spinners import Spinners

from mouth.asker import get_open_ai_key

bye_byes = 'bye', 'exit', 'quit', 'ciao', 'goodbye', 'good bye', 'good-bye', 'bye-bye', ''

# Set up your OpenAI API key
openai.api_key = get_open_ai_key()

# Initialize speech recognition and language model
r = sr.Recognizer()
nlp = spacy.load('en_core_web_sm')


def convert_speech_to_text():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        spinner = Halo(text='', spinner=Spinners.growVertical.value, color='cyan', animation='bounce')
        print("Listening...")
        spinner.start()
        audio = r.listen(source, timeout=5)

    try:
        text = r.recognize_google(audio)
        print("Speech:", text)
        return text
    except sr.UnknownValueError:
        spinner.fail("\033[31;40mUnknownValue" + "\033[0m")
    except sr.RequestError as e:
        spinner.fail("\033[31;40mException: {0}".format(e) + "\033[0m")
    except Exception as e:
        if spinner is not None:
            stop_and_clear(spinner)
        spinner.fail("\033[31;40mException: {0}".format(e) + "\033[0m")

    return ""


def stop_and_clear(spinner):
    spinner.stop()
    spinner.clear()


def chat_with_openai(messages):
    # Generate a response from OpenAI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=messages,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract the generated message from the response
    generated_message = response.choices[0].text.strip().split('\n')[-1]

    return generated_message


def run_chatbot():
    system_message = "System: I'm chatbot Cartuli! I always act like Donald Trump, I give concise answers: "
    conversation = f"{system_message}"

    try:
        print(clipboard.paste())
        while True:
            user_input = convert_speech_to_text()
            if not user_input:
                user_input = input("Enter your message manually: ")
            if user_input.lower() in bye_byes:
                exit()

            doc = nlp(user_input)
            user_input = " ".join(token.text for token in doc)
            conversation += f"\nUser: {user_input}"
            response = chat_with_openai(conversation)
            conversation += f"\nChatGPT: {response}"
            typewrite(response)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
        exit()


def typewrite(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


if __name__ == '__main__':
    run_chatbot()
    exit()
