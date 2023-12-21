file = open("Zadatak 9.1.in", "r")

lista = []

while True:
    linija = file.readline()
    if linija == "":
        break
    linija = linija.rstrip("\n")
    linija = linija.split()
    lista.append(linija)

nadjen = 0

for i in range(len(lista)):
    if "R" in lista[i]:
        nadjen = i
        break

nova = []

for i in range(nadjen, len(lista)):
    nova.append(lista[i])

brojac = 0
gdje_r = 0
zid = False

for i in range(len(nova[0])):
    if nova[0][i] == "R":
        gdje_r = i
        break

indeks_zida = 0
patos = False

for i in range(gdje_r + 1, len(nova[0])):
    if nova[0][i] == "#":
        zid = True
        indeks_zida = i
        break
    else:
        brojac += 1

if zid:
    for i in range(len(nova)):
        if nova[i][indeks_zida - 1] == "#":
            patos = True
            break
        else:
            brojac += 1

    if patos:
        print(brojac - 1)
        print("ne")
    else:
        print(brojac)
        print("da")

else:
    print(brojac + 1)
    print("da")
