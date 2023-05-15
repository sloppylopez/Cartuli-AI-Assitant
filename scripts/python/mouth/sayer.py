def sayer(text):
    print_with_black_background(text + "\n")


def sayer_err(text):
    print_with_black_background(text + "\n")


def print_with_black_background(text):
    print("\033[35;40m" + text + "\033[0m", end='', flush=True)


if __name__ == "__main__":
    # Example usage
    sayer("Hello, Cartuli!")
