# Independent check of (68.16) (Theorem 68): coefficient of c t^2 in [S_(K+2)] G_(J0+4), J0 = 2K+3, data H_0 = t h,
# h = (S_1+S_3)/4, G_0 = 0, free constant c S_K in P_(J0), all other constants zero. Truncated ring: c^i t^j, i<=1, j<=2.
# Logarithms: checked, not assumed. Any nonzero resonant forcing in the truncated ring raises an error.
import sys
from fractions import Fraction as Fr
from collections import defaultdict
sys.path.insert(0,'.')
from rec import add, sc, mul, d, COS, SIN
def padd(*ps):
    r=defaultdict(list)
    for p in ps:
        for k,v in p.items(): r[k].append(v)
    out={}
    for k,vs in r.items():
        s=add(*vs)
        if s: out[k]=s
    return out
def psc(c,p): return {k:sc(c,v) for k,v in p.items() if sc(c,v)}
def pmul(p,q):
    r=[]
    for (i1,j1),u in p.items():
        for (i2,j2),v in q.items():
            if i1+i2<=1 and j1+j2<=2:
                m=mul(u,v)
                if m: r.append({(i1+i2,j1+j2):m})
    return padd(*r)
def pd(p): return {k:d(v) for k,v in p.items() if d(v)}
def pmulf(f,p): return padd(*[{k:mul(f,v)} for k,v in p.items() if mul(f,v)])
def inv(p,n,free=None):
    a=Fr(3-n,2); out={}
    for key,g in p.items():
        r={}
        for (t,k),v in g.items():
            assert t=='s' and k%2==0,(t,k)
            den=k*k-a*a
            if den==0: raise RuntimeError(('resonant forcing nonzero in truncated ring',n,key,k,v))
            r[('s',k)]=v/den
        out[key]=r
    if free is not None:
        out=padd(out,{(1,0):{('s',free):Fr(1)}})
    return out
def run(K):
    J0=2*K+3; N=J0+4
    h={('s',1):Fr(1,4),('s',3):Fr(1,4)}
    H=[{(0,1):h}]; G=[{}]; P=[{}]
    for n in range(1,N+1):
        hn=[]; gn=[]
        for k in range(n):
            l=n-1-k
            hn.append(psc(Fr(l,2),pmul(pd(P[k]),H[l]))); hn.append(psc(Fr(3-k,2),pmul(P[k],pd(H[l]))))
            gn.append(psc(Fr(l+1,2),pmul(pd(P[k]),G[l]))); gn.append(psc(Fr(3-k,2),pmul(P[k],pd(G[l]))))
        gn.append(psc(Fr(n-1,2),pmulf(COS,H[n-1]))); gn.append(pmulf(SIN,pd(H[n-1])))
        H.append(psc(Fr(1,n),padd(*hn))); G.append(psc(Fr(1,n),padd(*gn)))
        if n==N:
            return G[n].get((1,2),{}).get(('s',K+2),Fr(0))
        resonant=(n-3)%4==0 and n>=7
        if resonant:
            m=(n-3)//4
            # resonant mode S_(2m): forcing must vanish in the truncated ring (no logarithm); split it off
            for key,g in G[n].items():
                assert g.get(('s',2*m),0)==0,('log forced',n,key,g.get(('s',2*m)))
        P.append(inv(G[n],n,free=K if n==J0 else None))
for K,exp in [(2,Fr(-30203,554400))]+[(K,Fr(K*(K+1)**2*(224*K**4+1624*K**3+3788*K**2+3194*K+695),256*(K+3)*(2*K-1)*(2*K+1)*(2*K+3)*(2*K+5)**2*(2*K+7))) for K in (4,6)]:
    v=run(K); print('K',K,'computed',v,'formula',exp,'MATCH' if v==exp else 'DIFFER')
