import os


def search_folders(directory, keyword):
    matches = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.endswith('.git')
                   and not d.endswith('.idea')
                   and not d.endswith('__pycache__')
                   and not d.endswith('venv')]
        for folder in dirs:
            if keyword.lower() in folder.lower():
                folder_path = os.path.join(root, folder)
                matches.append(folder_path)
    return matches


if __name__ == '__main__':
    target_keyword = "mo"
    search_directory = "C:\\Users\\sergi\\PycharmProjects\\Cartuli-AI-Assitant"

    result = search_folders(search_directory, target_keyword)
    print(result)
