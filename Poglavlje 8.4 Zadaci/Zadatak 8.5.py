from math import floor

brojevi = []

while True:
    m = input()
    if m == "":
        break
    brojevi.append(m)

for i in range(len(brojevi)):
    if int(brojevi[i][floor(len(brojevi[i])/2)]) > 5:
        print(brojevi[i], end=" ")
