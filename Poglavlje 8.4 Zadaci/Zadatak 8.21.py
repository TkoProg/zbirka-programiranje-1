n = input()

zadnji = ""
brojac = 0

for i in range(len(n) - 1, len(n) - 5, -1):
    zadnji += n[i]

zadnji = zadnji[::-1]

print("**** " * ((len(n) - len(zadnji)) // 4), end="")

print(zadnji, sep="")
