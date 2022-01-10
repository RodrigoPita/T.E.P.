'''
Duas configurações para um jogo

[A] jogar 3 vezes seguidas o dado e obter 3 valores iguais

[B] jogar 4 vezes seguidas o dado e obter 2 pares seguidos (1º e 2º, 3º e 4º)
'''
import random
def jogaDado():
    return random.randint(1, 6)

def jogadorA(x):
    result = 0
    for k in range(0, x):
        a = jogaDado()
        b = jogaDado()
        c = jogaDado()
        if a == b and b == c:
            result += 1
    return result

def jogadorB(x):
    result = 0
    for k in range(0, x):
        a = jogaDado()
        b = jogaDado()
        c = jogaDado()
        d = jogaDado()
        if a == b and c == d:
            result += 1
    return result

##for k in range(0, 10):
##    x = 10000
##    print(jogadorA(x), jogadorB(x))

'''
Construa uma função que simula o lançamento de um "dado de n faces", n >= 1,
com distribuição de probabilidades dada

Entrada: uma lista c/ n frequências relativas (não necessariamente normalizadas)
Saída: um valor entre 1 e n

Ex:
[1,1] simula uma moeda honesta
[1,1,1,1,1,1] simula um dado honesto
[3, 7] simula uma "moeda" onde uma das faces (1) sai com probabilidade 30%, e a outra (2) com 70%
[90,2,2,2,2,2] simula um dado viciado onde o "1" sai em 90% das vezes,
e os demais com equiprobabilidade
'''

def jogaDadoX(lista):
    soma = sum(lista)
    lista = [k/soma for k in lista]
    for k in range(1, len(lista)):
        lista[k] = lista[k] + lista[k-1]
    num = random.uniform(0.0, float(lista[-1]))
    for k in range(0, len(lista)):
        if num <= lista[k]:
            return k + 1

def jogadorAX(x, lista):
    result = 0
    for k in range(0, x):
        a = jogaDadoX(lista)
        b = jogaDadoX(lista)
        c = jogaDadoX(lista)
        if a == b and b == c:
            result += 1
    return result

def jogadorBX(x, lista):
    result = 0
    for k in range(0, x):
        a = jogaDadoX(lista)
        b = jogaDadoX(lista)
        c = jogaDadoX(lista)
        d = jogaDadoX(lista)
        if a == b and c == d:
            result += 1
    return result

