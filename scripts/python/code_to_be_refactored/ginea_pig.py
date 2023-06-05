def calculate_average(numbers):
    sum = 0
    count = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
        count = count + 1
    average = sum / count
    return average

# Test the function
nums = [2, 4, 6, 8, 10]
result = calculate_average(nums)
print("The average is: " + str(result))
