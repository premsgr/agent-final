import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 0), 0)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 4), 12)
        self.assertEqual(calc.mul(-2, 5), -10)
        self.assertEqual(calc.mul(0, 7), 0)

if __name__ == "__main__":
    unittest.main()
