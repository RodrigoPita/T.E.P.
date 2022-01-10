"""PROGRAMAÇÃO DINÂMICA"""
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
memo = set()
E = 'E'
D = 'D'

'''Bottom_up'''
def backtrack(sequencia, ocupado_esq, ocupado_dir, fila, L, seq_otimaL):
    # o estado atual já foi visto antes?
    representacao = (max(ocupado_esq, ocupado_dir), len(sequencia))
    if representacao in memo:
        return # estado ja foi visitado
    
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

    memo.add(representacao)

# Main
fila = eval(input("Digite a fila: "))
L = int(input("Digite L: "))
seq_otima = []
backtrack([], 0, 0, fila, L, seq_otima)

print(seq_otima)
print(len(seq_otima))

'''Top-down'''
def balsa(Lc, Lv, fila, indice, maisCheio):
#def balsa(Lc, Lv, fila, indice, maisCheio, seq): colocar os if
    sol_from_memo = memo.get([Lc, indice])
    if sol_from_memo is not None:
        return sol_from_memo

    tamanho = fila(indice)

    # caso base
    if tamanho > Lv:
        return 0
    # tenta do lado mais cheio
    capac1 = Lc - tamanho
    capac2 = Lv
    sol_cheio = 1 + ...
    balsa(max(capac1, capac2), min(capac1, capac2), fila, indice + 1)

    # tenta do lado mais vazio
    capac1 = Lc
    capac2 = Lv - tamanho
    sol_vazio = 1 + ...
    balsa(max(capac1, capac2), min(capac1, capac2), fila, indice + 1)

    result = max(sol_cheio, sol_vazio)
    memo[[Lc, indice]] = result
    return result

