from plyer import notification
def display_notification(message):
    notification.notify(
        title="‍🤓️Cartuli: ️",
        message=message,
        timeout=10000,
        toast=True
    )
