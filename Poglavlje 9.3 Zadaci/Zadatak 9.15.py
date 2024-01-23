file = open("Zadatak 9.15.in", "r")

mapa = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    mapa.append(red)

file.close()

for e in mapa:
    print(e)

# Ovaj zadatak je nemoguc lmao
