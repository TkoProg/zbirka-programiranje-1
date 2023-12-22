file = open("Zadatak 9.9.in", "r")

sekvenca = file.read()

indeks = sekvenca.find("AGGT")

najveci_ostatak = 0
pamti = ""

podsekvenca = sekvenca[indeks + 4:]

while True:
    if len(podsekvenca) < 5:
        break
    indeks1 = podsekvenca.find("AGGT")
    ostatak = podsekvenca[:indeks1]
    if len(ostatak) > najveci_ostatak:
        pamti = ostatak
        najveci_ostatak = len(pamti)
        podsekvenca = podsekvenca[indeks1 + 4:]
    else:
        podsekvenca = podsekvenca[indeks1 + 4:]
    if len(podsekvenca) < len(ostatak):
        break

print(pamti)
