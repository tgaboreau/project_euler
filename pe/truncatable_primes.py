import math
from datetime import datetime


def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(math.floor(n**0.5)+1)):
        if not n % i:
            return False
    return True


def has_0(n):
    return '0' in str(n)


def has_4(n):
    return '4' in str(n)


def has_6(n):
    return '6' in str(n)


def has_8(n):
    return '8' in str(n)


def ends_with_1(n):
    return str(n)[-1] == '1'


def istruncatable(n):
    s = str(n)
    for i in range(1, len(s)+1):
        if not isprime(int(s[0:i])):
            return False
    for i in range(1, len(s)):
        if not isprime(int(s[i:])):
            return False
    return True


start = datetime.now()

i = 0
j = 23
total = 0
while i < 11:
    if j % 3:
        if j % 5:
            if j % 7:
                if j % 11:
                    if j % 13:
                        if not has_0(j):
                            if not has_4(j):
                                if not has_6(j):
                                    if not has_8(j):
                                        if not ends_with_1(j):
                                            if istruncatable(j):
                                                total += j
                                                i += 1
    j += 2

print(total)
print(datetime.now()-start)
