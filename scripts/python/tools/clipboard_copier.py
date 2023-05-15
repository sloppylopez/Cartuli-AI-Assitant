import pyperclip

from mouth.sayer import sayer


def copy_to_clipboard(text, prefix):
    pyperclip.copy(prefix + text)
    # cartuli_says("Copied to clipboard: " + prefix + text)


if __name__ == "__main__":
    copy_to_clipboard("Text", "Prefix: ")
