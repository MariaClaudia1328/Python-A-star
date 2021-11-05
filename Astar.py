# implementação de funções relacionadas ao algoritmo de cálculo de rota A*

import numpy as np
# utilizado para gerar o arquivo de imagem resultante de printRoute()
from PIL import Image
# utilizadas para gerar sempre listas ordenadas
from heapq import heappush, heappop

from point import Point
from map import setMap, getMapOfVisited


class Astar():

    # define etapas básicas necessárias para que o A* seja executado
    def __init__(self):
        self.map = setMap()
        self.calculated_distances = getMapOfVisited(self.map)
        self.open_list = []  # lista utilizada para realizar a análise de f(n)
        self.end_point = None

    # executa o A*
    def run(self, start_point, end_point):
        self.end_point = None

        # Ponto de inicio da rota é marcado como visitado e em seguida
        # é adicionado à open_list
        self.saveCheaperDToPoint(start_point, self.calculated_distances)
        self.addToList(start_point, self.open_list)

        # se a open_list estiver vazia, o cálculo da rota é finalizado
        while(self.isEmpty(self.open_list) is False):
            n = self.selectLowestValueFn(self.open_list)

            reachable_points = self.getReachablePoints(n, self.map)

            # verifica para cada ponto vizinho, sua função heuristica, sua distância d,
            # e, assim, sua função de custo f(n)
            for point in reachable_points:
                h = self.h(point, end_point)
                point.d = self.d(point)
                point.fn = point.d + h

                if(point == end_point):  # chegou no final
                    self.end_point = point
                    return self.end_point  # finaliza cálculo

                # adiciona em open_list o ponto com menor distância
                if(self.pointHasCheaperD(point, self.calculated_distances)):
                    self.saveCheaperDToPoint(point, self.calculated_distances)
                    self.addToList(point, self.open_list)

        return self.end_point

    def saveCheaperDToPoint(self, point, calculated_distances):
        calculated_distances[point.y][point.x] = point.d

    # verifica qual ponto possui a menor distância
    def pointHasCheaperD(self, point, calculated_distances):
        return calculated_distances[point.y][point.x] > point.d

    # Acrescenta itens à lista de forma ordenada
    def addToList(self, item, list):
        heappush(list, item)

    # O menor valor de função de custo sempre será o primeiro elemento
    # a ser retirado da heap
    def selectLowestValueFn(self, list):
        return heappop(list)

    def isEmpty(self, list):
        if(not list):
            return True
        return False

    # procura por todos os vizinhos de um ponto
    def getReachablePoints(self, point, matrix):
        list = []

        # Passa por todos os 8 vizinhos de um elemento numa matriz
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(point.x + i < matrix.shape[1] and point.x + i >= 0
                   and point.y + j < matrix.shape[0] and point.y + j >= 0
                   # and (abs(i) != abs(j)) # cancela busca nas diagonais
                   and (i != 0 or j != 0)
                   ):
                    list.append(Point(point.x + i, point.y + j, parent=point))

        return [p for p in list if matrix[p.y][p.x] == 0]

    # Calcula função heuristica
    def h(self, point, end_point):
        return np.sqrt(point - end_point)

    # Calcula função de distância
    def d(self, point):
        point.d = point.parent.d + np.sqrt(point.parent - point)
        return point.d

    # Gera e imprime a rota em um arquivo .png em que cada elemento do mapa corresponde
    # a 20 pixeis
    def printRoute(self, end_point):
        point = end_point
        route = []
        # A rota é gerada aqui, a partir do ponto final até ponto inicial
        while(point != None):
            route.append(point)
            point = point.parent

        # Imprime no terminal a rota gerada em termos de x,y e f(n)
        # print(route)

        # A partir daqui começa as manipulações para imprimir o mapa e a rota no arquivo
        # de imagem
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
