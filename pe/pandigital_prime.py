import math
import itertools
import datetime

start = datetime.datetime.now()

fl = math.floor

def isprime(n):
    if not n%3:
        return False
    if not n%5:
        return False
    if not n%7:
        return False
    if n == 1:
        return False
    for i in range(2, int(fl(n**0.5)+1)):
        if not n % i:
            return False
    return True

n = 9
found = False
while n and not found:
    'calculate sum of digits of n pandigital'
    'if sum divisible by 3 then cant be prime'
    if (n/2.0)*(n+1)%3:
        digits = [str(num) for num in range(1,n)]
        perms = list(itertools.permutations(digits))
        perms_less = [perm for perm in perms if int(perm[-1])%2!=0]
        perms_less.sort(reverse=True)
        for perm in perms_less:
            if isprime(int(str(n) +''.join(perm))):
                print  str(n) + ''.join(perm)
                found = True
                break
    n-=1

print datetime.datetime.now()-start