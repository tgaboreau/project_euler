import datetime

start = datetime.datetime.now()

def numfacs(n):
    primfac = {}
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.setdefault(d, 0)
            primfac[d]+=1
            n /= d
        d += 1
    if n > 1:
        primfac.setdefault(d, 0)
        primfac[d]+=1
    i = 1
    for k, v in primfac.iteritems():
        i*=v+1
    return i
   
i = 0
j = 1
facs = 0
while facs<501:
    i+=j
    j+=1
    facs = numfacs(i)

print i
print datetime.datetime.now()-start