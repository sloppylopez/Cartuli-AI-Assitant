import sys

from spinners import Spinners

from brain.text_classificator import classify_command
from halo import Halo

from mouth.sayer import sayer
from tools.clipboard_copier import copy_to_clipboard


def get_input_text():
    text = input("Enter a command: ")
    if text.lower() == "exit":
        sys.exit(0)
    else:
        # Process the command or execute other logic
        sayer("Sending to ChatGPT: " + text)
        # Write question text to clipboard
        copy_to_clipboard(text, "Question: ")
        # Classify command text
        classify_command(text)
