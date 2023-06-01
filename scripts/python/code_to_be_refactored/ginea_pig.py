def calculate_average(numbers: list) -> float:
    total = 0
    for number in numbers:
        total += number
    if numbers:
        return total / len(numbers)
    else:
        return 0

# Test the function
nums = [2, 4, 6, 8, 10]
result = calculate_average(nums)
print(f"The average is: {result}")