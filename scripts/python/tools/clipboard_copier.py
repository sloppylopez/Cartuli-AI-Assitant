import pyperclip

from mouth.cartuli_says import cartuli_says


def copy_to_clipboard(text):
    pyperclip.copy(text)
    cartuli_says("Copied to clipboard: " + text)
