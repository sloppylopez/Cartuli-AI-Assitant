import unittest

def calculate_average1(numbers: list) -> float:
    total = 0
    for number in numbers:
        total += number
    if numbers:
        return total / len(numbers)
    else:
        return 0

class TestCalculateAverage(unittest.TestCase):
    def test_average_calculation(self):
        nums = [2, 4, 6, 8, 10]
        result = calculate_average1(nums)
        self.assertAlmostEqual(result, 6.0, places=2)

    def test_empty_list(self):
        nums = []
        result = calculate_average1(nums)
        self.assertEqual(result, 0)

    def test_single_number(self):
        nums = [5]
        result = calculate_average1(nums)
        self.assertEqual(result, 5.0)

if __name__ == '__main__':
    unittest.main()
