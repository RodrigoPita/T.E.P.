'''Entrada'''
L = []
ok = True
while ok:
    a = input("Ano de nascimento: ")
    b = input("Ano de morte: ")
    L.append([int(a), 1])
    L.append([int(b) + 1, 0])
    if len(L) > 11:
        ok = False
        
'''Saida'''
L.sort()
ano = 0
cont = 0
maxVivos = 0
for k in L:
    if k[1] == 1:
        cont += 1
    if k[1] == 0:
        cont -= 1
    if cont > maxVivos:
        maxVivos = cont
        ano = k[0]
print("O ano em mais pessoas estiveram vivas foi:", ano)
