# Classe para definir um ponto no mapa determinadas propriedades, essas
# propriedades são: localização no plano x,y ; função de custo f(n) ;
# nó pai; distância d
class Point:
    def __init__(self, x=0, y=0, fn=0, parent=None, d=0):
        self.fn = fn
        self.x = x
        self.y = y
        self.parent = parent
        self.d = d

    # utilizado para imprimir na tela
    def __str__(self):
        return str(f"({self.x}, {self.y}) fn:{self.fn}")

    # utilizado para imprimir na tela
    def __repr__(self):
        return str(f"({self.x}, {self.y}) fn:{self.fn}")

    # utilizado para comparar coordenadas de um ponto
    def __eq__(self, other):
        return other != None and self.x == other.x and self.y == other.y

    # utilizado para encontrar a menor função de custo
    def __lt__(self, other):
        return self.fn < other.fn

    # função de cálculo da distância para encontrar heurística
    def euclid(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2

    # utilizado para calcular heurística
    def __sub__(self, other):
        return self.euclid(other)
