m = int(input())
n = int(input())

harun = []
sead = []

for i in range(m+n):
    k = int(input())
    if i < m:
        harun.append(k)
    else:
        sead.append(k)

print(harun)
print(sead)

zbir_sead = 0
zbir_harun = 0

for i in range(len(sead)):
    zbir_sead += sead[i]

for i in range(len(harun)):
    zbir_harun += harun[i]

trigger = False

for i in range(len(sead)):
    if zbir_sead - sead[i] == zbir_harun:
        print("jeste")
        trigger = True
        break

if not trigger:
    print("nije")
