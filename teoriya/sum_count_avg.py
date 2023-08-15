n = int(input())
s = 0
count = 0
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        s += number
        count += 1
print(s)
print(count)
print(s / count)