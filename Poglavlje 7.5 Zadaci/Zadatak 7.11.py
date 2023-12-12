m = int(input())

lista = []

for i in range(m):
    a = int(input())
    lista.append(a)

indeksi = []

while True:
    n = int(input())
    if n == -1:
        break
    indeksi.append(n)

prvi = 0

for i in range(len(indeksi)):
    pamti = 0
    if i % 2 == 0:
        prvi = indeksi[i]
    else:
        drugi = indeksi[i]
        pamti = lista[prvi]
        lista[prvi] = lista[drugi]
        lista[drugi] = pamti

print(lista)
