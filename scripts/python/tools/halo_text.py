import keyboard
from spinners import Spinners

from halo import Halo


@Halo(text='Cartuli', spinner=Spinners.growVertical.value, placement='right')
def long_running_function():
    keyboard.wait("esc")  # Wait for the Escape key to be pressed
    # Run time consuming work here
    pass


if __name__ == "__main__":
    long_running_function()
