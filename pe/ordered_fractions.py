import math
from isprime import *

max = 1.0

start_numerator = float(3)
start_denominator = float(7)
limit = 1000000

for i in xrange(1, limit):
    numerator = math.floor(i/start_denominator*start_numerator)
    remainder = start_numerator/start_denominator - numerator/float(i)
    if 0 < remainder < max:
        max = remainder
        max_denominator = i
        max_numerator = int(numerator)
        

print max_numerator, max_denominator, max

    
            
