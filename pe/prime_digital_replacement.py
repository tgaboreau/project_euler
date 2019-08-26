import itertools
from datetime import datetime
import sys
from isprime import *


# Could definitely be cleaner...
def get_prime_family_value(n):
    'assuming that only primes are being passed as arguments'
    max_family_value = 1
    digits = [int(char) for char in str(n)]
    'for an 8 value family the lowest replaceable can only be 0, 1 or 2 so...'
    for swap_digit in (0, 1, 2):
        'make a list containing the index of each occurence of the swap_digit in digits'
        replaceables = [index for index, digit in  enumerate(digits) if digit == swap_digit]
        'make a list of different index combinations to replace'
        'eg the swap_digit might appear at index 2 and index 3, we want to try replacing each of these separately as well as both together'
        index_combinations = []
        for combo_length in range(1, len(replaceables)+1):
            index_combinations = index_combinations + list(itertools.combinations(replaceables, combo_length))
        'for each index combination...'
        for ic in index_combinations:
            'try replacing characters at those indeces with all values from 0 to 9, ignoring the initial swap_digit'
            'when the index combination contains 0, dont plug in the digit 0 as this will be a leading 0'
            if 0 in ic:
                lowest = 1
            else:
                lowest = 0
            ic_family_value = 1
            for i in range(lowest, 10):
                if i != swap_digit:
                    new_digits = [str(i) if index in ic else str(digit) for index, digit in enumerate(digits)]
                    'if number is prime then increment ic_family value'
                    if isprime(int(''.join(new_digits))):
                        ic_family_value += 1
                'if ic_family value > max_family_value then it becomes new max'
            max_family_value = max(max_family_value, ic_family_value)
    return max_family_value


start = datetime.now()

    
n = 11


while not isprime(n) or get_prime_family_value(n) < 8:
    n += 2


print n
print datetime.now()-start



