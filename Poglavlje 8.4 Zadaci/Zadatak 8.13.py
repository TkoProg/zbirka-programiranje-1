n = input().lower()

kraj = False

while True:
    if kraj:
        break
    prvo = n[0]
    n = n.replace(n[0], "")
    for i in range(len(n)):
        broj = n.count(n[i])
        if broj == len(n):
            kraj = True

print(n)
