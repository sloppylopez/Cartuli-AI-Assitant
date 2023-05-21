import hashlib
import os

import openai

from brain.token_counter import count_tokens


def read_files(folder_path):
    # Check if folder_path is a file
    if os.path.isfile(folder_path):
        with open(folder_path, 'rb') as file:
            file_content = file.read()
            file_hash = hashlib.sha256(file_content).hexdigest()
            file_contents = {file_hash: (file_content, os.path.basename(folder_path))}
    else:
        # Read all files in the given folder
        file_contents = {}
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as file:
                    file_content = file.read()
                    file_hash = hashlib.sha256(file_content).hexdigest()
                    file_contents[file_hash] = (file_content, file_name)
    return file_contents


def generate_responses(file_contents):
    # Generate responses for each file content with increasing prompts
    responses = {}
    for file_hash, file_content_tuple in file_contents.items():
        file_content = file_content_tuple[0]
        file_name = file_content_tuple[1]
        prompt = "Refactor this code as a Senior Engineer, avoid shadowing " \
                 "variables from outer scope if possible, respect original code indentation," \
                 "do not rename methods, for example if a methods is called read_files2 do not change it to read_files" \
                 " ```\n" + file_content.decode() + "\n```"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=count_tokens(prompt) * 2,
            temperature=0,
            n=1
        )
        responses[file_name] = response.choices[0].text.strip()
    return responses


def output_responses(responses, folder_path):
    # Check if folder_path is a file
    if os.path.isfile(folder_path):
        folder_path = os.path.dirname(folder_path)

    # Create the "generated" folder
    output_folder = os.path.join(folder_path, "ai_refactored")
    os.makedirs(output_folder, exist_ok=True)

    # Output the resulting files with the responses
    for file_name, response in responses.items():
        base_name, extension = os.path.splitext(file_name)
        output_file = os.path.join(output_folder, base_name + ".rfct" + extension)
        with open(output_file, 'w') as file:
            file.write(response.strip())


# Main script
refactor_path = "C:/Users/sergi/PycharmProjects/Cartuli-AI-Assitant/scripts/python/hands/refactor.py"
file_contents = read_files(refactor_path)
generated_responses = generate_responses(file_contents)
output_responses(generated_responses, refactor_path)