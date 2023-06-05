import json
import os

import autopep8
import openai

from brain.dict_comparator import return_non_matching_values
from brain.token_counter import count_tokens
from eyes.read_json_file import read_files_and_hash, read_json_file
from hands.get_image import get_full_from_relative
from hands.reformat_2_pep8 import format_code
from hands.transform_list_to_dict import list_2_dict
from tools.logger import logger


def generate_refactored_code(file_contents):
    # Generate responses for each file content with increasing prompts
    responses = {}
    try:
        for file_hash, file_content_tuple in file_contents.items():
            file_content = file_content_tuple[0]
            file_name = file_content_tuple[1]
            prompt = "Refactor the given Python code to adhere to PEP 8 guidelines. " \
                     "Make sure to not modify any existing comments or explanations from the code. " \
                     "Never ever add the special char '\\r' for indentation between lines, this is important." \
                     "Do not include comments or explanations in the refactored code.\n" \
                     "Code:" \
                     " \n" + file_content + "\n"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=count_tokens(prompt) * 2,
                temperature=0,
                n=1
            )
            logger("Usage of the request:\n" + str(response.usage))
            responses[file_name] = format_code(response.choices[0].text.strip())
    except Exception as e:
        print(e)
    return responses


def output_responses(responses, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Output the resulting files with the responses
    for file_name, response in responses.items():
        base_name, extension = os.path.splitext(file_name)
        if ".rfct" in base_name:  # If it's already a rfct file, don't add the extension
            output_file = os.path.join(output_folder, base_name + extension)
        else:
            output_file = os.path.join(output_folder, base_name + ".rfct" + extension)
        with open(output_file, 'w') as file:
            file.write(response.strip())


def refactor_files(target_file_contents):
    # Generate the refactored code from non-matching values
    refactored_codes = generate_refactored_code(target_file_contents)
    # Create the "ai_refactored" folder in the same directory as the target folder
    output_folder = os.path.join(target_folder_path, "ai_refactored")
    # Output the refactored code
    output_responses(refactored_codes, output_folder)
    # Update the long term memory
    output_content = read_files_and_hash(output_folder)
    # Remove ".rfct" from the file names
    # for key in output_content:
    #     file_name = output_content[key][1]
    #     if file_name.endswith(".rfct.py"):
    #         output_content[key][1] = file_name[:-8] + ".py"
    # Convert the tuples to lists for modification
    # updated_data = [
    #     (key, value[0], value [1][:-8] + ".py") if value[1].endswith(".rfct.py") else (key, value[0], value[1]) for
    #     key, value in output_content.items()]
    file_contents_json = json.dumps(output_content)  # Convert dictionary to JSON string
    # Write the long term memory to the hidden folder
    os.makedirs(hidden_folder_path, exist_ok=True)
    with open(hidden_file_path, "w") as file:
        file.write(file_contents_json)


def refactor_destination(target_folder_relative_path):
    global hidden_folder_path, hidden_file_path, target_folder_path, non_matching_values
    # Read long term memory, to see which files have been refactored already
    hidden_folder_path = get_full_from_relative("../.cartuli")
    hidden_file_path = os.path.join(hidden_folder_path, "long_term_hash_memory.json")
    long_term_hash_memory = read_json_file(hidden_file_path)
    # Read the target folder
    target_folder_path = get_full_from_relative(target_folder_relative_path)
    target_file_contents = read_files_and_hash(target_folder_path)
    # Compare the two dictionaries and get only the non-matching values
    non_matching_values = return_non_matching_values(long_term_hash_memory, target_file_contents)
    if len(non_matching_values) > 0:
        logger("Non matching values:\n" + json.dumps(non_matching_values))
    if non_matching_values is not None and \
            len(non_matching_values) > 0 or \
            len(long_term_hash_memory) == 0:
        refactor_files(non_matching_values)
    else:
        # user_input = input("No new files to refactor, do you want to do the refactor anyway? y/n: ")
        # if user_input.lower() == "y":
        refactor_files(long_term_hash_memory)


if __name__ == "__main__":
    refactor_destination("../code_to_be_refactored")
