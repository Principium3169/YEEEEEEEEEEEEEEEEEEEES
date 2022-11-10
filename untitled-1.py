a = list(map(int, input().split()))
a.sort()
number = int(input())

mid = len(a)//2
low = 0
high = len(a) - 1

while a[mid] != number and low <= high:
    if number > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low <= high:
    print(mid)
else:
    print('NO')