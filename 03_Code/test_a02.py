import pytest
from Calc import Calculator

# ...
def test_03():
    a = Calculator(1,2)
    """ Check that plus(1,2) = 3 """
    assert a.plus() == 3
