import tkinter as tk
import subprocess


def open_terminal():
    # Create the main window
    window = tk.Tk()
    window.overrideredirect(True)  # Remove window decorations
    window.geometry("400x300+0+0")  # Set window size and position

    # Define the animation functions
    def animate_open():
        window.attributes('-alpha', 0.0)  # Make window transparent
        window.deiconify()  # Show the window
        x = 0
        y = 0
        while x <= 1.0 and y <= 1.0:
            window.attributes('-alpha', x)  # Gradually increase transparency
            window.update_idletasks()
            x += 0.01
            y += 0.01

    def animate_close():
        x = 1.0
        y = 1.0
        while x >= 0.0 and y >= 0.0:
            window.attributes('-alpha', x)  # Gradually decrease transparency
            window.update_idletasks()
            x -= 0.01
            y -= 0.01
        window.withdraw()  # Hide the window

    # Open the terminal
    subprocess.Popen("start cmd.exe", shell=True)

    # Bind animations to window events
    window.bind("<Map>", lambda event: animate_open())  # Trigger animation on window open
    window.protocol("WM_DELETE_WINDOW", animate_close)  # Trigger animation on window close

    window.mainloop()


open_terminal()
