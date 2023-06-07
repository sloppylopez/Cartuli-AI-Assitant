def detect_line_separator(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    if b'\r\n' in data:
        return 'CRLF'
    elif b'\n' in data:
        return 'LF'
    else:
        return 'Unknown'
