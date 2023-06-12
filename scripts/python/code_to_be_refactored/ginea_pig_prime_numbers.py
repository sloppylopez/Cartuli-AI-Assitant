def is_prime(number):
    """Check if a number is prime or not"""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def calculate_primes(limit):
    """Calculate prime numbers up to a given limit"""
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    limit = int(input("Enter the limit (less than 10000): "))
    if limit > 10000:
        print("Limit should be less than 10000")
    else:
        primes = calculate_primes(limit)
        print(f"Prime numbers up to {limit} are:")
        print(*primes, sep=', ')
