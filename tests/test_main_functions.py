'''
    Test the functions of Main application
'''

import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../src"))
from game import get_place_args


def test_valid_place_input():
    expected_result = ((0,0),'EAST')
    actual_result = get_place_args('0,0,EAST')
    assert actual_result == expected_result

def test_invalid_x_coordinate():
    try:
        get_place_args('X,0,EAST')
        assert False
    except:
        assert True

def test_invalid_y_coordinate():
    try:
        get_place_args('0,Y,EAST')
        assert False
    except:
        assert True

def test_invalid_direction():
    try:
        get_place_args('0,0,DOWN')
        assert False
    except:
        assert True

def test_incomplete_param():
    try:
        get_place_args('0,0')
        assert False
    except:
        assert True
