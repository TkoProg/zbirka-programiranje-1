lista = input().split()

naopaka = list(reversed(lista))
najveci = []

for i in range(len(lista)):
    daljina = 0
    brojac = 0
    broj = lista[i]
    for j in range(len(lista)):
        if broj == naopaka[j]:
            break
        brojac += 1
    daljina = len(lista) - brojac - i
    najveci.append(daljina)

najveci.sort()

print(najveci[-1])
