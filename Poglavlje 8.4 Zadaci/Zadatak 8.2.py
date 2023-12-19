n = input().lower()

najveci = ["", "", "", "", ""]

for i in range(len(n)):
    if n[i] == 'a':
        najveci[0] += "a"
    if n[i] == 'e':
        najveci[1] += "e"
    if n[i] == 'i':
        najveci[2] += "i"
    if n[i] == 'o':
        najveci[3] += "o"
    if n[i] == 'u':
        najveci[4] += "u"

najveci = sorted(najveci)

print(najveci[0][0])

# Popocatepetl je vulkan u sredisnjem Meksiku, a njegov jedna()koplunp manji parnjak je vulkan Iztaccihuatl. Drugi je vulkan Sjeverne Amerike po visini, poslije Orizabe. To je jedan od aktivnijih vulkana u Meksiku. Zabiljezeno je vise od 20 velikih erupcija ovoga vulkana od dolaska Spanjolaca u Meksiko.
