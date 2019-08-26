import math
import itertools
from datetime import datetime

fl = math.floor

def isprime(n):
    if n == 1:
        return False
    if n in [3, 5, 7]:
        return True
    if not n % 3:
        return False
    if not n % 5:
        return False
    if not n % 7:
        return False
    for i in range(2, int(fl(n**0.5)+1)):
        if not n % i:
            return False
    return True


def count_distinct_prime_factors(n):
    return len(set([f for f in range(2, int(fl(n/2)+1)) if not n%f and isprime(f)]))

start = datetime.now()

i = 1

consecutives = 0
while consecutives < 4:
    if not i % 1000:
        print(i)
    if isprime(i):
        consecutives = 0
    elif count_distinct_prime_factors(i) == 4:
        consecutives += 1
    else:
        consecutives = 0
    i+=1

print(i - consecutives)
  
print(datetime.now()-start)
