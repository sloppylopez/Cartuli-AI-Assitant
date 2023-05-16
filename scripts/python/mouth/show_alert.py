import ctypes


def show_alert_dialog(title, message):
    message_box = ctypes.windll.user32.MessageBoxW
    message_box(None, message, title, 0x40 | 0x1)  # 0x40: MB_ICONINFORMATION, 0x1: MB_OK


if __name__ == "__main__":
    show_alert_dialog("Alert", "This is an alert message!")
