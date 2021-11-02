# implementação das funções específicas do A*
# fAstar = function A star

import numpy as np
from PIL import Image
from heapq import heappush, heappop

from point import Point
from map import setMap, getMapOfVisited


class Astar():
    def __init__(self):
        self.map = setMap()
        self.calculated_distances = getMapOfVisited(self.map)
        self.open_list = []
        self.end_point = None

    def run(self, start_point, end_point):
        self.end_point = None

        self.saveCheaperDToPoint(start_point, self.calculated_distances)
        self.addToList(start_point, self.open_list)

        while(self.isEmpty(self.open_list) is False):
            n = self.selectLowestValueFn(self.open_list)

            reachable_points = self.getReachablePoints(n, self.map)
            for point in reachable_points:
                h = self.h(point, end_point)
                point.d = self.d(point)
                point.fn = point.d + h

                if(point == end_point):  # chegou no final
                    self.end_point = point
                    return self.end_point

                if(self.pointHasCheaperD(point, self.calculated_distances)):
                    self.saveCheaperDToPoint(point, self.calculated_distances)
                    self.addToList(point, self.open_list)

        return self.end_point

    def saveCheaperDToPoint(self, point, calculated_distances):
        calculated_distances[point.y][point.x] = point.d

    def pointHasCheaperD(self, point, calculated_distances):
        return calculated_distances[point.y][point.x] > point.d

    def addToList(self, item, list):
        heappush(list, item)

    def selectLowestValueFn(self, list):
        return heappop(list)

    def isEmpty(self, list):
        if(not list):
            return True
        return False

    def getReachablePoints(self, point, matrix):
        list = []

        # passa por todos os 8 vizinhos
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(point.x + i < matrix.shape[1] and point.x + i >= 0
                   and point.y + j < matrix.shape[0] and point.y + j >= 0
                   # and (abs(i) != abs(j)) # cancela diagonais
                   and (i != 0 or j != 0)
                   ):
                    list.append(Point(point.x + i, point.y + j, parent=point))

        return [p for p in list if matrix[p.y][p.x] == 0]

    def h(self, point, end_point):
        return np.sqrt(point - end_point)

    def d(self, point):
        point.d = point.parent.d + np.sqrt(point.parent - point)
        return point.d

    def printRoute(self, end_point):
        point = end_point
        route = []
        while(point != None):
            route.append(point)
            point = point.parent

        print(route)

        map2 = self.map.copy()

        for i in route:
            map2[i.y][i.x] = 2

        scale = 20
        mapReshaped = map2.copy()
        mapReshaped.resize(
            (self.map.shape[0] * scale, self.map.shape[1] * scale))
        xMax = mapReshaped.shape[1]
        yMax = mapReshaped.shape[0]
        print(xMax, yMax)

        def getColor(id):
            if(id == 0):
                return 0xffffffff
            elif(id == 1):
                return 0xff000000
            elif(id == 2):
                return 0xff0000ff

        for x in range(xMax):
            for y in range(yMax):
                mapReshaped[y][x] = getColor(map2[int(y/scale)][int(x/scale)])

        img = Image.fromarray(np.array(mapReshaped), mode="RGBA")
        img.save("result.png")
