lista_neg = []
lista_nul = []
lista_poz = []
for i in range(10):
    n = int(input(f"Unesite {i+1} cio broj: "))
    if n < 0:
        lista_neg.append(n)
    elif n == 0:
        lista_nul.append(n)
    else:
        lista_poz.append(n)

[print(x, end=" ") for x in lista_neg]
[print(x, end=" ") for x in lista_nul]
[print(x, end=" ") for x in lista_poz]
