import shutil
import os


def backup_and_overwrite_file(file_path, new_content):
    # Create a backup by appending '.bak' to the original file name
    backup_path = file_path + '.bak'

    try:
        # Make a backup of the original file
        shutil.copy2(file_path, backup_path)

        # Overwrite the contents of the original file with the new content
        with open(file_path, 'wb') as file:
            file.write(new_content.encode())

        # Perform some operations using the modified file (e.g., printing its contents)
        with open(file_path, 'rb') as file:
            modified_content = file.read()
        print("Modified file content:")
        print(modified_content)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # In case of any error, remove the modified file and restore the backup
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(backup_path):
            shutil.move(backup_path, file_path)
        return


def restore_file_backup(backup_path, file_path):
    # Restore the original file by replacing the modified file with the backup
    shutil.move(backup_path, file_path)
    print("File successfully restored to its original state.")


if __name__ == "__main__":
    # Example usage
    file_path = 'C:\\Users\\sergi\\PycharmProjects\\Cartuli-AI-Assitant\\scripts\\python\\code_to_be_refactored\\ginea_pig.py'
    new_content = 'This is the new content.'

    backup_and_overwrite_file(file_path, new_content)
