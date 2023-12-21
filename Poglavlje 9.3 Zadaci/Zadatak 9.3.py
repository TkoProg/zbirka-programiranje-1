file = open("Zadatak 9.3.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("/n")
    red = red.split()
    matrica.append(red)

file.close()

print(matrica)

jedan = []
dva = []
tri = []

for i in range(len(matrica)):
    if matrica[i][2] == "1":
        ime_pre = matrica[i][0] + " " + matrica[i][1]
        jedan.append(ime_pre)
    elif matrica[i][2] == "2":
        ime_pre = matrica[i][0] + " " + matrica[i][1]
        dva.append(ime_pre)
    else:
        ime_pre = matrica[i][0] + " " + matrica[i][1]
        tri.append(ime_pre)

[print(x) for x in jedan]
print()
[print(x) for x in dva]
print()
[print(x) for x in tri]
