def kvadratOdBrojeva(n):
    brojac = 1
    for i in range(n):
        ponavljanje = 1
        for j in range(n):
            if j + brojac - 1 < n:
                print(j + brojac, end=" ")
            elif j == n:
                brojac = 0
            else:
                print(ponavljanje, end=" ")
                ponavljanje += 1
        brojac += 1
        print()


n = int(input("Unesite proizvoljan prirodan broj: "))
kvadratOdBrojeva(n)
