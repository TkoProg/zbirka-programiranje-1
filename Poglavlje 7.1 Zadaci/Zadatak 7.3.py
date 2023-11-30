brojevi = []

m = int(input("Unesite paran broj m: "))

for i in range(m):
    n = int(input(f"Unesite {i}. cijeli broj: "))
    brojevi.append(n)

najmanji = 0
najveci = 0
brojevi = sorted(brojevi)

for i in range(len(brojevi)):
    if i < len(brojevi) / 2:
        najmanji += brojevi[i]
    else:
        najveci += brojevi[i]

print()

print(f"Vas rezultat je: {najveci-najmanji}")
