number = int(input())
f = True
while number != 0:
    pre_number = number
    number = int(input())
    if pre_number <= number:
        f = False
if f:
    print('YES')
else:
    print('NO')