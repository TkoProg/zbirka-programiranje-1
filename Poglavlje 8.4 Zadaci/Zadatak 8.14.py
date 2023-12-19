n = input().lower()

n = n.replace(",", "")
n = n.replace(".", "")
n = n.replace("!", "")
n = n.replace("?", "")

n = n.split()

brojac = 0

for i in range(len(n)):
    if n[i][0] == n[i][-1]:
        brojac += 1

print(brojac)
