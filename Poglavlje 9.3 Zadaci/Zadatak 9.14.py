file = open("Zadatak 9.14.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    red = red.split()
    matrica.append(red)

file.close()

red_pal = True
mat_pal = True

for i in range(len(matrica)):
    for j in range(len(matrica[i])//2):
        if matrica[i][j] == matrica[i][-j-1]:
            continue
        else:
            red_pal = False

for j in range(len(matrica)):
    for i in range(len(matrica[j])//2):
        if matrica[i][j] == matrica[-i-1][j]:
            continue
        else:
            mat_pal = False

if red_pal and mat_pal:
    print("savrsena")
elif not red_pal and not mat_pal:
    print("nesavrsena")
else:
    print("polusavrsena")
