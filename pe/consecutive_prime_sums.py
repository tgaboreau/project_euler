from isprime import *

primes = []
i = 1
while sum(primes) + i < 1000000:
    if isprime(i):
        primes.append(i)
    i += 1


remove = 1
found = False

while not found:
    for i in range(1, remove+1):
        if -(remove-i):
            end = -(remove-i)
        else:
            end = None
        if isprime(sum(primes[i : end])):
            print(sum(primes[i : end]))
            found = True
    remove += 1


