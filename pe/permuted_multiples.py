from datetime import datetime
 
 
start = datetime.now()
 
 
def is_permuted(n):
#         return sorted(str(n)) == sorted(str(n*2)) == sorted(str(n*3)) == sorted(str(n*4)) == sorted(str(n*5)) == sorted(str(n*6))
        return len(str(n)) == len(str(n*2)) == len(str(n*3)) == len(str(n*4)) == len(str(n*5)) == len(str(n*6)) and set(str(n)) == set(str(n*2)) == set(str(n*3)) == set(str(n*4)) == set(str(n*5)) == set(str(n*6))
     
i = 1
while not is_permuted(i):
    i += 1


print i, datetime.now()-start

