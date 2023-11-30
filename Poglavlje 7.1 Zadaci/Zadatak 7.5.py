brojevi = []

while True:
    n = input("Unesite paran broj: ")
    if n == "":
        break
    brojevi.append(int(n))

najveci1 = 1000000000000000
najveci2 = 0

for i in range(len(brojevi)):
    if i < len(brojevi) / 2:
        if brojevi[i] < najveci1:
            najveci1 = brojevi[i]
    else:
        if brojevi[i] > najveci2:
            najveci2 = brojevi[i]

for i in range(najveci1, najveci2 + 1):
    if i % 2 == 0:
        print(i, end=" ")
