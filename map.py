import numpy as np

from point import Point


def setMap():
    matrix = np.array([[0, 1, 0, 0, 0, 0],
                       [0, 1, 1, 1, 1, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 1, 1, 1],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 1, 0],
                       [0, 0, 1, 0, 0, 0]
                       ], dtype=np.uintc)
    return matrix


def getMapOfVisited(map):
    return np.full(map.shape, np.inf)


def setStartPoint():
    start = Point(0, 0)
    return start


def setEndPoint():
    end = Point(2, 0)
    return end
