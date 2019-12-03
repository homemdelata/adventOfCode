import os
import sys

from day02_module import program


with open(os.path.join(sys.path[0], 'day02_input.txt'), 'r') as inputFile:
    lines = inputFile.read().splitlines()

    arrayInput = list(map(int, lines[0].split(',')))
    program(arrayInput)

    print(arrayInput[0])