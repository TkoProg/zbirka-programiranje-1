brojevi = []
zadnji = ""
prethodni = ""
ima = False

while True:
    broj = input("Unesite dvocifren broj: ")
    if broj == "":
        zadnji = prethodni[::-1]
        break
    brojevi.append(broj)
    prethodni = broj

for i in range(len(brojevi)):
    if zadnji == brojevi[i]:
        ima = True

if ima:
    print("Da")
else:
    print("Ne")
