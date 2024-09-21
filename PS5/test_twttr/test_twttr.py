import sys
import os

path = os.path.abspath('../../PS2/twttr')
sys.path.append(path)

from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

