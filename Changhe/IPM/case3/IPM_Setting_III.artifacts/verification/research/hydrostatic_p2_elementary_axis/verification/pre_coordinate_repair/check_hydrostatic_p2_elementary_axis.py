"""Manufactures for result240, before saved-state use."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json
import sympy as sp
import mpmath as mp
import hydrostatic_p2_elementary_axis as e
import hydrostatic_axis_log_constant as old
ROOT=Path('research/hydrostatic_p2_elementary_axis');V=ROOT/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(n,b,v=None):checks.append(dict(name=n,passed=bool(b),evidence=v))
def mm(f):return mp.mpf(f.numerator)/f.denominator
st=lambda x:mp.nstr(x,28)
t=sp.symbols('t',real=True)
check('j1 exact derivative',sp.simplify(sp.diff(2*t/(1-t*t)-sp.atanh(t),t)-(1+3*t*t)/(1-t*t)**2)==0)
check('j2 exact derivative',sp.simplify(sp.diff(4*sp.atanh(t)-3*t,t)-(1+3*t*t)/(1-t*t))==0)
for j in range(3,12):
 k=[F(0)]*(j+1);k[-1]=F(1);P=e.rational_polynomial(k);pol=sum(sp.Rational(a.numerator,a.denominator)*t**i for i,a in enumerate(P))
 check('j'+str(j)+' polynomial primitive',sp.expand(sp.diff(pol,t)-(1+3*t*t)*(1-t*t)**(j-3))==0)
 beta=sp.factorial(j-3)*sp.Rational(2)**(j-2)/sp.prod(range(3,2*j-2,2))
 check('j'+str(j)+' constant beta identity',sp.simplify(pol.subs(t,1)-j*beta)==0)
examples=[('signed',[0,3,-7,2,F(1,8),-1],[0,1,F(-3,10),F(11,100),F(-1,25)]),('logzero',[0,4,1,-2],[0,-1,F(2,3),F(-1,4)]),('leadingonly',[0,1],[0,1]),('highdegree',[0,-1,3,0,0,F(-1,7),2,0,-3,1],[0,1,2,-1,0,F(1,11)])]
records=[]
for digits in [65,100]:
 with mp.workdps(digits):
  for name,ks,hs in examples:
   kk=list(map(F,ks));hh=list(map(F,hs));PP=e.rational_polynomial(kk)
   for CC in [F(1,8),F(7,10),F(5)]:
    C=mm(CC);k=list(map(mm,kk));H=list(map(mm,hh));axis=e.Axis(C,H,k,list(map(mm,PP)));const=old.constants(C,H,k)
    for factor in ['0','0.01','0.5','1','16','1e4','1e12']:
     y=C*mp.mpf(factor);r=axis.evaluate(y);w=r['w'];tt=mp.sqrt(1-w);label=f'{digits} {name} C{CC} y/C{factor}'
     def integrand(u):return C*e.horner(k,1-u*u)*(1+3*u*u)/(1-u*u)**3
     direct=mp.quad(integrand,[0,tt/2,tt]) if y else mp.mpf(0)
     eps=mp.mpf(10)**(-digits+13)
     check(label+' complete quadrature',abs(r['V']-direct)<=eps*(1+abs(direct)),st(r['V']-direct))
     check(label+' coordinate equation',abs(C*tt/w**2-y)<=eps*(1+y))
     if y:
      v1=mp.diff(lambda yy:axis.evaluate(yy)['V'],y)
      g1=mp.diff(lambda yy:axis.evaluate(yy)['G'],y)
      g2=mp.diff(lambda yy:axis.evaluate(yy)['G'],y,2)
      r1=mp.diff(lambda yy:axis.evaluate(yy)['R'],y)
      for key,before,after in [('V1',v1,r['k']),('G1',g1,r['G1']),('G2',g2,r['G2']),('R1',r1,r['R1'])]:check(label+' derivative '+key,abs(before-after)<=eps*(1+abs(before)),st(before-after))
      if r['positive_denominator']:
       d=mp.diff(lambda yy:axis.evaluate(yy)['R']/axis.evaluate(yy)['Nf'],y);expected=2*r['stationary']/r['Nf']**2
       check(label+' normalized stationary derivative',abs(d-expected)<eps*(1+abs(d)))
     if mp.mpf(factor)>=16:
      previous=old.velocity(C,k,y,128)
      check(label+' independent tail-series inverse',abs(previous['V2']-r['V'])<=previous['remainder_bound']+eps*(1+abs(r['V'])),st(previous['V2']-r['V']))
     records.append(dict(digits=digits,name=name,C=str(CC),factor=factor,V=st(r['V']),R=st(r['R']),Nf=st(r['Nf'])))
    # Direct t polynomial endpoint gives the same constant without beta evaluation.
    k1=k[1] if len(k)>1 else mp.mpf(0);k2=k[2] if len(k)>2 else mp.mpf(0)
    M=C*(-k1/2+(4*k2-k1)*mp.log(2)+e.horner(axis.P,1))-const['B_log']*mp.log(C)
    check(f'{digits} {name} {CC} endpoint constant',abs(M-const['M'])<mp.mpf(10)**(-digits+10)*(1+abs(M)),st(M-const['M']))
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,records=records,proof_sha256=sha(ROOT/'PROOF.md'),module_sha256=sha(e.__file__),driver_sha256=sha(__file__),old_module_sha256=sha(old.__file__))
(V/'GATE.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([c for c in checks if not c['passed']])
if out['status']!='PASS':raise SystemExit(1)
