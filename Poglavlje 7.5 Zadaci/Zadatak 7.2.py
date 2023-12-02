najveca = -100
rijeci = []
suma = 0
prosjek = 0
brojac = 0

while True:
    n = input("Unesite rijec: ")
    if n == "":
        break
    rijeci.append(n)
    brojac += 1
    suma += len(n)

prosjek = suma / brojac

print()
print("Rijeci duze od prosjeka svih rijeci su: ")

for i in range(len(rijeci)):
    if len(rijeci[i]) > prosjek:
        print(rijeci[i])
