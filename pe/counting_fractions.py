from isprime import *

count = 0
for i in range(2, 10000):
    for j in range(1, i):
        if hcf(i, j) ==1:
            count += 1

print(count)
    
            
