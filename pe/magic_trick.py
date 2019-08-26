from random import randrange


coefficients = [randrange(2, 10) for i in range(randrange(5, 10))]

print(coefficients)

answer = 1

for digit in coefficients:
    answer *= digit
    
written = str(answer)

written =  [char for char in written]

print(written.pop(randrange(len(written))))



mod =  9 - sum([int(char) for char in written]) % 9
 
if mod and mod != 9:
    print('missing digit was %s' % mod)
else:
    print('missing digit was 9 or 0')
