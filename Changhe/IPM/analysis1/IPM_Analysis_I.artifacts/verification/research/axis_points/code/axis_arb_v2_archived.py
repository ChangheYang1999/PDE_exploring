"""Direct paired-kernel axis velocity with explicit singular-strip and Cauchy errors."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import sys,argparse,json,math,hashlib,time,resource
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,arb_mat,ctx
BASE=Path(__file__).resolve().parents[3];sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from strain_arb import Data,aa,jsball,cn,emit,utc

def beta(d,q,x):
 s=1-(1-q)**d.b
 return d.L*d.L*s/(d.L*d.L*s+x*x*(1-s))
def beta_complex(d,q,x):
 s=1-(1-q).pow(acb(d.b),analytic=True)
 den=d.L*d.L*s+x*x*(1-s)
 if not den.abs_lower()>0:return None
 return d.L*d.L*s/den

def radial_bound(d,x,a,b,pol):
 mid,rows=pol;h=aa((b-a)/2)
 q=acb(arb(mid,(3*h).upper()),arb(0,(2*h).upper()))
 v=1-q
 if not v.real>0:return None
 s=1-v.pow(acb(d.b),analytic=True)
 if not s.real>0 or not (s+d.r0*d.r0*(1-s)).abs_lower()>0:return None
 be=beta_complex(d,q,x)
 if be is None:return None
 delta2=((1-2*be)**2).real.lower()
 if not delta2>0:return None
 lower=arb(1).union(delta2).lower()
 lm=d.radial_bound(a,b,pol)
 if lm is None or not lm<12:return None
 ba=be.abs_upper();ker=ba**2*(1+4*ba**2)/lower**2
 return lm,ker,delta2

def angular_bound(d,a,b,delta0):
 mid=aa((a+b)/2)*arb.pi()/2;h=aa((b-a)/2)*arb.pi()/2
 tr=arb(mid,(2*h).upper());z=acb(tr,arb(0,h.upper()))
 co,si=z.cos(),z.sin()
 if not co.real>0:return None
 sinlower=(tr.sin()**2).lower()
 if not sinlower>0:sinlower=arb(0)
 lo=(delta0**2+(1-delta0**2)*sinlower-h.sinh()**2).lower()
 if not lo>0:return None
 bd=d.angle_bound(a,b)
 if bd is None or not bd[0]<12:return None
 cm,sm=co.abs_upper(),si.abs_upper()
 ker=cm**2*sm**2*(1+4*cm**2)/lo**2
 return bd[0],ker,lo

def prepare(d,x,args):
 qstar=1-(1+(x/d.L)**2)**((d.k-1)/2)
 center=F.from_float(float(qstar));hole=F(1,2**args.hole_bits)
 ha,hb=center-hole,center+hole
 assert aa(ha)<qstar and qstar<aa(hb)
 ba,bb=beta(d,aa(ha),x),beta(d,aa(hb),x)
 assert ba<arb(1)/2 and bb>arb(1)/2
 delta0=(1-2*ba).union(2*bb-1).lower()
 assert delta0>0
 cap=F(1,2**60);tcap=F(1,2**20)
 cuts=sorted(set([cap,1-cap,ha,hb]+[v for v in d.t if cap<v<1-cap]))
 stack=[(a,b,0) for a,b in zip(cuts[:-1],cuts[1:]) if not ha<=(a+b)/2<=hb];stack.reverse();rad=[]
 while stack:
  a,b,depth=stack.pop();pol=d.poly(a,b);bd=radial_bound(d,x,a,b,pol)
  if bd is None:
   assert depth<100,('radial depth',a,b)
   m=(a+b)/2;stack.extend([(m,b,depth+1),(a,m,depth+1)])
  else:rad.append((a,b,pol,*bd))
  if len(rad)%100==0 and rad:emit(stage='radial_prepare',x=str(x),accepted=len(rad),pending=len(stack))
 angular=[];stack=[(F(i,16),min(F(i+1,16),1-tcap),0) for i in range(16)];stack.reverse()
 while stack:
  a,b,depth=stack.pop();bd=angular_bound(d,a,b,delta0)
  if bd is None or not aa(b-a)*arb.pi()/2*bd[0].exp()*bd[1]*cn(args.nt)*arb(2)**(2*args.nt)<arb(args.angle_cell_tol):
   assert depth<100,('angle depth',a,b)
   m=(a+b)/2;stack.extend([(m,b,depth+1),(a,m,depth+1)])
  else:angular.append((a,b,*bd))
 Er=sum((aa(b-a)*lm.exp()*ker*cn(args.nq)*arb.pi()/16 for a,b,_,lm,ker,_ in rad),arb(0))
 Et=sum((aa(b-a)*arb.pi()/2*lm.exp()*ker*cn(args.nt)*arb(2)**(2*args.nt) for a,b,lm,ker,_ in angular),arb(0))
 Eh=aa(hb-ha)*3*arb.pi()/16*d.global_M;Ec=2*aa(cap)*3*arb.pi()/16*d.global_M
 dd=aa(tcap)*arb.pi()/2
 Ea=dd**3/3*(1+4*dd**2)/(1-dd**2)**2*(d.csum+d.ct*dd**(d.p-2)).exp()
 errors={'radial_gauss':Er,'angular_gauss':Et,'singular_strip':Eh,'radial_caps':Ec,'angular_cap':Ea}
 part={'qstar':jsball(qstar),'removed_q_strip':[str(ha),str(hb)],'min_abs_1_minus_2beta':jsball(delta0),'cap_q':str(cap),'cap_theta_normalized':str(tcap),'q':[[str(a),str(b)] for a,b,*_ in rad],'theta_over_pi_half':[[str(a),str(b)] for a,b,*_ in angular],'errors_before_prefactor':{k:jsball(v) for k,v in errors.items()},'error_in_velocity':jsball(x*d.pref*sum(errors.values(),arb(0)))}
 return rad,angular,part,sum(errors.values(),arb(0))

def main(args):
 ctx.prec=args.bits;ctx.threads=1;ctx.cap=8
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 start=time.monotonic();d=Data();x=aa(F(args.x));tag=args.tag
 assert x>0 and d.ct>=0 and d.p>2 and d.k>0 and d.k<1 and d.L>0
 source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 dependency_sha=hashlib.sha256((BASE/'research/canonical_inverse/code/strain_arb.py').read_bytes()).hexdigest()
 assert dependency_sha=='923db118bcc6f95039cba684100b8cd7ec39ae39f18e05343290b6e3ab494f0e'
 emit(stage='start',x=args.x,settings=vars(args),input_sha256=d.sha)
 rad,ang,part,error=prepare(d,x,args)
 evidence=BASE/'research/axis_points/evidence'
 part.update(utc=utc(),settings=vars(args),input_sha256=d.sha,script_sha256=source_sha,dependency_sha256=dependency_sha,radial_complex_rectangle={'real_radius_in_cell_half_lengths':3,'imag_radius_in_cell_half_lengths':2},angular_complex_rectangle={'real_radius_in_cell_half_lengths':2,'imag_radius_in_cell_half_lengths':1})
 pp=evidence/(tag+'_partition.json');pp.write_text(json.dumps(part,indent=2)+'\n')
 emit(stage='prepared',x=args.x,radial_cells=len(rad),angular_cells=len(ang),errors=part['errors_before_prefactor'],velocity_error=part['error_in_velocity'],seconds=time.monotonic()-start)
 if args.prepare_only:return
 qnw=[arb.legendre_p_root(args.nq,k,weight=True) for k in range(args.nq)]
 tnw=[arb.legendre_p_root(args.nt,k,weight=True) for k in range(args.nt)]
 assert all(w>0 for _,w in qnw+tnw)
 assert sum((w for _,w in qnw),arb(0)).contains(2) and sum((w for _,w in tnw),arb(0)).contains(2)
 thetas=[];weights=[];co2=[];si2=[]
 for a,b,*_ in ang:
  mid=aa((a+b)/2)*arb.pi()/2;h=aa((b-a)/2)*arb.pi()/2
  for node,w in tnw:
   th=mid+h*node;thetas.append(th);weights.append(h*w);co2.append(th.cos()**2);si2.append(th.sin()**2)
 angles=arb_mat([[(2*m*th).cos() for th in thetas] for m in range(d.nm)]+[[th.cos()**(d.p-2)*th.sin()**2 for th in thetas]])
 weighted=[w*c*s for w,c,s in zip(weights,co2,si2)]
 total=arb(0)
 for i,(a,b,(mid,rows),*_) in enumerate(rad):
  half=aa((b-a)/2);nodes=[mid+half*node for node,_ in qnw]
  radial=arb_mat([d.radial(q,mid,rows) for q in nodes]);exponents=radial*angles
  for j,(q,(_,w)) in enumerate(zip(nodes,qnw)):
   be=beta(d,q,x);b2=be*be;other=4*be*(1-be)
   acc=sum((exponents[j,k].exp()*weighted[k]*b2*(1-4*b2*co2[k])/(1-other*co2[k])**2 for k in range(len(thetas))),arb(0))
   total+=half*w*acc
  if (i+1)%10==0 or i+1==len(rad):emit(stage='quadrature',x=args.x,done=i+1,total=len(rad),sum=jsball(total),seconds=time.monotonic()-start)
 assert total.is_finite() and error.is_finite()
 velocity=x*d.pref*(total+arb(0,error.upper()))
 # Decimal outward endpoints of the audited strain ball, kept wider than its exact certificate.
 strain=arb('15.72608782162331').union(arb('15.72608782162370'))
 scalar_path=BASE/'research/canonical_inverse/evidence/strain_arb_20_32_result.json'
 scalar_sha=hashlib.sha256(scalar_path.read_bytes()).hexdigest()
 assert scalar_sha=='16135e23513f905fb835c57df9dbd424f5efe0b7d5fe76831bb18221520723db'
 assert strain.contains(arb(json.loads(scalar_path.read_text())['strain']['ball']))
 drift=x*(1+strain)/3+velocity
 out={'utc':utc(),'status':'POINT_ENCLOSURE_REQUIRES_INDEPENDENT_AUDIT','settings':vars(args),'input_sha256':d.sha,'script_sha256':source_sha,'dependency_sha256':dependency_sha,'scalar_certificate_sha256':scalar_sha,'partition_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),'quadrature_sum':jsball(total),'unscaled_error':jsball(error),'velocity_U1':jsball(velocity),'canonical_drift_w':jsball(drift),'seconds':time.monotonic()-start,'scope':'Point enclosure only, no profile existence or inverse theorem.'}
 (evidence/(tag+'_result.json')).write_text(json.dumps(out,indent=2)+'\n');emit(stage='result',**out)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--x',required=True);ap.add_argument('--tag',required=True);ap.add_argument('--bits',type=int,default=160);ap.add_argument('--nq',type=int,default=28);ap.add_argument('--nt',type=int,default=32);ap.add_argument('--hole-bits',type=int,default=24);ap.add_argument('--angle-cell-tol',default='1e-10');ap.add_argument('--prepare-only',action='store_true');main(ap.parse_args())
