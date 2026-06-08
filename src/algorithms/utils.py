def calcular_manhattan(tabuleiro_atual, estado_objetivo):
  """
    Calcula a Distância de Manhattan total para um estado do 8-Puzzle.
    
    :param tabuleiro_atual: Lista de 9 inteiros representando o estado atual.
    :param estado_objetivo: Lista de 9 inteiros representando o estado final desejado.
    :return: Inteiro representando o custo heurístico h(n).
    """
    distancia_total = 0

    # Percorremos todas as posições (de 0 a 8) do tabuleiro 3x3
    for i in range(9):
      valor = tabuleiro_atual[i]

      if valor != 0:
        # 1. Encontra onde a peça está agora
        linha_atual = i // 3
        coluna_atual = i % 3

        # 2. Encontra onde a peça deveria estar
        indice_objetivo = estado_objeetivo.index(valor)
        linha_obj = indice_objetivo // 3
        coluna_obj = indice_objetivo % 3

        # 3. Calcula a distância matemática entre esses dois pontos
        distancia_peca = abs(linha_atual - linha_obj) + abs(coluna_atual - coluna_obj)

        # 4. Soma ao total
        distancia_total += distancia_peca

    return distancia_total