n = int(input())
a = int(input())
print(n ** a)
p = 1
for i in range(a):
    p *= n
print(p)