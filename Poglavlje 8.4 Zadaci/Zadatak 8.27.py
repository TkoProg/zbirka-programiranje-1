n = input().lower()

prvo = n[0]
zadnje = n[-1]

ostala = n[1:-1]

ostala = sorted(ostala)

print(prvo, end="")
for i in range(len(ostala)):
    print(ostala[i], end="")
print(zadnje)
