from GrafoBipartido import GrafoBipartido;

if __name__ == "__main__":
  g = GrafoBipartido()
  g1 = GrafoBipartido()
  g2 = GrafoBipartido()
  
  for casal in ["A", "B", "C", "D", "E", "F"]:
      g.adicionar_vertice_u(casal)
      g1.adicionar_vertice_u(casal)
      g2.adicionar_vertice_u(casal)
  for quartos in ["1", "2", "3", "4", "5", "6"]:
      g.adicionar_vertice_v(quartos)
      g1.adicionar_vertice_v(quartos)
      g2.adicionar_vertice_v(quartos)

  #tempos 3 soluções distintas
  #SOLUÇÃO 1:
  g.adicionar_aresta("A", "1")
  g.adicionar_aresta("B", "2")
  g.adicionar_aresta("C", "3")
  g.adicionar_aresta("D", "6")
  g.adicionar_aresta("E", "4")
  g.adicionar_aresta("F", "5")

  #SOLUÇÃO 2:
  g1.adicionar_aresta("A", "1")
  g1.adicionar_aresta("B", "6")
  g1.adicionar_aresta("C", "3")
  g1.adicionar_aresta("D", "5")
  g1.adicionar_aresta("E", "4")
  g1.adicionar_aresta("F", "2")

  #SOLUÇÃO 3:
  g2.adicionar_aresta("A", "1")
  g2.adicionar_aresta("B", "6")
  g2.adicionar_aresta("C", "2")
  g2.adicionar_aresta("D", "6")
  g2.adicionar_aresta("E", "4")
  g2.adicionar_aresta("F", "5")

  print("Solução 1: ")
  print(g)

  bipartido, coloracao = g.eh_bipartido()
  # print(f"É bipartido? " "Sim" if {bipartido} else "Não")
  print()

  emp = g.emparelhamento_maximo()
  print(f"Emparelhamento máximo ({len(emp)} pares):")
  for u, v in emp.items():
      print(f"  {u} → {v}")
  print()


  print("Solução 2: ")
  print(g1)

  bipartido, coloracao = g1.eh_bipartido()
  # print(f"É bipartido? " "Sim" if {bipartido} else "Não")
  print()

  emp = g1.emparelhamento_maximo()
  print(f"Emparelhamento máximo ({len(emp)} pares):")
  for u, v in emp.items():
      print(f"  {u} → {v}")
  print()


  print("Solução 1: ")
  print(g2)

  bipartido, coloracao = g2.eh_bipartido()
  # print(f"É bipartido? " "Sim" if {bipartido} else "Não")
  print()

  emp = g2.emparelhamento_maximo()
  print(f"Emparelhamento máximo ({len(emp)} pares):")
  for u, v in emp.items():
      print(f"  {u} → {v}")
  print()