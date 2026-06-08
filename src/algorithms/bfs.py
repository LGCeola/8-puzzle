from collections import deque

def resolver_bfs(estado_inicial, estado_objetivo):
    # Fila padrão (FIFO - o primeiro a entrar é o primeiro a sair)
    fila = deque([estado_inicial])
    
    # Conjunto para guardar os estados que já visitamos
    visitados = set()

    while fila:
        # 1. Pega o estado mais antigo da fila (do lado esquerdo)
        estado_atual = fila.popleft()

        # 2. Verifica se chegamos na solução
        if estado_atual.tabuleiro == estado_objetivo:
            return reconstruir_caminho(estado_atual) # Retorna a lista de movimentos

        # Transforma o tabuleiro em tupla para poder salvar no 'set' de visitados
        tabuleiro_tupla = tuple(estado_atual.tabuleiro)

        # 3. Se já visitamos esse estado, ignoramos e passamos para o próximo
        if tabuleiro_tupla in visitados:
            continue

        # 4. Marca como visitado
        visitados.add(tabuleiro_tupla)

        # 5. Gera os próximos movimentos possíveis
        vizinhos = gerar_vizinhos(estado_atual)

        for vizinho in vizinhos:
            if tuple(vizinho.tabuleiro) not in visitados:
                # O BFS não precisa calcular heurística (h) ou custo (f) para ordenar a fila.
                # Ele apenas guarda quem é o pai para podermos desenhar o caminho no final.
                vizinho.pai = estado_atual
                
                # Adiciona no final da fila (lado direito)
                fila.append(vizinho)

    # Se a fila esvaziar e não achar o objetivo, o puzzle não tem solução
    return None