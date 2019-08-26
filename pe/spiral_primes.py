from isprime import *
from datetime import datetime

start = datetime.now()

tr, tl, bl, br = 3, 5, 7, 9
increment = 10
prime = 3.0
total = 4.0


while prime/total > 0.1:
    tr += increment
    tl += increment + 2
    bl += increment + 4
    br += increment + 6
    total += 4
    prime += isprime(tr)
    prime += isprime(tl)
    prime += isprime(bl)
    prime += isprime(br)
    increment += 8


print(total/2+1)

print(datetime.now()-start)