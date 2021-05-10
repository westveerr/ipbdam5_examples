import unittest
from count import add_values

class TestCountMethods(unittest.TestCase):

    def test_outcome(self):
        value1 = 3
        value2 = 3

        result = add_values(value1, value2)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
