import math
from datetime import datetime


start = datetime.now()


def find_hcf(a, b):
    for i in xrange(int(math.ceil(max(a, b)/2))+1, 0, -1):
        if not (a%i or b%i):
            return i
        

def get_minimal_x(d):
    y = 1
    x_prev = 0
    while (float(1 + d*y**2)**0.5) % 1.0:
        x2 = float(1 + d*y**2)
#         print x2, x2**0.5, x2**0.5 - x_prev
        x_prev = x2**0.5
        y+=1
    return int((1 + d*y**2)**0.5), y


max_x = 0    
for d in range(2, 1001):
    if not float(d)**0.5 % 1.0:
        continue
    else:
        low_x, y = get_minimal_x(d)
        print d, y, 1+d*y**2
        max_x = max(max_x, low_x)


print max_x      
print datetime.now()-start
    