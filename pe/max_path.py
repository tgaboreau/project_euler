pyramid = [[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,0o4,82,47,65],
[19,0o1,23,75,0o3,34],
[88,0o2,77,73,0o7,63,67],
[99,65,0o4,28,0o6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,0o4,68,89,53,67,30,73,16,69,87,40,31],
[0o4,62,98,27,23,9,70,98,73,93,38,53,60,0o4,23]]

nodes = {}

for row in pyramid:
    rowpos = 0
    for node in row:
        nodes['%s/%s' % (str(pyramid.index(row)), str(rowpos))]={'maxdist':0, 'pathdist':pyramid[pyramid.index(row)][rowpos]}
        if rowpos == 0:
            nodes['%s/%s' % (str(pyramid.index(row)), str(rowpos))]['pre_choices']=['%s/%s' % (str(pyramid.index(row)-1), str(rowpos))]
        elif rowpos == len(row)-1:
            nodes['%s/%s' % (str(pyramid.index(row)), str(rowpos))]['pre_choices']=['%s/%s' % (str(pyramid.index(row)-1), str(rowpos-1))]
        else:
            nodes['%s/%s' % (str(pyramid.index(row)), str(rowpos))]['pre_choices']=['%s/%s' % (str(pyramid.index(row)-1), str(rowpos-1)),'%s/%s' % (str(pyramid.index(row)-1), str(rowpos))]
        rowpos+=1

nodes['0/0']['pre_choices']=[]
nodes['0/0']['max_dist']=nodes['0/0']['pathdist']

for row in pyramid[1:]:
    rowpos = 0
    for node in row:
        nodename = '%s/%s' % (str(pyramid.index(row)), str(rowpos))
        max_pre = max([nodes[pre_choice]['max_dist'] for pre_choice in nodes[nodename]['pre_choices']])
        nodes[nodename]['max_dist'] = max_pre + nodes[nodename]['pathdist']
        rowpos +=1
        
print(max([values['max_dist'] for node, values in nodes.items()]))
        
       

        



    
    



