from collections import Counter
import operator


def eval(hand):
    numbers = hand[0]
    is_flush = hand[1]
    'determines if hand is a straight'
    is_straight = not any([v - i - numbers[0] for i, v in enumerate(numbers)])
    'counts number of occurences for each number'
    grouped_cards = Counter(numbers)
    'makes a list of the sizes of groups, e.g. 4 of a kind would be [4,1], full house would be [3,2]'
    group_sizes = grouped_cards.values()
    'decides the rank of the hand, straight flush being 8, high card being 0'
    if is_flush and is_straight:
        rank = 8
    elif 4 in group_sizes:
        rank = 7
    elif group_sizes == [3, 2]:
        rank = 6
    elif is_flush:
        rank = 5
    elif is_straight:
        rank = 4
    elif 3 in group_sizes:
        rank = 3
    elif 2 in group_sizes:
        rank = group_sizes.count(2)
    else:
        rank = 0
    'returns a list with rank as first element, remaining elements are numbers sorted in order of significance'
    'three of a kind with three fours, a 9 and and 8 would return [3, 4, 9, 8]'
    'full house with three 10s and two 9s would return [6,10,9]'
    return [rank] + [group[0] for group in sorted([(card, groupsize) for card, groupsize in grouped_cards.iteritems()], key = operator.itemgetter(1, 0), reverse = True)]

'variable to store number of player 1 wins'
p1_wins = 0

with open('poker.txt', 'r') as f:
    for row in f:
        'converts each row to list of 10 cards with picture cards replaced as numbers'
        row_cards = row.replace('\n', '').replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14').split(' ')
        'splits into two fives'
        first5, last5 = row_cards[:5], row_cards[5:]
        'makes a tuple with 2 elements: first element is sorted numbers, second element is TRUE or FALSE for a flush'
        p1_hand = (sorted([int(card[:-1]) for card in first5]), len(set([card[-1] for card in first5])) == 1)
        p2_hand = (sorted([int(card[:-1]) for card in last5]), len(set([card[-1] for card in last5])) == 1)
        'evaluates each tuple using the eval function'
        for p1, p2 in zip(eval(p1_hand), eval(p2_hand)):
            'iterates through the returned lists to find the first difference'
            'if the if difference is in favour of p1 then +1 for p1_wins'
            if p1 != p2:
                p1_wins += p1 > p2
                break


print p1_wins