a = input()
b = len(a)
if a[0: b] == a[::-1]:
    print(True)
else:
    print(False)