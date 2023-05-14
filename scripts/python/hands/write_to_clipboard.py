import pyperclip


def write_to_clipboard(text):
    pyperclip.copy(text)
    print("copied to clipboard:", text)