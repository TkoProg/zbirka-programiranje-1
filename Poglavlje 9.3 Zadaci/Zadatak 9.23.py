file = open("Zadatak 9.23.in", "r")

matrica = []
dzak = []
brojac = 0

while True:
    red = file.readline()
    if red == "":
        matrica.append(dzak)
        break
    red = red.rstrip("\n")
    red = red.split()
    if len(red[1]) > 1:
        if brojac == 0:
            brojac += 1
        else:
            matrica.append(dzak)
            dzak = []
    dzak.append(red)

file.close()

for i in range(len(matrica)):
    prosjek = True
    jedinice = []
    for j in range(1, len(matrica[i])):
        if int(matrica[i][j][1]) == 1:
            prosjek = False
            jedinice.append(matrica[i][j][0])
    if not prosjek:
        print(matrica[i][0][0], matrica[i][0][1], end=" ")
        for e in jedinice:
            print(e, end=" ")
    else:
        print(matrica[i][0][0], matrica[i][0][1], end=" ")
        print((int(matrica[i][1][1]) + int(matrica[i][2][1]) + int(matrica[i][3][1])) / 3, end=" ")
    print()
