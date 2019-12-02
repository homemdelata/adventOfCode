class UserQuit( Exception ): pass

def intCode(opCode, value1, value2):
    if opCode == 1:
        return value1 + value2
    elif opCode == 2:
        return value1 * value2
    elif opCode == 99:
        raise UserQuit
    else:
        raise ValueError

def program(arrayInput):
    opCode = arrayInput[0]
    positionValue1 = arrayInput[1]
    positionValue2 = arrayInput[2]
    positionResult = arrayInput[3]
    arrayInput[positionResult] = intCode(opCode, arrayInput[positionValue1], arrayInput[positionValue2])
    pass