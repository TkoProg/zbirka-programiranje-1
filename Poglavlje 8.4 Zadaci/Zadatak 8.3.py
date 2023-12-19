n = int(input())

rijeci = []

for i in range(n):
    r = input()
    rijeci.append(r)

nove = []
k = 0

for i in range(len(rijeci) - 1, -1, -1):
    brojac = 0
    for j in range(0, len(rijeci) - k - 1):
        brojac += len(rijeci[j])
    k += 1
    if brojac < len(rijeci[i]):
        nove.append(rijeci[i])

for i in range(len(nove) - 1, -1, -1):
    print(nove[i])
