file = open("Zadatak 9.2.in", "r")

brojevi = []
simboli = []
brojac = 0

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("/n")
    red = red.split()
    brojac += 1
    if red[0][0].isnumeric():
        brojevi.append(red)
    else:
        simboli.append(red)

file.close()

suma = 0

for i in range(len(simboli)):
    for j in range(len(simboli[i])):
        if (simboli[i][j] == "*") and (int(brojevi[i][j]) % 2 == 0):
            suma += int(brojevi[i][j])

print(suma)
