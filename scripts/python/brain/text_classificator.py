import spacy

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
                call_chatGPT(argument)
            else:
                print("Unknown command.")
            return

    print("Command not recognized. Trying luck with the heavy hitters")

# Perform the action: open a program
def open_program(program):
    print(f"Opening program: {program}")

    # Code to open the program goes here

# Perform the action: type characters
def type_chars(chars):
    print(f"Typing: {chars}")

    # Code to type the characters goes here

# Perform the action: search in terminal console
def search_terminal(query):
    print(f"Searching: {query}")

    # Code to perform the search in terminal console goes here

# Perform the action: open the OS default music player
def open_music_player():
    print("Opening music player")

    # Code to open the OS default music player goes here

# Perform the action: run a script
def run_script(script):
    print(f"Running script: {script}")

    # Code to run the script goes here

# Perform the action: run a script
def call_chatGPT(script):
    print(f"Running script: {script}")

    # Code to run the script goes here
    # asker()
