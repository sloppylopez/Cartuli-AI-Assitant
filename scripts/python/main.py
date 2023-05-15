# from scripts.python.ears.voice_command_listener import voice_command_listener
import sys

import keyboard

from ears.voice_command_listener import voice_command_listener
# from ears.voice_command_listener_threaded import voice_recognize_worker
from mouth.cartuli_says import cartuli_says


def main():
    # voice_recognize_worker()
    voice_command_listener()
    # cartuli_says("Program finished.")


if __name__ == "__main__":
    main()
    sys.exit(0)

print("after __name__ guard")
print("after __name__ guard")
print("after __name__ guard")
print("after __name__ guard")
print("after __name__ guard")
print("after __name__ guard")