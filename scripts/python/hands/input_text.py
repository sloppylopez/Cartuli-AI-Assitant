import sys

from brain.text_classificator import classify_and_run_command
from hands.copy_to_clipboard import copy_to_clipboard_prefix
from tools.logger import logger


def get_input_text():
    logger("Enter text manually...")
    text = input()
    if text.lower() == "exit":
        sys.exit(0)
    else:
        # Process the command or execute other logic
        if text != '' and not None:
            logger("Sending to ChatGPT: " + text)
            # Write question text to clipboard
            copy_to_clipboard_prefix(text, "Question: ")
            # Classify command text
            classify_and_run_command(text)
        else:
            get_input_text()
