import pytest

from day02_module import intCode
from day02_module import UserQuit
from day02_module import program

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
    with pytest.raises(ValueError):
        opCode = 30
        value1 = 2
        value2 = 3
        result = intCode(opCode, value1, value2)

def test_day02_testProgram01():
    arrayInput = [1,9,10,3,2,3,11,0,99,30,40,50]
    program(arrayInput)
    assert arrayInput == [3500,9,10,70,2,3,11,0,99,30,40,50]

def test_day02_testProgram02():
    arrayInput = [1,0,0,0,99]
    program(arrayInput)
    assert arrayInput == [2,0,0,0,99]

def test_day02_testProgram03():
    arrayInput = [2,3,0,3,99]
    program(arrayInput)
    assert arrayInput == [2,3,0,6,99]

def test_day02_testProgram04():
    arrayInput = [2,4,4,5,99,0]
    program(arrayInput)
    assert arrayInput == [2,4,4,5,99,9801]

def test_day02_testProgram05():
    arrayInput = [1,1,1,4,99,5,6,0,99]
    program(arrayInput)
    assert arrayInput == [30,1,1,4,2,5,6,0,99]
