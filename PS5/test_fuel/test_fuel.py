import sys
import os
import pytest

path = os.path.abspath('../../PS3/fuel')
sys.path.append(path)

from fuel import convert

def test_normal():
    assert convert('13/97') == '13%'
    assert convert('100/200') == '50%'
    assert convert('3/99') == '3%'

def test_value():
    with pytest.raises(ValueError):
        convert('15/11')
        convert('3.5/4.9')

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('13/0')

def test_ef():
    assert convert('3/576') == 'E'
    assert convert('348/349') == 'F'