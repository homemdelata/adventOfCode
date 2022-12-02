import os
import sys

from day03_module import Wire, checkIntersections, closerIntersection, getDistance, getLowerSteps

with open(os.path.join(sys.path[0], 'day03_input.txt'), 'r') as inputFile:
    lines = inputFile.read().splitlines()
    wire1 = Wire(lines[0].split(','))
    wire2 = Wire(lines[1].split(','))
    intersections = checkIntersections(wire1, wire2)
    closerPoint = closerIntersection(intersections)
    distance = getDistance(closerPoint)
    print('distancia - parte 1: {}'.format(distance))

    totalSteps = getLowerSteps(wire1, wire2)
    print('passos - parte 2: {}'.format(totalSteps))