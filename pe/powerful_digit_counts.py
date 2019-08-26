import math
counter = 0

for i in range(1, 100):
    print i, counter
    j = 1
    while len(str(j**i)) <= i:
        if len(str(j**i)) == i:
            counter += 1
        j += 1