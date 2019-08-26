# import itertools
from datetime import datetime
# 
# digits = [str(n) for n in range(1,10)]
# 
# perms = itertools.permutations(digits, len(digits))
# 
# numstrings = sorted([''.join(p) for p in perms], reverse = True)
# 
# def checkPandigital(numstring):
#     'starts with chunk lenghts of 1, 2, 3 and 4'
#     'recursively checks if remainder of string begins with'
#     'a number equal to (position + 1)/position times the current chunk'
#     'if end of string is reached then numstring is a pandigital multiple'
#     for i in range(1, 5):
#         position = 1
#         chunk = numstring[:i]
#         remainder = numstring[i:]
#         while remainder:
#             chunk, remainder, endReached = checkForNextChunk(chunk, remainder, position)
#             position += 1
#             if endReached:
#                 return True
#     return False
# 
# def checkForNextChunk(chunk, remainder, position):
#     'works out if next chunk of numstring'
#     'is eaual to (position+1)/position times the previous chunk'
#     'returns next chunk, remainder if True'
#     'returns None, None if false'
#     'return endReached = True if end of whole string is reached'
#     next_num = str(int(chunk)/position*(position + 1))
#     next_num_len = len(next_num)
#     if remainder.startswith(next_num):
#         return remainder[:next_num_len], remainder[next_num_len:], remainder.endswith(next_num)
#     return None, None, None
# 
start = datetime.now()
#            
# for numstring in numstrings:
#     if checkPandigital(numstring):
#         print numstring
#         break
#      
# print datetime.now()-start

# better solution below...

def is_pan(i):
    pan = str(i)
    n = 2
    while len(pan) < 10:
        if sorted(pan) == ['1', '2','3', '4', '5', '6', '7', '8', '9']:
            return True
        else:
            pan = pan + str(i*n)
            i+=1
    return False
        
i = 9876

while not is_pan(i):
    i-=1

print i
print datetime.now()-start
