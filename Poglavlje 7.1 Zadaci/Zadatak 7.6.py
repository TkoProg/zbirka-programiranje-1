brojevi = []

for i in range(5):
    n = int(input(f"Unesite {i+1}. broj: "))
    brojevi.append(n)

brojevi = sorted(brojevi, reverse=True)

print(brojevi[2])
