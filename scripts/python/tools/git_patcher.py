import os
import subprocess

from eyes.read_file import read_file
from hands.back_up_and_overwrite_file import backup_and_overwrite_file, restore_file_backup
from hands.get_image import get_full_from_relative
from hands.reformat_2_pep8 import replace_file_crlf_to_lf
from tools.logger import logger


def git_diff(destination):
    try:
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
        file_name_split = file_name.split(".")
        refactored_file, backup_file, patch_file = generate_file_variations(file_name_split[0],
                                                                            "." + file_name_split[1])
        ai_refactored_folder = os.path.join(to_be_refactored_folder, ".ai_refactored")
        os.makedirs(ai_refactored_folder, exist_ok=True)
        origin = os.path.join(ai_refactored_folder, refactored_file)
        destination = os.path.join(to_be_refactored_folder, file_name)
        destination_backup = os.path.join(to_be_refactored_folder, backup_file)
        ai_refactored_code = read_file(origin)
        """Backup and overwrite file with refactored code, create a patch and restore the original file"""
        backup_and_overwrite_file(destination, ai_refactored_code)
        """Replace LF with CRLF to avoid randomness in the diff patch"""
        replace_file_crlf_to_lf(to_be_refactored_folder + "\\" + file_name)
        """Get git diff patch"""
        git_patch = git_diff(destination)
        """Write patch to file"""
        save_patch(ai_refactored_folder, git_patch, patch_file)
        """Restore original file"""
        restore_file_backup(destination_backup, destination)
        """Replace LF with CRLF to avoid randomness in the diff patch"""
        replace_file_crlf_to_lf(to_be_refactored_folder + "\\" + file_name)


def save_patch(ai_refactored_folder, git_patch, patch_file):
    if git_patch is not None:
        patch_file = os.path.join(ai_refactored_folder, patch_file)
        if git_patch is not None:
            with open(patch_file, 'w') as file:
                file.write(git_patch)
        logger(f"Patch saved to: {patch_file}")
    else:
        logger("No patch generated")


def generate_file_variations(file_name, extension):
    return [
        file_name + '.rfct' + extension,
        file_name + extension + '.bak',
        file_name + extension + '.patch'
    ]


if __name__ == "__main__":
    # Example usage
    to_be_refactored_folder = get_full_from_relative(r"..\code_to_be_refactored")
    get_patch(to_be_refactored_folder, ['ginea_pig.py'])
