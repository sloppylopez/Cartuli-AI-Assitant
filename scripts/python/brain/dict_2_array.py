def dict_2_array(data):
    return [data[key][1] for key in data]


if __name__ == "__main__":
    data = {
        '3462c63bca323787cd0dea8615b028d5db0effa8ea54ce2dae01385c852ddcc8': (
            'def calculate_average(numbers):\r\n    sum_ = 0\r\n    count = 0\r\n    for i in range(len(numbers)):\r\n        sum_ += numbers[i]\r\n        count += 1\r\n    average = sum_ / count\r\n    return average\r\n\r\n# Test the function\r\nnums = [2, 4, 6, 8, 10]\r\nresult = calculate_average(nums)\r\nprint("The average is: " + str(result))',
            'ginea_pig.py'
        ),
        '6678d84e890b527f8d93f07445e07e780dce81ffbf8117908a5087222b5b7aca': (
            'def is_prime(number):\r\n    if number <= 1:\r\n        return False\r\n    for i in range(2, int(number ** 0.5) + 1):\r\n        if number % i == 0:\r\n            return False\r\n    return True\r\n\r\ndef calculate_primes(limit):\r\n    primes = []\r\n    for num in range(2, limit):\r\n        if is_prime(num):\r\n            primes.append(num)\r\n    return primes\r\n\r\nif __name__ == "__main__":\r\n    limit = int(input("Enter the limit (less than 10000): "))\r\n    if limit > 10000:\r\n        print("Limit should be less than 10000")\r\n    else:\r\n        primes = calculate_primes(limit)\r\n        print("Prime numbers up to", limit, "are:")\r\n        print(primes)',
            'ginea_pig_prime_numbers.py'
        )
    }
    file_array = dict_2_array(data)
    print(file_array)
