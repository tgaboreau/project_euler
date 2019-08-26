from isprime import *

i = 1
j = 2
while i * j < 1000000:
    if isprime(j):
        i*=j
    j+=1
print(i)



    
            
"""

totients = {}


for i in range(2, 1000):
    if primes[i]:
        print i
        totients[i] = i-1
        continue
    else:
        for j in range(2, i):
            print i, j
            if hcf(j, i) == 1:
                totients[i*j] = totients[i] * totients[j]
 
pprint(totients)

"""