"""Exact Fourier symbols, symbolic edge products and independent moment bounds."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/yface_structure/evidence';ctx.prec=320;ctx.threads=1;iv.dps=160
assert sys.flags.optimize==0
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
aa=lambda q:arb(F(q).numerator)/F(q).denominator
iq=lambda q:iv.mpf(F(q).numerator)/F(q).denominator
def af(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ae(x):assert x.is_finite();return af(x.mid())-af(x.rad()),af(x.mid())+af(x.rad())
def rf(t):s,m,e,b=t;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ie(x):assert not iv.isinf(x) and not iv.isnan(x);return tuple(map(rf,x._mpi_))
def poly(*terms):
 out={}
 for coeff,xp,names in terms:
  key=(xp,tuple(sorted(names)));out[key]=out.get(key,F(0))+F(coeff)
 return {k:v for k,v in out.items() if v}
def mul(p,q):
 return poly(*[(c*d,i+j,m+n) for (i,m),c in p.items() for (j,n),d in q.items()])
def add(p,q):return poly(*[(c,i,n) for (i,n),c in list(p.items())+list(q.items())])
rx=poly((2,1,('p2',)),(4,3,('p4',)),(6,5,('p6',)))
ry=poly((1,2,('dp2',)),(1,4,('dp4',)),(1,6,('dp6',)))
w1=poly((1,1,('v11',)),(F(1,3),1,('sigma',)),(1,3,('v13',)),(1,5,('v15',)))
w2=poly((1,0,('v20',)),(F(1,3),0,('sigma','y')),(1,2,('v22',)),(1,4,('v24',)))
product=add(mul(rx,w1),mul(ry,w2))
q2=poly((2,2,('p2','v11')),(F(2,3),2,('p2','sigma')),(1,2,('dp2','v20')),(F(1,3),2,('dp2','sigma','y')))
q4=poly((4,4,('p4','v11')),(F(4,3),4,('p4','sigma')),(2,4,('p2','v13')),(1,4,('dp4','v20')),(F(1,3),4,('dp4','sigma','y')),(1,4,('dp2','v22')))
assert {k:v for k,v in product.items() if k[0]==2}==q2 and {k:v for k,v in product.items() if k[0]==4}==q4
assert all(i>=6 for (i,n) in product if i not in [2,4])
sc=0
for x in map(F,[-3,0,2]):
 for y in map(F,[-5,0,7]):
  if not x and not y:continue
  d=x*x+y*y;u1=x*y/d;u2=-x*x/d
  assert u1==y*x/d and u2+1==y*y/d;sc+=2
rows=[]
for a in map(F,['0.125','1','2','5','32']):
 for n in range(9):
  exact=F(math.factorial(n))/a**n
  av=arb(n+1).gamma()/aa(a)**n
  vv=iv.mpf(1)
  for j in range(1,n+1):vv=vv*j/iq(a)
  al,ah=ae(av);il,ih=ie(vv);assert al<=exact<=ah and il<=exact<=ih
  rows.append({'a':str(a),'n':n,'exact':str(exact),'arb':[str(al),str(ah)],'iv':[str(il),str(ih)]})
# An admissible rational-width variant with smaller epsilon at a=6.45.
prev=None
for j in range(1,31):
 b=F(1,2**j);eps=b**16/16;assert 0<eps<b/8
 if prev is not None:assert b+eps<prev[0]-prev[1]
 prev=b,eps
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_STRUCTURE_REQUIRES_REVIEW','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/yface_structure/PROOF.md'),'snapshot_sha256':sha(E/'lead_yface_snapshot.md'),'symbol_identities':sc,'q2_monomials':len(q2),'q4_monomials':len(q4),'product_monomials':len(product),'laplace_moment_cases':len(rows),'interval_containments':2*len(rows),'rational_spike_supports':30,'rows':rows,'scope':'Exact structural checks only. Moment methods use a common proved Laplace identity, gamma versus integration-by-parts recurrence. No N6 collar constants or full remainder bound.'}
(E/'structure.json').open('x').write(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
