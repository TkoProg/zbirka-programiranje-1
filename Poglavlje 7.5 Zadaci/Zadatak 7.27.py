brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ispravan = True

matrica = []
for i in range(3):
    n = input().split()
    matrica.append(n)

lista = []

for i in range(3):
    for j in range(3):
        lista.append(int(matrica[i][j]))

for i in range(len(brojevi)):
    pojavljivanje = lista.count(brojevi[i])
    if pojavljivanje != 1:
        ispravan = False

for i in range(len(lista)):
    if 1 > lista[i] or lista[i] > 9:
        ispravan = False

if ispravan:
    for i in range(3):
        for j in range(3):
            print(matrica[i][j], end=" ")
        print()
    print("ispravan")
else:
    for i in range(3):
        for j in range(3):
            print(matrica[i][j], end=" ")
        print()
    print("neispravan")
