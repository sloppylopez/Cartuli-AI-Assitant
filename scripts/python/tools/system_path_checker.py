import re


def is_system_path(path):
    pattern = r'^[a-zA-Z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*$'
    match = re.match(pattern, path)
    return match is not None


if __name__ == "__main__":
    # Test the function
    path = r'c:\users\sergi\pycharmprojects\cartuli'
    print(is_system_path(path))  # Output: True

    path = r'/users/sergi/pycharmprojects/cartuli'
    print(is_system_path(path))  # Output: False
