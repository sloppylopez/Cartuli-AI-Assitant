def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

# Test the function
nums = [2, 4, 6, 8, 10]
result = calculate_average(nums)
print("The average is: " + str(result))