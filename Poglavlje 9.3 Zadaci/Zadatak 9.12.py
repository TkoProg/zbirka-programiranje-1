file = open("Zadatak 9.12.in", "r")

sedmica = []
dan = []
dan_ili_ne = True

while True:
    red = file.readline()
    red = red.rstrip("\n")
    if red == "":
        break
    if len(red) == 1:
        dan = []
        sedmica.append(dan)
        continue
    else:
        red = red.split()
        dan.append(red)

file.close()

najmanja = sedmica[0][0][-1]
najveca = sedmica[0][0][-1]
najm_grad = ""
dan_u_sedm_najm = 0
najv_grad = ""
dan_u_sedm_najv = 0

for i in range(len(sedmica)):
    for j in range(len(sedmica[i])):
        if float(sedmica[i][j][-1]) < float(najmanja):
            najmanja = sedmica[i][j][-1]
            najm_grad = sedmica[i][j][:-1]
            dan_u_sedm_najm = i
        elif float(sedmica[i][j][-1]) > float(najveca):
            najveca = sedmica[i][j][-1]
            najv_grad = sedmica[i][j][:-1]
            dan_u_sedm_najv = i

sedmica = ["ponedeljak", "utorak", "srijeda", "cetvrtak", "petak", "subota", "nedelja"]

for i in range(len(najm_grad)):
    print(najm_grad[i], end=" ")

print(najmanja, end=" ")
print(sedmica[dan_u_sedm_najm])

for i in range(len(najv_grad)):
    print(najv_grad[i], end=" ")

print(najveca, end=" ")
print(sedmica[dan_u_sedm_najv])
