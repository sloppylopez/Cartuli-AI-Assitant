# from scripts.python.ears.voice_command_listener import voice_command_listener
from scripts.python.ears.voice_command_listener_threaded import recognize_worker
from scripts.python.mouth.cartuli_says import cartuli_says


def main():
    cartuli_says("¡Cómo están los máquinas!")
    recognize_worker()
    cartuli_says("Program finished.")
    # voice_command_listener()


if __name__ == "__main__":
    main()
