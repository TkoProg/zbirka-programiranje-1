lista = input().split()

lista = [int(x) for x in lista]

brojac = 0

for i in range(1, len(lista)):
    if lista[i-1] < lista[i]:
        brojac += 1

print(brojac)

drugi = 0

for i in range(len(lista) - 1):
    zbir = 0
    if lista[i] < 0:
        continue
    # print(lista[i], end=" | ")
    for j in range(i + 1, len(lista)):
        if lista[j] < 0:
            continue
        zbir += lista[j]
        # print(lista[j], end=" ")

    if zbir < lista[i]:
        drugi += 1
    # print()

print(drugi)
