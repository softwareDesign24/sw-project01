import pytest
from Calc import Calculator

# test_plus(1,5,6)
def test01():
    a = Calculator(1,1)
    """ Check that plus(1,1) = 2 """
    assert a.plus() == 2

def test02():
    a = Calculator(5,10)
    """ Check that plus(5,10) = 15 """
    assert a.plus() == 15