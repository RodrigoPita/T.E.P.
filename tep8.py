'''
Problema da Mochila 0/1 (knapsack)

Força Bruta - Backtracking
1- Primeiro objeto, coloca ou não coloca, segundo...
2- Qual será o próximo objeto que eu posso colocar? o Primeiro, qual o pró...

-Recursão e Recursão com Memoização
Coloca o elemento1 e resolve o problema da mochila menor
com os elementos 2 até o n ou não coloca o elemento1
e resolve o problema da mochila com um elemento a menos
'''

def backtrack(W, itens, estadoCorrente, valores = {}):    
    # o estado corrente merece tratamento especial?
    if len(itens) == 0:
        print(max(valores))
        return # nada mais a ser feito, estamos numa folha da árvore

    if len(itens[0]) < 3:
        [itens[k].append(itens.index(itens[k])+1) for k in range(0, len(itens))]

    # para cada próximo passo possível ...
    for objeto in itens:
        
        if objeto in estadoCorrente:
            continue # este item já foi colocado na mochila

        pesoTotal = sum(row[0] for row in estadoCorrente)
        if pesoTotal + objeto[0] > W:
            continue # este está passando do limite de peso
        
        # dá o passo, gerando uma nova configuração
        estadoCorrente.append(objeto)
        
        valorTotal = sum(row[1] for row in estadoCorrente)
        estado = tuple(set([k[2] for k in estadoCorrente]))
        valores[valorTotal] = estado
        
        print(max(valores), valores[max(valores)])
        
        # chama recursivamente
        backtrack(W, itens, estadoCorrente, valores)

        # limpa a sujeira
        estadoCorrente.pop()


# [[peso, valor]]
itens = [[1, 5], [2, 3], [4, 5], [2, 3], [5, 2]]
#itens = [[1, 5], [5, 2], [4, 5], [2, 3], [2, 3]]
W = 10
#itens = [[5, 10], [4, 40], [6, 30], [3, 50]]
#W = 10
estadoInicial = []

valores = {}

backtrack(W, itens, estadoInicial, valores)





'''
n = len(itens)
def rec(n, W, itens):
    if n == 0 or W == 0:
        return 0
    elif itens[n-1][0] > W:
        result = rec(n-1, W, itens)
    else:
        tmp1 = rec(n-1, W, itens)
        tmp2 = itens[n-1][1] + rec(n-1, W - itens[n-1][0], itens)
        result = max(tmp1, tmp2)
    return result
'''
