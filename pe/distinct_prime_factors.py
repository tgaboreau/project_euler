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
    prime_factors = []
    complete = False
    while not complete:
        if n == 1:
            return len(set(prime_factors))
        if isprime(n):
            prime_factors.append(n)
            return len(set(prime_factors))
        for prime in primes:
            if not n%prime:
                prime_factors.append(prime)
                n = n/prime
                break
    
#     prime_factors = []
#     for prime in primes:
#         if prime > n:
#             break
#         while not n % prime:
#             prime_factors.append(prime)
#             n /= prime
#     return len(set(prime_factors))
            

# print count_distinct_prime_factors(12)



start = datetime.now()

primes = []
i = 1

consecutives = 0
while consecutives < 4:
    if isprime(i):
        primes.append(i)
        consecutives = 0
    elif count_distinct_prime_factors(i) == 4:
        consecutives += 1
    else:
        consecutives = 0
    i+=1

print i - consecutives
  
print datetime.now()-start


