import copy

grafo_original = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('D', 4), ('E', 1)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 4), ('E', 3), ('G', 6)],
    'E': [('B', 1), ('D', 3), ('F', 2)],
    'F': [('C', 5), ('E', 2), ('G', 4)],
    'G': [('D', 6), ('F', 4)]
}

def imprime_grafo(g):
    for u in g:
        for v, peso in g[u]:
            print(f"{u} --({peso})--> {v}")
            
def imprimir_arestas_sem_repeticao(grafo):
    arestas_impressas = set()
    for u in grafo:
        for v, peso in grafo[u]:
            if (v, u, peso) not in arestas_impressas:
                print(f"{u} --({peso})--> {v}")
                arestas_impressas.add((u, v, peso))

def gerar_combinacoes(lista, tamanho):

    def gerar_combinacoes_recursivo(inicio, tamanho, combinacao_atual):
        if tamanho == 0:
            yield combinacao_atual[:]
            return
        
        for i in range(inicio, len(lista)):
            combinacao_atual.append(lista[i])
            yield from gerar_combinacoes_recursivo(i + 1, tamanho - 1, combinacao_atual)
            combinacao_atual.pop()
    
    return gerar_combinacoes_recursivo(0, tamanho, [])

def criarsubgrafoeconomicoconfiavel(grafo):
    grafonovo = {v: [] for v in grafo}
    lista_arestas = []
    arestas_adicionadas = set()
    
    for u in grafo:
        for v, peso in grafo[u]:
            if (v, u) not in arestas_adicionadas and (u, v) not in arestas_adicionadas:
                lista_arestas.append((u, v, peso))
                arestas_adicionadas.add((u, v))

    lista_arestas.sort(key=lambda x: x[2])

    arestas_mst = set()
    count = 0
    for u, v, peso in lista_arestas:
        if not verificarcaminho(grafonovo, u, v):  
            grafonovo[u].append((v, peso))
            grafonovo[v].append((u, peso))
            arestas_mst.add((u, v, peso))
            count += 1
            if count == len(grafo) - 1:
                break
    arestas_restantes = [a for a in lista_arestas if a not in arestas_mst and (a[1], a[0], a[2]) not in arestas_mst]
    melhor_custo = float('inf')
    melhor_grafo = None
    melhor_arestas_adicionais = None
    
    for num_arestas in range(1, len(arestas_restantes) + 1):
        for combinacao in gerar_combinacoes(arestas_restantes, num_arestas):
            grafo_teste = {v: [] for v in grafo}
            
            for u, v, peso in arestas_mst:
                grafo_teste[u].append((v, peso))
                grafo_teste[v].append((u, peso))
            
            custo_adicional = 0
            for u, v, peso in combinacao:
                grafo_teste[u].append((v, peso))
                grafo_teste[v].append((u, peso))
                custo_adicional += peso
            
            if not encontrar_arestas_criticas(grafo_teste):
                custo_total = sum(peso for _, _, peso in arestas_mst) + custo_adicional
                if custo_total < melhor_custo:
                    melhor_custo = custo_total
                    melhor_grafo = copy.deepcopy(grafo_teste)
                    melhor_arestas_adicionais = combinacao
                    print(f"novo grafo de custo minimo: {custo_total}")
                    print("arestas aducionadas:", melhor_arestas_adicionais)
    
    if melhor_grafo is None:
        print("Nnao achou solucao para a 2 conectividade")
        return grafonovo
    
    print(f"\nmelhor/mais economica solucao encontrada")
    print(f"custo total: {melhor_custo}")
    print("arestas da MST:", arestas_mst)
    print("arestas adicionadas:", melhor_arestas_adicionais)
    
    return melhor_grafo

def encontrar_arestas_criticas(grafo):
    pontes = []
    for u in grafo:
        for v, peso in grafo[u]:
            if u < v: 
                grafoteste = copy.deepcopy(grafo)
                try:
                    grafoteste[u].remove((v, peso))
                except ValueError:
                    pass
                try:
                    grafoteste[v].remove((u, peso))
                except ValueError:
                    pass

                if not checarconectividade(grafoteste):
                    pontes.append((u, v, peso))
    return pontes

def checarconectiviadesemaresta2(grafo, v, u, peso):
    grafoteste = copy.deepcopy(grafo)
    for vert, peso_aresta in grafoteste[v]:
        if vert == u and peso_aresta == peso:
            grafoteste[v].remove((vert, peso_aresta))
            break
    
    for vert, peso_aresta in grafoteste[u]:
        if vert == v and peso_aresta == peso:
            grafoteste[u].remove((vert, peso_aresta))
            break
    return checarconectividade(grafoteste)

def recursaodevizinhos(grafo, vertice, visitados):
    visitados.add(vertice)
    for v, _ in grafo[vertice]:
        if v not in visitados:
            recursaodevizinhos(grafo, v, visitados)

def checarconectividade(grafo):
    visitados = set()
    primeirovertice = list(grafo.keys())[0]
    recursaodevizinhos(grafo, primeirovertice, visitados)
    
    if len(grafo) == len(visitados):
        print("e conexo\n")
        return True
    else:
        print("nao e conexo\n")
        return False

def verificarcaminho(grafo, u, v):
    visitados = set()
    return dfs_caminho(grafo, u, v, visitados)

def dfs_caminho(grafo, atual, destino, visitados):
    if atual == destino:
        return True
    visitados.add(atual)
    for viz, _ in grafo[atual]:
        if viz not in visitados:
            if dfs_caminho(grafo, viz, destino, visitados):
                return True
    return False
subgrafo = criarsubgrafoeconomicoconfiavel(grafo_original)
imprimir_arestas_sem_repeticao(subgrafo)