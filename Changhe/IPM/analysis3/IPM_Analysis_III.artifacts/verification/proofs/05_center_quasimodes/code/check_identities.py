from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
import sympy as S
import numpy as np
TOP=Path(__file__).resolve().parents[1]
ROOT=TOP.parents[1]
a,b,m=S.symbols('a b m',real=True)
p=(b*m-1)/(b-a);q=(1-a*m)/(b-a)
assert S.factor(p+q-m)==0 and S.factor(a*p+b*q-1)==0
ell=S.symbols('ell',positive=True)
aa=1-2*ell;bb=4*ell-1
p2=S.factor(p.subs({a:aa,b:bb,m:2}));q2=S.factor(q.subs({a:aa,b:bb,m:2}))
assert S.factor(p2-(8*ell-3)/(6*ell-2))==0
assert S.factor(q2-(4*ell-1)/(6*ell-2))==0
assert S.factor(2*m+2-2*(m+S.Rational(1,2))-1)==0
assert S.factor(2*(m-1)-2*(m+S.Rational(1,2))+1+2)==0
assert S.factor(2*(m+1)+(-2*m-2)+1-1)==0
k=S.symbols('k',real=True)
assert S.factor(2*(k-3)+(-2*k-3)+1+8)==0
INP=ROOT/'research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
d=np.load(INP,allow_pickle=False)
rat=lambda x:F(*float(x).as_integer_ratio())
kk=rat(d['k']);bi=rat(d['bi']);bo=rat(d['bo']);el=1/kk
assert 0<kk<F(1,2) and el>2 and bi>4 and bo>3-kk
pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]
exps=[kk-j*(1-kk)-2*l for j,l in pairs]
assert exps[0]==kk and all(x<=2*kk-1 for x in exps[1:])
assert 3-bo<2*kk-1
knots=list(map(rat,d['knots']))
assert knots[:8]==[knots[0]]*8 and knots[-8:]==[knots[-1]]*8
assert all(knots[j]<knots[j+1] for j in range(7,len(knots)-8))
res={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS',
 'input_sha256':hashlib.sha256(INP.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'identities':['p+q=m','a*p+b*q=1','normalized p_2 and q_2','Sobolev scaling exponent 1','velocity Fourier radial power -2','center image radial power 1','far image radial power -8'],
 'exact_input_checks':['0<k<1/2','ell=1/k>2','bi>4','bo>3-k','all subleading density exponents <=2k-1','outer correction density exponent <2k-1','degree-seven clamped knots with simple interior knots'],
 'k':str(kk),'ell':str(el),'bi':str(bi),'bo':str(bo),
 'scope':'Exact algebra and finite input inequalities; complete analytic argument is in PROOF.md.'}
(TOP/'evidence/identities.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
