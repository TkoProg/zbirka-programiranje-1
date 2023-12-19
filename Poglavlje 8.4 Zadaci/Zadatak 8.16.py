n = input()

povlake = []

for i in range(len(n)):
    povlake.append(" ")

recenica = []

for i in range(len(n)):
    recenica.append(n[i])

for i in range(len(recenica)):
    if recenica[i] == "i" and recenica[i-1] == " " and recenica[i+1] == " ":
        recenica[i] = "I"
        povlake[i] = "-"

[print(x, end="") for x in recenica]
print()
[print(x, end="") for x in povlake]
