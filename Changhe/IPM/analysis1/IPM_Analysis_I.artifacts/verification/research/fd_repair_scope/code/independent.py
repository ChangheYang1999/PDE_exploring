"""Independent rational Fourier/jet calculations and iv power-form row weights."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
import hashlib,json,sys,tokenize,io
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/fd_repair_scope'
def check(v,t):
 if not v:raise ValueError(t)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rr(q):q=F(q);return str(q.numerator)+'/'+str(q.denominator)
def iq(a):
 sign,m,e,bc=a;return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
def enc(a):return [rr(iq(a._mpi_[0])),rr(iq(a._mpi_[1]))]
def mul(p,q):
 out={}
 for i,a in p.items():
  for j,b in q.items():out[i+j]=out.get(i+j,F(0))+a*b
 return {i:a for i,a in out.items() if a}
# Work with i sin(theta)=(z-z^-1)/2, so every arithmetic operation is rational.
a=mul(mul({1:F(1,2),-1:F(1,2)},{1:F(1,2),-1:F(1,2)}),{1:F(1,2),-1:F(-1,2)});check(a=={3:F(1,8),1:F(1,8),-1:F(-1,8),-3:F(-1,8)},'rational angular coefficients')
p={1:F(1),3:F(-3),5:F(3),7:F(-1)}
def jet(x,n):return sum((v*F(factorial(i),factorial(i-n))*F(x)**(i-n) for i,v in p.items() if i>=n),F(0))
jets={str(x):[str(jet(x,n)) for n in range(3)] for x in [-1,0,1]};check(jets=={'-1':['0','0','0'],'0':['0','1','0'],'1':['0','0','0']},'direct jets')
# Separate literal/token read, with no AST or execution of teammate source.
source=(D/'evidence/c2_gram2_source.py.txt').read_text();tokens=list(tokenize.generate_tokens(io.StringIO(source).readline));compact=''.join(t.string for t in tokens if t.type not in [tokenize.COMMENT,tokenize.NL,tokenize.NEWLINE,tokenize.INDENT,tokenize.DEDENT,tokenize.ENDMARKER])
fragments=['quad=ROWS.endswith("q")','sq_dt=np.sqrt(dtv)','sq_dt=np.ones(Ne-1)','dt=np.diff(t_eval)','wm=0.5*(w_i[1:]+w_i[:-1])','der=((X3[1:]-X3[:-1])*(wm*sq_dt/dt)[:,None,None]).reshape((Ne-1)*Mout,nc)','forjoinin(tmin,t00):']
for f in fragments:check(f in compact,'independent source fragment')
# Twenty-four signed secant fixtures without algebraic symbolic simplification.
secants=0
for jm in [-7,-2,1,5]:
 for den in [3,11,29]:
  for sign in [-1,1]:
   jump=F(jm,17);width=F(2,den);am=F(sign*den,13);ap=F(jm,7);base=F(11,31);lo=base-am*width/2;hi=base+jump+ap*width/2
   check((hi-lo)/width==jump/width+(am+ap)/2,'signed direct secant');secants+=1
fixture=json.loads((D/'evidence/fixture.json').read_text());q={n:F(fixture[n]) for n in ['L','k','cl','R','d','Delta']};iv.dps=180
def I(v):return iv.mpf(v.numerator)/v.denominator
L,k,cl,R,d,Delta=[I(q[n]) for n in ['L','k','cl','R','d','Delta']];weights=[]
for sign in [-1,1]:
 radius=iv.exp(iv.ln(R)+sign*Delta/2);u=radius/L;weights.append((1+u)**iv.mpf('0.5')*u**(-3)*(1+u*u)**((3-k)/2))
jump=q['R']**3*q['d']/12;wm=(weights[0]+weights[1])/2;v={'weight_left':enc(weights[0]),'weight_right':enc(weights[1]),'H1_jump':enc(wm*I(jump)/Delta),'H1q_jump':enc(wm*I(jump)*Delta**iv.mpf('-0.5'))}
primary=json.loads((D/'evidence/compute.json').read_text());check(primary['jump_coefficient']==rr(jump),'separate jump');check(primary['compact_polynomial_jets']==jets,'separate jets')
ceilings={'H1_jump':['99378689/1000000000000000','99378690/1000000000000000'],'H1q_jump':['14054269/1000000000000000','14054270/1000000000000000']}
for name,interval in v.items():
 a,b=map(F,interval);c,d=map(F,primary['arb_exact_intervals'][name]);check(max(a,c)<=min(b,d),'independent interval intersection')
 if name in ceilings:
  lo,hi=map(F,ceilings[name]);check(F(1,10**11)<lo<min(a,c)<=max(b,d)<hi,'strict outward fixture endpoints')
pins={}
for n,h in primary['files'].items():check(sha(B/n)==h,'primary pin');pins[n]=h
for pth in [D/'evidence/compute.json',Path(__file__)]:pins[str(pth.relative_to(B))]=sha(pth)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_RATIONAL_FOURIER_JETS_SECANTS_AND_IV180_FIXTURE','source_token_checks':len(fragments),'signed_secant_checks':secants,'iv_exact_intervals':v,'strict_common_bounds':ceilings,'files':pins,'scope':'General amplification inference only. Actual numerical row differences, retained Q, spectrum transfer and PDE endpoints OPEN.'}
pth=D/'evidence/independent.json';check(not pth.exists(),'immutable');pth.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:out[n] for n in ['utc','status','source_token_checks','signed_secant_checks','strict_common_bounds']}))
