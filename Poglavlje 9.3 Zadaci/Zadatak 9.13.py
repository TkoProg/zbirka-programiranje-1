file = open("Zadatak 9.13.in", "r")

matrica = []
brojac  = 0

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    red = red.split()
    if brojac == 0:
        brojac += 1
        continue
    else:
        matrica.append(red)

file.close()

broj = []
ponavljanja = []
linija = []

for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        linija.append(matrica[i][j])

for i in range(len(linija)):
    if linija[i] in broj:
        continue
    else:
        koliko = linija.count(linija[i])
        broj.append(linija[i])
        ponavljanja.append(koliko)

nova = sorted(ponavljanja)

for i in range(-1, -4, -1):
    indeks = ponavljanja.index(nova[i])
    print(broj[indeks], nova[i])
