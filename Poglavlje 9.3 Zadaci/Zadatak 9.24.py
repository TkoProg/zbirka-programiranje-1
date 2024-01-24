file = open("Zadatak 9.24.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    red = red.split()
    matrica.append(red)

file.close()

matrica.sort()

brojac = 0
x = 0
y = 0

for i in range(len(matrica)):
    if brojac == 2:
        print(matrica[i-1][0], (x**2 + y**2)**(1/2))
        x = 0
        y = 0
        brojac = 0
    if brojac < 3:
        if matrica[i][1] == "G":
            y = int(matrica[i][2])
        if matrica[i][1] == "DO":
            y = -int(matrica[i][2])
        if matrica[i][1] == "L":
            x = -int(matrica[i][2])
        if matrica[i][1] == "DE":
            x = int(matrica[i][2])
        brojac += 1

print(matrica[-1][0], (x**2 + y**2)**(1/2))
