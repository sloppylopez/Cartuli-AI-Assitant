import time

from tools.logger import print_with_black_background


def typewriter_print(text, delay=0.02, color="\033[32;40m"):
    for char in text:
        print_with_black_background(char, color)
        time.sleep(delay)
    print()


if __name__ == "__main__":
    # Example usage
    typewriter_print("Hello, this is a typewriter effect!")
    # Wait for a few seconds
    time.sleep(2)
    typewriter_print("You can create typing effects using this approach.")
    # Wait for a few seconds
    time.sleep(2)
    # Clear the terminal (if needed)
    # print("\033c", end='')
    typewriter_print("Thank you for using the typewriter effect!")
