import winreg


def get_installed_apps():
    app_list = []

    # Open the registry key for installed applications
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    # Enumerate through subkeys to retrieve application information
    for i in range(winreg.QueryInfoKey(key)[0]):
        subkey_name = winreg.EnumKey(key, i)
        subkey = winreg.OpenKey(key, subkey_name)

        try:
            # Read the DisplayName and InstallLocation values
            app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
            install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]

            # Append the app name and install location to the app_list
            app_list.append((app_name, install_location))
        except FileNotFoundError:
            pass

    # Close the registry key
    winreg.CloseKey(key)

    return app_list


# Get the list of installed applications with their installation paths
installed_apps = get_installed_apps()

# Print the list of installed applications with their installation paths
for app, path in installed_apps:
    print("App Name:", app)
    print("Installation Path:", path)
    print()
