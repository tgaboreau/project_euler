import itertools
coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.reverse()


def countperms(target, coins):
    counter = 0
    for i in range(0,target/coins[0]+1):
        limit1 = coins[0]*i
        for j in range(0,(target-limit1)/coins[1]+1):
            limit2 = limit1 + coins[1]*j
            for k in range(0,(target-limit2)/coins[2]+1):
                limit3 = limit2 + coins[2]*k
                for l in range(0,(target-limit3)/coins[3]+1):
                    limit4 = limit3 + coins[3]*l
                    for m in range(0,(target-limit4)/coins[4]+1):
                        limit5 = limit4 + coins[4]*m
                        for n in range(0,(target-limit5)/coins[5]+1):
                            limit6 = limit5 + coins[5]*n
                            for o in range(0,(target-limit6)/coins[6]+1):
                                limit7 = limit6 + coins[6]*o
                                for p in range(0,(target-limit7)/coins[7]+1):
                                    if i*coins[0] + j*coins[1] + k*coins[2] + l*coins[3] + m*coins[4] + n*coins[5] + o*coins[6] + p*coins[7] == target:
#                                         print i, j, k, l, m, n, o, p
                                        counter += 1
    return counter

print(countperms(200, coins))