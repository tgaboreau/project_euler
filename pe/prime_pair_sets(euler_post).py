import math
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


def ispair(a, b):
    return isprime(int(str(a) + str(b))) and isprime(int(str(b) + str(a)))

pairs = {}
primes = []
i = 3
fifthprimes = None
fourthprimes = None
# while not fifthprimes:
while not fourthprimes:
    if isprime(i):
        primes.append(i)
        firstprime = i
        pairs[i] = [p for p in primes[:-1] if ispair(firstprime, p)]
        for i2 in pair
        for secondprime in secondprimes:
            thirdprimes = [p for p in pairs[secondprime] if ispair(firstprime, p)]
            for thirdprime in thirdprimes:
                fourthprimes = [p for p in pairs[thirdprime] if p in secondprimes and p in thirdprimes]
                for fourthprime in fourthprimes:
                    if fourthprimes:
                        print fourthprimes
#                     fifthprimes = [p for p in pairs[fourthprime] if p in secondprimes and p in thirdprimes and p in fourthprimes]
#                     if fifthprimes:
#                         found = True
#                         print firstprime + secondprime + thirdprime + fourthprime + fifthprimes[0]
        pairs[i] = secondprimes
    i += 1   
            
  

