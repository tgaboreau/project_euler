from datetime import datetime

def digit_sum(a, b):
    return sum([int(char) for char in str(a**b)])

start = datetime.now()

print max([digit_sum(a, b) for a in xrange(99, 100) for b in xrange(1, 100)])

print datetime.now()-start
