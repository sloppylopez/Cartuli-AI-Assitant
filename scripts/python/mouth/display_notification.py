import sys

from plyer import notification

from scripts.python.hands.get_image import get_file_from_path


def display_notification(message):
    try:
        notification.notify(
            title="Cartuli: ️",
            message=message,
            timeout=10000,
            toast=True,
            app_icon=get_file_from_path("../../../cartuli-logo-master-small.ico")
        )
    except:
        pass


if __name__ == "__main__":
    display_notification("Hello, World!")
