import sys

from plyer import notification
def display_notification(message):
    try:
        notification.notify(
            title="Cartuli: ️",
            message=message,
            timeout=10000,
            toast=True,
            app_icon="C:\elgato\images\cartuli-logo-master-small.ico"
        )
    except:
        pass

if __name__ == "__main__":
    display_notification("Hello, World!")