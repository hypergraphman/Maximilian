p = 1
number = int(input())
while number != 0:
    if number % 2 != 0:
        p *= number
    number = int(input())
print(p)