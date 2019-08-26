from isprime import *
from datetime import datetime

start = datetime.now()

pairs = {}
primes = []

i = 3
found = False

def ispair(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
#     print ab, ba
    if isprime(ab):
        return isprime(ba)

# while not found:
#     if isprime(i):
#         primes.append(i)
#         secondprimes = [p for p in primes[:-1] if ispair(i, p)]
#         for secondprime in secondprimes:
#             thirdprimes = set(pairs[secondprime]) & set(secondprimes)
#             for thirdprime in thirdprimes:
#                 fourthprimes = set(pairs[thirdprime]) & set(thirdprimes)
#                 for fourthprime in fourthprimes:
#                     fifthprimes = set(pairs[fourthprime]) & set(fourthprimes)
#                     if fifthprimes:
#                         found = True
#                         print i, secondprime, thirdprime, fourthprime, list(fifthprimes)[0]
#                         print i + secondprime + thirdprime + fourthprime + list(fifthprimes)[0]
#         pairs[i] = secondprimes
#     i += 1

base = 3
   
while not found:
    if isprime(base):
        print base
        primes.append(base)
        secondprimes = []
        
        for prime in primes[:-1]:
            if ispair(base, prime):
                secondprimes.append(prime)
                 
                for prime2 in pairs[prime]:
                    thirdprimes = []
                    if prime2 in secondprimes[-1]:
                        thirdprimes.append(prime2)
                         
                        for prime3 in pairs[prime2]:
                            fourthprimes = []
                            if prime3 in thirdprimes:
                                fourthprimes.append(prime3)
 
                                for prime4 in pairs[prime3]:
                                    if prime4 in fourthprimes:
                                        print prime, prime2, prime3, prime4
                                        found = True
        pairs[i] = secondprimes
    base += 1
#                                         

print datetime.now() - start   


