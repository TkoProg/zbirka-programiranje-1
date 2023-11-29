def sabiranjeBrojeva(n):
    n = str(n)
    brojac = 0
    suma = 0
    tacno = False
    while True:
        for i in range(len(n)):
            suma += int(n[i])
        if suma < 10:
            return suma
        else:
            n = str(suma)
            suma = 0


n = int(input("Unesite visecifren broj: "))

print(sabiranjeBrojeva(n))
