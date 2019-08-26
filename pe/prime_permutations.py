import itertools
import math
import datetime
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

def get_perms(num):
    return [int(''.join(perm)) for perm in itertools.permutations(str(num)) if int(''.join(perm)) > num]
    
start = datetime.datetime.now()   
i = 1488
found = False
while not found:
    if isprime(i):
        perms = get_perms(i)
        for perm in perms:
            if isprime(perm):
                if isprime(2*perm-i) and sorted(str(perm)) == sorted(str(2*perm-i)) :
                    print i, perm, 2*perm-i
                    found = True
                    break
    i+=1
    
print datetime.datetime.now()-start    



     



