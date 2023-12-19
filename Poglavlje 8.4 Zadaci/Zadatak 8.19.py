n = input()

n = "[" + n + "]"

brojac = 0
k = 0
uzastopni = []

if n == "":
    print(0)
else:
    for i in range(len(n) - 1):
        brojac = 0
        k = 0
        if n[i] == n[i+1]:
            k = i
            while True:
                if n[i] != n[k] or k == len(n) - 1:
                    break
                if n[i] == n[k]:
                    brojac += 1
                k += 1
        if k == len(n) - 1 and i == len(n) - 1:
            brojac += 1
        uzastopni.append(brojac)

    print(uzastopni)

    uzastopni = sorted(uzastopni)

    print(uzastopni[-1])
