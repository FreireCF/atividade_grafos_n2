from GrafoBipartido import GrafoBipartido
from itertools import combinations

def questao2():
  g = GrafoBipartido()

  for onibus in ["A", "B", "C", "D", "E"]:
    g.adicionar_vertice_u(onibus)

  for vagas in ["1", "2", "3", "4", "5", "6"]:
    g.adicionar_vertice_v(vagas)

  restricoes = {
    "A": ["1", "2", "4", "5"],
    "B": ["2", "3"],
    "C": ["3"],
    "D": ["2", "3"],
    "E": ["4", "5", "6"],
  }

  for onibus, vagas in restricoes.items():
    for vaga in vagas:
      g.adicionar_aresta(onibus, vaga)

  print(g)
  print()

  print("vgas disponíveis por ônibus:")
  for onibus in sorted(g.particao_u):
    vagas = sorted(g.vizinhos(onibus))
    print(f"  Ônibus {onibus}: vagas {', '.join(vagas)}")
  print()

  emparelhamento = g.emparelhamento_maximo()
  total_onibus   = len(g.particao_u)
  total_pareados = len(emparelhamento)

  print(f"Emparelhamento máximo encontrado ({total_pareados} de {total_onibus} ônibus):")
  for onibus in sorted(emparelhamento):
    print(f"  Ônibus {onibus} → Vaga {emparelhamento[onibus]}")
  print()

  sem_vaga = sorted(g.particao_u - set(emparelhamento.keys()))
  if sem_vaga:
    print(f"Sem vaga: ônibus {', '.join(sem_vaga)}")
    print()

  print("─" * 45)
  print("Conclusão: ")
  print()

  onibus_list = sorted(g.particao_u)
  violacao_encontrada = False

  for tamanho in range(1, len(onibus_list) + 1):
    for subconj in combinations(onibus_list, tamanho):
      vizinhos = set()
      for o in subconj:
        vizinhos.update(g.vizinhos(o))

      if len(vizinhos) < len(subconj):
        print("Violação encontrada!")
        print()
        violacao_encontrada = True

  if violacao_encontrada:
    print("NÃO é possível estacionar todos os ônibus ao mesmo tempo")
  else:
    print("É possível estacionar todos os ônibus.")

if __name__ == "__main__":
  questao2()