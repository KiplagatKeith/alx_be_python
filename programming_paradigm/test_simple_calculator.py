import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        #result = self.calc.add(2,3)
        self.assertEqual(self.calc.add(2,3), 5)

        #result = self.calc.add(-1, 1)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        #result = self.calc.subtract(5, 3)
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiplication(self):
        #result = self.calc.multiply(2, 3)
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_division(self):
        #result = self.calc.divide(4, 2)
        self.assertEqual(self.calc.divide(4, 2), 2)

        with self.assertRaises(ValueError):
            self.calc.divide(3, 0)


if __name__ == "__main__":
    unittest.main()