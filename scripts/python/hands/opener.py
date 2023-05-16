import subprocess
import psutil


def run_opera_gx():
    opera_gx_path = r"C:\Users\sergi\AppData\Local\Programs\Opera GX\launcher.exe"
    subprocess.Popen([opera_gx_path])


def activate_opera_gx(process):
    # Activate the Opera GX window and make it topmost
    handle = psutil.Process(process.pid)
    handle.send_signal(0)


def open_browser():
    # Check if Opera GX is running
    opera_gx_name = "opera.exe"
    for process in psutil.process_iter(['name']):
        if process.info['name'] == opera_gx_name:
            # Opera GX is already running, activate the existing instance
            activate_opera_gx(process)
            return

    # Opera GX is not running, open a new instance
    run_opera_gx()


if __name__ == "__main__":
    open_browser()
