n = input().split(", ")
m = input()

for i in range(len(n)):
    zvjezdice = "*" * len(n[i])
    m = m.replace(n[i], zvjezdice)

print(m)

# Programiranje je pisanje upustava racunaru sta i kako da ucini, a izvodi se u nekom od programskih jezika. Programiranje je umjetnost i umijece u stvaranju programa za racunare. Stvaranje programa sadrzi u sebi elemente dizajna, umjetnosti, nauke, mtematike kao i inzinjeringa. Osoba koja stvara programe zove se programer.
