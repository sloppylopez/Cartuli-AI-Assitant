# from scripts.python.ears.voice_command_listener import voice_command_listener
import keyboard

from ears.voice_command_listener_threaded import recognize_worker
from mouth.cartuli_says import cartuli_says


def main():
    keyboard.wait("esc")
    cartuli_says("¡Cómo están los máquinas!")
    recognize_worker()
    cartuli_says("Program finished.")
    # keyboard.wait("esc")
    # voice_command_listener()


if __name__ == "__main__":
    main()
