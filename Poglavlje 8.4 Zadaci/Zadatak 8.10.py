n = input().lower()

e = 0
a = 0

for i in range(len(n)):
    if n[i] == "e":
        e += 1
    elif n[i] == "a":
        a += 1

if e > a:
    print("E")
elif e < a:
    print("A")
else:
    print("AE")
