import pytest

from day03_module import Wire, checkIntersections, closerIntersection, getDistance

testWireData = [
        (
            ("R8","U5","L5","D3"),
            [
                (0,0),
                (8,0),
                (8,5),
                (3,5),
                (3,2)
            ]
        ),
        (
            ("U7","R6","D4","L4"),
            [
                (0,0),
                (0,7),
                (6,7),
                (6,3),
                (2,3)
            ]
        )
]

testWireIds = [
    "teste de pontos 1",
    "teste de pontos 2"
]

@pytest.mark.parametrize("coordinates, expectedResult", testWireData, ids=testWireIds)
def test_day03_testWire(coordinates, expectedResult):
    testWire = Wire(coordinates)
    assert testWire.points == expectedResult

testIntersectionData = [
        (
            [
                ("R8","U5","L5","D3"),
                ("U7","R6","D4","L4")
            ]
            ,[
                (3,3),
                (6,5)
            ]
        )
]

testIntersectionIds = [
    "teste de intersecção 1"
]

@pytest.mark.parametrize("coordinates, expectedResult", testIntersectionData, ids=testIntersectionIds)
def test_day03_testIntersection(coordinates, expectedResult):
    testWire1 = Wire(coordinates[0])
    testWire2 = Wire(coordinates[1])
    intersections = checkIntersections(testWire1, testWire2)
    result = True
    for intersection in intersections:
        result = result and (intersection in expectedResult)

    assert  result

testCloserIntersectionData = [
    (
        [
            (3,3),
            (6,5)
        ],
        (3,3)
    ),
    (
        [
            (8,9),
            (6,5)
        ],
        (6,5)
    ),
    (
        [
            (2,2),
            (-1,-1)
        ],
        (-1,-1)
    )
]

testCloserIntersectionIds = [
    "teste de proximidade 1",
    "teste de proximidade 2",
    "teste de proximidade 3"
]

@pytest.mark.parametrize("intersections, expectedResult", testCloserIntersectionData, ids=testCloserIntersectionIds)
def test_day03_testCloserIntersection(intersections, expectedResult):
    assert closerIntersection(intersections) == expectedResult

testDistanceFromPointData = [
    (
        (3,3),
        6
    ),
    (
        (8,7),
        15
    ),
    (
        (-1,-3),
        4
    ),
    (
        (3,-7),
        10
    )
]

testDistanceFromPointIds = [
    "teste de disntancia 1",
    "teste de disntancia 2",
    "teste de disntancia 3",
    "teste de disntancia 4"
]

@pytest.mark.parametrize("point, expectedResult", testDistanceFromPointData, ids=testDistanceFromPointIds)
def test_day03_testDistanceFromPoint(point, expectedResult):
    assert getDistance(point) == expectedResult

testDistanceFromCoordinatesData = [
    (
        [
            ("R8","U5","L5","D3"),
            ("U7","R6","D4","L4")
        ],
        6
    ),
    (
        [
            ("R75","D30","R83","U83","L12","D49","R71","U7","L72"),
            ("U62","R66","U55","R34","D71","R55","D58","R83")
        ],
        159
    ),
    (
        [
            ("R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"),
            ("U98","R91","D20","R16","D67","R40","U7","R15","U6","R7")
        ],
        135
    )
]

testDistanceFromCorrdinatesIds = [
    "teste de disntancia 1",
    "teste de disntancia 2",
    "teste de disntancia 3"
]

@pytest.mark.parametrize("coordinates, expectedResult", testDistanceFromCoordinatesData, ids=testDistanceFromCorrdinatesIds)
def test_day03_testDistanceFromCoordinates(coordinates, expectedResult):
    wire1 = Wire(coordinates[0])
    wire2 = Wire(coordinates[1])
    intersections = checkIntersections(wire1, wire2)
    closerPoint = closerIntersection(intersections)
    assert getDistance(closerPoint) == expectedResult