import pyperclip


def copy_to_clipboard(text):
    pyperclip.copy(text)


def copy_to_clipboard_prefix(prefix, text):
    pyperclip.copy(prefix + text)


def copy_from_clipboard():
    clipboard_content = pyperclip.paste()
    return clipboard_content


if __name__ == "__main__":
    copy_to_clipboard_prefix("Prefix: ", "Text")
    copy_to_clipboard("Text: ")
    print(copy_from_clipboard())
