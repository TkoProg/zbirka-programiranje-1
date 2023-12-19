lista = []

while True:
    n = input()
    if n == "":
        break
    lista.append(n)

for i in range(len(lista)):
    if lista[i][0] != "b":
        print(lista[i], end=" ")
