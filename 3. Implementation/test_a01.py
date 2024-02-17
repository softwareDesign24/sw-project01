import pytest
from Calc import Calculator

# ...
def test_01():
    a = Calculator(1,1)
    """ Check that plus(1,1) = 2 """
    assert a.plus() == 2

def test_02():
    a = Calculator(5,10)
    """ Check that plus(5,10) = 15 """
    assert a.plus() == 1