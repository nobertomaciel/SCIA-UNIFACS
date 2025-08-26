grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristica = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 1,
    'F': 0
}

inicio = 'A'
objetivo = 'F'

caminho = busca_gulosa(grafo, inicio, objetivo, heuristica)

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Caminho não encontrado.")

