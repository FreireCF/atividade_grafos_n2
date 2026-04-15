from collections import defaultdict, deque

class GrafoBipartido:
  def __init__(self):
    self.grafo = defaultdict(list)
    self.particao_u = set()
    self.particao_v = set()

  def adicionar_vertice_u(self, vertice):
    if vertice in self.particao_v:
      raise ValueError(f"Vértice '{vertice}' já está em V.")
    self.particao_u.add(vertice)
    self.grafo[vertice]

  def adicionar_vertice_v(self, vertice):
    if vertice in self.particao_u:
      raise ValueError(f"Vértice '{vertice}' já está em U.")
    self.particao_v.add(vertice)
    self.grafo[vertice]

  def adicionar_aresta(self, u, v):
    if u not in self.particao_u:
      raise ValueError(f"'{u}' não pertence à partição U.")
    if v not in self.particao_v:
      raise ValueError(f"'{v}' não pertence à partição V.")
    self.grafo[u].append(v)
    self.grafo[v].append(u)

  def vizinhos(self, vertice):
    return list(self.grafo[vertice])

  def grau(self, vertice):
    return len(self.grafo[vertice])

  def eh_bipartido(self):
    cor = {}
    todos = list(self.grafo)

    for inicio in todos:
      if inicio in cor:
        continue
      fila = deque([inicio])
      cor[inicio] = 0

      while fila:
        atual = fila.popleft()
        for vizinho in self.grafo[atual]:
          if vizinho not in cor:
            cor[vizinho] = 1 - cor[atual]
            fila.append(vizinho)
          elif cor[vizinho] == cor[atual]:
            return False, None  

      return True, cor

  def bfs(self, origem):
    visitados = set()
    fila = deque([origem])
    visitados.add(origem)
    ordem = []

    while fila:
      vertice = fila.popleft()
      ordem.append(vertice)
      for vizinho in self.grafo[vertice]:
        if vizinho not in visitados:
          visitados.add(vizinho)
          fila.append(vizinho)

    return ordem

  def emparelhamento_maximo(self):
    par_u = {}  
    par_v = {} 

    def bfs_nivel():
      nivel = {}
      fila = deque()
      for u in self.particao_u:
        if u not in par_u:
          nivel[u] = 0
          fila.append(u)
        else:
          nivel[u] = float('inf')
      encontrou = False

      while fila:
        u = fila.popleft()
        for v in self.grafo[u]:
          prox = par_v.get(v)
          if prox is None:
            encontrou = True
          elif prox not in nivel or nivel[prox] == float('inf'):
            nivel[prox] = nivel[u] + 1
            fila.append(prox)
      return encontrou, nivel

    def dfs(u, nivel):
      for v in self.grafo[u]:
        prox = par_v.get(v)
        if prox is None or (
          nivel.get(prox) == nivel[u] + 1 and dfs(prox, nivel)
        ):
          par_u[u] = v
          par_v[v] = u
          return True
      nivel[u] = float('inf')
      return False

    while True:
      encontrou, nivel = bfs_nivel()
      if not encontrou:
        break
      for u in self.particao_u:
        if u not in par_u:
          dfs(u, nivel)

    return par_u

  def __str__(self):
    linhas = [
      f"Partição U: {sorted(self.particao_u)}",
      f"Partição V: {sorted(self.particao_v)}",
    ]
    return "\n".join(linhas)