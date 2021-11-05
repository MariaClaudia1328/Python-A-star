# Implementação de funções relacionadas ao mapa

import numpy as np
from point import Point


# Mapa é convertido em uma matriz. Nesse caso, ele é apenas uma matriz
# onde 0 é o caminho livre e 1 são paredes
def setMap():
    matrix = np.array([[0, 1, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 1, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0],
                       [0, 1, 0, 1, 1, 1, 1],
                       [0, 1, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 1, 0, 0],
                       [0, 1, 0, 0, 1, 0, 0],
                       [0, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]
                       ], dtype=np.uintc)
    print(matrix)
    return matrix


# Matriz utilizada para marcar pontos que já foram analisados pelo algoritmo A*. Os pontos
# que não foram analisados tem custo para serem atingidos (d) infinito
def getMapOfVisited(map):
    return np.full(map.shape, np.inf)


# Define ponto de inicio da rota
def setStartPoint():
    start = Point(0, 0)
    return start


# Define ponto final da rota
def setEndPoint():
    end = Point(2, 0)
    return end
