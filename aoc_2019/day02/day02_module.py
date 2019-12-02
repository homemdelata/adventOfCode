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
    pass