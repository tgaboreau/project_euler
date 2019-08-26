import math
fl = math.floor
import pickle

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


def factors(n):
    return [1] + [f for f in range(2, int(fl(n/2)+1)) if not n%f] + [n]


def get_s(n):
    factorlist = factors(n)
    s = 0
    for i in range(0, len(factorlist)-1):
        for j in range(i+1, len(factorlist)):
            if not factorlist[j]%factorlist[i]:
                s += 1
    return s


def get_p(m):
    primes = 0
    i = 2
    p = 1
    while primes < m:
        if isprime(i):
            p *= i
            primes += 1
        i += 1    
    return p

def get_primes(start, m):
    primes = []
    i = start + 1
    while len(primes) < m:
        if isprime(i):
            primes.append(i)
        i += 1    
    return primes


primelists = []
start = 1

while len(primelists) < 904:
    print(len(primelists))
    l = get_primes(start, 1000)
#     print l
    primelists.append(l)
    start = primelists[-1][-1]

l = get_primes(start, 961)
print(l)

primelists.append(l)

pickle_out = open('904961_primes.pickle', 'wb')
pickle.dump(primelists, pickle_out)
pickle_out.close()



    

def get_E(m, n):
    x = get_s(get_p(m)**n)
    E = 0
    divides = True
    while divides:
        E += 1
        if not x%2**E:
            continue
        else:
            return E - 1


def get_Q(n):
    Q = 0
    for i in range(1, n+1):
        print(i)
        Q += get_E(904961, i)
    return Q

# print get_Q(8)
    
    



    
