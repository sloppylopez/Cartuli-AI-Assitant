import spacy

from scripts.python.mouth.chat_gpt_asker import asker
from scripts.python.mouth.cartuli_says import cartuli_says, cartuli_types

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
    for token in doc:
        if token.text.lower() in commands:
            action = commands[token.text.lower()]
            argument = text.split(token.text, 1)[1].strip()  # Extract the argument after the command

            if action == "open_program":
                open_program(argument)
            elif action == "type_chars":
                type_chars(argument)
            elif action == "search_terminal":
                search_terminal(argument)
            elif action == "open_music_player":
                open_music_player()
            elif action == "run_script":
                run_script(argument)
            elif action == "run_script":
                call_chat_gpt(argument)
            else:
                cartuli_types("Command not recognized from list...")
            return
    cartuli_types("Command not in list... trying with ChatGPT")
    asker(text)


# Perform the action: open a program
def open_program(program):
    cartuli_says(f"Opening program: {program}")

    # Code to open the program goes here
    exit()


# Perform the action: type characters
def type_chars(chars):
    cartuli_says(f"Typing: {chars}")

    # Code to type the characters goes here
    exit()


# Perform the action: search in terminal console
def search_terminal(query):
    cartuli_says(f"Searching: {query}")

    # Code to perform the search in terminal console goes here
    exit()


# Perform the action: open the OS default music player
def open_music_player():
    cartuli_says("Opening music player")

    # Code to open the OS default music player goes here
    exit()


# Perform the action: run a script
def run_script(script):
    cartuli_says(f"Running script: {script}")

    # Code to run the script goes here
    exit()


# Perform the action: run a script
def call_chat_gpt(script):
    cartuli_says(f"Running script: {script}")

    # Code to run the script goes here
    asker(None)
    exit()
