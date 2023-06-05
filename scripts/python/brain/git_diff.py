import subprocess

from tools.logger import logger


def git_diff(origin, destination):
    command = ['git', 'diff', '--patch', origin, destination]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        diff_output = output.decode('utf-8')
        logger(diff_output)
    except subprocess.CalledProcessError as e:
        logger(f"An error occurred: {e.output.decode('utf-8')}")
        logger(f"An error occurred: {e.output.decode('utf-8')}")


if __name__ == "__main__":
    # Example usage
    file1 = r'C:\Users\sergi\PycharmProjects\Cartuli-AI-Assitant\scripts\python\code_to_be_refactored\ai_refactored\ginea_pig.rfct.py'
    file2 = r'C:\Users\sergi\PycharmProjects\Cartuli-AI-Assitant\scripts\python\code_to_be_refactored\ginea_pig.py'
    git_diff(file1, file2)
