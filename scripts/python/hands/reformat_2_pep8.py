import autopep8
import os

from tools.logger import logger


def replace_string_lf_with_crlf(input_string):
    crlf_string = input_string.replace('\n', '\r\n')
    return crlf_string


def replace_file_lf_with_crlf(file_path):
    # Read the file
    with open(file_path, 'rb') as file:
        content = file.read()

    # Replace LF with CRLF
    updated_content = content.replace(b'\n', b'\r\n')

    # Write the updated content back to the file
    with open(file_path, 'wb') as file:
        file.write(updated_content)


def replace_file_crlf_to_lf(file_path):
    temp_file = file_path + '.tmp'

    with open(file_path, 'rb') as input_file, open(temp_file, 'wb') as output_file:
        for line in input_file:
            line = line.replace(b'\r\n', b'\n')
            output_file.write(line)

    # Replace the original file with the temporary file
    os.replace(temp_file, file_path)
    print("Line endings converted successfully.")


def replace_string_crlf_with_lf(input_string):
    lf_string = input_string.replace('\r\n', '\n')
    return lf_string


def format_code(code):
    # logger(code)
    formatted_code = autopep8.fix_code(code)
    # logger(formatted_code)
    cleaned_code = formatted_code.replace('\r', '')
    cleaned_code = cleaned_code.replace('\r\n', '')
    cleaned_code = cleaned_code.replace('\n\n', '\n')
    # logger(cleaned_code)
    return cleaned_code


if __name__ == "__main__":
    code = '''def is_prime(number):

    """Check if a number is prime or not"""

    if number <= 1:

        return False

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:

            return False

    return True'''
    format_code(code)

# code = '''def is_prime(number):
#
# """Check if a number is prime or not"""
#
# if number <= 1:
#
# return False
#
# for i in range(2, int(number ** 0.5) + 1):
#
# if number % i == 0:
#
# return False
#
# return True'''
#
# print(code)
#
# # Indent the code using autopep8
# formatted_code = autopep8.fix_code(code)
#
# print(formatted_code)
