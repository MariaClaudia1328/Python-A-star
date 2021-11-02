class Point:
    def __init__(self, x=0, y=0, fn=0, parent=None, d=0):
        self.fn = fn
        self.x = x
        self.y = y
        self.parent = parent
        self.d = d

    def __str__(self):
        return str(f"({self.x}, {self.y}) fn:{self.fn}")

    def __repr__(self):
        return str(f"({self.x}, {self.y}) fn:{self.fn}")

    def __eq__(self, other):
        return other != None and self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.fn < other.fn

    def euclid(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def __sub__(self, other):
        return self.euclid(other)
