#Questão 3 concluida
import copy
grafo_teste333 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 3)],
    'C': [('A', 4), ('B', 2), ('D', 5)],
    'D': [('B', 3), ('C', 5), ('E', 1)],
    'E': [('D', 1), ('C', 6)]
}
def recursaodevizinhos(grafo,vertice,visitados):
    visitados.add(vertice)
    
    for v,pesos in grafo[vertice]:
        if v not in visitados:
            recursaodevizinhos(grafo,v,visitados)

def checarconectividade(grafo):
    visitados = set()
    primeirovertice = list(grafo.keys())[0]
    recursaodevizinhos(grafo,primeirovertice,visitados)
    
    if len(grafo) == len(visitados):
        print("é conexo\n")
        return True
        
    else :
        print("não é conexo\n")
        return False
    
def checarconectiviadesemaresta(grafo):
    grafoteste = copy.deepcopy(grafo)
    aresta_de_saida = (input("digite de qual nó sai a aresta (ex : A)"))
    aresta_de_chegada = (input("digite o nó em que essa aresta chega( ex: B)"))
    pesodaligacao = (input("digite o peso da conexao"))
    for v, peso in grafoteste [aresta_de_saida]:
       if v == aresta_de_chegada and peso == pesodaligacao:
           grafoteste [aresta_de_saida].remove((v, peso))
           break 
    
    for v,peso in grafoteste [aresta_de_chegada]:
        if v == aresta_de_saida and peso == pesodaligacao:
            grafoteste [aresta_de_chegada].remove((v,peso))
            break
   
    checarconectividade(grafoteste)
    
    
    
checarconectiviadesemaresta(grafo_teste333)
                

##
## fim questão 3
##     