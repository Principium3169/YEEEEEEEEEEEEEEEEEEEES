a = int(input())
def is_prime(a):
    b = 0 
    for i in range(1, a + 1):
        if a % i == 0:
            b += 1
    if b == 2:
        return True
    else:
        return False
print(is_prime(a))