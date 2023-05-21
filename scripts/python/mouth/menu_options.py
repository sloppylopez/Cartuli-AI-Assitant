from mouth.chat_with_openapi import run_chatbot
from tools.logger import logger


def display_options(options):
    logger("Select an option:")
    for i, option in enumerate(options, 1):
        logger(f"{i}. {option}")
    print()


def menu_options():
    options = ["Voice", "Text", "Voice + Clipboard", "Text + Clipboard", "Refactor Text + Clipboard",
               "Refactor Location + Clipboard"]
    while True:
        display_options(options)
        num_options = len(options)
        choice = input(f"Enter your choice (1-{num_options}): ")
        if choice.isdigit() and 1 <= int(choice) <= num_options:
            run_chatbot(choice)
        else:
            logger("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu_options()
