n = int(input("Unesite broj: "))
lista = []

for i in range(n):
    a = int(input(f"Unesite {i+1} broj: "))
    lista.append(a)

lista.sort()

m = int(input("Unesite broj: "))

for i in range(m, len(lista)-m):
    print(lista[i], end=" ")
