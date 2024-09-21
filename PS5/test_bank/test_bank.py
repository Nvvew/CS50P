import sys
import os

path = os.path.abspath('../../PS1/bank')
sys.path.append(path)

from bank import value

def test_value():
    assert value('helloworld') == 0
    assert value('happyworld') == 20
    assert value('fuckworld') == 100
    assert value('hell') == 20

