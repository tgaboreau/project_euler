import itertools
from datetime import datetime

start = datetime.now()

'starts with all 3 digits numbers divisible by 2 where all digits in number are unique'
possibles = ["%03d" % m for m in range(10,1000) if not m%2 and len(set("%03d" % m)) == len("%03d" % m)]

for p in (3, 5, 7, 11, 13, 17):
    'finds all 3 digits numbers divisible by p where all digits in number are unique'
    tdms = ["%03d" % m for m in range(10,1000) if not m%p and len(set("%03d" % m)) == len("%03d" % m)]
    'checks each tdm against each poss in possibles'
    'finds matches where last two digits of poss is the same as the first two digits of tdm, and third digit of tdm is not in poss'
    'replaces possibles list with list of matches with list of matches'
    'so with each iteration of p, the string is poss get one digit longer'
    possibles = [poss + tdm[2] for poss in possibles for tdm in tdms if poss[-2:] == tdm [:2] and tdm[2] not in poss]

'what you are left with now is a list of 9 digit strings which fit the criteria of the question'

'now for each string, add the digit which isnt in the string to the start of the string to make it a 10-digit pandigital'
'but dont check for zeros because a zero at the beginning would not count as a proper one'

print(sum([int(digit + poss) for poss in possibles for digit in '123456789' if digit not in poss]))

print(datetime.now()-start)

# see other methods below


# pans = list(itertools.permutations([str(num) for num in range(0,10)]))
# 
# total=0
# 
# for pan in pans:
#     if not int(pan[3])%2:
#         if not int(pan[5])%5:
#             if not int(''.join(pan[2:5]))%3:
#                 if not int(''.join(pan[4:7]))%7:
#                     if not int(''.join(pan[5:8]))%11:
#                         if not int(''.join(pan[6:9]))%13:
#                             if not int(''.join(pan[7:10]))%17:
#                                 total += int(''.join(pan))

pans = list(itertools.permutations([num for num in range(0,10)]))

total=0

# for pan in pans:
#     divisible = True
#     if not pan[0]:
#         continue
#     original_num = sum([v*10**(9-i) for i, v in enumerate(pan)])
#     num = 1*original_num
#     for p in (17, 13, 11, 7, 5, 3):
#         if not (num % 1000) % p:
#             num = (num - num%10)/10
#         else:
#             divisible = False
#             break
#     if divisible and not num % 2:
#         print original_num
#         total += original_num


# for pan in pans:
#     if not pan[0]:
#         continue
#     num = sum([v*10**(9-i) for i, v in enumerate(pan)])
#     if not ((num - num % 100000)/100000) % 2:
#         if not ((num - num % 1000)/1000) % 5:
#             if not (((num - num % 10000)/10000) % 1000) % 3:
# #                 if not (((num - num % 100)/100) % 100000) % 7:
#                 print num, (((num - num % 100)/100) % 100000)
# #                     if not (((num - num % 10)/10) % 1000000) % 11:
                
#                 if not ((num - num % 100)/100) % 7:
#                     if not ((num - num % 10)/10) % 11:
#                         if not ((num - num % 100000)/100000) % 13:
#                             if not ((num - num % 100000)/100000) % 17:



