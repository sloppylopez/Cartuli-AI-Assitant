def logger(text, color="\033[35;40m"):
    print_with_black_background(text + "\n", color)


def logger_err(text, color="\033[35;40m"):
    print_with_black_background(text + "\n", color)


def print_with_black_background(text, color="\033[35;40m"):
    print(color + text + "\033[0m", end='', flush=True)


if __name__ == "__main__":
    # Example usage
    logger("Hello, Cartuli!")
