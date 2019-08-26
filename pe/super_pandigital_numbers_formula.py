def get(n):
    return (n**n-n)/(n-1)**2 + n**(n-2)*(n-1) - 1

print get(12)