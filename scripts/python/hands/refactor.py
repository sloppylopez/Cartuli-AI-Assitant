import hashlib
import json
import os

import openai

from brain.compare_dictionaries import compare_dictionaries
from brain.token_counter import count_tokens


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


def read_file(file_path):
    # Check if folder_path is a file
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file_to_read:
            file_content = file_to_read.read()
    return file_content


def generate_responses(file_contents):
    # Generate responses for each file content with increasing prompts
    responses = {}
    for file_hash, file_content_tuple in file_contents.items():
        file_content = file_content_tuple[0]
        file_name = file_content_tuple[1]
        prompt = "Refactor this code as a Senior Engineer, avoid shadowing " \
                 "variables from outer scope if possible, respect original code indentation," \
                 "do not rename methods, for example if a methods is called read_files2 do not change it to read_files" \
                 " ```\n" + file_content + "\n```"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=count_tokens(prompt) * 2,
            temperature=0,
            n=1
        )
        responses[file_name] = response.choices[0].text.strip()
    return responses


def output_responses(responses, folder_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Output the resulting files with the responses
    for file_name, response in responses.items():
        base_name, extension = os.path.splitext(file_name)
        output_file = os.path.join(output_folder, base_name + ".rfct" + extension)
        with open(output_file, 'w') as file:
            file.write(response.strip())


hidden_folder_path = "C:/Users/sergi/PycharmProjects/Cartuli-AI-Assitant/scripts/python/.cartuli"
hidden_file_path = os.path.join(hidden_folder_path, "long_term_hash_memory.json")
long_term_hash_memory = read_files_and_hash(hidden_file_path)
target_folder_path = "C:/Users/sergi/PycharmProjects/Cartuli-AI-Assitant/scripts/python/code_to_be_refactored"
target_file_contents = read_files_and_hash(target_folder_path)
matching_values = compare_dictionaries(long_term_hash_memory, target_file_contents)
print(matching_values)
generated_responses = generate_responses(target_file_contents)  # Use the JSON string here
# Check if folder_path is a file
if os.path.isfile(target_folder_path):
    folder_path = os.path.dirname(target_folder_path)
# Create the "generated" folder
output_folder = os.path.join(target_folder_path, "ai_refactored")
output_responses(generated_responses, target_folder_path, output_folder)
long_term_hash_memory = read_files_and_hash(output_folder)
file_contents_json = json.dumps(long_term_hash_memory)  # Convert dictionary to JSON string
os.makedirs(hidden_folder_path, exist_ok=True)
with open(hidden_file_path, "w") as file:
    file.write(file_contents_json)
