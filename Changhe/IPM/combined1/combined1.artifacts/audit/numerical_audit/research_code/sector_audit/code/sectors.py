"""Independent exact Cartesian differentiation of homogeneous Fourier sectors."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
import json, hashlib
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[3]

def enc(q):return f'{q.numerator}/{q.denominator}'
def aq(q):return arb(q.numerator)/arb(q.denominator)
def choose(x,n):
    out=Q(1)
    for j in range(n):out*= (x-j)/(j+1)
    return out

def collect(items,kind):
    out=defaultdict(Q)
    for n,c in items:
        if kind=='s' and n==0:continue
        if n<0:n,c=-n,(-c if kind=='s' else c)
        out[n]+=c
    return {n:c for n,c in out.items() if c}

def dx(poly,s,kind):
    return collect(((k,v) for n,c in poly.items() for k,v in ((n-1,c*(s+n)/2),(n+1,c*(s-n)/2))),kind)

def dy(poly,s,kind):
    target='s' if kind=='c' else 'c'
    sg=1 if kind=='s' else -1
    return collect(((k,v) for n,c in poly.items() for k,v in ((n-1,sg*c*(s+n)/2),(n+1,-sg*c*(s-n)/2))),target)

def add(a,b,scale=1):
    out=a.copy()
    for n,c in b.items():out[n]=out.get(n,Q(0))+scale*c
    return {n:c for n,c in out.items() if c}

def product_cs(cos,sin):
    return collect(((k,v) for n,a in cos.items() for m,b in sin.items() for k,v in ((m+n,a*b/2),(m-n,a*b/2))),'s')

def sectors(state,qmax=2):
    c=Q(state['cl']);g=1/c;delta=1-g
    coef=defaultdict(dict)
    for key,value in zip(state['order'],state['coefficients']):
        j,m,k=key;coef[j,m][k]=Q(value)
    branches=1+max(j for j,m in coef)
    def alpha(j,q):return g-j*delta-2*q
    G={};U1={};U2={};RX={};RY={};POT={}
    for j in range(branches):
        p=(3+g-j*delta)/2
        for q in range(qmax+1):
            s=alpha(j,q)+3
            C={2*m:sum(a*choose(p-k,q) for k,a in terms.items()) for (jj,m),terms in coef.items() if jj==j}
            C={n:v for n,v in C.items() if v}
            POT[j,q]=C
            lap={n:(s*s-n*n)*v for n,v in C.items()}
            G[j,q]={n:-v for n,v in dy(lap,s-2,'c').items()}
            xy=dy(dx(C,s,'c'),s-1,'c')
            U1[j,q]={n:-v for n,v in dy(xy,s-2,'s').items()}
            U2[j,q]=dx(xy,s-2,'s')
            RX[j,q]=dx(G[j,q],s-3,'s')
            RY[j,q]=dy(G[j,q],s-3,'s')
    E={}
    for h in range(2*branches):
        for q in range(qmax+1):
            e={n:(c*alpha(h,q)-1)*v for n,v in G.get((h,q),{}).items()}
            for i in range(branches):
                j=h-1-i
                if not 0<=j<branches:continue
                for u in range(q+1):
                    v=q-u
                    e=add(e,product_cs(U1[i,u],RX[j,v]))
                    e=add(e,product_cs(RY[j,v],U2[i,u]))
            E[h,q]={n:v for n,v in e.items() if v}
    return alpha,POT,G,E

if __name__=='__main__':
    ctx.prec=256
    state=json.loads((ROOT/'research/baseline/data/state131_independent.json').read_text())
    alpha,C,G,E=sectors(state)
    old=json.loads((ROOT/'research/baseline/data/prior_state131_tail.json').read_text())
    print('Prior E_coefficients shape',str(old['E_coefficients'])[:100],flush=True)
    records=[]
    for (h,q),poly in sorted(E.items(),key=lambda item:alpha(*item[0]),reverse=True):
        ss=sum((v*v for v in poly.values()),Q(0))
        full=(arb.pi()*aq(ss)).sqrt()
        rec={'h':h,'q':q,'exponent':enc(alpha(h,q)),'exponent_arb':aq(alpha(h,q)).str(30),
             'exact_zero':not poly,'sine_coefficients':{str(k):enc(v) for k,v in sorted(poly.items())},
             'full_circle_norm':full.str(45),'quadrant_norm':(full/2).str(45),
             'max_harmonic':max(poly,default=0)}
        records.append(rec)
        if alpha(h,q)>=-2:print(h,q,rec['exponent_arb'],rec['full_circle_norm'],flush=True)
    assert E[1,0][39]==Q(old['E1_sin39_exact'])
    assert G[0,0]=={int(k):Q(v) for k,v in old['leading_density_angular_coefficients'].items()}
    data={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'canonical_sha256':state['canonical_serialization_sha256'],
          'method':'Cartesian homogeneous differentiation, rational arithmetic, arb norm conversion at 256 bits',
          'qmax':2,'first3_checked_against_prior':False,'sin39_exact_match':True,'leading_density_exact_match':True,'sectors':records}
    (ROOT/'research/sector_audit/verification/state131_sectors.json').write_text(json.dumps(data,indent=2)+'\n')
