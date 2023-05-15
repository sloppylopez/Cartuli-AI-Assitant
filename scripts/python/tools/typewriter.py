import time

from mouth.cartuli_says import cartuli_types, cartuli_says


def typewriter_print(text, delay=0.02):
    for char in text:
        cartuli_types(char)
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
