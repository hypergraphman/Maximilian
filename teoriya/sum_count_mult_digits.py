s = 0
count = 0
p = 1
number = int(input())
while number != 0:
    digit = number % 10
    s += digit
    p *= digit
    count += 1
    number //= 10
print(s)
print(count)
print(p)