"""Refined node design (second pass) for the uniform comparison on [1/200, 199/200]: about 1.3 geometric steps in
alpha near 0 and in 1-alpha near 1, spacing 1/40 in the middle. Lower nodes: 4 equal parts per upper segment plus one
neighbour beyond each end of each shape group. Same shape groups and plan-reference exponents as nodes.json."""
from fractions import Fraction as F
import json
UP=[F(x) for x in ('1/200 13/2000 17/2000 11/1000 29/2000 19/1000 1/40 4/125 1/25 13/250 13/200 2/25 1/10 3/25 7/50 33/200 '
    '19/100 11/50 1/4 11/40 3/10 13/40 7/20 3/8 2/5 17/40 9/20 19/40 1/2 21/40 11/20 23/40 3/5 5/8 13/20 27/40 7/10 29/40 '
    '3/4 31/40 4/5 33/40 17/20 7/8 9/10 183/200 93/100 943/1000 191/200 963/1000 97/100 122/125 49/50 123/125 987/1000 '
    '1979/2000 124/125 1987/2000 199/200').split()]
SUB=4
LOW=[]
for a,b in zip(UP,UP[1:]):
    LOW+=[a+k*(b-a)/SUB for k in range(SUB)]
LOW.append(UP[-1])
LOW=[UP[0]-(UP[1]-UP[0])/SUB]+LOW+[UP[-1]+(UP[-1]-UP[-2])/SUB]
old=json.load(open('nodes.json'))
groups=[]
for g in old['groups']:
    s,e=F(g['start']),F(g['end']);i=LOW.index(s);j=LOW.index(e)
    groups.append(dict(start=g['start'],end=g['end'],shape=g['shape'],step=g['step'],far_ref=g['far_ref'],
                       nodes=[str(x) for x in LOW[i-1:j+2]],upper_nodes=[str(x) for x in UP if s<=x<=e]))
assert all(x<y for x,y in zip(UP,UP[1:])) and all(x<y for x,y in zip(LOW,LOW[1:]))
json.dump(dict(upper=[str(x) for x in UP],lower=[str(x) for x in LOW],groups=groups),open('nodes2.json','w'),indent=1)
oldup=set(F(x) for x in old['upper'])
new=[x for x in UP if x not in oldup]
open('new_upper2.txt','w').write(','.join(str(x) for x in new))
print(len(UP),len(LOW),len(new),[len(g['nodes']) for g in groups],[len(g['upper_nodes']) for g in groups])
