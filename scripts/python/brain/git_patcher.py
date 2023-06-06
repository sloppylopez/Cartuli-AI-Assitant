import os
import subprocess

from eyes.read_file import read_file
from hands.back_up_and_overwrite_file import backup_and_overwrite_file, restore_file_backup
from tools.logger import logger


# def git_diff(destination):
#     # TODO: This is to avoid some error I can't recall. Fix it.
#     os.chdir("C:\\Users\\sergi\\PycharmProjects\\Cartuli-AI-Assitant\\scripts\\python")
#     command = ['git', 'diff', '--patch', destination]
#     try:
#         output = subprocess.check_output(command, stderr=subprocess.STDOUT)
#         diff_output = output.decode('utf-8')
#         logger(diff_output)
#         return diff_output
#     except subprocess.CalledProcessError as e:
#         logger(f"An error occurred: {e.output.decode('utf-8')}")

def git_diff(destination):
    # Get the path of the current script file
    script_path = os.path.abspath(__file__)

    # Modify the path to navigate to the desired directory
    project_path = os.path.dirname(os.path.dirname(script_path))
    target_directory = os.path.join(project_path)

    try:
        # Change the current working directory
        os.chdir(target_directory + "\\code_to_be_refactored")
        # This is to avoid warnings about line endings
        config_command = ['git', 'config', '--global', 'core.autocrlf', 'true']
        config_output = subprocess.check_output(config_command, stderr=subprocess.STDOUT)
        logger(config_output.decode('utf-8'))
        # This is recommended to do by git documentation
        config_command = ['git', 'config', '--global', 'core.eol', 'lf']
        config_output = subprocess.check_output(config_command, stderr=subprocess.STDOUT)
        logger(config_output.decode('utf-8'))

        command = ['git', 'diff', '--patch', destination]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        diff_output = output.decode('utf-8')
        logger(diff_output)
        return diff_output
    except subprocess.CalledProcessError as e:
        logger(f"An error occurred: {e.output.decode('utf-8')}")


def get_patch(to_be_refactored_folder, file_array):
    for file_name in file_array:
        """Get refactored code"""
        refactored_file, backup_file, patch_file = generate_file_variations(file_name.split(".")[0], "." + file_name.split(".")[1])
        ai_refactored_folder = os.path.join(to_be_refactored_folder, "ai_refactored")
        os.makedirs(ai_refactored_folder, exist_ok=True)
        origin = os.path.join(ai_refactored_folder, refactored_file)
        destination = os.path.join(to_be_refactored_folder, file_name)
        destination_backup = os.path.join(to_be_refactored_folder, backup_file)
        ai_refactored_code = read_file(origin)
        """Backup and overwrite file with refactored code, create a patch and restore the original file"""
        backup_and_overwrite_file(destination, ai_refactored_code)
        git_patch = git_diff(destination)
        restore_file_backup(destination_backup, destination)
        patch_file = os.path.join(ai_refactored_folder, patch_file)
        """Write patch to file"""
        if git_patch is not None:
            with open(patch_file, 'w') as file:
                file.write(git_patch)
        logger(f"Patch saved to: {patch_file}")


def generate_file_variations(file_name, extension):
    variations = [
        file_name + '.rfct' + extension,
        file_name + extension + '.bak',
        file_name + extension + '.patch'
    ]
    return variations


if __name__ == "__main__":
    # Example usage
    to_be_refactored_folder = r"C:\Users\sergi\PycharmProjects\Cartuli-AI-Assitant\scripts\python\code_to_be_refactored"
    get_patch(to_be_refactored_folder, ['ginea_pig.py', 'ginea_pig_prime_numbers.py'])
