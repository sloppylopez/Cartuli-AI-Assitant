import spacy
from mouth.asker import asker
from tools.logger import logger

# Load the spaCy English language model
nlp = spacy.load('en_core_web_sm')

# Set of commands and their corresponding actions
commands = {
    "open": "open_program",
    "type": "type_chars",
    "search": "search_terminal",
    "play": "open_music_player",
    "run": "run_script",
    "chatGPT": "call_chatGPT"
}


# Process user input and perform the corresponding action
def classify_command(text):
    doc = nlp(text)
    first_token = doc[0].text.lower() if len(doc) > 0 else None
    if first_token in commands:
        action = commands[first_token]
        argument = text.split(first_token, 1)[1].strip()  # Extract the argument after the command
        if action == "type_chars":
            type_chars(argument)
        if first_token == "open":
            open_program(argument)
        elif action == "search_terminal":
            search_terminal(argument)
        elif action == "open_music_player":
            open_music_player()
        elif action == "run_script":
            run_script(argument)
        elif action == "call_chatGPT":
            call_chat_gpt(argument, text)
    else:
        asker(text)


# Perform the action: open a program
def open_program(program):
    logger(f"Opening program: {program}")
    # Code to open the program goes here
    exit()


# Perform the action: type characters
def type_chars(chars):
    logger(f"Typing: {chars}")
    # Code to type the characters goes here
    exit()


# Perform the action: search in terminal console
def search_terminal(query):
    logger(f"Searching: {query}")
    # Code to perform the search in terminal console goes here
    exit()


# Perform the action: open the OS default music player
def open_music_player():
    logger("Opening music player")
    # Code to open the OS default music player goes here
    exit()


# Perform the action: run a script
def run_script(script):
    logger(f"Running script: {script}")
    # Code to run the script goes here
    exit()


# Perform the action: run a script
def call_chat_gpt(script, text):
    logger(f"Running script: {script}")
    # Code to run the script goes here
    asker(text)
    exit()
