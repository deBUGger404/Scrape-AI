import unittest
from rk_mylib_test.operations import add, subtract

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

if __name__ == "__main__":
    unittest.main()

from mylib import add, subtract

print(add(2, 3))         # Outputs: 5
print(subtract(5, 2))    # Outputs: 3