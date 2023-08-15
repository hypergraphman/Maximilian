maximum = -(10**10)
n = int(input())
for i in range(n):
    number = int(input())
    if number > maximum:
        maximum = number
print(maximum)