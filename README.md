# Algoritmo A\*

## Visão geral da implementação

    O algoritmo A* irá buscar pela menor distância entre dois pontos em um mapa, estudando a distância entre pontos vizinhos e entre esses pontos e o ponto final.

    A ideia geral é:

    - Receber ponto inicial e final da rota
    - Criar uma lista (chamada de open_list) e acrescente o ponto inicial à ela. Também é criada uma matriz, chamada de calculated_distances, que irá marcar os pontos que já foram analisados. No começo, o ponto inicial é armazenado nela
    - Iniciar a análise no primeiro ponto. A análise consta de encontrar os vizinhos, calcular a heuristica h e o custo até chegar a esse ponto a partir do ponto inicial ou analisado, d. A partir do d e h calculados, temos a função de custo f(n). Nessa análise, também é colocado o ponto de análise como ponto pai dos pontos vizinhos. Na análise dos vizinhos é feita uma busca para encontrar o vizinho com a menor função de custo. Esse vizinho é adicionado a open_list e a análise passa ser nesse ponto. Caso não encontre, retornamos ao ponto pai para procurar a menor função de custo novamente, repetindo a análise até esvaziar a open_list, retornando o ponto final da rota
