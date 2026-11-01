"""Independent full rational k-cycle, then exact expansion at infinity."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
import sympy as S
from general_fixed_deficit_audit import low,sine,cycle
from flint import fmpq as Q
start=time.monotonic();root=Path('research/72_higher_factorial_gain');k=S.Symbol('k');delta=S.Rational(2,3)
def rat(x):return S.Rational(str(x))
def add(out,j,v):out[j]=out.get(j,S.Integer(0))+v
rows=[]
for b in [Q(-1),Q(0),Q(1,5),Q(1)]:
 lf,lg=low(3,{1:Q(1),3:b});F={r:{m:rat(v) for m,v in sine(A).items()} for r,A in lf.items()};G={r:{m:rat(v) for m,v in sine(A).items()} for r,A in lg.items()};HF={};HG={0:{0:S.Integer(1)}}
 for r in range(1,4):
  out={};lam=6*k+2*(r-1)
  for i in range(r):
   j=r-i;Ph=2-2*k-delta*i;pl=1-delta*j
   for off,h in HG[i].items():
    w=2*k-2+off
    for ell,a in F[j].items():
     add(out,off+ell,h*a*(Ph*ell-pl*w)/2);add(out,off-ell,h*a*(Ph*ell+pl*w)/2)
  for i in range(1,r):
   j=r-i;Pl=2-delta*i;ph=1-2*k-delta*j
   for ell,g in G[i].items():
    for off,h in HF[j].items():
     w=2*k-2+off
     add(out,off+ell,g*h*(Pl*w-ph*ell)/2);add(out,off-ell,-g*h*(Pl*w+ph*ell)/2)
  HF[r]={j:S.cancel(v/lam) for j,v in out.items() if v!=0}
  if r<3:
   gp={};P=2-2*k-delta*r
   for off,v in HF[r].items():
    w=2*k-2+off
    add(gp,off+1,-v/(2*(w+1+P)));add(gp,off-1,v/(2*(w-1-P)))
   HG[r]={j:S.cancel(v) for j,v in gp.items() if v!=0}
 kr=S.cancel(-HF[3].get(1,0)/2);num,den=map(lambda z:S.Poly(z,k),S.fraction(kr));d=den.degree();assert num.degree()<=d
 lam=num.nth(d)/den.nth(d);mu=(num.nth(d-1)*den.nth(d)-num.nth(d)*den.nth(d-1))/den.nth(d)**2
 be=rat(b);expected_lam=(314-2925*be+6735*be**2+75*be**3)/259200;expected_mu=(-3022+34665*be-68355*be**2-105225*be**3)/1555200
 assert lam==expected_lam and mu==expected_mu,(b,lam,mu)
 tests=[]
 for kk in [16,32,64]:
  exact=cycle(3,lf,lg,kk,0);assert rat(exact)==kr.subs(k,kk);tests.append(dict(k=kk,exact_cartesian_match=True))
 rows.append(dict(b=str(b),kR_numerator=str(num.as_expr()),kR_denominator=str(den.as_expr()),Lambda=str(lam),mu=str(mu),degree_num=num.degree(),degree_den=d,finite_cycles=tests))
 print(json.dumps(dict(b=str(b),Lambda=str(lam),mu=str(mu),elapsed_s=time.monotonic()-start)),flush=True)
record=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),method='full rational function in k; Cartesian low coefficients; four-point exact b interpolation',all_passed=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
(root/'verification/exact_rational_first_jet.json').write_text(json.dumps(record,indent=2)+'\n')
for name in ['exact_rational_first_jet.py','general_fixed_deficit_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps({k:v for k,v in record.items() if k!='rows'}))
