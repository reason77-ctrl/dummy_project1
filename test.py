import unittest

class TestCalculator(unittest.TestCase):

    def test_addition_int(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_sub(self):
        a = 5
        b = 3
        result = a-b
        self.assertEqual(result, 2)

    def test_multiply(self):
        a = 5
        b = 3
        result = a*b
        self.assertEqual(result, 15)

    def test_divide(self):
        a = 10
        b = 2
        result = a/b
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()