import math
import itertools
from pprint import pprint
from datetime import datetime

start = datetime.now()

def same_length_pwd(cipher, pwd):
    return pwd*(int(math.floor(len(cipher)/len(pwd)))) + pwd[:len(cipher)%len(pwd)]

 
cipher = open('cipher.txt', 'r').read().split(',')
cipher = [int(char) for char in cipher]

answer = None
test_chars = 40
lower_alpha = [a for a in range(97, 123)]
pwds = itertools.permutations(lower_alpha, 3)
while not answer:
    for pwd in pwds:
        cipher_section = cipher[:test_chars]
        pwd = same_length_pwd(cipher_section, pwd)
        new_bits = [pwd[i] ^ cipher_section[i] for i in range(len(pwd))]
        new_text = ''.join([chr(bit) for bit in new_bits])
        if new_text.find(' the ') > -1:
            answer = pwd
            print(sum([bit for bit in new_bits]))
            break
    test_chars += 10


print(datetime.now()-start)



    
