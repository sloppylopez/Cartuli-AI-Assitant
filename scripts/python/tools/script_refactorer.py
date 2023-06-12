# Prompt:
def refactor_script_prompt(script):
    """
    Refactors the given script by fixing several flaws.

    Args:
        script (str): The original script to be refactored.

    Returns:
        str: The refactored script.
    """

    refactored_script = ""
    # Your code goes here

    return refactored_script


# Test case:
original_script = '''
Python Script:

def my_function():
  x = 5
  y = 10
  if x > y:
    print("x is greater than y") # This should use an else statement
  else:
    print("y is greater than x")
'''

if __name__ == '__main__':
    refactor_prompt = refactor_script_prompt(original_script)
    print(refactor_prompt)
