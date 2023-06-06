def calculate_average2(numbers):
    sum_ = 0
    count = 0
    for i in range(len(numbers)):
        sum_ += numbers[i]
        count += 1
    average = sum_ / count
    return average

# Test the function
nums = [2, 4, 6, 8, 10]
result = calculate_average2(nums)
print("The average is: " + str(result))