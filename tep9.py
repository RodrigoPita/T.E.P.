'''
Tecnica "O último entra ou não?"
Divisão e Conquista
'''

W = 4
#[[peso, valor]]
itens = ((4,20), (8,10), (4,6))
'''
itens = ((1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
         (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1))
'''
n = len(itens)

memo = {}
def resolverSubProblema(itens, quantItensDisponivel, capacidade):
    instancia = (quantItensDisponivel, capacidade)
    result_from_memo = memo.get(instancia)
    if result_from_memo is not None:
        return result_from_memo

    ultimoItemDisponivel = itens[quantItensDisponivel-1]
    if capacidade == 0 or quantItensDisponivel == 0:
        return 0
    
    if quantItensDisponivel == 1:
        if ultimoItemDisponivel[0] <= capacidade:
            return ultimoItemDisponivel[1]
        else:
            return 0
    if ultimoItemDisponivel[0] > capacidade:
        solLevandoOUltimo = 0
    else:
        solLevandoOUltimo = (ultimoItemDisponivel[1] +
                             resolverSubProblema(itens,
                                                 quantItensDisponivel-1,
                                                 capacidade - ultimoItemDisponivel[0]))
    
    solNaoLevandoOUltimo = resolverSubProblema(itens,
                                               quantItensDisponivel-1,
                                               capacidade)

    result = max(solLevandoOUltimo, solNaoLevandoOUltimo)
    memo[instancia] = result
    return result
