'''
Entrada: um array de inteiros quase ordenado
(ele está "rodado")

2  5  8  10 / 15  18

15  18  2  5  8  10 ---> Resposta:2

Saida: o menor elemento do array
'''
import datetime
from math import ceil
from random import randint

L = [15, 18, 2, 5, 8, 10]

def func(x):
    inicio = datetime.datetime.now()
    tam = ceil(len(x)/2)
    mid = x[tam-1]
    bot = x[0]
    top = x[-1]
    while True:
        if mid - x[x.index(mid)-1] < 0:
            duracao = datetime.datetime.now() - inicio
            return(mid, duracao.seconds)
        elif bot == top:
            mid = x[x.index(bot)-1]
            duracao = datetime.datetime.now() - inicio
            return(mid, duracao.seconds)
        elif mid < top:
            top = mid
        else:
            bot = mid
        tam = ceil((x.index(top) - x.index(bot))/2 + x.index(bot))
        mid = x[tam]

def gerador(y):
    #y = tamanho da lista a ser gerada
    A = []
    n = randint(0, y)
    passo = randint(0, 50)
    x = randint(-y, y)
    print("x:", x)
    while len(A) < y:
        A.append(x)
        x += passo
    A.sort()
    A = (A[-n:] + A[:-n])
    return(A)
