"""Rational-point lower bounds for the signed principal-symbol constant."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import sys,json,time
from flint import arb,arb_poly,acb,ctx,fmpq_poly
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/point_witness/code'))
from radial import Radial,ar
from cartesian import CartesianJet

def source(name):
 if name.startswith('C1-'):return ROOT/f'research/candidate_audits/data/{name}/canonical.json'
 if name.startswith('state'):return ROOT/f'research/baseline/data/{name}_independent.json'
 return ROOT/f'research/refit_audit/data/{name}_canonical.json'

def run(name):
 ctx.prec=512;start=time.monotonic();p=source(name);model=Radial(p)
 funcs={};U=fmpq_poly([1,-1])
 for field,A in [('rho_x',model.rx),('rho_y',model.ry)]:
  funcs[field]=[(j,n,arb_poly([ar(v) for v in P]),arb_poly([ar(v) for v in P(U)])) for (j,n),P in A.items()]
 maxn=max(n for A in funcs.values() for j,n,P,Q in A)
 kpath=ROOT/f'research/background_sobolev/verification/{name}.json'
 if kpath.exists():
  kd=json.loads(kpath.read_text());kappa=arb(kd['gradient_identity_conditional_HS_upper']);ks='structured Hilbert-Schmidt norm'
 else:kappa=arb(0);ks='zero, using only kappa>=0'
 rows=[];best=None
 for i in range(-4,7):
  x=Fraction(2)**i
  for j in range(-4,5):
   y=x*Fraction(2)**j;xa=arb(x.numerator)/x.denominator;ya=arb(y.numerator)/y.denominator
   r2=xa*xa+ya*ya;r=r2.sqrt();R=1+r2;t=r2/R;u=1/R;z=acb(xa/r,ya/r)
   powers=[acb(1)]
   for n in range(maxn):powers.append(powers[-1]*z)
   rp={j:R**ar(exp)/r2**2 for j,exp in model.p.items()};v={}
   for field,A in funcs.items():
    total=arb(0)
    for j,n,P,Q in A:
     trig=powers[n].imag if field=='rho_x' else powers[n].real
     total+=rp[j]*(P(t) if t<arb('0.5') else Q(u))*trig
    v[field]=total
   theta=((v['rho_x']**2+v['rho_y']**2).sqrt()-v['rho_y'])/2
   gap=theta+kappa-(ar(model.c)-1)
   row={'point':[str(x),str(y)],'theta':theta.str(60),'failure_gap':gap.str(60),'strict_failure':bool(gap>0)}
   rows.append(row)
   if best is None or theta>arb(best['theta']):best=row
 jet=CartesianJet(p,*best['point']);jf=jet.fields()
 jt=((jf['rho_x']**2+jf['rho_y']**2).sqrt()-jf['rho_y'])/2
 assert jt.overlaps(arb(best['theta']))
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'source_sha256':sha256(p.read_bytes()).hexdigest(),
      'precision_bits':ctx.prec,'kappa_choice':ks,'kappa':kappa.str(60),'best':best,
      'cartesian_best_theta':jt.str(60),'cartesian_overlap':True,'rows':rows,'elapsed_seconds':time.monotonic()-start}
 dest=ROOT/f'research/background_points/verification/{name}_signed_scan.json';dest.write_text(json.dumps(out,indent=2)+'\n')
 print(name,best,'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':
 for name in sys.argv[1:]:run(name)
