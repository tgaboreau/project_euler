import math

fl = math.floor

def isprime(n):
    if n == 1:
        return False
    elif not n%2:
        return False
    for i in range(3, int(fl(n**0.5)+1), 2):
        if not n % i:
            return False
    return True


def hcf(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a