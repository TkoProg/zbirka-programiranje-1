n = input()

original = n

# n = n.replace(",", "")
# n = n.replace(".", "")

n = n.split()

m = []

for i in range(len(n)):
    prazno = " " * len(n[i])
    m.append(prazno)

for i in range(len(n)):
    if len(n[i]) > 5:
        if not n[i][-1].isalpha():
            povlaka = "-" * (len(n[i]) - 1)
            povlaka += " "
        else:
            povlaka = "-" * len(n[i])
        m[i] = povlaka

[print(x, end="") for x in original]
print()
[print(x, end=" ") for x in m]
