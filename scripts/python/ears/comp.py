import keyboard

def on_hotkey():
    print("Hotkey pressed!")

# Add the hotkey
keyboard.add_hotkey("Ctrl+Shift+A", on_hotkey)

input("Press Enter to remove the hotkey...")

# Remove the hotkey
keyboard.remove_hotkey("Ctrl+Shift+A")

print("Hotkey removed!")