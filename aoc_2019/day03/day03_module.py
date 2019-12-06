class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Wire:
    lines = []

    def __init__(self, coordinates):
        self.coordinates = coordinates
        
def checkIntersections(wire1, wire2):
    return []

def closerIntersection(intersections):
    return ()

def getDistance(point):
    return 0