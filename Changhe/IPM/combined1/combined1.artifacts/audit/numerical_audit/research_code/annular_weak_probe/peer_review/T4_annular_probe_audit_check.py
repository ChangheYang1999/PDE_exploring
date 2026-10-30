from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time,sys
from math import comb
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
from polar_fields import fields,square_groups,td,T,U,ZERO,ar
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(rows,j,v):
 if v:rows[j]=rows.get(j,ZERO)+v
def homogenize(poly,R):
 d=poly.degree();return sum((v*T**k*U**(d-k)/R**(2*k) for k,v in enumerate(poly)),ZERO),d
def bernstein(poly,d):return [sum((poly[j]*Q(comb(i,j),comb(d,j)) for j in range(i+1)),Q(0)) for i in range(d+1)]
def integrate(poly,e,lo,hi):
 coeff=(T*poly)(U);power=e+1;aa=ar(lo);bb=ar(hi)
 va=aa**ar(power);vb=bb**ar(power);result=arb(0)
 for v in coeff:
  if v:
   term=(bb/aa).log() if power==0 else (vb-va)/ar(power)
   result+=ar(v)*term
  va*=aa;vb*=bb;power+=1
 return result
def run(name,radii,bits):
 start=time.monotonic();ctx.prec=bits
 src=ROOT/'data'/f'{name}_canonical.json';target=ROOT/'source'/f'N4_{name}.json'
 c,delta,rho,stream=fields(json.loads(src.read_text()));bgroups,_=square_groups(stream,delta,2);cgroups,_=square_groups(rho,delta,1)
 na={};nb={}
 for (j,m),ss in stream.items():
  ds=td(ss,(j+1)*delta/2,2)
  for (i,n),rr in rho.items():
   if abs(n-m)!=1:continue
   sign=1 if n>m else -1
   put(na,i+j,sign*m*ss*rr);put(nb,i+j,ds*rr)
 q=(T-1)**2*(4-T)**2;ev=q+2*T*q.derivative();w=q*q+ev*ev;sv=(3*c+1)*q+2*c*T*q.derivative()
 assert bernstein(q(1+3*T),4)==[0,0,Q(27,2),0,0]
 assert bernstein(ev(1+3*T),4)==[0,27,Q(135,2),-108,0]
 integ=(T*sv*sv).integral();a2=arb.pi()/2*ar(integ(Q(4))-integ(Q(1)));A=a2.sqrt()
 peer=json.loads(target.read_text());assert peer['source_sha256']==digest(src)
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'precision_bits':bits,'source_sha256':digest(src),'peer_sha256':digest(target),'proof_sha256':digest(ROOT/'PROOF.md'),'code_sha256':digest(Path(__file__)),'helper_sha256':digest(ROOT/'code/polar_fields.py'),'method':'polar weak background pairing and complete polar squares; no residual cache','probes':[]}
 print('constructed',name,'seconds',time.monotonic()-start,flush=True)
 for Rint in radii:
  R=Q(Rint);lo=1/(1+4*R*R);hi=1/(1+R*R);qh,qd=homogenize(q,R);eh,ed=homogenize(ev,R);sh,sd=homogenize(sv,R);wh,wd=homogenize(w,R);ch,cd=homogenize(q*q,R)
  linear=-arb.pi()/ar(2*R*R)*sum((integrate(rr*sh,(j+1)*delta/2-3-sd,lo,hi) for (j,n),rr in rho.items() if n==1),arb(0))
  nonlinear=arb.pi()/ar(4*R*R)*sum((integrate(na[j]*eh-nb[j]*qh,(j+2)*delta/2-3-qd,lo,hi) for j in na),arb(0))
  pairing=linear+nonlinear
  b2=arb.pi()/ar(2*R**4)*sum((integrate(v*wh,(j+2)*delta/2-3-wd,lo,hi) for j,v in bgroups.items()),arb(0))
  c2=arb.pi()/ar(2*R**4)*sum((integrate(v*ch,(j+2)*delta/2-3-cd,lo,hi) for j,v in cgroups.items()),arb(0))
  assert b2>0 and c2>0
  B=b2.sqrt();C=c2.sqrt();D=A+B+C;H=Q(108)/(R*R);I=abs(pairing);radius=2*I/(D+(D*D+4*ar(H)*I).sqrt())
  vals={'pairing':pairing,'A':A,'B':B,'C':C,'D':D,'L2_radius_lower':radius}
  peerrow=next(v for v in peer['probes'] if v['R_exact']==str(R))
  checks={k:v.overlaps(arb(peerrow[k])) for k,v in vals.items()};checks['H_exact']=str(H)==peerrow['gradient_sup_upper_exact'];assert all(checks.values()),(name,R,checks)
  out['probes'].append({'R_exact':str(R),**{k:v.str(90) for k,v in vals.items()},'gradient_sup_upper_exact':str(H),'linear_pairing':linear.str(90),'nonlinear_pairing':nonlinear.str(90),'comparisons':checks})
  out['elapsed_seconds']=time.monotonic()-start;(ROOT/'verification'/f'{name}_{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
  print(name,'R',R,'radius',radius.str(24),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('names',nargs='+');p.add_argument('--radii',type=int,nargs='+',default=[8,16,32,16384]);p.add_argument('--bits',type=int,default=2048);args=p.parse_args()
 for name in args.names:run(name,args.radii,args.bits)
