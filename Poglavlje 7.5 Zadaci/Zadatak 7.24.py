n = input().split()

n = [int(x) for x in n]

c = 0
ogledalo = []

for i in range(len(n)):
    counter = 0
    c = 0
    zavrseno = False
    for j in range(len(n)-1, i, -1):
        counter = 0
        c = 0
        if n[i] == n[j]:
            counter += 1
            c = 1
            while True:
                if i + c > len(n) - 1:
                    break
                if j - c < 0:
                    break
                if n[i+c] != n[j-c]:
                    break
                if n[i+c] == n[j-c]:
                    counter += 1
                if i == len(n) - 1:
                    continue
                c += 1
        ogledalo.append(counter)

ogledalo.sort()

print(ogledalo[-1])
