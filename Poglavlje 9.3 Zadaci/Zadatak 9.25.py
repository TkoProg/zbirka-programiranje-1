file = open("Zadatak 9.25.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    red = red.split()
    matrica.append(red)

file.close()

for i in range(len(matrica)):
    matrica[i][2] = int(matrica[i][2])

nova = sorted(matrica, key=lambda x: x[2])


nova.sort(reverse=True)

prodavaci = []
zarada = []
pojavljeni_prodavaci = []
totalna_prodaja = []

for i in range(len(nova)):
    if nova[i][0] not in pojavljeni_prodavaci:
        pojavljeni_prodavaci.append(nova[i][0])
        zarada.append(nova[i][2])
    elif nova[i][0] in pojavljeni_prodavaci:
        mjesto = pojavljeni_prodavaci.index(nova[i][0])
        zarada[mjesto] += nova[i][2]

zadnja = []

for i in range(len(pojavljeni_prodavaci)):
    place_holder = []
    place_holder.append(pojavljeni_prodavaci[i])
    place_holder.append(zarada[i])
    zadnja.append(place_holder)

bas_zadnja = sorted(zadnja, key=lambda x: x[1], reverse=True)

for i in range(3):
    print(bas_zadnja[i][0], bas_zadnja[i][1])

auta = ""

for i in range(len(nova)):
    auta += nova[i][1] + " "

auta = auta.split()
pojavila = []
oboje = []
posljednje = []

for i in range(len(auta)):
    if auta[i] not in pojavila:
        oboje = []
        pojavljivanja = auta.count(auta[i])
        pojavila.append(auta[i])
        oboje.append(pojavljivanja)
        oboje.append(auta[i])
        posljednje.append(oboje)

posljednje.sort(reverse=True)

for i in range(3):
    print(posljednje[i][1], posljednje[i][0])
