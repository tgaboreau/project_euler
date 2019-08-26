import math
from isprime import *


def checkcons(a, b, max):
    n = 0
    while isprime(n**2 + n*a + b):
        n+=1
    return n
        
     
max = 0
for b in range(3, 1000, 2):
    if isprime(b):
        for a in range(-b, 1000, 2):
            primes = checkcons(a,b, max)
            if primes > max:
                max, maxa, maxb = primes, a, b


print(maxa*maxb)