n = int(input())

lista = []

for i in range(n):
    m = input()
    lista.append(m)

duzi = True
kraci = True
k = 1
pobjednici = []

for i in range(len(lista) - 1, -1, -1):
    duzi = True
    kraci = True
    if len(lista[i]) % 2 == 0:
        for j in range(len(lista) - 1 - k, -1, -1):
            if len(lista[j]) < len(lista[i]):
                kraci = False
                break
        if kraci:
            pobjednici.append(lista[i])
        k += 1
    else:
        for j in range(len(lista) - 1 - k, -1, -1):
            if len(lista[j]) > len(lista[i]):
                duzi = False
                break
        if duzi:
            pobjednici.append(lista[i])
        k += 1

pobjednici = pobjednici[::-1]

[print(x) for x in pobjednici]
