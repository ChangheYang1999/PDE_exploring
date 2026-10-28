"""Independent full-polygon point checks for the coupled Stieltjes cell rule."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,random
from fractions import Fraction
import mpmath as m
from flint import arb,ctx
import certify_axis_projection_stieltjes_v3 as C
ctx.prec=192;m.mp.dps=70
ROOT=Path(__file__).resolve().parents[1];rng=random.Random(202610280711)
def mpq(q):
 q=Fraction(q);return m.mpf(q.numerator)/q.denominator
def ab(x):return arb(m.nstr(x,75))
def seg(x,y,A,B,ray=False):
 u,v=B[0]-A[0],B[1]-A[1];t=((x-A[0])*u+(y-A[1])*v)/(u*u+v*v)
 t=max(0,t) if ray else min(1,max(0,t))
 return m.hypot(x-A[0]-t*u,y-A[1]-t*v)
def f(X,Y,a,b,t,K):
 # Full thirteen-feature geometry, in original coordinates x=X+1/2.
 x=X+m.mpf('.5');ds=[X]
 for pole,direction in [(m.mpf(1),1),(m.mpf(0),-1)]:
  for s in [-1,1]:
   ds.append(seg(x,Y,(pole,0),(m.mpf('.5'),m.mpf(s)/2)))
   end=(pole+direction*b,s*b)
   ds.append(seg(x,Y,(pole,0),end))
   ds.append(seg(x,Y,end,(end[0]+direction*m.sqrt(3),end[1]+s),True))
 w=x-1;B=abs(w) if w<=b else b+(w-b)/m.sqrt(3)
 g=2**(a-1)*m.sign(B-Y)*min(ds)**a
 r=m.hypot(w,Y);e=w*w-Y*Y
 P=(r**a+m.sign(e)*(abs(e)/r)**a)/2 if r else m.mpf(0)
 h=2**(a-1)*X**a
 return max(-h,min(h,g+t,-m.mpf('.5')+P/K))
rows=[]
for aq,bq,tq,kq in [('3/10','3/2','0','1007/1000'),('1/2','3/4','-3/20','1021/1000'),('3/4','3/4','-3/10','53/50'),('9/10','7/20','-3/10','11/10')]:
 a,b,t,K=map(mpq,[aq,bq,tq,kq]);aa,bb,tt,kk=map(C.aa,[aq,bq,tq,kq])
 ve_mp=[m.exp(-8+j*m.mpf(16)/32) for j in range(33)]
 ve=list(map(ab,ve_mp));pe=[C.profile(v,aa) for v in ve]
 n=0;improved=0;active=0
 for sign in [-1,1]:
  for i in range(40):
   ul=-14 if sign==-1 else -12;ur=m.log(m.mpf('.48')) if sign==-1 else 8
   logd=ul+(ur-ul)*rng.random();dl=m.exp(logd);dr=dl*m.exp(m.mpf(rng.randrange(1,60))/10000)
   di=ab(dl).union(ab(dr));X,h,factor,gs,ps,fs=C.data(di,ve,pe,sign,aa,bb,tt,kk)
   for j in range(32):
    mass,basic=C.mass_lower(j,h,factor,gs,ps,fs,pe)
    assert (mass>=basic or mass.overlaps(basic)) and (mass>=0 or mass.contains(0)),(aq,sign,i,j,str(mass),str(basic))
    if mass>basic:improved+=1
    if mass>0:active+=1
    for wt in [m.mpf(0),m.mpf('.5'),m.mpf(1)]:
     d=dl+(dr-dl)*wt;X0=m.mpf('.5')+sign*d
     delta=f(X0,d*ve_mp[j],a,b,t,K)-f(X0,d*ve_mp[j+1],a,b,t,K)
     assert delta>=-m.mpf('1e-60')
     exact=ab(delta)
     assert mass<=exact or mass.overlaps(exact),(aq,sign,i,j,str(mass),m.nstr(delta,30))
     n+=1
 rows.append(dict(alpha=aq,point_decreases=n,strictly_improved_cells=improved,positive_cells=active));print(rows[-1],flush=True)
paths=[Path(__file__),ROOT/'code/certify_axis_projection_stieltjes_v3.py',ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/coupled_profile/PROOF.md']
res=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=192,independent_decimal_digits=70,rows=rows,source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},verdict='PASS finite adversarial-grid diagnostics. Analytic proof is separate.')
out=ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/coupled_profile/verification';out.mkdir(exist_ok=True);(out/'independent_cell_checks.json').write_text(json.dumps(res,indent=2)+'\n')
