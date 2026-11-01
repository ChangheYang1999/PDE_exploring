import sys, numpy as np, math
import tuned
from fractions import Fraction
N=int(sys.argv[1]); b=float(sys.argv[2]); M=int(sys.argv[3])
for n in range(1,4*N):
    x=n*Fraction(2,3)-2
    if x.denominator==1 and x>=2 and int(x)%2==0: tuned.rq_of[n]=int(x)
F,G,Hf,st=tuned.run(2,3,{1:1.0,M:b},N,tune=True)
F0,G0,_,st0=tuned.run(2,3,{1:1.0,M:b},N,tune=False)
for s,s0 in zip(st,st0):
    n=s['n']
    if n%3: continue
    l=s['l1']
    line='%4d l1=%.3e root=%.4f untuned=%.3e root=%.4f'%(n,l,l**(1/n),s0['l1'],s0['l1']**(1/n))
    if n in Hf:
        h=Hf[n]; line+=' H=%.3e |H|^(1/n)=%.4f slope=%.4e'%(h['H'],abs(h['H'])**(1/n),h['slope'])
    if 'obstr' in s: line+=' ob=%.1e'%s['obstr']
    print(line)
