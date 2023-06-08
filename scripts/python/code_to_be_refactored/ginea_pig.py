import math


def calculate_area(radius):
    # Flaw: Inconsistent naming convention (should use snake_case)
    Result = 3.14 * radius * radius

    # Flaw: Redundant math module import (math module not required for simple multiplication)
    area = math.pi * radius ** 2

    # Flaw: Hard-coded constant value (should use math.pi instead of 3.14)
    radius_squared = radius * radius
    circle_area = math.pi * radius_squared

    # Flaw: Unused variable (Result is assigned but never used)
    return circle_area


# Flaw: Incorrect parameter type (expects a number, not a string)
calculate_area("5")

# Flaw: No type checking or error handling for invalid input
