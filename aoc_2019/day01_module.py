import math

def calculateFuel(mass):
    fuel = math.floor(mass/3) - 2
    return fuel

def calculateTotalModuleFuel(mass):
    totalModuleFuel = 0
    fuel = calculateFuel(mass)
    while fuel > 0:
        totalModuleFuel += fuel
        fuel = calculateFuel(fuel)
    return totalModuleFuel