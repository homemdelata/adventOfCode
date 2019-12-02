import pytest

from day02_module import intCode
from day02_module import UserQuit

def test_day02_opcode1():
    opCode = 1
    value1 = 2
    value2 = 3
    result = intCode(opCode, value1, value2)
    assert result == 5

def test_day02_opcode2():
    opCode = 2
    value1 = 2
    value2 = 3
    result = intCode(opCode, value1, value2)
    assert result == 6

def test_day02_opcode99():
    with pytest.raises(UserQuit):
        opCode = 99
        value1 = 2
        value2 = 3
        result = intCode(opCode, value1, value2)


def test_day02_opcode_wrong():
    array = [3,2,3,3]
    with pytest.raises(ValueError):
        opCode = 30
        value1 = 2
        value2 = 3
        result = intCode(opCode, value1, value2)
