# independent recomputation of the conservative radius eps0 of checker result 157
from fractions import Fraction as F
import math
def run(ell,K,M,g0):
    p=1/F(ell); d=1-p; s=[p-i*d for i in range(K+1)]
    L=[]
    for i in range(K):
        q=abs(s[i]+1)
        if q==0: B=F(1)
        else:
            cands=[m for m in (2*math.floor(q/2),2*math.floor(q/2)+2,2) if m>=2]
            B=max((m+q)/abs(m-q) for m in cands)
        L.append(B*(F(3,2)**K+1)/2)
    C=[F(1)]
    for k in range(1,K+1):
        C.append(sum(L[i]*(abs(s[k-1-i])+1)*C[i]*C[k-1-i] for i in range(k))/(ell*k*d))
    e0=min(F(1),abs(g0)/(2*M*(K+1)*C[K]*(2**K+1)**K))
    return float(e0)
print(run(F(3),5,2,F(-177047,301056000000)))
print(run(F(5,2),9,4,F(26243642326438735772269905591088207,4898218301752285282303033607434666157015040)))
