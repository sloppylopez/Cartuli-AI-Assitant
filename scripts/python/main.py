import sys
import threading

import keyboard

from mouth.chat_with_openapi import run_chatbot


def main():
    run_chatbot()
    keyboard.wait("esc")
    sys.exit(0)


if __name__ == "__main__":
    main()
