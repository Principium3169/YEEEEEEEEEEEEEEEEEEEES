a = list(map(int, input().split()))
b = 0
c = 0
d = 0
for i in range(len(a)):
    b += a[i]
print(b)
while sum(a) > 0:
    c += sum(a)
    a = []
print(c)



    