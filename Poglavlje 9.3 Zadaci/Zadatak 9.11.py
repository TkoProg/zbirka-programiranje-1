file = open("Zadatak 9.11.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    red = red.split()
    matrica.append(red)

file.close()

temperature = []

mjeseci = ["Januar", "Februar", "Mart", "April", "Maj", "Juni", "Juli", "August", "Septembar", "Oktobar", "Novembar", "Decembar"]

for j in range(len(matrica[0])):
    suma = 0
    for i in range(len(matrica)):
        suma += float(matrica[i][j])
    temperature.append(round(suma / 5, 2))

[print(x, end=" ") for x in temperature]

najveca = sorted(temperature)

# Nije zavrsen zadatak ja mislim, ne sjecam se