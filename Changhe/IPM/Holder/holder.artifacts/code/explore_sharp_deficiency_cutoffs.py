"""Floating cutoff selection only. The proof, not this scan, supplies the bound."""
from pathlib import Path
from datetime import datetime,timezone
import math,json
ROOT=Path(__file__).resolve().parents[1]
G=.91596559417721901505

def formulas(r,e=.01):
    pi=math.pi; ln2=math.log(2); lr=math.log(r)
    E=-math.log1p(-r*r)/2; N=.5-2*lr/pi
    L=max(-math.log1p(-2*r),(1+2*r)*math.log1p(2*r))
    BC=r*r/(2*(1-r)**2)*(-lr+.5+2*G/pi)
    BD=r*r/(2*(1-r)**2)*(-lr+.5+ln2)
    Z=(N+E)*math.expm1(e*ln2)/e+2**(e+1)/pi*(1/(1-e)+.5-math.log(1.5))
    lc=lr+ln2/2-.5; ld=lr+ln2-1
    return ((lc*lc+.25)/pi+Z+BC+E*L,(ld*ld+1-pi*pi/12)/pi+Z+BD+3*E*L)

def finite(a,r):
    pi=math.pi; ln2=math.log(2);lr=math.log(r)
    E=-math.log1p(-r*r)/2;N=.5-2*lr/pi
    L=max(-math.log1p(-2*r),(1+2*r)*math.log1p(2*r))
    BC=r*r/(2*(1-r)**2)*(-lr+.5+2*G/pi)
    BD=r*r/(2*(1-r)**2)*(-lr+.5+ln2)
    T=2**(a+1)/pi*a*(1/(1-a)+.5-math.log(1.5))
    nonlocal_cost=2**a*N+math.expm1(a*ln2)*E+T
    a2=2**(1+a/2)/(pi*(a+2))
    AA=math.exp(math.lgamma(1+a/2)-math.lgamma(1.5+a/2))/(2*math.sqrt(pi))
    return(2*a2*math.exp(a*lr)/a+nonlocal_cost+a*(BC+E*L),
           2*AA*math.exp(a*lr)/a+.5+nonlocal_cost+a*(BD+3*E*L))

def main():
    grid=[i/100000 for i in range(20000,42001)]
    rows=[(r,formulas(r)) for r in grid]
    best=[min(rows,key=lambda row:row[1][j]) for j in range(2)]
    f=[]
    for a in [.001,.005,.01,.05,.1,.2,.3,.5,.75,.9,.99]:
        vr=[(r,finite(a,r)) for r in grid]
        f.append({'alpha':str(a),'best_C':min(vr,key=lambda row:row[1][0]),'best_D':min(vr,key=lambda row:row[1][1])})
    out={'time_utc':datetime.now(timezone.utc).isoformat(),'status':'HEURISTIC, no certificate','epsilon':'1/100',
         'best_uniform':best,'simple':{'1/3':formulas(1/3),'8/25':formulas(.32),'3/10':formulas(.3)},'finite':f}
    path=ROOT/'08_improved_upper_bounds/explicit_second_term/sharp_deficiency/verification/exploration.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
