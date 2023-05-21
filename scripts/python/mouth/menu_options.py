from hands.copy_to_clipboard import copy_to_clipboard
from mouth.chat_with_openapi import run_chatbot
from tools.logger import logger


def display_options(options):
    logger("Select an option:")
    for i, option in enumerate(options, 1):
        logger(f"{i}. {option}")
    print()


def menu_options():
    options = ["Voice", "Text", "Voice + Clipboard", "Text + Clipboard"]
    display_options(options)
    num_options = len(options)

    while True:
        choice = input(f"Enter your choice (1-{num_options}): ")
        if choice.isdigit() and 1 <= int(choice) <= num_options:
            # chosen_option = options[int(choice) - 1]
            # copy_to_clipboard(chosen_option)
            run_chatbot(choice)
            break
        else:
            logger("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu_options()
