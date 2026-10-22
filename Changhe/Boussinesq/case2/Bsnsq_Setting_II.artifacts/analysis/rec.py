# Independent check of the beta = 2 formal recursion (Remark 39.1 form), z-independent orders up to G_7.
from fractions import Fraction as Fr
from collections import defaultdict
def add(*fs):
    r=defaultdict(Fr)
    for f in fs:
        for k,v in f.items(): r[k]+=v
    return {k:v for k,v in r.items() if v!=0}
def sc(c,f): return {k:c*v for k,v in f.items() if c*v!=0}
def norm(t,k,c):
    # t in 's','c'; returns dict with k>=0
    if t=='s':
        if k==0: return {}
        if k<0: return {('s',-k):-c}
        return {('s',k):c}
    else:
        return {('c',abs(k)):c}
def mul(f,g):
    r=[]
    for (t1,a),u in f.items():
        for (t2,b),v in g.items():
            c=u*v/2
            if t1=='s' and t2=='s': r+= [norm('c',a-b,c),norm('c',a+b,-c)]
            elif t1=='c' and t2=='c': r+= [norm('c',a-b,c),norm('c',a+b,c)]
            elif t1=='s' and t2=='c': r+= [norm('s',a+b,c),norm('s',a-b,c)]
            else: r+= [norm('s',b+a,c),norm('s',b-a,c)]
    return add(*r)
def d(f):
    r=[]
    for (t,k),v in f.items():
        if t=='s': r.append(norm('c',k,k*v))
        else: r.append(norm('s',k,-k*v))
    return add(*r)
def inv_ell(g,j):
    a=Fr(3-j,2); r={}
    for (t,k),v in g.items():
        assert t=='s' and k%2==0, (t,k)
        den=k*k-a*a
        if den==0: raise ZeroDivisionError(('resonance',j,k,v))
        r[('s',k)]=v/den
    return r
COS={('c',1):Fr(1)}; SIN={('s',1):Fr(1)}
def run(H0,G0,N):
    H=[H0]; G=[G0]; P=[inv_ell(G0,0)]
    for n in range(1,N+1):
        hn=[]; gn=[]
        for k in range(n):
            l=n-1-k
            hn.append(sc(Fr(l,2),mul(d(P[k]),H[l]))); hn.append(sc(Fr(3-k,2),mul(P[k],d(H[l]))))
            gn.append(sc(Fr(l+1,2),mul(d(P[k]),G[l]))); gn.append(sc(Fr(3-k,2),mul(P[k],d(G[l]))))
        gn.append(sc(Fr(n-1,2),mul(COS,H[n-1]))); gn.append(mul(SIN,d(H[n-1])))
        H.append(sc(Fr(1,n),add(*hn))); G.append(sc(Fr(1,n),add(*gn)))
        try: P.append(inv_ell(G[n],n))
        except ZeroDivisionError as e:
            P.append(None); return H,G,P,e.args[0]
    return H,G,P,None
h={('s',1):Fr(1,4),('s',3):Fr(1,4)}
H,G,P,res=run(h,{},7)
print('certificate (G0=0):',res)
for n in (1,3,5): print('G',n,sorted(G[n].items(),key=lambda x:x[0][1]))
for n in (2,4,6): print('H',n,sorted(H[n].items(),key=lambda x:x[0][1]))
print('P7 log coeff', res[3]/(4*1*1) if res else None)  # D(4m-D)p = g, top term g z/(4m) for degree-0 g, m=1
G0=sc(Fr(-1),mul(SIN,d(h)))
H,G,P,res=run(h,G0,7)
print('Remark 39.1 pair:',res)
