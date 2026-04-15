from collections import defaultdict, deque

# ====================== COMPATIBILIDADES ======================
# doador -> lista de receptores que ele pode doar
compatibilidade = {
    'O': ['O', 'A', 'B', 'AB'],
    'A': ['A', 'AB'],
    'B': ['B', 'AB'],
    'AB': ['AB']
}

# ====================== GRAFO BIPARTIDO ======================
def construir_grafo(doadores, receptores):
    """
    doadores: lista de tipos dos doadores (pode ter repetidos)
    receptores: lista de tipos dos receptores (pode ter repetidos)
    """
    grafo = defaultdict(list)
    
    # Para diferenciar doadores e receptores repetidos, usamos índices
    for i, tipo_doador in enumerate(doadores):
        for j, tipo_receptor in enumerate(receptores):
            if tipo_receptor in compatibilidade.get(tipo_doador, []):
                grafo[f'D{i}'].append(f'R{j}')
    
    return grafo


# ====================== EMPARELHAMENTO MÁXIMO (Hopcroft-Karp simplificado via BFS/DFS) ======================
def bfs(grafo, pairing, dist):
    queue = deque()
    for u in grafo:
        if pairing[u] is None:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    
    dist[None] = float('inf')
    
    while queue:
        u = queue.popleft()
        if dist[u] < dist[None]:
            for v in grafo[u]:
                if dist[pairing[v]] == float('inf'):
                    dist[pairing[v]] = dist[u] + 1
                    queue.append(pairing[v])
    return dist[None] != float('inf')


def dfs(u, grafo, pairing, dist):
    if u is None:
        return True
    for v in grafo[u]:
        if dist[pairing[v]] == dist[u] + 1:
            if dfs(pairing[v], grafo, pairing, dist):
                pairing[v] = u
                pairing[u] = v
                return True
    dist[u] = float('inf')
    return False


def emparelhamento_maximo(grafo):
    pairing = {u: None for u in grafo}          # pairing[doador] = receptor
    for v in set(v for edges in grafo.values() for v in edges):
        pairing[v] = None                       # pairing[receptor] = doador
    
    matching = 0
    dist = {}
    
    while bfs(grafo, pairing, dist):
        for u in grafo:
            if pairing[u] is None:
                if dfs(u, grafo, pairing, dist):
                    matching += 1
    return matching, pairing


# ====================== EXEMPLO DE USO ======================
if __name__ == "__main__":
    # Exemplo: suponha que temos esses doadores e receptores
    doadores = ['A', 'B', 'AB', 'O']
    receptores = ['A', 'B', 'AB', 'O']
    
    grafo = construir_grafo(doadores, receptores)
    tamanho, pares = emparelhamento_maximo(grafo)
    
    print(f"Número máximo de pares possíveis: {tamanho}\n")
    print("Emparelhamentos encontrados:")
    for d, r in pares.items():
        if d.startswith('D') and r is not None:
            idx_d = int(d[1:])
            idx_r = int(r[1:])
            print(f"Doador {doadores[idx_d]} (índice {idx_d}) → Receptor {receptores[idx_r]} (índice {idx_r})")