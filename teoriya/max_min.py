maximum = -(10**10)
minimum = 10**10
count = 0
number = int(input())
while number != 0:
    if 160 <= number <= 180:
        count += 1
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    number = int(input())
print(count)
print(maximum)
print(minimum)
