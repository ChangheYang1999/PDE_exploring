"""Independent high-precision point and derivative checks for the projection certificates."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
import numpy as np,mpmath as mp
from flint import arb,ctx
from certify_axis_projection_stieltjes_v2 import witness
from certify_axis_projection_density import density
ctx.prec=192;mp.mp.dps=60;ROOT=Path(__file__).resolve().parents[1]
def dist(X,Y,x0,y0,x1,y1,ray=False):
 dx=x1-x0;dy=y1-y0;q=((X-x0)*dx+(Y-y0)*dy)/(dx*dx+dy*dy)
 q=max(0,q) if ray else min(1,max(0,q));return mp.sqrt((X-x0-q*dx)**2+(Y-y0-q*dy)**2)
def exact_f(X,Y,alpha,b,shift,K):
 a=mp.mpf('.5');d=min(X,dist(X,Y,0,a,a,0),dist(X,Y,a,0,a+b,b),dist(X,Y,a+b,b,a+b+mp.sqrt(3),b+1,True))
 B=a-X if X<a else X-a if X<a+b else (X-a+(mp.sqrt(3)-1)*b)/mp.sqrt(3)
 c=mp.power(2,alpha-1);g=(1 if Y<B else -1)*c*d**alpha;h=c*X**alpha;dx=X-a;r=mp.sqrt(dx*dx+Y*Y);e=dx*dx-Y*Y
 P=(r**alpha+mp.sign(e)*(abs(e)/r)**alpha)/2
 return max(-h,min(h,min(g+shift,-a+P/K)))
def aa(x):return arb(str(x))
def main():
 rng=np.random.default_rng(93633);rows=[]
 for astr,kstr in [('1/2','1021/1000'),('3/4','53/50')]:
  af=F(astr);kf=F(kstr);alpha=mp.mpf(af.numerator)/af.denominator;K=mp.mpf(kf.numerator)/kf.denominator;b=mp.mpf('.75');shift=mp.mpf('-.15');count=positive=0;worst=-mp.inf
  for sign in [-1,1]:
   for _ in range(1200):
    u=float(rng.uniform(-10,-.72 if sign<0 else 5));vw=float(rng.uniform(-5,5));du=float(rng.uniform(.0001,.008));dv=float(rng.uniform(.0001,.04))
    dl=mp.exp(u);dr=mp.exp(u+du);vl=mp.exp(vw);vr=mp.exp(vw+dv);db=aa(dl).union(aa(dr));vb=aa(vl).union(aa(vr))
    lower,branch=density(db,vb,sign,aa(alpha),aa(b),aa(shift),aa(K));lb=mp.mpf(lower.lower().str(70,radius=False))
    for q in [.211,.517,.839]:
     d=dl+q*(dr-dl);v=vl+(1-q)*(vr-vl);X=mp.mpf('.5')+sign*d;Y=d*v;f=exact_f(X,Y,alpha,b,shift,K)
     enc=witness(db,aa(v),sign,aa(alpha),aa(b),aa(shift),aa(K));assert enc.contains(aa(f)),('point',astr,sign,u,vw,enc,f)
     if lb>0:
      rate=-mp.diff(lambda yy:exact_f(X,yy,alpha,b,shift,K),Y)
      pref=X*d*v*v/(mp.pi*(1+v*v)*((X+mp.mpf('.5'))**2+d*d*v*v));value=pref*rate
      ex=lb-value;worst=max(worst,ex);assert ex<mp.mpf('1e-35'),('density',astr,branch,ex)
      positive+=1
     count+=1
  rows.append(dict(alpha=astr,point_enclosures=count,positive_density_checks=positive,largest_density_excess=str(worst)))
 paths=[Path(__file__),ROOT/'code/certify_axis_projection_stieltjes_v2.py',ROOT/'code/certify_axis_projection_density.py']
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,status='Independent mpmath60-digit diagnostics passed; interval proofs supply rigor.',source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
 path=ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/verification/independent_cell_checks.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
