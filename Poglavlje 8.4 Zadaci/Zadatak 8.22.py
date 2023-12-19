lista = []

while True:
    n = input().lower()
    if n == "":
        break
    n = n.replace(" ", "")
    lista.append(n)

tajna = ""
k = 0

for i in range(len(lista)):
    slovo = lista[i][k]
    tajna += slovo
    k += 1

print(tajna)
