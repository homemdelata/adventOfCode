from day04_module import isValidPassword, isValidPasswordPart2

validRange = range(124075,580769)

passwordQuantity = 0

for password in validRange:
    strPassword = str(password)
    if isValidPassword(strPassword):
        passwordQuantity += 1

print('Possible passwords in part 1: {}'.format(passwordQuantity))

passwordQuantity = 0

for password in validRange:
    strPassword = str(password)
    if isValidPasswordPart2(strPassword):
        passwordQuantity += 1

print('Possible passwords in part 2: {}'.format(passwordQuantity))
