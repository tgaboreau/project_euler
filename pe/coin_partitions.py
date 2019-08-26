"""Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.


OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O


xxxxxxx

xxxxxx x

xxxxx x x
xxxxx xx
xxxx xxx
xxxx xx x
xxx xx xx
xxx xxx x
xxx x x x x



Find the least value of n for which p(n) is divisible by one million."""


def countSubGroup(totalCoins, maxSize, runningTotal = 0):
#     if maxSize == 1:
#         return totalCoins
    fullPiles = totalCoins / maxSize
    remainder = totalCoins % maxSize
    while fullPiles:
        
        if remainder:
            if maxSize > 1:
                'if there is a remainder run the count subgroup function on the remainder with a maxSize reduced by 1'
                runningTotal += countSubGroup(remainder, maxSize-1)
            else:
                remainder = 0
                
        
        else:
            'else reduces full piles by 1 and add those coins to the remainder'
            fullPiles -= 1
            remainder += maxSize

        
        
   
print(countSubGroup(6, 1))


