"""
testing for the math.py module

"""

import fcm
import pytest

def test_add():
    assert fcm.math.add(4,7) == 11
    assert fcm.math.add(3,7) == 10
