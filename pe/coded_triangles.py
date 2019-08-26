import datetime

start = datetime.datetime.now()

words = open('words.txt').next().replace('"','').split(',')

def is_trinum(n):
    return (((8*n)+1)**0.5).is_integer()

def wordtotal(word):
    return sum([ord(char)-64 for char in word])

print len([word for word in words if is_trinum(wordtotal(word))])

print datetime.datetime.now()-start

