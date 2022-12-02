import os
import sys

from day02_module import program


with open(os.path.join(sys.path[0], 'day02_input.txt'), 'r') as inputFile:
    lines = inputFile.read().splitlines()

    arrayInput = list(map(int, lines[0].split(',')))
    program(arrayInput)

    print(arrayInput[0])

    expectedResult = 19690720
    noun = 0
    verb = 0
    for noun in range(99):
        for verb in range(99):
            arrayInput = list(map(int, lines[0].split(',')))
            arrayInput[1] = noun
            arrayInput[2] = verb
            program(arrayInput)
            if arrayInput[0] == expectedResult:
                print('noun: {}'.format(noun))
                print('verb: {}'.format(verb))
                print('result: {}'.format(100 * noun + verb))