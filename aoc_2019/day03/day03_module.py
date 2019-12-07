class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Wire:
    points = []
    lines = []

    def getNextPoint(self, point, coordinate):
        direction = coordinate[0]
        distance = int(coordinate[1:])
        newPoint = ()
        if direction == "R":
            newPoint = (point[0] + distance, point[1])
        elif direction == "L":
            newPoint = (point[0] - distance, point[1])
        elif direction == "U":
            newPoint = (point[0], point[1] + distance)
        elif direction == "D":
            newPoint = (point[0], point[1] - distance)
        return newPoint

    def buildWirePoints(self, coordinates):
        points = []
        points.append((0,0))
        for coordinate in coordinates:
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

def isHorizontal(line):
    point1 = line[0]
    point2 = line[1]
    return point1[0] - point2[0] != 0

def lineIntersection(line1, line2):
    #se as duas forem horizontais, não tem intersecção
    if isHorizontal(line1) and isHorizontal(line2):
        return False

    #se as duas forem verticais, não tem intersecção
    if not isHorizontal(line1) and not isHorizontal(line2):
        return False

    if isHorizontal(line1):
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