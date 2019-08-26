import math

'''
starts at the last term of the simple fraction,
works towards the first term to get the approximation of e,
given the length of the simple fraction we are working to
'''

def get_e_simplified_fraction(n):
    convergents = []
    for i in range(n):
        if i == 0 or i%3 == 2:
            convergents.append(int(2*math.ceil((i+1)/3.0)))
        else:
            convergents.append(1)
    return convergents


def get_numerator(simple_frac):
    num, den = 1, simple_frac[-1]
    for i in range(len(simple_frac)-2, 0, -1):
        num, den = previous_term(num, den, simple_frac[i])
    num = num + simple_frac[0]*den
    return num


def previous_term(numer1, denom1, denom0):
    return denom1, denom0 * denom1 + numer1


sf = get_e_simplified_fraction(100)
print sum([int(char) for char in str(get_numerator(sf))])



