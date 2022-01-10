'''
Problema da Carga da Balsa

Balsa para atravessar veículos de um lado pro outro do rio

Fila Eesquerda e Direita

Comprimento da Balsa = L

Cada veículo tem um l

Entrada: array de n inteiros representando os tamanhos do veículo na fila
         L representando o tamanho da balsa

Saída: Sequência E, D, D, E, ... que embarque a maior quantidade de veículos
'''
## Tentativa falha de fazer o backtrack
##Ex = [4, 6, 1, 6, 1, 9]
##L = 10
##eC = [[1,"E"], [2, "D"]]
##def backtrack(L, arr, estadoCorrente = [[], []]):
##    E = estadoCorrente[0]
##    D = estadoCorrente[1]
##    contE = 0
##    contD = 0
##    if len(E) != 0:
##        for k in E:
##            contE += k
##        if cont <= L:
##            finalE = E
##    if len(D) != 0:
##        for l in D:
##            contD += l
##        if cont <= L:
##            finalD = D

E = 'E'
D = 'D'

def backtrack(sequencia, ocupado_esq, ocupado_dir, fila, L, seq_otimaL):
    # o estado corrente merece tratamento especial?
    if len(sequencia) > len(seq_otima):
        seq_otima.clear()
        for elemento in sequencia:
            seq_otima.append(elemento)

    # para cada próximo passo possível ...
    tamanho_prox = fila[len(sequencia)]
    # esquerda
    if(ocupado_esq + tamanho_prox) <= L:
        ocupado_esq += tamanho_prox
        sequencia.append(E)
        backtrack(sequencia, ocupado_esq, ocupado_dir, fila, L, seq_otima)
        sequencia.pop()
        ocupado_esq -= tamanho_prox
    # direita
    if(ocupado_dir + tamanho_prox) <= L:
        ocupado_dir += tamanho_prox
        sequencia.append(D)
        backtrack(sequencia, ocupado_esq, ocupado_dir, fila, L, seq_otima)
        sequencia.pop()
        ocupado_dir -= tamanho_prox


# Main
fila = eval(input("Digite a fila: "))
L = int(input("Digite L: "))
seq_otima = []
backtrack([], 0, 0, fila, L, seq_otima)

print(seq_otima)
print(len(seq_otima))
