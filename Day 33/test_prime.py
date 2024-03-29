import unittest
import is_prime

class TestPrimes(unittest.TestCase):
    def test_primes(self):
        self.assertEqual(is_prime.is_prime(1), True)
        self.assertEqual(is_prime.is_prime(2), True)
        self.assertEqual(is_prime.is_prime(3), True)
        self.assertEqual(is_prime.is_prime(4), False)
        self.assertEqual(is_prime.is_prime(5), True)
        self.assertEqual(is_prime.is_prime(6), False)
        self.assertEqual(is_prime.is_prime(7), True)


if __name__ == '__main__':
    unittest.main()
