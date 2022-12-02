

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

def doubleNotInLargeGroup(password):
    if not hasDouble(password):
        return False
    
    repeated = []
    count = 1

    currentNumber = password[0]
    for number in password[1:]:
        if currentNumber == number:
            count += 1
        else:
            repeated.append(count)
            count = 1
        currentNumber = number
    repeated.append(count)
    return 2 in repeated

def isValidPassword(password):
    return hasDouble(password) and neverDecrease(password)

def isValidPasswordPart2(password):
    return hasDouble(password) and neverDecrease(password) and doubleNotInLargeGroup(password)
