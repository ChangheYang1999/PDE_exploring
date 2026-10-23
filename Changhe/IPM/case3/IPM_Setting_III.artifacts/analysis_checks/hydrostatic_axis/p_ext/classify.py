# classify the Case II patterns (e, A_0, mu) for odd m by the proved exclusions:
# e <= 1; equal multiplicities; 261 lemma (single exceptional: nu > mu excluded; nu < mu needs A_0 = 1 and mu - nu > n >= 1);
# e = 2: the three weights must be (nu, mu, mu) with nu < mu (258: three distinct weights force three real nodes, M_2 > 0)
import sys
from collections import Counter
from scan_sym import multisets
def status(m,e,A0,mu):
    c=Counter(mu)
    if len(c)==1: return 'equal'
    if len(c)==2:
        (v1,k1),(v2,k2)=c.items()
        if k1==1 or k2==1:
            nu,muu=(v1,v2) if k1==1 else (v2,v1)
            if k1==1 and k2==1 and len(mu)==2: return 'two nodes?'
            if nu>muu: return 'lemma nu>mu'
            if A0>=3: return 'lemma A0>=3'
            if muu-nu<2: return 'lemma mu-nu<=n'
            return 'lemma-survivor n<%d'%(muu-nu)
    if e==2:
        return 'e2 distinct weights (all real)'
    return 'OPEN'
for m in [int(x) for x in sys.argv[1].split(',')]:
    for e in range(2,(m-3)//2+1):
        for A0 in range(1,m+1,2):
            tot=(m-A0)//2
            if tot<e+1: continue
            for mu in multisets(tot,e+1):
                st=status(m,e,A0,mu)
                if not st.startswith(('equal','lemma nu','lemma A0','lemma mu','e2 distinct')): print(m,e,A0,mu,st)
