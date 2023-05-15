# from scripts.python.ears.voice_command_listener import voice_command_listener
import sys

import keyboard

from ears.voice_command_listener import voice_command_listener
# from ears.voice_command_listener_threaded import voice_recognize_worker
from mouth.cartuli_says import cartuli_says


def main():
    keyboard.add_hotkey("F19", lambda: voice_command_listener())
    # voice_recognize_worker()
    voice_command_listener()
    # cartuli_says("Program finished.")
    keyboard.wait("esc")  # Wait for the Escape key to be pressed
    keyboard.remove_hotkey("F19")


if __name__ == "__main__":
    main()
    sys.exit(0)

print("after __name__ guard")
