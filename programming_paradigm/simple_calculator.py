import unittest
from test_simple_calculator import SimpleCalculator

class Test(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        result = self.calc.add(2,3)
        self.assertEqual(result, 5)

        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)

    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calc.divide(4, 2)
        self.assertEqual(result, 2)

        with self.assertRaises(ValueError):
            self.calc.divide(3, 0)


if __name__ == "__main__":
    unittest.main()