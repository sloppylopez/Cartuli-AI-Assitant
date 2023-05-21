import spacy
from mouth.asker import asker, chat_with_openai
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
    "chatGPT": "call_chatGPT",
    "refactor": "refactor_code",
}


def get_system_message(choice, messages):
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
    
```
"""
    prompt = ""
    if choice == '5':  # Refactor + Clipboard
        prompt = "Given the following Python code, please refactor it and provide the refactored version," \
                 "avoid shadowing variables from outer scope if possible," \
                 "write the code in the most legible way possible for humans:\n" \
                 " ```\n" + messages + "\n```"
    return prompt


# Process user input and perform the corresponding action
def classify_and_run_command(choice, conversation):
    argument = ''
    doc = nlp(conversation)
    first_token = doc[0].text.lower() if len(doc) > 0 else None
    if choice == '5':  # Refactor + Clipboard
        first_token = 'refactor'
    if first_token in commands:
        action = commands[first_token]
        if choice != '5':  # Refactor + Clipboard
            argument = conversation.split(first_token, 1)[1].strip()  # Extract the argument after the command
        conversation = get_system_message(choice, conversation)
        if action == "type_chars":
            type_chars(argument)
        elif action == "open":
            open_program(argument)
        elif action == "search_terminal":
            search_terminal(argument)
        elif action == "open_music_player":
            open_music_player()
        elif action == "run_script":
            run_script(argument)
        elif action == "call_chatGPT":
            call_chat_gpt(argument, conversation)
        elif action == "refactor_code":
            return refactor_code(conversation)
    else:
        asker(conversation)


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


# Perform the action: refactor code
def refactor_code(text):
    logger(f"{text}")
    # Code to run the script goes here
    # asker(text)
    response = chat_with_openai(text)
    return response
