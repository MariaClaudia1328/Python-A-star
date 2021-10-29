# set a map grid as matrix 
# set start point and end point
# add start point to open list
# if open list is empty, end of execution
# if open list is not empty, select the lowest value of f(n) pois as point n from open list
# add point n to close list
# add the point that can be reached from point n to open list
# set these points parent node as n
# if these point have been in open list, select the lowest value of f(n) point as point n from open list
# if these point haven't been in open list and end point in open list, end od execution
# if these point haven't been in open list and end point aren't in open list, come back to verify if open list is empty 

import map # importa mapa e pontos de inicio e fim da rota
import fAstar # funções do A*

# recebe mapa formatado como matriz para os cálculos
map_ = map.setMap()
# recebe ponto de começo e fim da rota
start_point = map.setStartPoint()
end_point = map.setEndPoint()

# adiciona ponto de começo a lista aberta
fAstar.addOpenList(start_point)   

# se lista aberta está vazia, o algoritmo é encerrado
while(fAstar.openListEmpty() is False):
    while(True):
        n = fAstar.selectLowestValueFn()
        fAstar.addCloseList(n)
        p = fAstar.canReachedFromN(n)
        fAstar.addOpenList(p)
        fAstar.setParentNode(p,n)
        if(fAstar.isInOpenList(p)):
            continue
        else:
            break
    if(fAstar.isInOpenList(end_point)):
        break
    else: 
        continue

