n = input()
m = int(input())

iza_decimale = n[-m:]

prije_decimale = n[:-m]

print(prije_decimale, ".", iza_decimale, sep="")
