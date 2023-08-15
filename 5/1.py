n = int(input())
k = int(input())
maximum = -(10**10)
result = None
for i in range(n, k + 1):
    s = 0
    for j in range(1, i + 1):
        if i % j == 0:
            s += j
    if s > maximum:
        maximum = s
        result = i
print(result, maximum)