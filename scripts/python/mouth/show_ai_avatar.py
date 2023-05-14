import sys
import time
import tkinter as tk

import keyboard
from PIL import Image, ImageTk

from scripts.python.hands.get_image import get_file_from_path


def fade_in(window):
    alpha = window.attributes("-alpha")
    while alpha < 1:
        alpha += 0.013  # Increase alpha by 0.013 (30% faster)
        window.attributes("-alpha", alpha)
        window.update()
        time.sleep(0.008)  # Sleep for 0.008 seconds (30% faster)


def fade_out(window):
    try:
        alpha = window.attributes("-alpha")
        while alpha > 0:
            alpha -= 0.013  # Decrease alpha by 0.013 (30% faster)
            window.attributes("-alpha", alpha)
            window.update()
            time.sleep(0.008)  # Sleep for 0.008 seconds (30% faster)
        window.destroy()
    except tk.TclError:
        pass


def display_image(image_path, is_f19_pressed):
    # Start displaying the image when F19 key is pressed
    root = tk.Tk()
    root.attributes("-alpha", 0)  # Set initial transparency to 0
    root.overrideredirect(True)  # Remove window decorations
    root.geometry("+0+0")  # Place window at the down-right corner of the screen

    image = Image.open(image_path)
    width, height = image.size

    canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0)
    canvas.pack()

    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    root.attributes("-topmost", True)  # Keep the window on top of other windows
    root.update()
    if is_f19_pressed:
        fade_in(root)

    while True:
        if not root.state() == "normal" or not root.winfo_viewable():
            break
        if not keyboard.is_pressed("F19"):
            fade_out(root)
            break
        root.update_idletasks()
        root.update()
        time.sleep(0.1)

    fade_out(root)


if __name__ == "__main__":
    # display_image(get_file_from_path("../../../images/cartuli-logo-master.png"))
    keyboard.add_hotkey("F19", lambda: display_image(get_file_from_path("../../../images/cartuli-logo-master.png")))
    keyboard.wait("esc")  # Wait until the 'esc' key is pressed, this is to debug comfortably
