a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(len(a)):
    if a[i] not in b:
        c.append(a[i])
print(*c)