import itertools

def get_cubic_perms(i, digit_sum):
    return len([c for c in cubes[digit_sum] if sorted(str(i)) == sorted(str(c))]) + 1


def get_smallest_perm(n):
    for c in cubes[digit_sum]:
        if sorted(str(n)) == sorted(str(c)):
            return c


cubes = {}
cube = 0
i = 1
while i:
    cube, last_cube = i**3, cube
    if len(str(cube)) > len(str(last_cube)):
        cubes = {}
    digit_sum = sum(int(char) for char in str(cube))
    cubes.setdefault(digit_sum, [])
    if get_cubic_perms(cube, digit_sum) == 5:
        break
    cubes[digit_sum].append(cube)
    i += 1
    
print get_smallest_perm(cube)
     
