import psutil
import subprocess
import winreg
import ctypes

def find_process(name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == name.lower():
            return proc.info['pid']
    return None

def bring_to_top(app_name):
    try:
        app_handle = ctypes.windll.user32.FindWindowW(None, app_name)
        ctypes.windll.user32.SetForegroundWindow(app_handle)
        ctypes.windll.user32.ShowWindow(app_handle, 5)
        print("Application brought to the top...")
    except Exception as e:
        print("Failed to bring the application to the top:", str(e))

def run_application(app_path):
    try:
        subprocess.Popen(app_path)
        print("Application launched.")
    except subprocess.CalledProcessError:
        print("Failed to launch the application.")

def get_app_path(app_name):
    app_path = None
    try:
        uninstall_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
        num_subkeys = winreg.QueryInfoKey(uninstall_key)[0]

        for i in range(num_subkeys):
            subkey_name = winreg.EnumKey(uninstall_key, i)
            subkey = winreg.OpenKey(uninstall_key, subkey_name)
            try:
                display_name = winreg.QueryValueEx(subkey, 'DisplayName')[0]
                if app_name.lower() in display_name.lower():
                    app_path = winreg.QueryValueEx(subkey, 'InstallLocation')[0]
                    break
            except OSError:
                continue
            finally:
                subkey.Close()

    except OSError:
        pass
    finally:
        uninstall_key.Close()

    return app_path

def search_and_run_app(app_name):
    running_pid = find_process(app_name)
    if running_pid:
        bring_to_top(app_name)
    else:
        app_path = get_app_path(app_name)
        if app_path:
            run_application(app_path)
        else:
            print("Application not found.")

# Example usage
app_name = input("Enter the application name: ")
search_and_run_app(app_name)
