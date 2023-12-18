a1 = int(input())

novi = str(a1)

brojevi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pojavljivanja = []

while True:
    zbir = 0
    for i in range(len(novi)):
        zbir += int(novi[i])
    novi += str(zbir)
    for i in range(len(novi)):
        if int(novi[i]) not in pojavljivanja:
            pojavljivanja.append(int(novi[i]))
    pojavljivanja = sorted(pojavljivanja)
    if brojevi == pojavljivanja:
        break

print(novi)
