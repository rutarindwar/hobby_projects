# Aggregate radiomilwakee playlist


import operator


def merge(d1, d2, merge_fn=lambda x,y:y):
    """merge(d1, d1, lambda x,y: x+y)"""
    
    result = dict(d1)
    for k,v in d2.iteritems():
        if k in result:
            result[k] = merge_fn(result[k], v)
        else:
            result[k] = v
    return result


m = []

for i in range(1,11):
    fin = open('RadioMilwaukee_%d_2014.txt'%i, 'r')
    d = [k.strip() for k in fin.readlines()]
    tmp = [k.split('||') for k in d]
    foo = [[k.strip() for k in h] for h in tmp]
    m = m+foo
    fin.close()
    print i
    
s = {}
for it in m:
    if it[1] not in s:
        s[it[1]]= [it[0]]
    else:
        if it[0] not in s[it[1]]:
            s[it[1]].append(it[0])

ss = sorted(s.values(),key=len, reverse=1)
