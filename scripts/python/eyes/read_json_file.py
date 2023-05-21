import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Example usage:
json_file_path = 'C:/Users/sergi/PycharmProjects/Cartuli-AI-Assitant/scripts/python/.cartuli/long_term_hash_memory.json'

json_data = read_json_file(json_file_path)
print(list(json_data.keys())[0])