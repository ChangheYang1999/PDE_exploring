#!/usr/bin/env python3
"""Independent controls for packet150; manufactured sources, no NUM code."""
import argparse,json,time,hashlib,math
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sympy as S
import mpmath as mp

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
 root=Path(args.out);root.mkdir(parents=True,exist_ok=True);start=time.monotonic();rows=[]
 def check(name,ok,**data):rows.append(dict(name=name,verdict='PASS' if bool(ok) else 'FAIL',**data))
 def zero(z):return S.simplify(S.expand(z))==0
 t,r,th=S.symbols('t r th',positive=True,real=True)
 # Solve polynomial coefficient equations, then differentiate the actual
 # polar source. This includes both odd reflection mode types and logs.
 def pinverse(a,b,c,B,extra=0):
  d=S.degree(B,t)+extra;us=S.symbols('u:'+str(d+1));Q=sum(us[j]*t**j for j in range(d+1))
  equations=S.Poly(S.expand(a*Q+b*S.diff(Q,t)+c*S.diff(Q,t,2)-B),t).all_coeffs()
  if extra:equations.append(us[0])
  sol=S.solve(equations,us,dict=True)
  if len(sol)!=1:raise RuntimeError((a,b,c,B,sol))
  return S.expand(Q.subs(sol[0]))
 log_cases=[]
 for e,k in [(S.Rational(3,2),1),(S.Rational(-1,2),2),(S.Rational(5,7),3),(0,2),(1,1),(-1,1),(2,2),(-2,2),(3,3),(-3,3)]:
  B=1+2*t-3*t*t+t**3;res=(e*e-k*k==0)
  Q=pinverse(-(e*e-k*k),-2*e,-1,B,1 if res else 0)
  mode=S.cos(k*th) if k%2 else S.sin(k*th)
  psi=r**e*Q.subs(t,S.log(r))*mode
  lap=S.diff(psi,r,2)+S.diff(psi,r)/r+S.diff(psi,th,2)/r**2
  check(f'poisson_log_e{e}_k{k}',zero(-lap-r**(e-2)*B.subs(t,S.log(r))*mode) and zero(mode.subs(th,S.pi-th)+mode))
  log_cases.append(dict(e=str(e),k=k,source_polynomial=str(B),solution_polynomial=str(Q),resonant=res))
 # Euler inversion cannot encounter a resonance below the leading degree.
 for beta in [S.Rational(9,4),S.Rational(13,5),3,7]:
  s=1/S.Rational(beta);m=1-2*s
  for K,n in [(2,0),(3,0),(1,1),(2,3)]:
   q=-K*s-n;B=2-3*t+t*t;Q=pinverse(1+beta*q,beta,0,B)
   u=r**q*Q.subs(t,S.log(r))
   check(f'euler_vorticity_{beta}_{K}_{n}',q<-s and zero(beta*r*S.diff(u,r)+u-r**q*B.subs(t,S.log(r))))
   h=1-(K+1)*s-n;Q=pinverse(beta*(h-m),beta,0,B);u=r**h*Q.subs(t,S.log(r))
   check(f'euler_temperature_{beta}_{K}_{n}',h<m and zero(beta*r*S.diff(u,r)-(beta-2)*u-r**h*B.subs(t,S.log(r))))
 # Exact rational threshold schedules and all indices that can contribute
 # above the terminal scalar thresholds. They test finite termination and
 # integer shifts produced by both actual harmonic terms.
 schedules=[]
 for beta in [F(9,4),F(13,5),F(17,7),F(3),F(4),F(11,2),F(10),F(20)]:
  s=1/beta
  def inE(v):return any(v-k*s>=0 and (v-k*s).denominator==1 for k in range(1,math.floor(v/s)+1))
  mu=3*s/2;seq=[mu]
  while mu<=3:
   options=[mu+s*F(j,97) for j in range(33,65)]
   mu=next(z for z in options if z<4 and z not in [1,3] and not inE(z));seq.append(mu)
   if len(seq)>1000:raise RuntimeError('induction did not terminate')
  check(f'threshold_termination_{beta}',3<mu<4 and all(not inE(z) and z not in [1,3] for z in seq) and all(s/3<b-a<2*s/3 for a,b in zip(seq,seq[1:])))
  indices=[(K,n) for K in range(1,math.floor((mu+s)/s)+1) for n in range(4) if K*s+n<mu+s]
  good=True;pair_count=0
  for K,n in indices:
   for L,h in indices:
    q=-(K+L)*s-(n+h);q2=(1-K*s-n)+(-L*s-h-1)
    temp=1-(K+L+1)*s-(n+h)
    good &= (q==q2 and q<-s and temp<1-2*s)
    pair_count+=1
   for degree,shift in [(1,1),(-1,3)]:
    good &= ((degree-1)+(-K*s-n-1)==-K*s-(n+shift))
  check(f'nonlinear_degree_closure_{beta}',good,pair_count=pair_count)
  schedules.append(dict(beta=str(beta),weights=list(map(str,seq)),final_weight=str(mu),improvements=len(seq)-1))
 # Full-plane radial manufactures rho=x*(1+r^2)^(-(mu+1)/2).
 # Solve its radial ODE analytically, then compare the moment and gauge
 # with independent adaptive radial integrals at 70 decimal digits.
 mp.mp.dps=70;radial=[]
 for mur in [F(1,2),F(3,2),F(5,2),F(7,2),F(19,20),F(21,20),F(59,20),F(61,20)]:
  mu=mp.mpf(mur.numerator)/mur.denominator;a=(mu+1)/2
  def I(r):return ((1+r*r)**(2-a)-1)/(2*(2-a))-((1+r*r)**(1-a)-1)/(2*(1-a))
  def J(r):return ((1+r*r)**(1-a)-1)/(2*(1-a))
  def h(r):return -J(r)/2+I(r)/(2*r*r) if r else mp.mpf(0)
  C=-1/(2*(mu-1)) if mu>1 else mp.mpf(0)
  D=1/((mu-1)*(mu-3)) if mu>3 else mp.mpf(0)
  errs=[]
  for rr in [mp.mpf('0.3'),mp.mpf(1),mp.mpf(7)]:
   iq=mp.quad(lambda z:z**3*(1+z*z)**(-a),[0,rr]);jq=mp.quad(lambda z:z*(1+z*z)**(-a),[0,rr])
   err=max(abs(I(rr)-iq),abs(J(rr)-jq),abs(mp.diff(h,rr,2)+3*mp.diff(h,rr)/rr+(1+rr*rr)**(-a)))
   errs.append(float(err))
  if mu>1:
   # Beta integral equals the full-plane center gauge coefficient;
   # the adaptive integral is compactified and split near its endpoint.
   gamma_C=-mp.beta(1,a-1)/4
   check(f'radial_center_constant_{mur}',abs(C-gamma_C)<mp.mpf('1e-60'))
  if mu>3:
   gamma_D=mp.beta(2,a-2)/4
   check(f'radial_dipole_constant_{mur}',abs(D-gamma_D)<mp.mpf('1e-60'))
  ratios=[]
  for rr in [mp.mpf(10)**k for k in [2,4,8,12]]:
   # Psi at angle0 is r*h. The ratios test the lemma's exact remainder
   # power after removing the harmonics available at this weight.
   rem=rr*(h(rr)-C-D/(rr*rr));ratios.append(float(rem/rr**(2-mu)))
  check(f'radial_inverse_{mur}',max(errs)<1e-55,max_absolute_ode_and_integral_error=max(errs))
  check(f'radial_remainder_power_{mur}',max(map(abs,ratios))<1e5,scaled_remainders=ratios)
  radial.append(dict(mu=str(mur),C=str(C),D=str(D),scaled_remainders=ratios,max_absolute_ode_and_integral_error=max(errs)))
 result=dict(status='PASS' if all(q['verdict']=='PASS' for q in rows) else 'FAIL',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,checks=rows,log_cases=log_cases,schedules=schedules,radial_manufactures=radial,limitations=['Computational controls supplement the standalone informal proof; they do not prove its general function-space estimates.','Radial vorticity manufactures do not solve both stationary B2 equations or meet the required nonzero temperature normalization.','Finite rational threshold schedules test representative parameters only; the proof treats every beta>2.'])
 (root/'results.json').write_text(json.dumps(result,indent=2)+'\n')
 inputs=[Path(__file__),Path('research/150_finite_exterior_expansion/PROOF.md')]
 (root/'build_inputs.json').write_text(json.dumps({'inputs':[{'path':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs]},indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['checks','log_cases','schedules','radial_manufactures']},indent=2))
 print('checks',len(rows),'failed',[q['name'] for q in rows if q['verdict']=='FAIL'])
 if result['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
