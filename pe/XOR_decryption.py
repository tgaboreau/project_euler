import math
import itertools
from pprint import pprint
from datetime import datetime


def to_8_bit(char):
    n = ord(char)
    print(n)

def from_8_bit(binary):
    return sum([int(binary[i])*2**(7-i) for i in range(8)])


def xor_encode_char(c, p):
    cbin = '%.8d' % int(bin(c)[2:])
    pbin = '%.8d' % int(bin(p)[2:])
    binary = ''.join([str(+(cbin[i] != pbin[i])) for i in range(8)])
    return from_8_bit(binary)


def xor_encode(cipher, pwd):
    return [encode_map[cipher[i]][pwd[i]] for i in range(len(cipher))]


def same_length_pwd(cipher, pwd):
    pwd = [ord(char) for char in pwd]
    return pwd*(int(math.floor(len(cipher)/len(pwd)))) + pwd[:len(cipher)%len(pwd)]

 
start = datetime.now()

encode_map = {i : {} for i in range(256)}
for i in range(256):
    for j in range(i + 1, 256):
        try:
            encode_map[i][j]
        except KeyError:
            k = xor_encode_char(i, j)
            for perm in itertools.permutations((i, j, k), 3):
                encode_map[perm[0]][perm[1]] = perm[2]
 
 
cipher = open('cipher.txt', 'r').read().split(',')
cipher = [int(char) for char in cipher][:50]


lower_alpha = [chr(a) for a in range(97, 123)]
for pwd in itertools.permutations(lower_alpha, 3):
    pwd = same_length_pwd(cipher, pwd)
    new_text = ''.join([chr(char) for char in xor_encode(cipher, pwd)])
    if new_text.find(' the ') > -1:
        print(sum([char for char in xor_encode(cipher, pwd)]))
        break

print(datetime.now()-start)



    
