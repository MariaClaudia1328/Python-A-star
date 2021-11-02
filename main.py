import map
from Astar import Astar

start_point = map.setStartPoint()
end_point = map.setEndPoint()

aStar = Astar()

end_point = aStar.run(start_point, end_point)
aStar.printRoute(end_point)
