import json
import os

import openai

from brain.compare_dictionaries import return_non_matching_values
from brain.token_counter import count_tokens
from eyes.read_json_file import read_files_and_hash, read_json_file
from hands.get_image import get_full_from_relative
from tools.logger import logger

# Read long term memory, to see which files have been refactored already
hidden_folder_path = get_full_from_relative("../.cartuli")
hidden_file_path = os.path.join(hidden_folder_path, "long_term_hash_memory.json")
long_term_hash_memory = read_json_file(hidden_file_path)
# Read the target folder
target_folder_path = get_full_from_relative("../code_to_be_refactored")
target_file_contents = read_files_and_hash(target_folder_path)
# Compare the two dictionaries and get only the non-matching values
non_matching_values = return_non_matching_values(long_term_hash_memory, target_file_contents)
logger(json.dumps(non_matching_values))


def generate_refactored_code(file_contents):
    # Generate responses for each file content with increasing prompts
    responses = {}
    for file_hash, file_content_tuple in file_contents.items():
        file_content = file_content_tuple[0]
        file_name = file_content_tuple[1]
        prompt = "Refactor this code as a Senior Engineer, avoid shadowing " \
                 "variables from outer scope if possible," \
                 "Remember use this rule always 'PEP 8: E305 expected 2 blank " \
                 "lines after class or function definition'," \
                 "make performance improvements and edge cases\n" \
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


def output_responses(responses, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Output the resulting files with the responses
    for file_name, response in responses.items():
        base_name, extension = os.path.splitext(file_name)
        if base_name.contains("."):
            output_file = os.path.join(output_folder, base_name + ".rfct" + extension)
        else:  # If it's already a rfct file, don't add the extension
            output_file = os.path.join(output_folder, base_name + extension)
        with open(output_file, 'w') as file:
            file.write(response.strip())


def refactor_files(long_term_hash_memory):
    # Generate the refactored code from non-matching values
    refactored_codes = generate_refactored_code(
        non_matching_values or long_term_hash_memory)  # Use the JSON string here
    # Create the "ai_refactored" folder in the same directory as the target folder
    output_folder = os.path.join(target_folder_path, "ai_refactored")
    # Output the refactored code
    output_responses(refactored_codes, output_folder)
    # Update the long term memory
    file_contents_json = json.dumps(read_files_and_hash(output_folder))  # Convert dictionary to JSON string
    # Write the long term memory to the hidden folder
    os.makedirs(hidden_folder_path, exist_ok=True)
    with open(hidden_file_path, "w") as file:
        file.write(file_contents_json)


if non_matching_values is not None and \
        len(non_matching_values) > 0:
    refactor_files(long_term_hash_memory)
else:
    user_input = input("No new files to refactor, do you want to do the refactor anyway? y/n: ")
    if user_input.lower() == "y":
        refactor_files(long_term_hash_memory)
