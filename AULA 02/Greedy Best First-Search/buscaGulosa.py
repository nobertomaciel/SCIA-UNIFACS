import heapq

def busca_gulosa(grafo, inicio, objetivo, heuristica):
    # Fila de prioridade: (heuristica, nó, caminho)
    fronteira = []
    heapq.heappush(fronteira, (heuristica[inicio], inicio, [inicio]))

    visitados = set()

    while fronteira:
        h_atual, no_atual, caminho = heapq.heappop(fronteira)

        if no_atual == objetivo:
            return caminho  # Caminho encontrado

        if no_atual in visitados:
            continue

        visitados.add(no_atual)

        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                novo_caminho = caminho + [vizinho]
                heapq.heappush(fronteira, (heuristica[vizinho], vizinho, novo_caminho))

    return None  # Caminho não encontrado

