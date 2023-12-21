file = open("Zadatak 9.6.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.split()
    matrica.append(red)

file.close()

povrsina = 0
indeks_pocetka = 0

for i in range(len(matrica)):
    pocetak = False
    kraj = False
    brojac = 0
    brojac2 = 0
    print(matrica[i])
    for j in range(len(matrica[i])):
        if (not pocetak) and (not kraj):
            if matrica[i][j] == "#":
                pocetak = True
                kraj = False
                brojac += 1
        elif pocetak and (not kraj):
            if matrica[i][j] == "#":
                kraj = False
                pocetak = False
                brojac += 1
            else:
                brojac += 1
    povrsina += brojac
    print(povrsina)

# Nisam znao ali sam jako blizu da uradim

# for i in range(len(matrica)):
#     print(matrica[i])
#     drugi_indeks = 0
#     prvi_indeks = 0
#     for j in range(len(matrica[i])):
#         if matrica[i][j] == "#":
#             prvi_indeks = j
#             break
#     for k in range(len(matrica[i]) - 1, -1, -1):
#         if matrica[i][k] == "#":
#             drugi_indeks = k
#             break
#     polja = drugi_indeks - prvi_indeks + 1
#     print(polja)
#     povrsina += polja
