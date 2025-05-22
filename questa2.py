## questão 2 feita   e garantida
def verificarcaminho(grafo, u, v):
    if u not in grafo or v not in grafo:
        return False
    visitados = set()
    return dfs(grafo, u, v, visitados)

def dfs(grafo, atual, alvo, visitados):
    if atual == alvo:
        return True
    visitados.add(atual)
    for vizinho, _ in grafo.get(atual, []):
        if vizinho not in visitados:
            if dfs(grafo, vizinho, alvo, visitados):
                return True
    return False

def criarsubgrafocommenorpeso(rede):
    grafonovo = {v: [] for v in rede}
    lista_arestas = []
    arestas_adicionadas = set()

    for u in rede:
        for v, peso in rede[u]:
            if (v, u) not in arestas_adicionadas and (u, v) not in arestas_adicionadas:
                lista_arestas.append((u, v, peso))
                arestas_adicionadas.add((u, v))

    # Ordena as arestas por peso crescente
    lista_arestas.sort(key=lambda x: x[2])

    count = 0
    for u, v, peso in lista_arestas:
        if not verificarcaminho(grafonovo, u, v):  # se não forma ciclo
            grafonovo[u].append((v, peso))
            grafonovo[v].append((u, peso))
            count += 1
            if count == len(rede) - 1:
                break

    print("subgrafo gerador minimo construido:")
    print(grafonovo)
    return grafonovo


criarsubgrafocommenorpeso( grafo ) #insira o grafo na forma de lista de adjacencia aqui 
