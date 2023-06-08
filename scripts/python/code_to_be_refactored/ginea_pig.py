import math

def calculate_area(radius):
    """Use snake_case for consistent naming convention"""
    result = math.pi * radius ** 2
    return result

# Call the function with an argument
calculate_area(5)

# Check for valid parameter type
if not isinstance(radius, (int, float)):
    raise TypeError("Radius must be a number")