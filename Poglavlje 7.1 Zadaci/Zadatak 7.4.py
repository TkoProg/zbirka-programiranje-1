gradovi = []

while True:
    n = input("Unesite imena gradova: ")
    if n == "":
        break
    gradovi.append(n)

brojS = 0
brojB = 0

gradS = []
gradB = []

for i in range(len(gradovi)):
    if gradovi[i][0] == "S":
        brojS += 1
        gradS.append(gradovi[i])
    if gradovi[i][0] == "B":
        brojB += 1
        gradB.append(gradovi[i])

if brojS > brojB:
    for i in range(len(gradS)):
        print(gradS[i], end=" ")

elif brojS < brojB:
    for i in range(len(gradB)):
        print(gradB[i], end=" ")

else:
    for i in range(len(gradovi)):
        if gradovi[i][0] == "S":
            print(gradovi[i], end=" ")
        if gradovi[i][0] == "B":
            print(gradovi[i], end=" ")
