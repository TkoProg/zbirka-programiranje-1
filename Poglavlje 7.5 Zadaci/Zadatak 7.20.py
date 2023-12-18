n = int(input())

lista = []
matrica = []
red = []
brojac = 0

for i in range(n**2):
    m = int(input())
    lista.append(m)

indeks = 0

while True:
    if brojac == n:
        matrica.append(red)
        red = []
        brojac = 0
    if len(matrica) == n:
        break
    red.append(lista[indeks])
    brojac += 1
    indeks += 1

rezultati = []

for i in range(len(matrica)):
    zbir = 0
    for j in range(len(matrica)):
        zbir += matrica[j][i]
    rezultati.append(zbir)

[print(x) for x in rezultati]
