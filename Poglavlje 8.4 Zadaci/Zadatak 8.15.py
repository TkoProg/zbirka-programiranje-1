n = input().lower()
m = input().lower()

nalazi_se = True

i = 0

for e in m:
    nasao = False
    while i < len(n) and not nasao:
        if n[i] == e:
            nasao = True
        i += 1
    if not nasao:
        nalazi_se = False

if nalazi_se:
    print("Nalazi se!")
else:
    print("Ne nalazi se!")
