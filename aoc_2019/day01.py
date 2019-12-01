import os
import sys

from day01_module import calculateFuel
from day01_module import calculateTotalModuleFuel

fuelRequirementPartOne = 0

with open(os.path.join(sys.path[0], 'day01_input.txt'), 'r') as inputFile:
    lines = inputFile.read().splitlines()
    for line in lines:
        fuelRequirementPartOne += calculateFuel(int(line))

print(fuelRequirementPartOne)

fuelRequirementPartTwo = 0

with open(os.path.join(sys.path[0], 'day01_input.txt'), 'r') as inputFile:
    lines = inputFile.read().splitlines()
    for line in lines:
        fuelRequirementPartTwo += calculateTotalModuleFuel(int(line))

print(fuelRequirementPartTwo)
