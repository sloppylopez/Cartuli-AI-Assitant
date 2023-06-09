from plyer import notification

from hands.get_image import get_full_from_relative
from tools.logger import logger


def display_notification(message):
    try:
        notification.notify(
            title="Cartuli: ️",
            message=message,
            timeout=10000,  # milliseconds
            toast=True,
            app_icon=get_full_from_relative("../../../images/cartuli-logo-master-small.ico")
        )
    except Exception as e:
        logger(e)
        pass


if __name__ == "__main__":
    display_notification("Hello, Cartuli!")
