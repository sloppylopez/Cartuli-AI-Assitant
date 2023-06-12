import os
import random
import sys
import time
import tkinter as tk

from PIL import Image, ImageTk

from hands.get_image import get_full_from_relative
from tools.logger import logger

image_folder = get_full_from_relative("../../../images")

# Get a list of image files from the specified folder
image_files = [file for file in os.listdir(image_folder) if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

# Create a Tkinter window
window = tk.Tk()
window.title("Random Image")
window.attributes("-topmost", True)
window.overrideredirect(True)

# Set the initial window transparency
window.attributes("-alpha", 0.0)


# Function to gradually increase the window's transparency
def fade_in():
    for i in range(0, 45):
        alpha = i / 10.0
        window.attributes("-alpha", alpha)
        window.update()
        time.sleep(0.05)


# Function to gradually decrease the window's transparency
def fade_out():
    for i in range(45, -1, -1):
        alpha = i / 10.0
        window.attributes("-alpha", alpha)
        window.update()
        time.sleep(0.05)


# Function to close the window
def close_window():
    fade_out()
    window.destroy()
    sys.exit(0)


# Function to get the image path
def get_image_path(source_img):
    if source_img is not None:
        return os.path.join(image_folder, source_img)
    else:
        return os.path.join(image_folder, random.choice(image_files))


def show_image_on_window(image_path):
    global gif_image, label, update_gif
    if image_path is None:
        image_path = get_image_path(image_path)
        logger(f"Image folder path: {image_path}")
    # Load the image
    if image_path.lower().endswith(".gif"):
        # Load and display an animated GIF
        gif_image = Image.open(image_path)
        width, height = gif_image.size
        label = tk.Label(window)
        label.pack()

        # Function to update the GIF frames
        def update_gif(frame):
            gif_image.seek(frame)
            frame_image = gif_image.copy()
            frame_tk = ImageTk.PhotoImage(frame_image)
            label.configure(image=frame_tk)
            label.image = frame_tk
            window.after(gif_image.info["duration"], update_gif, (frame + 1) % gif_image.n_frames)

        update_gif(0)  # Start updating the frames

    else:
        # Load and display a static image (JPEG, PNG)
        image = Image.open(image_path)
        width, height = image.size
        max_size = 200
        if width > max_size or height > max_size:
            # Resize the image while maintaining the aspect ratio
            aspect_ratio = width / height
            if width > height:
                new_width = max_size
                new_height = int(new_width / aspect_ratio)
            else:
                new_height = max_size
                new_width = int(new_height * aspect_ratio)
            image.thumbnail((new_width, new_height), Image.LANCZOS)
            width, height = image.size
        image_tk = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=image_tk)
        label.pack()
    # Calculate the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate the window position
    x = screen_width - width - 70
    y = screen_height - height - 55
    # Set the window position
    window.geometry(f"{width}x{height}+{x}+{y}")
    # Run the fade-in animation
    fade_in()
    close_window()
    # Run the script until the window is closed
    window.mainloop()
