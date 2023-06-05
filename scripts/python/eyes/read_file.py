import hashlib
import json
import os

from tools.logger import logger


def read_json_file(file_path):
    data = {}
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except Exception as e:
        logger(f"Could not read file {file_path}; {e}")
        pass
    return data


def read_files_and_hash(folder_path):
    # Check if folder_path is a file
    if os.path.isfile(folder_path):
        with open(folder_path, 'rb') as file_to_refactor:
            file_content = file_to_refactor.read()
            file_hash = hashlib.sha256(file_content).hexdigest()
            file_contents = {file_hash: (file_content.decode(), os.path.basename(folder_path))}
    else:
        # Read all files in the given folder
        file_contents = {}
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as file_to_refactor:
                    file_content = file_to_refactor.read()
                    file_hash = hashlib.sha256(file_content).hexdigest()
                    file_contents[file_hash] = (file_content.decode(), file_name)
    return file_contents


def read_file_binary(file_path):
    # Check if folder_path is a file
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file_to_read:
            file_content = file_to_read.read()
    return file_content


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except IOError:
        print(f"Error: Could not read file '{file_path}'")


if __name__ == "__main__":
    # Example usage:
    json_file_path = 'C:/Users/sergi/PycharmProjects/Cartuli-AI-Assitant/scripts/python/.cartuli/long_term_hash_memory.json'
    json_data = read_json_file(json_file_path)
    print(list(json_data.keys())[0])
