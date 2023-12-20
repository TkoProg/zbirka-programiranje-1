m = input().upper()
prva = []

for i in range(len(m)):
    prva.append(m[i])

lista = []
lista.append(prva)

for i in range(len(m) - 1):
    n = input().upper()
    rijec = []
    for j in range(len(n)):
        rijec.append(n[j])
    lista.append(rijec)

kolone = []

for j in range(len(lista)):
    pojedinacno = []
    for i in range(len(lista)):
        pojedinacno.append(lista[i][j])
    kolone.append(pojedinacno)

if lista == kolone:
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end=" ")
        print()
    print("ispravan")
else:
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end=" ")
        print()
    print("neispravan")
