n = int(input())

rijeci = []

for i in range(n):
    r = input()
    rijeci.append(r)

brojac = 1

rijeci = rijeci[::-1]

ispunjava = []

for i in range(len(rijeci)):
    rijec = rijeci[i]
    total = 0
    for j in range(brojac, len(rijeci)):
        total += len(rijeci[j])
    if total < len(rijec):
        ispunjava.append(rijec)
    brojac += 1

ispunjava = ispunjava[::-1]

[print(x) for x in ispunjava]
