file = open("Zadatak 9.4.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.split()
    matrica.append(red)

file.close()

nesigurni = []

for i in range(len(matrica)):
    sifra = matrica[i][1]
    if (matrica[i][0] == sifra) or (len(sifra) < 5) or ("1234" in sifra):
        nesigurni.append(matrica[i])

[print(x[0], x[1]) for x in nesigurni]
