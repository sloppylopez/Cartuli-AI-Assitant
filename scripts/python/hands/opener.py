import pygetwindow as gw
import subprocess

def run_opera_gx():
    opera_gx_path = r"C:\Users\sergi\AppData\Local\Programs\Opera GX\launcher.exe"
    subprocess.Popen([opera_gx_path])

def main():
    # Check if Opera GX is running
    opera_gx_title = "Opera GX"
    opera_gx = gw.getWindowsWithTitle(opera_gx_title)

    if opera_gx:
        # Opera GX is already running
        opera_gx[0].activate()
    else:
        # Opera GX is not running, open a new instance
        run_opera_gx()

if __name__ == "__main__":
    main()
