# from math import *
# import datetime
# 
# 
# def find_d(n):
#     limits = [0,9,189,2890,38890,488890,5888890]
#     tier = float(limits.index(min(filter(lambda x:x-n<0, limits), key=lambda x:abs(x-n))))
#     i = tier
#     addnum=0
#     while i>0:
#         addnum+=10**i
#         i-=1
# 
#     return int(str(int(floor((n+addnum)/(tier+1))))[int(round(((n+addnum)/(tier+1)%1)/(1/(tier+1))))])
# 
# 
# 
# start = datetime.datetime.now()
#    
# i = 1
# for num in [1,10,100,1000,10000,100000,1000000]:
#     i*=find_d(num)
# print i
#   
# print datetime.datetime.now()-start
# 

'no idea how the first way works but i wrote it at some point and it does work'

i = 0
j = 1
constant = ''
while i <= 1000000:
    constant = constant + str(j)
    i += len(str(j))
    j+=1

answer = 1
for num in [1,10,100,1000,10000,100000,1000000]:
    answer*=int(constant[num-1])

print answer