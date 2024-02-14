import unittest
from Calc import Calculator

# test_plus(1,5,6)

class Tests(unittest.TestCase):
    def test01(self):
        a = Calculator(1,1)
        """ Check that plus(1,1) = 2 """
        self.assertTrue(a.plus() == 2)

    def test02(self):
        a = Calculator(5,10)
        """ Check that plus(5,10) = 15 """
        self.assertTrue(a.plus() == 15)

if __name__ == "__main__":
    unittest.main()