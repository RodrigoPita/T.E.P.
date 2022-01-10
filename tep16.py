'''
UNION FIND

Entrada: um array A de inteiros positivos

Pergunta: de quantas maneiras podemos particionar A = X U Y, X ∩ Y = {}
X != {}, Y != {}, de forma que M.D.C.(πx, πy) == 1?

Exemplos:

1) A = [3, 7]
Resposta: 2 maneiras
X = {3}, Y = {7} ou X = {7}, Y = {3}

2) A = [2, 4, 8, 16, 20, 34]
Resposta: 0 maneiras
'''

representante = {}
rank = {}

def createSet(x):
    representante[x] = x
    rank[x] = 1
    
def union(x, y):
    if representante.get(x) == representante.get(y):
        return ("Repetido")
    X = find(x)
    Y = find(y)

    if rank.get(X) < rank.get(Y):
        representante[X] = Y
    elif rank.get(X) > rank.get(Y):
        representante[Y] = X
    else:
        representante[X] = Y
        rank[Y] += 1
        
    estado()

def find(x):
    r = representante.get(x)
    if r == x:
        return x
    r = find(r)
    representante[x] = r
    return r

def estado():
    print("C", "|", "r", "|", "R")
    for k in rank:
        print(k, "|", representante.get(k), "|", rank.get(k))
    

'''
Bingo de Permutações

Entrada: Tamanho da Tupla
Sáida: Identificar a Tupla completa e quantas Tuplas você recebeu até acontecer
'''
