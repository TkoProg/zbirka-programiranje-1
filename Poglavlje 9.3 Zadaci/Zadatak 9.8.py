import random

n = int(input("Unesite seed: "))

random.seed(n)

file = open("Zadatak 9.8.in", "r")

lista = []

red = file.read().splitlines()

print(red)

broj = int(red[0])

sifra = ""

for i in range(broj):
    gen = random.randint(2, len(red))
    sifra += red[gen].lower()

print(sifra)

file.close()
