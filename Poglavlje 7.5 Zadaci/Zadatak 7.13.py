lista  = []

while True:
    n = input()
    if n == "":
        break
    n = int(n)
    lista.append(n)

parni = []
neparni = []

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        parni.append(lista[i])
    else:
        neparni.append(lista[i])

parni.sort()
k = 0
brojac = 0

while True:
    if k == len(lista) - 1:
        break
    if lista[k] % 2 == 0:
        lista[k] = parni[brojac]
        brojac += 1
    k += 1

print(lista)
