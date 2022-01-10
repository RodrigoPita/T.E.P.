'''
Quadrado de Palavras

Entrada: lista de palavras
Saída: Maior quadrado de palavras possível
(matriz de caracteres, onde cada linha e coluna seja uma palavra válida da lista)
'''

FILE = "palavras.txt"
palavras = []

for k in open(FILE):
    palavras.append(k.strip('\n'))
    palavras.sort(key = lambda item: (len(item), item))

def tamanhos(lista):
    tam = []
    for k in lista:
        tam.append(len(k))
    return tam

def quadradoPalavras(lista):
    tamanhos_maior_palavra = max(tamanhos(lista))
    
def divideList(lista): 
    dct = {} 
  
    for elemento in lista: 
        if len(elemento) not in dct: 
            dct[len(elemento)] = [elemento] 
        elif len(elemento) in dct: 
            dct[len(elemento)] += [elemento] 
      
    result = [] 
    for key in sorted(dct): 
        result.append(dct[key]) 
      
    return result 
