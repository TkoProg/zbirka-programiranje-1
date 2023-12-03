lista = []

while True:
    n = input()
    if n == "-1":
        break
    lista.append(n)

sortirana_lista = sorted(lista)

najveci = int(lista[0])

for i in range(len(lista)):
    if int(lista[i][::-1]) > najveci:
        najveci = int(lista[i][::-1])

print(najveci - int(lista[0]))
