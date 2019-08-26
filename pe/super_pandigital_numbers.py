import itertools
import sys


def to_base_n(n, x):
    digits = []
    while x:
        digits.append(int(x%n))
        x = (x - x%n)/n
    return digits


def pandigital_in_base(n, x):
    digits = to_base_n(n, x)
    return set(digits).issuperset(set([i for i in range(0, n)])) 


def pandigital_in_base_10(x):
    return set([int(char) for char in str(x)]).issuperset(set([i for i in range(0, 10)])) 


first_digit = 1

super_pandigitals = []

check_bases = (11, 9, 8, 7, 6, 5, 4, 3, 2)

while len(super_pandigitals) < 10:
    last_digits = [i for i in range(0, 12) if i <> first_digit]
    perms = itertools.permutations(last_digits)
    super_pan = True
    for perm in perms:
        total = sum([v*12**(10-i) for i, v in enumerate(perm)]) + first_digit*12**11
        if not pandigital_in_base_10(total):
            continue
        for cb in check_bases:    
            if not pandigital_in_base(cb, total):
                super_pan = False
                break
        if super_pan:    
            super_pandigitals.append(total)
    first_digit += 1
    

print super_pandigitals
        

        
        
        
        
        
        
#         for base in check_bases:
#             if not pandigital_in_base(base, total):
#                 break
#             print perm, total
#             found = True
#             break
#     first_digit += 1
    


# 
# 
# digits = [d for d in range(1, super_level)]
# 
# 
# 
# perms = itertools.permutations(digits)
# 
# 
# 
# for perm in perms:
#     value = sum([v*super_level**i for i, v in enumerate(perm)])
#     print perm, value
#     i = super_level - 1
#     super_pan = True
#     while super_pan:
#         if pandigital_in_base(i, value):
#             if i == 2:
#                 print value
#                 sys.exit()
#             i -= 1
#             continue
#         else:
#             break
# 
#         
#         
#             
#             
#             
#         
#         

