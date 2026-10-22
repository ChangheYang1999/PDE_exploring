"""Independent exact polynomial identities and two interval parameter formulas."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3]; E=B/'research/source_cusp_audit/evidence';ctx.prec=320;ctx.threads=1;iv.dps=160
assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def af(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ae(x):assert x.is_finite();return af(x.mid())-af(x.rad()),af(x.mid())+af(x.rad())
def rf(t):s,m,e,b=t;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ie(x):assert not iv.isinf(x) and not iv.isnan(x);return tuple(map(rf,x._mpi_))
def diff(p,axis):
 q={}
 for ij,c in p.items():
  degree=ij[axis]
  if degree:
   dest=list(ij);dest[axis]-=1;dest=tuple(dest);q[dest]=q.get(dest,F(0))+degree*c
 return {i:c for i,c in q.items() if c}
def add(*ps):
 q={}
 for p in ps:
  for i,c in p.items():q[i]=q.get(i,F(0))+c
 return {i:c for i,c in q.items() if c}
p={(2,1):F(1),(0,3):F(-1,3)};xx=diff(diff(p,0),0);yy=diff(diff(p,1),1);xy=diff(diff(p,0),1)
assert xx=={(0,1):F(2)} and yy=={(0,1):F(-2)} and add(xx,yy)=={} and xy=={(1,0):F(2)}
assert all(i%2==0 and j%2==1 for i,j in p)
# Independently evaluate the displayed differential identities at rational points.
checks=0
for s in [F(-3,2),F(0),F(5,7)]:
 for y in [F(-2,3),F(0),F(7,5)]:
  evalp=lambda q:sum(c*s**i*y**j for (i,j),c in q.items())
  assert evalp(xx)==2*y and evalp(yy)==-2*y and evalp(xy)==2*s;checks+=3
A=F('10.1507252');g=F('29.7494907');d=1+g;a=g/(A-1);q=A+2-a
exact={'a':a,'p':d/A,'gamma':g/A,'s_fast':(g+(A+3)/2)/A,'s_1':(g+(A+3)/2)/A+2-2/A,'q_minus_half':q-F(1,2),'alpha_star':d/A-3}
x,y=aa(A),aa(g)
ar={'a':y/(x-1),'p':(1+y)/x,'gamma':y/x,'s_fast':(y+(x+3)/2)/x,'s_1':(y+(x+3)/2)/x+2-2/x,'q_minus_half':x+2-y/(x-1)-aa(F(1,2)),'alpha_star':(1+y)/x-3}
x,y=iq(A),iq(g);inv=1/x;pv=(1+y)*inv
vr={'a':(y*inv)/(1-inv),'p':pv,'gamma':pv-inv,'s_fast':iq(F(1,2))+(y+iq(F(3,2)))*inv,'s_1':iq(F(5,2))+(y-iq(F(1,2)))*inv,'q_minus_half':(x*x+x-2-y)/(x-1)-iq(F(1,2)),'alpha_star':(y+1-3*x)*inv}
rows={}
for key,v in exact.items():
 al,ah=ae(ar[key]);il,ih=ie(vr[key]);assert al<=v<=ah and il<=v<=ih
 rows[key]={'exact':str(v),'arb_lower':str(al),'arb_upper':str(ah),'iv_lower':str(il),'iv_upper':str(ih),'display':ar[key].str(28)}
assert 3<a<4 and F(3)<exact['p']<F(4) and F(21,4)<exact['s_1']<q-F(1,2)
# No resonance Ai+j=d with nonnegative integer i,j for these illustrative constants.
nonres=[]
for i in range(4):
 v=d-A*i;assert v>0 and v.denominator!=1;nonres.append({'i':i,'d_minus_Ai_exact':str(v)})
assert d-4*A<0
# Reconstruct the conjugation coefficient at the polynomial level in the symbol m.
assert (-A-2+a)==-q and a*(A-1)-g==0 and q+a==A+2
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ELEMENTARY_REQUIRES_REVIEW','scope':'Exact illustrative A and g, frozen mu=1. Not enclosures of the actual source parameters. Polynomial checks support the independently proved cutoff construction; they do not audit the complete cusp expansion.','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/source_cusp_audit/PROOF.md'),'lead_snapshot_sha256':sha(E/'lead_pcusp1_PROOF_snapshot.md'),'parameters':{'A_exact':str(A),'g_exact':str(g),'mu_exact':'1'},'polynomial_point_identity_checks':checks,'interval_containments':14,'rows':rows,'nonresonance':nonres,'conjugation_exact':True}
(E/'elementary.json').open('x').write(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'checks':checks,'interval_containments':14,'values':{k:v['display'] for k,v in rows.items()}},indent=2))
