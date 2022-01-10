#numero magico -> quadrado perfeito e triangular
def intersect(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 
L = []
x = 1
stepX = 2
y = 1
stepY = 3
k = 0
ok = True
while ok:
    if len(L) > k:
        print(L)
        k = len(L)
        
    if x == y:
        L.append(x)
        y += stepY
        stepY += 2
    if x < y:
        x += stepX
        stepX += 1
    if y < x:
        y += stepY
        stepY += 2




'''
    if math.sqrt(x) - int(math.sqrt(x)) == 0 and int(math.sqrt(x))**2 == x:
        L.append(x)
        print(x)
'''

##1
##36
##1225
##41616
##1413721
##48024900
##1631432881
##55420693056
##1882672131025
##63955431761796
##2172602007770041
##73804512832419600
