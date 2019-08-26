import math
from datetime import datetime

def pentagonal(n):
    return (n*(3*n-1)/2)
  
def is_pos_natural(n):
  return n >= 1 and int(n) == n
  
def is_pentagonal(p):
    return is_pos_natural((math.sqrt(24*p+1)+1)/6)

a = 1
b = 1

answered = 0

start = datetime.now()

while not answered:
    pa = pentagonal(a)
    b = 1
    while b < a:
        pb = pentagonal(b)
        if is_pentagonal(pa+pb):
            if is_pentagonal(pa-pb):
                print pa-pb
                answered = 1          
        b+=1
    a+=1
    

print datetime.now()-start   

# pentags = [pentagonal(i) for i in range(1,1000)]
# 
# 
# print pentags
#  
# crossref={}
#  
# for a in pentags:
#     for b in pentags:
#         if b>=a:
#             continue
#         crossref['%s/%s' % (str(a), str(b))] = {}
#         crossref['%s/%s' % (str(a), str(b))]['sum'] = a + b
#         crossref['%s/%s' % (str(a), str(b))]['diff'] = a-b
#         print a, b, crossref['%s/%s' % (str(a), str(b))]
#  
# for pair, values in crossref.iteritems():
#     if values['sum'] in pentags and values['diff'] in pentags:
#         print pair
#      


   