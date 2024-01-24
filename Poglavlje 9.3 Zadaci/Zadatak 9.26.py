file = open("Zadatak 9.26.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    red = red.split()
    matrica.append(red)

file.close()

klubovi = []

for i in range(len(matrica)):
    if matrica[i][0] not in klubovi:
        klubovi.append(matrica[i][0])
    if matrica[i][-1] not in klubovi:
        klubovi.append(matrica[i][-1])

bodovi = []

for i in range(len(klubovi)):
    bodovi.append(0)

for i in range(len(matrica)):
    if int(matrica[i][1]) > int(matrica[i][3]):
        gdje = klubovi.index(matrica[i][0])
        bodovi[gdje] += 3
    elif int(matrica[i][1]) < int(matrica[i][3]):
        gdje = klubovi.index(matrica[i][4])
        bodovi[gdje] += 3
    else:
        gdje1 = klubovi.index(matrica[i][4])
        gdje2 = klubovi.index(matrica[i][0])
        bodovi[gdje1] += 1
        bodovi[gdje2] += 1

lista = []

for i in range(len(klubovi)):
    zadnje = [klubovi[i], bodovi[i]]
    lista.append(zadnje)

lista.sort(key=lambda x: x[1], reverse=True)

for i in range(len(lista)):
    print(lista[i][0], lista[i][1])
