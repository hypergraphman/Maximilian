a = int(input())
b = int(input())
for i in range(a, b + 1):
    end = i % 10
    start = i
    while start > 10:
        start //= 10
    if start == end == 8:
        print(i)
