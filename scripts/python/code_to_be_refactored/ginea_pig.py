import math


def calculate_area(radius):
    # Flaw 1: Inconsistent naming convention (should use snake_case)
    Result = 3.14 * radius * radius

    # Flaw 2: Redundant math module import (math module not required for simple multiplication)
    area = math.pi * radius ** 2

    # Flaw 3: Hard-coded constant value (should use math.pi instead of 3.14)
    radius_squared = radius * radius
    circle_area = math.pi * radius_squared

    # Flaw 4: Unused variable (Result is assigned but never used)
    return circle_area


# Flaw 5: Missing function call with an argument
calculate_area()

# Flaw 6: Incorrect parameter type (expects a number, not a string)
calculate_area("5")

# Flaw 7: No type checking or error handling for invalid input
