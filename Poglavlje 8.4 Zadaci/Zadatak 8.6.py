lista = []

while True:
    m = input()
    if len(m) != 1:
        break
    lista.append(m)

suma = 0

for i in range(len(lista)):
    if not lista[i].isnumeric():
        continue
    else:
        if int(lista[i]) % 2 == 0:
            suma += int(lista[i])

print(suma)
