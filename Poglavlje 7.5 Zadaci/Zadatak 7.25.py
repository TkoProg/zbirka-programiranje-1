file = open("Zadatak 7.25.in", "r")

lista = []

while True:
    linija = file.readline().rstrip("\n")
    if linija == "":
        break
    linija = linija.split(", ")
    lista.append(linija)

file.close()

drzave = []
najveca = []
najvise = 0

for i in range(len(lista)):
    drzava = lista[i][1]
    if drzava not in drzave:
        for j in range(i, len(lista)):
            if drzava == lista[j][1]:
                if int(lista[i][2]) <= int(lista[j][2]):
                    najvise = lista[j][0]
        drzave.append(drzava)
        najveca.append(najvise)

najveca = sorted(najveca)

[print(x) for x in najveca]
