n = input().lower()

n = n.replace(",", "")
n = n.replace(".", "")

n = n.split()

brojac = 0
rijeci = []
broj_ponavljanja = []

for i in range(len(n)):
    rijec = n[i]
    if n[i] not in rijeci:
        rijeci.append(n[i])
        broj = n.count(rijec)
        broj_ponavljanja.append(broj)

# Zavrsni Ispit iz programiranja ima cetiri zadatka, a ispit iz programiranja tokom semestra ima tri zadatka, i znaci da ima jedan zadatak vise, ali zato ispit ima i vise vremena za izradu sva cetiri zadatka.

for i in range(len(broj_ponavljanja)):
    if broj_ponavljanja[i] > 1:
        print(f"{rijeci[i]}: {broj_ponavljanja[i]}")
