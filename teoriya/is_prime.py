n = int(input())
f = True
for i in range(2, n // 2 + 1):
    if n % i == 0:
        f = False
if f:
    print('prime')
else:
    print('not prime')