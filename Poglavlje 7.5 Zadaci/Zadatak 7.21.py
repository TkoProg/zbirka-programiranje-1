n = int(input())

matrica = []

for i in range(n):
    red = []
    for j in range(n):
        m = int(input())
        red.append(m)
    matrica.append(red)

suma1 = 0
suma2 = 0

for i in range(n):
    suma1 += (matrica[i][i])

for i in range(n):
    suma2 += matrica[i][n-i-1]

print(suma1 * suma2)
