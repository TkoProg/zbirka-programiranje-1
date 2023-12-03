import math

m = int(input())
lista = []

for i in range(m):
    n = int(input())
    lista.append(n)

pivot = lista[math.floor(m/2)]
manje = []
vece = []

for i in range(len(lista)):
    if i == math.floor(m/2):
        continue
    if lista[i] <= pivot:
        manje.append(lista[i])
    else:
        vece.append(lista[i])

[print(x, end=" ") for x in manje]
print(pivot, end=" ")
[print(x, end=" ") for x in vece]
