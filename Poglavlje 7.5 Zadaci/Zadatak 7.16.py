brojevi = input().split()

lista = [int(x) for x in brojevi]

n = int(input())

sortirana = sorted(lista)

nti_najveci = sortirana[-n]

print(sortirana[-1] - nti_najveci)
