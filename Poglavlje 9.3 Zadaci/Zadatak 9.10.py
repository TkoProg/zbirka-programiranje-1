file = open("Zadatak 9.10.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("/n")
    red = red.split()
    matrica.append(red)

file.close()

nova = []

red = int(matrica[0][0])
kolona = int(matrica[0][1])

for i in range(red):
    neka = []
    for j in range(kolona):
        neka.append(" ")
    nova.append(neka)

for i in range(1, len(matrica)):
    for j in range(len(matrica[i])):
        x = int(matrica[i][0][1])
        y = int(matrica[i][1][0])
        simbol = matrica[i][2]
        nova[x][y] = simbol

for i in range(len(nova)):
    for j in range(len(nova[i])):
        print(nova[i][j], end=" ")
    print()
