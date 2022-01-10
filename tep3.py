'''
Conjectura de Collatz

f(x) = 3x + 1 se x ímpar
f(x) = x/2 se for par

g(x) --> tamanho da sequência x, f(x), fof(x), ..., 1


Entrada: xmin, xmax

[xmin, xmax] --> qual o x com o maior g(x)

Saída: x e g(x)
'''
import datetime

memo = {}
TAM = 100000

def f(x):
    if (x & 1 == 0):
        x /= 2
    else:
        x = x*3 + 1
    return(int(x))

def g(x):
    cont = 1
    y = x
    while y != 1:
        if y in memo:
            cont = cont + memo[y] - 1
            break
        y = f(y)
        cont += 1
    if x < TAM:
        memo[x] = cont
    return cont

def xEg(xmin, xmax):
    inicio = datetime.datetime.now()
    cont = 0
    gmax = 0
    xmelhor = 0
    for x in range(xmin, xmax+1):
        cont = g(x)
        if cont > gmax:
            gmax = cont
            xmelhor = x
    duracao = datetime.datetime.now() - inicio
    return([xmelhor, gmax], duracao.seconds)
