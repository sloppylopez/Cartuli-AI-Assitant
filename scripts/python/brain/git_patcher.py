import difflib
import os
import subprocess

from eyes.read_file import read_json_file, read_file_binary, read_file
from hands.back_up_and_overwrite_file import backup_and_overwrite_file, restore_file_backup
from tools.logger import logger


def git_diff(destination):
    os.chdir("C:\\Users\\sergi\\PycharmProjects\\Cartuli-AI-Assitant\\scripts\\python")
    command = ['git', 'diff', '--patch', destination]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        diff_output = output.decode('utf-8')
        logger(diff_output)
        return diff_output
    except subprocess.CalledProcessError as e:
        logger(f"An error occurred: {e.output.decode('utf-8')}")


def get_patch(to_be_refactored_folder):
    ai_refactored_folder = os.path.join(to_be_refactored_folder, "ai_refactored")
    os.makedirs(ai_refactored_folder, exist_ok=True)
    origin = os.path.join(ai_refactored_folder, "ginea_pig_prime_numbers.rfct.py")
    destination = os.path.join(to_be_refactored_folder, "ginea_pig_prime_numbers.py")
    destination_backup = os.path.join(to_be_refactored_folder, "ginea_pig_prime_numbers.py.bak")
    ai_refactored_code = read_file(origin)

    backup_and_overwrite_file(destination, ai_refactored_code)
    git_patch = git_diff(destination)
    restore_file_backup(destination_backup, destination)
    patch_file = os.path.join(ai_refactored_folder, "ginea_pig_prime_numbers.py.patch")

    if git_patch is not None:
        with open(patch_file, 'w') as file:
            file.write(git_patch)
    print(f"Patch saved to: {patch_file}")


if __name__ == "__main__":
    # Example usage
    to_be_refactored_folder = r"C:\Users\sergi\PycharmProjects\Cartuli-AI-Assitant\scripts\python\code_to_be_refactored"
    get_patch(to_be_refactored_folder)
