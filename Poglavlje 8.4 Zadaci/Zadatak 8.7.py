lista = []

while True:
    m = input()
    if m == "":
        break
    lista.append(m)

for i in range(len(lista)):
    if lista[i][-1] == "." and len(lista[i]) < 20:
        print(lista[i])
