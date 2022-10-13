a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
if len(a) > len(b):
    for i  in range(len(b)):
        if b[i] in a:
            c.append(b[i])
else:
    for i  in range(len(a)):
        if a[i] in b:
            c.append(a[i])
print(*c)