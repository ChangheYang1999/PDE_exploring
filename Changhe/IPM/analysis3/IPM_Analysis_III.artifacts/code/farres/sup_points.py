"""Independent original-data residual point audit. No floating angular division."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import importlib.util,json,hashlib,bisect,argparse,time
from flint import arb,arb_poly,ctx
ROOT=Path('data/farres');LANE=Path('verification')
def load(name,path):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
G=load('own_global',LANE/'proofs/68_independent_global_coefficients/code/global_check.py')
ANG=load('own_angle',LANE/'proofs/98_exact_angular_norm/code/angular.py')
aa=G.aa

def evaluate(ep,s):
 return sum((G.C.horner(p,s)*(aa(e)*s).exp() for e,p in ep.terms.items()),arb(0))

def j_part(H,b):
 out=G.EP()
 for e,p in H.terms.items():
  if e==b:out.addterm(e,[arb(0)]+[-v/(j+1) for j,v in enumerate(p)])
  else:out=out+G.EP({e:p}).particular(-b).scale(-1)
 return out

def endpoint(d,cache,t,side):
 H=G.density_eps(d,side);s=aa(t-(d.tm if side=='inner' else d.tp))
 if side=='outer':P,Q,_,_=G.outer_eps(d,cache)
 else:
  fac=(2*aa(d.tm)).exp();j0=list(map(arb,cache['J_inner']));P=[];Q=[]
  for n in range(1,262):
   I=H[n-1].particular(2*n+4);b=2*n-4;J=j_part(H[n],b)
   hom=j0[n-1]-J.atzero()
   if n==1:
    central=fac*hom;target=3/aa(d.k)-1
    assert central.overlaps(target)
    hom=target/fac
   J.addterm(b,[hom])
   P.append((J+I.scale(-1)).expmul(2).scale(n*fac))
   Q.append(((J+I).scale(n)+(H[n]+H[n-1]).scale(F(-1,2))).expmul(2).scale(fac))
 rh=[evaluate(v,s) for v in H];drh=[evaluate(v.deriv(),s) for v in H]
 return rh,drh,[evaluate(v,s) for v in P],[evaluate(v,s) for v in Q],[evaluate(v.deriv(),s) for v in P]

def point(d,cache,t):
 if t<d.tm:return endpoint(d,cache,t,'inner')
 if t>d.tp:return endpoint(d,cache,t,'outer')
 span=bisect.bisect_right(d.knots,t)-1;ix=d.spans.index(span);a,b=d.knots[span:span+2]
 rows=d.poly(span).tolist();IL=list(map(arb,cache['I_left'][ix]));JR=list(map(arb,cache['J_right'][ix]))
 H,Sf,errs=G.C.local_series(rows,IL,JR,a,b,aa(t),arb(0))
 fac=(2*aa(t)).exp()
 rh=H[0];drh=H[1]
 P=[2*n*fac*Sf[n-1][0] for n in range(1,262)]
 Q=[fac*(4*v[0]+v[1]) for v in Sf]
 Pt=[2*n*fac*(2*Sf[n-1][0]+Sf[n-1][1]) for n in range(1,262)]
 return rh,drh,P,Q,Pt

def residual_sines(rh,drh,P,Q,ell):
 # All Laurent arrays use the same center. Products then have center2L.
 L=523
 def poly(items,kind):
  out=[arb(0) for _ in range(2*L+1)]
  for k,c in items:
   if k==0:out[L]+=c
   else:out[L+k]+=c;out[L-k]+=c if kind=='cos' else -c
  return arb_poly(out)
 vr=poly([(0,ell)]+[(2*n,-v/2) for n,v in enumerate(P,1)],'cos')
 sd=poly([(2*j+1,3*v+drh[j]) for j,v in enumerate(rh)],'sin')
 sq=poly([(2*n,v) for n,v in enumerate(Q,1)],'sin')
 ct=poly([(2*j+1,(2*j+1)*v/2) for j,v in enumerate(rh)],'cos')
 sr=poly([(2*j+1,v) for j,v in enumerate(rh)],'sin')
 shift=arb_poly([arb(0)]*L+[arb(1)])
 out=vr*sd+sq*ct-sr*shift
 return [out[2*L+2*j+1] for j in range(523)]

def cofactor(sines):
 # sin((2n+1)theta)/sin(theta)=1+2 sum_{j=1}^n cos(2jtheta).
 tail=arb(0);A=[arb(0) for _ in sines]
 for j in range(len(sines)-1,-1,-1):
  tail+=sines[j];A[j]=tail*(1 if j==0 else 2)
 assert ANG.axis(A).contains(0)
 return ANG.quotient(A)

def main():
 p=argparse.ArgumentParser();p.add_argument('--bits',type=int,default=384);p.add_argument('--points',default='-40,-10,0,4,10,30');args=p.parse_args()
 ctx.prec=args.bits;ctx.threads=1;start=time.monotonic()
 d=G.M.Data();G.check_hash(d);cache=G.load_cache(d);ell=1/aa(d.k);D=4*ell-1;mm=ANG.moments(1044);results=[]
 for ts in args.points.split(','):
  t=F(ts);rh,drh,P,Q,Pt=point(d,cache,t);sines=residual_sines(rh,drh,P,Q,ell);B=cofactor(sines)
  l1F=sum((abs(v) for v in sines),arb(0));l1r=sum((abs(v) for v in rh),arb(0));th=[arb.pi()*i/200 for i in range(1,100)]
  supF=max(abs(float(sum((v*((2*j+1)*x).sin() for j,v in enumerate(sines)),arb(0)).mid())) for x in th)
  supr=max(abs(float(sum((v*((2*j+1)*x).sin() for j,v in enumerate(rh)),arb(0)).mid())) for x in th)
  print(json.dumps({'t':ts,'l1F':float(l1F.mid()),'l1rho':float(l1r.mid()),'supF_over_r3':supF,'suprho_over_r3':supr}),flush=True);continue
  gamma=ANG.axis(B);qq=ANG.quotient(B);rem=ANG.beta_mass()*ANG.normalized_square(qq,mm)
  omega=(aa(F(-1,2) if t<0 else F(27,4))*aa(t)).exp()
  alpha=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(rh)),arb(0))
  alphat=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(drh)),arb(0))
  rate=ell-sum(((-1)**n*v for n,v in enumerate(P,1)),arb(0))
  ratet=-sum(((-1)**n*v for n,v in enumerate(Pt,1)),arb(0))
  axis_direct=rate*alphat+(D-rate-2*ratet)*alpha
  assert (gamma-axis_direct).contains(0)
  th=arb.pi()/7
  direct=(ell-sum((v*(2*n*th).cos() for n,v in enumerate(P,1)),arb(0)))*sum(((3*v+drh[j])*((2*j+1)*th).sin() for j,v in enumerate(rh)),arb(0))
  direct+=sum((v*(2*n*th).sin() for n,v in enumerate(Q,1)),arb(0))*sum(((2*j+1)*v*((2*j+1)*th).cos() for j,v in enumerate(rh)),arb(0))
  direct-=sum((v*((2*j+1)*th).sin() for j,v in enumerate(rh)),arb(0))
  reconstructed=th.cos()**2*th.sin()*sum((v*(2*j*th).cos() for j,v in enumerate(B)),arb(0))
  assert (direct-reconstructed).contains(0)
  item={'t':str(t),'gamma':G.rec(gamma),'axis_energy_density':G.rec(omega*gamma**2),'remainder_energy_density':G.rec(omega*rem),'total_energy_density':G.rec(omega*(gamma**2+rem)),
   'raw_sine_axis_defect':G.rec(sum(((-1)**j*v for j,v in enumerate(sines)),arb(0))),
   'axis_formula_difference':G.rec(gamma-axis_direct),'reconstruction_difference':G.rec(direct-reconstructed)}
  results.append(item)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'t':ts,'axis':(omega*gamma**2).str(14),'remainder':(omega*rem).str(14),'seconds':time.monotonic()-start}),flush=True)
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS_POINT_CHECKS_ONLY','bits':args.bits,'original_sha256':d.sha,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start,'results':results}
 (ROOT/f'sup_points_{args.bits}.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
