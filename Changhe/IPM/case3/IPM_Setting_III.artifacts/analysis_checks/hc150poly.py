# g_* for the trace sin th + eps sin N th as an exact polynomial in eps (same recurrence as hc150.py).
from fractions import Fraction as F
import sys
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): c[i+j]+=x*y
    return c
def add(a,b):
    n=max(len(a),len(b)); return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def sc(a,w): return [x*w for x in a]
def run(ell,kstar,mstar,N):
    p=1/ell; d=1-p; s=lambda k: p-k*d
    P={0:{1:[F(1)],N:[F(0),F(1)]}}; H={}
    def dx(Pk,sk):
        G={}
        for n,c in Pk.items():
            for mm,w in ((n+1,(sk-n)/2),(n-1,(sk+n)/2)):
                if mm!=0: G[mm]=add(G.get(mm,[F(0)]),sc(c,w))
        return G
    for k in range(1,kstar+1):
        G=dx(P[k-1],s(k-1)); H[k-1]={m:sc(g,1/(m*m-(s(k-1)+1)**2)) for m,g in G.items()}
        acc={}
        for i in range(k):
            j=k-1-i; si,sj=s(i),s(j)
            for m,h in H[i].items():
                for n,c in P[j].items():
                    hc=mul(h,c)
                    for f,w in ((n+m,(-m*sj+(si+1)*n)/2),(n-m,(-m*sj-(si+1)*n)/2)):
                        if f==0: continue
                        sg=1
                        if f<0: f,sg=-f,-1
                        acc[f]=add(acc.get(f,[F(0)]),sc(hc,sg*w))
        P[k]={n:sc(v,1/(ell*k*d)) for n,v in acc.items() if any(v)}
    return dx(P[kstar],s(kstar)).get(mstar,[F(0)])
N=int(sys.argv[1])
import numpy as np
for ell,ks,ms in ((F(3),5,2),(F(5,2),9,4)):
    g=run(ell,ks,ms,N)
    print(ell,"N=",N,"coeffs (float):",[float(x) for x in g])
    r=np.roots([float(x) for x in g[::-1]]) if len(g)>1 else []
    print("  real roots:",sorted([x.real for x in r if abs(x.imag)<1e-9]))
