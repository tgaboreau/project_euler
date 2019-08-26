import math
import itertools

# this code works but it's horrible
# the idea is to generate lists of all tri, square, pen etc... numbers
# then starting with one list, check other lists to see
# what could possible be the next step in the cycle
# for each next step, repeat the same idea
# except don't look in lists which have already been used earlier
# in the sequence
# this could probably be done recursively but it hurt my brain trying
# to do it that way

def tri(n):
    return n*(n+1)/2

def square(n):
    return n**2
 
def pen(n):
    return n*(3*n-1)/2
 
def hex(n):
    return n*(2*n+1)
 
def hep(n):
    return n*(5*n-3)/2
 
def oct(n):
    return n*(3*n-2)

numlists = {}

for func in (tri, square, pen, hex, hep, oct):
    numlists[func.__name__] = []
    i = 1
    while func(i) <1010:
        i+=1
        pass
    while func(i) < 10000:
        numlists[func.__name__].append(func(i))
        i += 1
   
'this code works but its horrible'

def get_poss_next(other_lists, exclude, n):
    output = {}
    other_lists_temp = other_lists.copy()
    for ex in exclude:
        other_lists_temp.pop(ex)
    nextstart = str(n)[2:]
    for other_list, values in other_lists_temp.iteritems():
        for v in values:
            if str(v).startswith(nextstart):
                output.setdefault(other_list, [])
                output[other_list].append(v)
    return output



startlist = numlists.pop('oct')

for poss in startlist:
    five_lists = get_poss_next(numlists, [], poss)

    for five_list, five_values in five_lists.iteritems():
        for five_value in five_values:
            
            
            four_lists = get_poss_next(numlists, [five_list], five_value)
    
            for four_list, four_values in four_lists.iteritems():
                for four_value in four_values:
 
            
                    three_lists = get_poss_next(numlists, [five_list, four_list], four_value)

                    for three_list, three_values in three_lists.iteritems():
                        for three_value in three_values:
                            
                            
                            two_lists = get_poss_next(numlists, [five_list, four_list, three_list], three_value)

                            for two_list, two_values in two_lists.iteritems():
                                for two_value in two_values:
                                    
                                    
                                    one_lists = get_poss_next(numlists, [five_list, four_list, three_list, two_list], two_value)

                                    if one_lists:
                                        for one_list, one_values in one_lists.iteritems():
                                            if str(poss).startswith(str(one_values[0])[2:]):
                                                print poss + five_value + four_value + three_value + two_value + one_values[0]
        

    
        
    


