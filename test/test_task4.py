import unittest
from unittest.mock import patch
from io import StringIO
import string
import random
from task4 import generate_password  # Import your generate_password function

class TestGeneratePassword(unittest.TestCase):

    def test_valid_input(self):
        # Test with a valid input (length = 10)
        with patch('builtins.input', return_value='10'):
            password = generate_password()
            self.assertEqual(len(password), 10)
            self.assertTrue(any(c.isupper() for c in password))
            self.assertTrue(any(c.islower() for c in password))
            self.assertTrue(any(c in "#.@!" for c in password))
            self.assertTrue(any(c.isdigit() for c in password))

    def test_invalid_input_too_low(self):
        # Test with an invalid input (length = 4)
        with patch('builtins.input', return_value='4'):
            password = generate_password()
            self.assertIsNone(password)

    def test_invalid_input_too_high(self):
        # Test with an invalid input (length = 20)
        with patch('builtins.input', return_value='20'):
            password = generate_password()
            self.assertIsNone(password)

if __name__ == '__main__':
    unittest.main()
