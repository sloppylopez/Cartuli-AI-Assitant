import sys
import threading

import keyboard
from halo import Halo
from spinners import Spinners

from ears.voice_command_listener import voice_command_listener

# from spinners import Spinners
# from halo import Halo

MAX_ATTEMPTS = 3


def main():
    # Add hotkey on-the-fly, so we can ask another question without running the python again
    keyboard.add_hotkey("F19", lambda: threading.Thread(target=voice_command_listener(0)).start())
    # voice_recognize_worker() This is to run threaded, but it works way slower for some reason...
    threading.Thread(target=voice_command_listener(0)).start()
    keyboard.wait("esc")  # Wait for the Escape key to be pressed
    keyboard.remove_hotkey("F19")


if __name__ == "__main__":
    main()
    sys.exit(0)

print("after __name__ guard")
