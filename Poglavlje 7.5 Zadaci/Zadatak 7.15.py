import statistics as s

# n = input().split()

# n = [1,1,1,4,4,3,5,5,2,3,2,3,2,3,2,3,5,5,3]
#
# # najveci = s.mode(n)
# # print(n.count(najveci))
#
# # print(najveci)
#
# brojac = 0
# ponavljanja = 0
# uporedba = 0
# skupine = []
# prvi = True
#
# for i in range(len(n)):
#     broj = n[i]
#     if ponavljanja == 0:
#         prethodni = broj
#         ponavljanja += 1
#         brojac += 1
#         continue
#     if prethodni == broj:
#         brojac += 1
#     else:
#         skupine.append(brojac)
#         prethodni = 0
#         brojac = 0
#
# print(skupine)

# ADI NACIN

n = [1, 1, 1, 4, 4, 3, 5, 5, 2, 5, 5, 3]
c = 0
s = 0
p = 0
while c != len(n)-1:
    b = n[c]
    for j in n[c+1:]:
        if b == j:
            c += 1
            p = 1
        elif p == 1:
            s += 1
            c += 1
            p = 0
            break
        else:
            c += 1
            p = 0
            break
if n[len(n)-1] == n[len(n)-2]:
    s += 1
print(s)
