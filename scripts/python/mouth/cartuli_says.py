def cartuli_says(text):
    print_with_black_background("\nCartuli: " + text + "\n")


def print_with_black_background(text):
    print("\033[48;5m" + text + "\033[0m", end='', flush=True)


if __name__ == "__main__":
    # Example usage
    cartuli_says("Hello, Cartuli!")
