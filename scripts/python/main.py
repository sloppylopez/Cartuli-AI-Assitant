from scripts.python.ears.voice_command_listener import voice_command_listener
from scripts.python.mouth.cartuli_says import cartuli_says


def main():
    cartuli_says("¡Cómo están los máquinas!")
    voice_command_listener()

if __name__ == "__main__":
    main()
