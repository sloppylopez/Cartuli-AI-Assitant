import math

def calculate_area(radius):
    # Consistent naming convention (snake_case)
    radius_squared = radius * radius
    circle_area = math.pi * radius_squared
    return circle_area

# Function call with an argument
calculate_area(5)

# Type checking or error handling for invalid input
try:
    calculate_area(int(input("Enter a number: ")))
except ValueError:
    print("Invalid input. Please enter a valid number.")