n = input().lower()

print(n)

n = n.split()

print(n)

najduze = []
prethodni = 0

for i in range(len(n)):
    rijec = n[i]
    brojac = 0
    rijec2 = ""
    if i == 0:
        for k in range(len(rijec)):
            if rijec[k].isalpha():
                brojac += 1
        prethodni = brojac
        najduze.append(rijec)
        continue
    for j in range(len(rijec)):
        if rijec[j].isalpha():
            brojac += 1
            rijec2 += rijec[j]
    print(brojac, end=" ")
    if prethodni <= brojac:
        prethodni = brojac
        najduze.append(rijec2)

print(najduze)

neka = sorted(najduze)

najduza = len(neka[-1])

for i in range(len(najduze)):
    duzina = len(najduze[i])
    if duzina == najduza:
        print(najduze[i])

# Popocatepetl je vulkan u sredisnjem Meksiku, a njegov manji parnjak je vulkan Iztaccihuatl. Drugi je vulkan Sjeverne Amerike po visini, poslije Orizabe. To je jedan od aktivnijih vulkana u Meksiku. Zabiljezeno je vise od 20 velikih erupcija ovoga vulkana od dolaska Spanjolaca u Meksiko.
