def cartuli_says(text):
    print_blue("\nCartuli: " + text + "\n")


def cartuli_types(text):
    print("\033[48;5m" + text + "\033[0m", end='', flush=True)
    # typewriter_print(text)


def print_blue(text):
    print("\033[48;5m" + text + "\033[0m", end='', flush=True)
