import heapq

def resolver_a_star(estado_inicial, estado_objetivo):
  # Fila de prioridade (fronteira) que sempre nos dá o menor f(n)
  fronteira = []

  # heapq exige uma tupla. O primeiro valor é a prioridade (f(n))
  heapq.heappush(fronteira, (estado_inicial.f, estado_inicial))

  # Conjunto para guardar os estados que já visitamos (evita loops infinitos)
  visitados = set()

  while fronteira:
    # 1. Pega o estado com o menor custo f(n)
    _, estado_atual = heapq.heappop(fronteira)

    # 2. Verifica se chegamos na solução
    if estado_atual == estado_objetivo:
      return reconstruir_caminho(estado_atual) # Retorna lista de movimentos

    # 3. Marca como visitado
    visitados.add(tuple(estado_atual.tabuleiro))

    # 4. Gera os próximos movimentos possíveis (cima, baixo, esq, dir)
    vizinhos = gerar_vizinhos(estado_atual)

    for vizinho in vizinhos:
      if tuple(vizinho.tabuleiro) not in visitados:
        vizinho.g = estado_atual.g + 1
        vizinho.h = calcular_manhattan(vizinho.tabuleiro, estado_objetivo)
        vizinho.f = vizinho.g + vizinho.h

        vizinho.pai = estado_atual

        heapq.heappush(fronteira, (vizinho.f, vizinho))

    # Se a fila esvaziar e não achar o objetivo, o puzzle não tem solução
    return None