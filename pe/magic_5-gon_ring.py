import itertools

#Horribe code

digits = [1,2,3,4,5,6,7,8,9]
magic_orders = []
for pa in itertools.permutations(digits, 2):
    line1 = [10]
    digits_a = digits[:]
    line1.append(digits_a.pop(digits_a.index(pa[0])))
    line1.append(digits_a.pop(digits_a.index(pa[1])))
 
    for pb in itertools.permutations(digits_a, 2):
        if sum(pb) + line1[2] == sum(line1):
            line2 = []
            digits_b = digits_a[:]
            line2.append(digits_b.pop(digits_b.index(pb[0])))
            line2.append(line1[2])
            line2.append(digits_b.pop(digits_b.index(pb[1])))
             
            for pc in itertools.permutations(digits_b, 2):
                if sum(pc) + line2[2] == sum(line2):
                    line3 = []
                    digits_c = digits_b[:]
                    line3.append(digits_c.pop(digits_c.index(pc[0])))
                    line3.append(line2[2])
                    line3.append(digits_c.pop(digits_c.index(pc[1])))
 
                    for pd in itertools.permutations(digits_c, 2):
                        if sum(pd) + line3[2] == sum(line3):
                            line4 = []
                            digits_d = digits_c[:]
                            line4.append(digits_d.pop(digits_d.index(pd[0])))
                            line4.append(line3[2])
                            line4.append(digits_d.pop(digits_d.index(pd[1])))
                             
                            line5 = [digits_d[0], line4[2], line1[1]]
                            if sum(line5) == sum(line1):
                                magic_orders.append([line1[0], line2[0], line3[0], line4[0], line5[0], line1[1], line2[1], line3[1], line4[1], line5[1]])
     
  
def describe_ring(order):
    outer = order[:len(order)/2]
    inner = order[len(order)/2:]
    description = ''
    lowest_outer_pos = outer.index(min(outer))
    outer_order = outer[lowest_outer_pos:] + outer[:lowest_outer_pos] 
    for i in outer_order:
        description = description + str(i)
        description = description + str(inner[outer.index(i)])
        description = description + str(inner[(outer.index(i)+1) % len(inner)])
    return description                                   
                 
print(max([describe_ring(order) for order in  magic_orders]))












         

