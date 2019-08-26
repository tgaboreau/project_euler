from datetime import datetime
import math
from math import sqrt
from isprime import *
from pprint import pprint

limit = 1000000


def sieve(limit):
    limitn = limit + 1
    sieve = [True] * (limitn)
    sieve[0] = False
    sieve[1] = False
    for i in xrange(2,int(math.sqrt(limit))+1):
        if not sieve[i]:
            continue
        for pointer in xrange(i**2, limitn, i):
            sieve[pointer] = False
    return sieve
#  
primes = sieve(limit)


def get_totient(n):
    totient = n
    i = 2
    while i <= n:
        if primes[i]:
            if not n % i:
                totient *= (1.0-1.0/i)
        i+=1
    return int(totient)


for i in range(2, 10000):
    get_totient(i)
    
totients = {}
 

