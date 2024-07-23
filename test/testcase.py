import unittest
from add import addition  # Assuming 'addition' is defined in 'addition_program.py'

class TestAdditionFunction(unittest.TestCase):

    def test_addition_positive_numbers(self):
        result = addition(3, 5)
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        result = addition(-3, -5)
        self.assertEqual(result, -8)

    def test_addition_mixed_numbers(self):
        result = addition(2.5, 3.5)
        self.assertAlmostEqual(result, 6.0, places=1)

    def test_addition_zero(self):
        result = addition(0, 0)
        self.assertEqual(result, 0)

        

if __name__ == '__main__':
    unittest.main()
