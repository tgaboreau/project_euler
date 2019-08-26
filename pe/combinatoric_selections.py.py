from datetime import datetime

import math

def factorial(n):
    for i in range(2, n):
        n*=i
    return n

count = 0
for n in range(23, 101):
    for r in range(2, n):
        if factorial(n)/(factorial(r) * factorial(n-r)) > 1000000:
            count+=1
            
print(count)