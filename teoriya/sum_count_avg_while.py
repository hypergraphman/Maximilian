s = 0
count = 0
number = int(input())
while number != 0:
    if number % 2 == 0:
        s += number
        count += 1
    number = int(input())
print(s)
print(count)
print(s / count)