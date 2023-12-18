def fibonaci(n):
    broj = 1
    holder = 0
    for i in range(n):
        prethodni = broj
        broj = holder
        broj = prethodni + broj
        holder = prethodni
    return broj


n = input().upper()
sek = input().split()

sek = [int(x) for x in sek]

slova = []

for i in range(len(n)):
    if 65 <= ord(n[i]) <= 90:
        slova.append(n[i])

zadnja = []

for i in range(len(slova)):
    zadnja.append(0)

print(zadnja)

for i in range(len(sek)):
    clan = 1
    while True:
        if fibonaci(clan) == sek[i]:
            print(clan)
            break
        clan += 1
    zadnja[clan - 1] = slova[i]

print(zadnja)
