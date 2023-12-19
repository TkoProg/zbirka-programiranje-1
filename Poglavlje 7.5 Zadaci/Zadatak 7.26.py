n = int(input())

matrica = []

for i in range(n):
    red = []
    for j in range(n):
        m = int(input())
        red.append(m)
    matrica.append(red)

nova_matrica = []

for i in range(n):
    kolona = []
    for j in range(n):
        el_kolone = matrica[j][i]
        kolona.append(el_kolone)
    nova_matrica.append(kolona)

for i in range(len(nova_matrica)):
    nova_matrica[i] = sorted(nova_matrica[i])

print()

for i in range(n):
    for j in range(n):
        print(nova_matrica[j][i], end=" ")
    print()
