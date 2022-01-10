'''
Entrada n

Saida: Todas as permutações caóticas dos primeiros n números


backtrack(estado corrente C):
    testa se C é estado "final" ("alvo"), se for, imprime e retorna
    for each "próximo passo possível" p (obetendo a configuração Cp):
        dê o passo p, isto é, transforme C em Cp
        backtrack(Cp)
        desfaz o passo p
'''

memo = {}
def countCaotic(n):
    result_from_memo = memo.get(n)
    if result_from_memo is not None:
        return result_from_memo
    if n == 1:
        return 0
    if n == 2:
        return 1
    result = (n-1)*(countCaotic(n-1)+countCaotic(n-2))
    memo[n] = result
    return result


def backtrack(estadoCorrente, n):
    if len(estadoCorrente) == n:
        print(estadoCorrente)
        return # nada mais a ser feito, estamos numa folha da árvore
    
    for numero in range(1, n+1):
        if numero in estadoCorrente:
            continue # este numero já apareceu; não pode ser repetido
        if numero == len(estadoCorrente) + 1:
            continue # não posso colocar o número na próxima posição
                     # (seria a posicção "certa" (não-caótica) dele)
                     
        # dá o passo, gerando uma nova configuração
        estadoCorrente.append(numero)

        # chama recursivamente
        backtrack(estadoCorrente, n)

        # limpa a sujeira
        estadoCorrente.pop()

n = 5
estadoInicial = []
backtrack(estadoInicial, n)
