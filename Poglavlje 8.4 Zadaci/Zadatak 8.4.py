lista = []

while True:
    n = input().lower()
    if n == "":
        break
    lista.append(n)

ispunjava = []

for i in range(len(lista)):
    if (lista[i][0] == lista[i][-1]) and (lista[i].count(lista[i][0]) == 2):
        ispunjava.append(lista[i])

[print(x) for x in ispunjava]
