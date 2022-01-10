class Aresta():
    def __init__(self, de:int, para:int, peso:int):
        self.de = de
        self.para = para
        self.peso = peso

    def operadorBool(self, outraAresta):
        if (self.peso < outraAresta.peso):
            return True
        else:
            return False

class ConjuntosDisjuntos():

    pais = []
    ranks = []
    
    def __init__(self, numeroElementos:int):
        self.numeroElementos = numeroElementos
        self.pais = [0]*(numeroElementos+1)
        for i in range(1, numeroElementos+1):
            self.pais[i] = i
        self.ranks = [1]*(numeroElementos+1)

    def pai(vertice:int):
        return self.pais[vertice]

    def setPai(vertice:int, novoPai:int):
        self.pais[vertice] = novoPai

    def rank(vertice:int):
        return self.ranks[vertice]

    def setRank(vertice:int, rank:int):
        self.ranks[vertice] = rank

    def find(vertice:int):
        verticeAtual = vertice
        while(verticeAtual != pai(verticeAtual)):
            setPai(verticeAtual, pai(pai(verticeAtual)))
            verticeAtual = pai(verticeAtual)
        return verticeAtual

    def union(verticeUm:int, verticeDois:int):
        raizUm = find(verticeUm)
        raizDois = find(verticeDois)

        if(rank(raizDois) > rank(raizUm)):
            setPai(raizUm, raizDois)
        if(rank(raizUm) == rank(raizDois)):
            setRank(raizUm, rank(raizUm)+1)
        setPai(raizDois, raizUm)

arestas = []
n, m = input().split()
n = int(n)
m = int(m)
conjuntos = ConjuntosDisjuntos(n)

for a0 in range(0, m):
    a, b, w = input().split()
    arestas.append(Aresta(a, b, w))

arestas.sort()

count = 0
custoAcumulado = 0
numeroZeraveis = 0
