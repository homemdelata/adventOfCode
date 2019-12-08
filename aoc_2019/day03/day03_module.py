class Coordinate():

    def getCoordinateDistance(self, coordinate):
        return int(coordinate[1:])
    
    def __init__(self, coordinateString):
        self.direction = coordinateString[0]
        self.distance = self.getCoordinateDistance(coordinateString)
    
class Wire:
    points = []
    lines = []

    def getNextPoint(self, point, coordinate):
        newPoint = ()
        if coordinate.direction == "R":
            newPoint = (point[0] + coordinate.distance, point[1])
        elif coordinate.direction == "L":
            newPoint = (point[0] - coordinate.distance, point[1])
        elif coordinate.direction == "U":
            newPoint = (point[0], point[1] + coordinate.distance)
        elif coordinate.direction == "D":
            newPoint = (point[0], point[1] - coordinate.distance)
        return newPoint

    def buildWirePoints(self, coordinatesString):
        points = []
        points.append((0,0))
        for coordinateString in coordinatesString:
            coordinate = Coordinate(coordinateString)
            lastPoint = points[-1]
            nextPoint = self.getNextPoint(lastPoint, coordinate)
            points.append(nextPoint)
        return points
    
    def getLines(self, points):
        lines = []
        for x in range(len(points)-1):
            line = (points[x], points[x+1])
            lines.append(line)
        return lines

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.points = self.buildWirePoints(coordinates)
        self.lines = self.getLines(self.points)

def isLineHorizontal(line):
    point1 = line[0]
    point2 = line[1]
    return point1[0] - point2[0] != 0

def lineIntersection(line1, line2):
    #se as duas forem horizontais, não tem intersecção
    if isLineHorizontal(line1) and isLineHorizontal(line2):
        return False

    #se as duas forem verticais, não tem intersecção
    if not isLineHorizontal(line1) and not isLineHorizontal(line2):
        return False

    if isLineHorizontal(line1):
        horizontalLine = line1
        verticalLine = line2
    else:
        horizontalLine = line2
        verticalLine = line1

    #verifica se tem intersecção no X
    if verticalLine[0][0] in range(horizontalLine[0][0], horizontalLine[1][0], 1 if horizontalLine[0][0] <= horizontalLine[1][0] else -1):
        intersectionX = verticalLine[0][0]
    else:
        return False

    #verifica se tem intersecção no y
    if horizontalLine[0][1] in range(verticalLine[0][1], verticalLine[1][1], 1 if verticalLine[0][1] <= verticalLine[1][1] else -1):
        intersectionY = horizontalLine[0][1]
    else:
        return False

    #se uma for horizontal e outra vertical, verifica se tem intersecção
    return (intersectionX, intersectionY)


def checkIntersections(wire1, wire2):
    wire1Lines = wire1.lines
    wire2Lines = wire2.lines
    intersections = []
    for line1 in wire1Lines:
        for line2 in wire2Lines:
            intersection = lineIntersection(line1, line2)
            if intersection:
                intersections.append(intersection)
    #remove o (0,0)
    if (0,0) in intersections: intersections.remove((0,0))
    return intersections

def closerIntersection(intersections):
    closer = intersections[0]
    for intersection in intersections[1:]:
        if getDistance(intersection) < getDistance(closer):
            closer = intersection
    return closer

def getDistance(point):
    a = point[0] if point[0] > 0 else -point[0]
    b = point[1] if point[1] > 0 else -point[1]
    return a + b

def isPointInLine(point, line):
    isXInLine = True
    isYInLine = True

    point_X = point[0]
    point_Y = point[1]

    linePoint_1_X = line[0][0]
    linePoint_1_Y = line[0][1]

    linePoint_2_X = line[1][0]
    linePoint_2_Y = line[1][1]

    if isLineHorizontal(line):
        isXInLine = point_X in range(linePoint_1_X, linePoint_2_X, 1 if linePoint_1_X <= linePoint_2_X else -1)
        isYInLine = point_Y == linePoint_1_Y
    else:
        isXInLine = point_X == linePoint_1_X
        isYInLine = point_Y in range(linePoint_1_Y, linePoint_2_Y, 1 if linePoint_1_Y <= linePoint_2_Y else -1)
    return isXInLine and isYInLine


def getSteps(wire, point):
    steps = 0
    points = wire.points
    coordinates = wire.coordinates
    lines = wire.lines
    

    index = 0
    currentPoint = points[index]
    line = lines[index]
    while not isPointInLine(point, line):
        coordinate = Coordinate(coordinates[index])
        steps += coordinate.distance
        index += 1
        currentPoint = points[index]
        line = lines[index]
    #adiciona os passos até o ponto
    steps += abs(currentPoint[0]-point[0]) + abs(currentPoint[1]-point[1])

    return steps

def getLowerSteps(wire1, wire2):
    intersections = checkIntersections(wire1, wire2)
    lowerSteps = None
    for intersection in intersections:
        steps = getSteps(wire1, intersection) + getSteps(wire2, intersection)
        if lowerSteps is None or steps < lowerSteps:
            lowerSteps = steps


    return lowerSteps