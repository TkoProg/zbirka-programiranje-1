file = open("Zadatak 9.5.in", "r")

matrica = []
suma = 0

while True:
    red = file.readline()
    if red == "":
        break
    red = red.split()
    for i in range(3):
        suma += float(red[i])

print(suma)

file.close()
