from math import floor

n = int(input())

lista = []

for i in range(n):
    m = int(input())
    lista.append(m)

lista2 = sorted(lista)

medijan = floor(len(lista) / 2)

izbaci = lista2[medijan]

for i in range(len(lista)):
    if lista[i] == izbaci:
        continue
    print(lista[i], end=" ")
