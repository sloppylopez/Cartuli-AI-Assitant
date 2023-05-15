import pygetwindow as gw
import subprocess


def run_opera_gx():
    opera_gx_path = r"C:\Users\sergi\AppData\Local\Programs\Opera GX\launcher.exe"
    subprocess.Popen([opera_gx_path])


def open_browser():
    # Check if Opera GX is running
    opera_gx_title = "GX Corner - Opera"
    opera_gx = gw.getWindowsWithTitle(opera_gx_title)
    gw.getAllTitles()
    if opera_gx:
        # Opera GX is already running
        opera_gx[0].activate()
    else:
        # Opera GX is not running, open a new instance
        run_opera_gx()


if __name__ == "__main__":
    open_browser()
