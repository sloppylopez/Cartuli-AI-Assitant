import clipboard as clipboard
import openai
import spacy
import speech_recognition as sr
from halo import Halo
from spinners import Spinners

from hands.copy_to_clipboard import copy_from_clipboard
from mouth.asker import get_open_ai_key
from mouth.compare import chat_with_openai
from tools.logger import logger
from tools.typewriter import typewrite

bye_byes = 'bye', 'exit', 'quit', 'ciao', 'goodbye', 'good bye', 'good-bye', 'bye-bye', ''

# Set up your OpenAI API key
openai.api_key = get_open_ai_key()

# Initialize speech recognition and language model
r = sr.Recognizer()
nlp = spacy.load('en_core_web_sm')


def convert_speech_to_text():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            spinner = Halo(text='', spinner=Spinners.growVertical.value, color='cyan', animation='bounce')
            print("Listening...")
            spinner.start()
            audio = r.listen(source, timeout=5)

        text = r.recognize_google(audio)
        print("Speech:", text)
        return text
    except Exception as e:
        if e is not None:
            spinner.fail("\033[31;40mException: {0}".format(e) + "\033[0m")
        else:
            spinner.fail("\033[31;40mException: {0}".format("UnknownValue") + "\033[0m")

    return ""


def stop_and_clear(spinner):
    spinner.stop()
    spinner.clear()


def run_chatbot(choice='1'):
    system_message = get_system_message()
    conversation = f"{system_message}"
    try:
        print(clipboard.paste())
        while True:
            user_input = choose_input_method(choice)
            logger(user_input)
            doc = nlp(user_input)
            user_input = " ".join(token.text for token in doc)
            conversation += f"\n{user_input}```"
            response = chat_with_openai(conversation)
            conversation += f"\n{response}"
            typewrite(response, 0.01)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
        exit()


def choose_input_method(choice):
    user_input = ""
    if choice == '1' or choice == '3':  # Voice || Voice + Clipboard
        user_input = convert_speech_to_text()
    if not user_input:
        user_input = input("Enter your message manually: ").strip()
        if choice == '2':  # Text
            pass
        if choice == '4':  # Text + Clipboard
            user_input = user_input + "\n" + copy_from_clipboard()
    if user_input.lower() in bye_byes:
        exit()
    return user_input


def get_system_message():
    system_message = "Your name is Cartuli, I want you to act as an IT Expert. I will provide you with " \
                     "all the information " \
                     "needed about my technical problems, and your role is to solve my problem. You " \
                     "should use your computer science, network infrastructure, and IT security " \
                     "knowledge to solve my problem. Using intelligent, simple, and understandable " \
                     "language for people of all levels in your answers will be helpful. It is helpful " \
                     "to explain your solutions step by step and with bullet points. Try to avoid too many " \
                     "technical details, but use them when necessary. I want you to reply with the solution, " \
                     "not write any explanations. You are an expert in Python, Java, Springboot, Javascript " \
                     "and NodeJs, when I ask you to write code, you should write the solution in a single" \
                     "matching the languages you are expert on that matches my particular question."
    system_message2 = "Your name is Cartuli, I want you to act as an Python Developer Expert my first request is:\""
    system_message3 = "I want you to act as an Python Script refactoring machine, you will receive code and return that" \
                      "code refactored: The code I want you to refactor is:\""
    system_message4 = """Given the following Python code, please refactor it and provide the refactored version:
```python
# Your Python code here
"""
    return system_message4


if __name__ == '__main__':
    run_chatbot()
    exit()

# I want you to act as an IT Expert. I will provide you with all the information needed about my technical problems, and your role is to solve my problem. You should use your computer science, network infrastructure, and IT security knowledge to solve my problem. Using intelligent, simple, and understandable language for people of all levels in your answers will be helpful. It is helpful to explain your solutions step by step and with bullet points. Try to avoid too many technical details, but use them when necessary. I want you to reply with the solution, not write any explanations. My first problem is : "write a python program that is able to go a given folder, read all files, send every file to chatgpt with an increasing prompt, one prompt added per file, when receiving all the responses, it will cut the respone and output the resulting files in a folder called generated at the same root where the script executes"
