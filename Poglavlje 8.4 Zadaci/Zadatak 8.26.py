n = input().lower()
m = input().lower()

novi = ""
drugi = ""
anagram = True

i = 0

for i in range(len(n)):
    if n[i].isalpha():
        novi += n[i]

for i in range(len(m)):
    if m[i].isalpha():
        drugi += m[i]

for i in range(len(novi)):
    if drugi.count(novi[i]) == novi.count(novi[i]):
        continue
    else:
        anagram = False

if anagram:
    print("Anagrami")
else:
    print("Nisu anagrami")
