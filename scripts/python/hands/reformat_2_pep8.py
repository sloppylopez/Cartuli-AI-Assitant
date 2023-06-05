import autopep8

from tools.logger import logger


def format_code(code):
    logger(code)
    formatted_code = autopep8.fix_code(code)
    logger(formatted_code)
    cleaned_code = formatted_code.replace('\r', '')
    cleaned_code = cleaned_code.replace('\r\n', '')
    cleaned_code = cleaned_code.replace('\n\n', '\n')
    logger(cleaned_code)
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
