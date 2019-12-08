

def hasDouble(password):
    double = False
    currentNumber = password[0]
    for number in password[1:]:
        if currentNumber == number:
            double = True
        currentNumber = number
    return double


def neverDecrease(password):
    never = True
    currentNumber = int(password[0])
    for letter in password[1:]:
        number = int(letter)
        if number < currentNumber:
            never = False
        currentNumber = number
    return never

def isValidPassword(password):
    return hasDouble(password) and neverDecrease(password)
