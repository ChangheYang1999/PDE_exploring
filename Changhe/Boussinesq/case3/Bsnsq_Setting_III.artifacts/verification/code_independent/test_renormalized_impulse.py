#!/usr/bin/env python3
"""Independent exact controls for research149; no teammate code is imported."""
import argparse,json,math,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import sympy as S

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
 out=Path(args.out);out.mkdir(parents=True,exist_ok=True);t0=time.monotonic();checks=[]
 def check(name,ok,**details):
  checks.append(dict(name=name,verdict='PASS' if bool(ok) else 'FAIL',**details))
 def zero(z):return S.simplify(S.expand_trig(z))==0
 # Finite rational enumeration. Every collision is detectable with K<=3 beta
 # and total n<=2; higher positive indices cannot make any relevant zero.
 betas=sorted({Fraction(M,d) for d in range(1,9) for M in range(1,65) if 2<Fraction(M,d)<=8})
 coll=[]
 for b in betas:
  s=1/b; Kmax=math.floor(3*b)
  es={2-k*s-n for k in range(1,Kmax+1) for n in range(3)}
  hs={1-k*s-n for k in range(2,Kmax+1) for n in range(3)}
  harm={Fraction(1),Fraction(-1),Fraction(-2),Fraction(-3)}
  mainzero=(-1 in es or -2 in hs or any(1-e in es for e in es) or any(-h in es for h in hs))
  gaugezero=(0 in es or -1 in hs)
  negharmzero=any(1-e in es or -e in hs for e in harm if e<0)
  pairzero=any(1-e in harm for e in harm)
  check(f'collision_beta_{b}',mainzero==(b.denominator<=3) and not negharmzero and not pairzero and (not gaugezero or b.denominator<=2))
  coll.append(dict(beta=str(b),main_collision=mainzero,gauge_collision=gaugezero))
 # Polar identities from actual derivatives, including logarithms.
 r,th,t,e=S.symbols('r th t e',positive=True,real=True)
 Q=1+t*S.cos(th)+t**2*S.sin(2*th)+t**3*S.cos(3*th)
 psi=r**e*Q.subs(t,S.log(r))
 lap=S.diff(psi,r,2)+S.diff(psi,r)/r+S.diff(psi,th,2)/r**2
 expected=r**(e-2)*(e**2*Q+2*e*S.diff(Q,t)+S.diff(Q,t,2)+S.diff(Q,th,2)).subs(t,S.log(r))
 check('polar_log_laplacian',zero(lap-expected))
 for degree in [-3,-2,-1,1,2,3]:
  for j in [1,2,3]:
   mode=S.cos(abs(degree)*th)
   eq=(degree**2+0)*t**j*mode+2*degree*S.diff(t**j*mode,t)+S.diff(t**j*mode,t,2)+S.diff(t**j*mode,th,2)
   coeff=S.expand(eq).coeff(t,j-1)
   check(f'nonzero_harmonic_log_{degree}_{j}',zero(coeff-2*degree*j*mode) and 2*degree*j!=0)
 D,C,s=S.symbols('D C s',real=True)
 dip=D*S.cos(th)/r
 green=(dip*S.cos(th)-r*S.cos(th)*S.diff(dip,r))*r
 check('dipole_green_sign',zero(S.integrate(green,(th,0,2*S.pi))-2*S.pi*D))
 # Exact tail from radial Poisson inversion, then vorticity transport.
 c=-1/((3-s)*(1-s));psit=c*r**(2-s)*S.cos(th)+C*r*S.cos(th)+D/r*S.cos(th)
 om=r**(-s)*S.cos(th)
 lap=S.diff(psit,r,2)+S.diff(psit,r)/r+S.diff(psit,th,2)/r**2
 check('radial_tail_inverse',zero(lap+om))
 adv=(S.diff(psit,r)*S.diff(om,th)-S.diff(psit,th)*S.diff(om,r))/r
 full=S.cos(th)*S.sin(th)*(2*r**(-2*s)/((3-s)*(1-s))-(s+1)*C*r**(-s-1)+(1-s)*D*r**(-s-3))
 check('full_radial_tail_residual',zero(adv-full))
 # Compact vorticity manufacture with exact polynomial interior and harmonic
 # exterior. It has C^7 vorticity, sufficient for these classical identities,
 # but is deliberately not labelled a C-infinity B2 profile.
 x,y,b=S.symbols('x y beta',real=True)
 hi=-sum((-1)**k*S.binomial(8,k)*r**(2*k+2)/((2*k+4)*(2*k+2)) for k in range(9))
 I1=S.integrate(r**3*(1-r**2)**8,(r,0,1));Di=I1/2;Ci=hi.subs(r,1)-Di;ho=Ci+Di/r**2
 check('compact_dipole_value',I1==S.Rational(1,180) and Di==S.Rational(1,360))
 for j in range(10):check(f'compact_stream_join_derivative_{j}',zero(S.diff(hi-ho,r,j).subs(r,1)))
 check('compact_stream_not_C10',not zero(S.diff(hi-ho,r,10).subs(r,1)))
 hic=sum(S.expand(hi).coeff(r,2*k)*(x*x+y*y)**k for k in range(1,10))
 psii=S.expand(x*hic);omi=x*(1-x*x-y*y)**8;v1=-S.diff(psii,y);v2=S.diff(psii,x)
 check('compact_cartesian_inverse',zero(-S.diff(psii,x,2)-S.diff(psii,y,2)-omi))
 check('compact_center_gauge',v1.subs({x:0,y:0})==0 and v2.subs({x:0,y:0})==0)
 residual=S.expand((b*x+v1)*S.diff(omi,x)+(b*y+v2)*S.diff(omi,y)+omi)
 def disk(poly):
  ans=0
  for (i,j),val in S.Poly(poly,x,y).terms():
   if i%2 or j%2:continue
   a,c=i//2,j//2
   moment=S.factorial(2*a)*S.factorial(2*c)*S.pi/(4**(a+c)*S.factorial(a)*S.factorial(c)*S.factorial(a+c+1))
   ans+=val*moment
  return S.simplify(ans)
 moment=disk(x*residual)
 check('compact_residual_impulse_all_beta',zero(moment-2*S.pi*(1-3*b)*Di),exact_moment=str(moment))
 check('compact_other_affine_moments',zero(disk(residual)) and zero(disk(y*residual)))
 # Same residual's boundary calculation for any exterior circle; build the
 # vector stress and normals directly in polar coordinates.
 pse=r*ho*S.cos(th);px=S.cos(th)*S.diff(pse,r)-S.sin(th)*S.diff(pse,th)/r
 py=S.sin(th)*S.diff(pse,r)+S.cos(th)*S.diff(pse,th)/r
 exterior_boundary=(-px*py*S.cos(th)-(py**2-px**2)*S.sin(th)/2+(1-3*b)*(pse*S.cos(th)-r*S.cos(th)*S.diff(pse,r)))*r
 boundary=S.integrate(S.expand_trig(S.expand(exterior_boundary)),(th,0,2*S.pi))
 check('compact_complete_boundary',zero(boundary-moment))
 # Exact C8 positive radial f, smoothly matched through eight derivatives.
 # Taylor binomial truncation lies strictly below the singular tail on (0,1),
 # so its I1 can be raised to the zero-D value by a positive interior bump.
 u=S.symbols('u',positive=True);sign_examples=[]
 for br in [S.Rational(9,4),S.Rational(13,5),S.Rational(17,7)]:
  sr=1/br;ar=(sr+1)/2
  fbase=sum(S.rf(ar,k)/S.factorial(k)*(1-u)**k for k in range(9));bump=(1-u)**9
  ibase=S.integrate(u*fbase/2,(u,0,1));jb=S.integrate(u*bump/2,(u,0,1))
  az=S.simplify((1/(3-sr)-ibase)/jb)
  check(f'positive_tail_amplitude_{br}',az>0 and jb==S.Rational(1,220))
  for mult in [0,1,2]:
   ff=fbase+mult*az*bump;ival=S.simplify(ibase+mult*az*jb);dval=S.simplify((ival-1/(3-sr))/2)
   joins=all(zero(S.diff(ff-u**(-ar),u,j).subs(u,1)) for j in range(9))
   check(f'positive_tail_D_{br}_{mult}',joins and (dval<0 if mult==0 else dval==0 if mult==1 else dval>0),D=str(dval))
   sign_examples.append(dict(beta=str(br),amplitude_multiple=mult,D=str(dval),D_decimal=float(dval),I1=str(ival),regularity='C8 at r=1; smooth near origin; control only'))
 # Global thermal transport cannot be omitted: compact polynomial Theta.
 temp=(1-x*x-y*y)**8
 check('thermal_hypothesis_countercontrol',zero(disk(x*(-S.diff(temp,x)))-disk(temp)) and disk(temp)>0,temperature_integral=str(disk(temp)))
 result=dict(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,status='PASS' if all(q['verdict']=='PASS' for q in checks) else 'FAIL',checks=checks,rational_collision_cases=coll,positive_examples=sign_examples,limits=['Finite algebraic and finite-regularity manufactures supplement the informal proof.','No computation supplies the asymptotic expansion for a B2 profile.','Theta=0 compact-vorticity manufactures do not meet nonzero thermal normalization.'])
 (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
 (out/'build_inputs.json').write_text(json.dumps({'inputs':[{'path':str(Path(__file__).resolve()),'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},{'path':str(Path('research/149_renormalized_impulse/PROOF.md').resolve()),'sha256':hashlib.sha256(Path('research/149_renormalized_impulse/PROOF.md').read_bytes()).hexdigest()}]},indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['checks','rational_collision_cases','positive_examples']},indent=2));print('checks',len(checks),'failed',[q['name'] for q in checks if q['verdict']=='FAIL'])
 if result['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
