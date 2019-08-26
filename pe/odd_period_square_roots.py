import math
from datetime import datetime


def find_hcf(a, b, c):
    for i in range(int(math.ceil(max(a, b, c)/2))+1, 0, -1):
        if not (a%i or b%i or c%i):
            return i


def continue_fraction(numerator, n, remainder = None):
    root_integer = int(math.floor(n**0.5))
    if not remainder:
        remainder = -root_integer
    denominator = n-remainder**2
    remainder *= -numerator
    hcf = find_hcf(remainder, denominator, numerator)
    remainder /= hcf
    denominator /= hcf
    new_integer = 0
    while remainder - denominator >= -root_integer:
        remainder -= denominator
        new_integer += 1
    return  new_integer, remainder, denominator
        

start = datetime.now()

counter = 0

for n in range(0, 10000):
    if n**0.5%1.0:
        period = []
        numerator, remainder = 1, -int(math.floor(n**0.5))
        initial_numerator = numerator * 1
        initial_remainder = remainder * 1
        while n:
            integer, remainder, numerator = continue_fraction(numerator, n, remainder)
            period.append(integer)
            if remainder == initial_remainder and numerator == initial_numerator:
                break
        print(n, period)
        if len(period) % 2:
            counter += 1
            
print(counter)
print(datetime.now()-start)
