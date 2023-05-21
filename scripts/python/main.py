import sys

import keyboard

from mouth.menu_options import menu_options


def main():
    menu_options()
    keyboard.wait("esc")
    sys.exit(0)


if __name__ == "__main__":
    main()
