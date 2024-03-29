# Day 35: Write a simple unit test for a function that adds two numbers
import unittest
import add_nums


class TestPrimes(unittest.TestCase):
    def test_sum1(self):
        self.assertEqual(add_nums.add_nums(1, 2), 3)

    def test_sum2(self):
        self.assertEqual(add_nums.add_nums(0, 0), 0)

    def test_sum3(self):
        self.assertEqual(add_nums.add_nums(9, 9), 18)


if __name__ == '__main__':
    unittest.main()
