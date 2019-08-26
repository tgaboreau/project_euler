import math
from datetime import datetime

fl = math.floor

def get_solutions(perimeter):
    solutions = []
    perimeter = float(perimeter)
    
    'for a in range 1 to third of perimeter'
    for a in range(1,int(fl(perimeter/3))):
        
        a = float(a)
        
        'if a already in solutions then skip'
        if a in [solution[1] for solution in solutions]:
            continue
        
        'calculate c'
        c = ((p-a)**2+a**2)/(2*(p-a))
        
        'if c not integer then skip'
        if c % 1.0:
            continue
        
        'calculate b'
        b = math.sqrt(c**2-a**2)
        
        'if b is integer then add to solutionss'
        if not b % 1.0:
            solutions.append([a,b,c])
    return solutions
 
start = datetime.now()
        
print max([(len(get_solutions(p)),p) for p in range(1,1001)])

print datetime.now()-start

    
