lista = input().split()
lista = [int(x) for x in lista]

prvi_maksimum = 0
drugi_maksimum = 0

for i in range(1, len(lista) - 1):
    if lista[i-1] < lista[i] > lista[i+1]:
        prvi_maksimum = i
        break

for i in range(len(lista) - 2, 1, -1):
    if lista[i-1] < lista[i] and lista[i] > lista[i+1]:
        drugi_maksimum = i
        break

brojac = 0

for i in range(prvi_maksimum, drugi_maksimum + 1):
    brojac += 1

print(brojac)
