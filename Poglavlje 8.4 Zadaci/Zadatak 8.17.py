n = input().lower()
m = input().lower()

for i in range(len(m)):
    if m[i] in n:
        n = n.replace(m[i], "")

pojavljivanja = []

for i in range(len(n)):
    if n[i] not in pojavljivanja:
        pojavljivanja.append(n[i])

print(len(pojavljivanja))
