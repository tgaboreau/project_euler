import math
import itertools
import datetime

def GenerateDivisors(n):
    return sum([i for i in range(1,int(math.floor(n/2))+1) if n%i ==0])


def check_abundance(n):
    print(n)
    total = 0
    for i in range(1,int(math.floor(n/2))+1):
        if not n%i:
            total += i
            if total > n:
                return True
    return False
    
    
start = datetime.datetime.now()

abundants = []

abundants = [i for i in range(1, 28124) if check_abundance(i)]

# for i in range(1,28124): 
#     if GenerateDivisors(i)>i:
#         abundants.append(i)
print(len(abundants))
# print abundants


abundant_pairs = list(itertools.product(abundants, repeat=2))


abundant_sums = list(set([sum(pair) for pair in abundant_pairs if sum(pair)<28124]))
# print abundant_sums

# abundant_sums = [sum(pair) for pair in list(itertools.product(abundants, repeat=2))]

nums = [i for i in range(1,28124) if i not in abundant_sums]

# print nums

print(sum(nums))

print(datetime.datetime.now()-start)

