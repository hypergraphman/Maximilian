x = int(input())
y = int(input())
a = x
b = y
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
nod = a
print(nod)
nok = x * y // nod
print(nok)