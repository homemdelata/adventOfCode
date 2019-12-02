class UserQuit( Exception ): pass

def intCode(opCode, value1, value2):
    if opCode == 1:
        return 0
    elif opCode == 2:
        return 0
    elif opCode == 99:
        raise UserQuit
    else:
        raise ValueError