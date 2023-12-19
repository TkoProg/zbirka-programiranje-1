n = input().lower()

indeks = 0

samoglasnici = "aeiou"

for i in range(1, len(n)):
    if n[i] in samoglasnici:
        indeks = i
        break

prvi = n[:indeks+1]
drugi = n[indeks+1:]

print(drugi+prvi)
