def provjeraPonavljanja(n,m):
    n = str(n)
    m = str(m)
    if m in n:
        return "Nalazi se"
    else:
        return "Ne nalazi se"


n = int(input())
m = int(input())

print(provjeraPonavljanja(n, m))
