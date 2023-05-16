import sys
import threading

import keyboard

from ears.voice_command_listener import voice_command_listener


def register_hotkey():
    keyboard.add_hotkey("F19", lambda: threading.Thread(target=voice_command_listener).start())


def main():
    register_hotkey()
    threading.Thread(target=voice_command_listener).start()
    keyboard.wait("esc")
    keyboard.unregister_hotkey("F19")
    sys.exit(0)


if __name__ == "__main__":
    main()

print("after __name__ guard")
