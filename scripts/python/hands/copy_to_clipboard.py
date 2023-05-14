import pyperclip

from scripts.python.mouth.cartuli_says import cartuli_says


def copy_to_clipboard(text):
    pyperclip.copy(text)
    cartuli_says("copied to clipboard:" + text)
