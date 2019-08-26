import math

def reverse_and_add(n):
    return n + int(str(n)[::-1])

def is_pallindrome(n):
    nstring = str(n)
    half_len = int(math.floor(len(nstring)/2))
    return nstring[:half_len] == nstring[-half_len:][::-1]

def is_lychrel(n):
    i = 0
    while i < 49:
        n = reverse_and_add(n)
        if is_pallindrome(n):
            return i + 1
        i += 1
    return False

non_lychrels = []

for i in range(1, 10000):
    if not is_lychrel(i):
        non_lychrels.append(i)
        
print(len(non_lychrels))


    