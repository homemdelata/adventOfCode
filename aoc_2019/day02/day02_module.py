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
    iteration = 0
    position = 0
    while position + 4 < len(arrayInput):
        opCode = arrayInput[position + 0]
        positionValue1 = arrayInput[position + 1]
        positionValue2 = arrayInput[position + 2]
        positionResult = arrayInput[position + 3]
        value1 = arrayInput[positionValue1]
        value2 = arrayInput[positionValue2]
        try:
            arrayInput[positionResult] = intCode(opCode, value1, value2)
        except UserQuit:
            break
        iteration += 1
        position = iteration * 4
    pass