# insert good solution here

import math
import inspect

def decimalstring(n):
    outstring = ''
    numerator = 10
    for i in range(1,5000):
        outstring = outstring +str(int(math.floor(numerator/n)))
        numerator = (numerator%n)*10
    return outstring



