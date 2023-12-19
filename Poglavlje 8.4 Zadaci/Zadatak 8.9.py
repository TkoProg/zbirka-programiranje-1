lista = []

while True:
    n = input()
    if n == "":
        break
    lista.append(n)

samoglasnici = "aeiouAEIOU"

for i in range(len(lista)):
    nova_rijec = ""
    for j in range(len(lista[i])):
        if lista[i][j] in samoglasnici:
            continue
        nova_rijec += lista[i][j]
    print(nova_rijec)
