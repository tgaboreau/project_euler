expansion = 2
occurences = 0

numerator = 3
denominator = 2

while expansion < 1000:
    denominator, numerator = denominator + numerator, numerator + denominator*2
    if len(str(numerator)) > len(str(denominator)):
        occurences += 1
    expansion += 1
        
print(occurences)
