import math
from datetime import datetime

start = datetime.now()

def triangular(n):
    return (n*(n+1))/2
 
def is_pentagonal(p):
    return (((24*p+1)**0.5+1)/6).is_integer()


def is_hexagonal(p):
    return (((8*p+1)**0.5+1)/4).is_integer()


a = 287

answered = False

while not answered:
    ta = triangular(a)
    if is_pentagonal(ta) and is_hexagonal(ta):
        print(ta)
        answered = True
    a += 1

        
print(datetime.now() - start)        
        
        



