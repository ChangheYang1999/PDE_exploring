#!/usr/bin/env python3
"""Verifier-owned nonlinear Laurent recurrence solver. Never import teammate code."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,time,hashlib,argparse,sys
import check_all_order_fraction_jets as arithmetic
from check_all_order_fraction_jets import Jet
ap=argparse.ArgumentParser();ap.add_argument('--order',type=int,default=5);ap.add_argument('--width',type=int,default=100);ap.add_argument('--tag',default='n5w100');ap.add_argument('--C',default='1');ap.add_argument('--k',default='-1');args=ap.parse_args()
assert 2<=args.order<=16 and 32<=args.width<=300
arithmetic.WIDTH=args.width
V=Path('research/324_nonlinear_formal_jet_checks/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[];records=[]
C=F(args.C);k=F(args.k);assert C*k
def ck(name,truth,detail=None):
 checks.append(dict(name=name,passed=bool(truth),detail=detail))
 if not truth:raise AssertionError((name,detail))
B=Jet({1:1,2:k,13:-C*k/260});Bd=B.der();q=(8+2*Bd)/B;h=(5+Bd)/B
ck("base_q_residue",q.at(-1)==10,str(q.at(-1)));ck("base_h_residue",h.at(-1)==6,str(h.at(-1)))
t=(q-Jet({-1:10})).primitive().exp().shift(10);Y=(h-Jet({-1:6})).primitive().exp().shift(6);jprime=t/(B*Y);ck("base_J_analytic_integrand",jprime.val()>=0,dict(valuation=jprime.val(),known_high=jprime.high));J=jprime.primitive();eta=Y*(-k**7/231-C*J)
th={1:t*C/2};om={0:eta};vel={0:B};tp={n:t**n for n in range(args.order+2)}

def vnext(j):return-(om[j]+vel[j].der().der()/F(2*j+1))/F(2*j+2)
def thermal(l):
 return sum((F(2*(l-a),2*a+1)*vel[a].der()*th[l-a]-vel[a]*th[l-a].der()for a in range(1,l)),Jet())
def vort(j,theta_next):
 return -2*(j+1)*theta_next+sum((F(2*(j-a)+1,2*a+1)*vel[a].der()*om[j-a]-vel[a]*om[j-a].der()for a in range(1,j+1)),Jet())
def particular(rhs,z):
 g=rhs/(B*z);r=g.at(-1);return z*g.primitive(),r,g.high

def exact_zero(label,j,lower=0,upper=None):
 end=j.high if upper is None else min(upper,j.high)
 if end-lower<20:raise AssertionError((label,"insufficient tested range",lower,end))
 nz=[(e,str(j.at(e)))for e in range(lower,end)if j.at(e)]
 ck(label,not nz,dict(known_high=j.high,tested_low=lower,tested_high=end,tested_count=end-lower,first_nonzero=nz[:3]))
def checkpoint(status):
 d=dict(started_utc=start,checkpoint_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,status=status,parameters=vars(args),records=records,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),arithmetic_sha256=hashlib.sha256(Path(arithmetic.__file__).read_bytes()).hexdigest(),scope='Finite exact nonlinear coefficient controls only. No convergence or global B2 profile.')
 (V/(args.tag+'.json')).write_text(json.dumps(d,indent=2)+'\n')
 return d

def coefficient_dump():
 out={}
 for label,fields in [('theta',th),('omega',om),('v',vel)]:
  out[label]={str(n):{'known_high':j.high,'coefficients':{str(e):str(c)for e,c in sorted(j.d.items())}}for n,j in fields.items()}
 (V/(args.tag+'_coefficients.json')).write_text(json.dumps(out,indent=2)+'\n')

try:
 vel[1]=vnext(0)
 th[2],r,_=particular(thermal(2),tp[2]);ck('base_T2_residue',r==0,str(r))
 om[1],r,_=particular(vort(1,th[2]),t*Y);ck('base_V1_residue',r==0,str(r));vel[2]=vnext(1)
 checkpoint('BASE_COMPLETE')
 for n in range(2,args.order+1):
  begin=time.monotonic();nextT,rT,precT=particular(thermal(n+1),tp[n+1]);_,rO,precO=particular(vort(n,nextT),tp[n]*Y)
  diagT=12*C*k/F(5*(2*n+1));off=-k**8*F(2*n+5,385*(2*n+1));diagO=-9*C*k/F(10*n)
  E=-rT/diagT;Fnew=-(rO+off*E)/diagO;Z=tp[n-1]*Y
  saved=(th[n],om[n-1],vel[n])
  for label,echange,fchange,wantT,wantO in [('Eplus',E+1,Fnew,diagT,off),('Fplus',E,Fnew+1,F(0),diagO)]:
   th[n]=saved[0]+echange*tp[n];om[n-1]=saved[1]-2*n*echange*Z*J+fchange*Z;vel[n]=vnext(n-1)
   trialT,trialRT,_=particular(thermal(n+1),tp[n+1]);_,trialRO,_=particular(vort(n,trialT),tp[n]*Y)
   ck(f'n{n}_{label}_thermal_negative',trialRT==wantT,dict(actual=str(trialRT),expected=str(wantT)))
   ck(f'n{n}_{label}_vorticity_negative',trialRO==wantO,dict(actual=str(trialRO),expected=str(wantO)))
   th[n],om[n-1],vel[n]=saved
  th[n]=th[n]+E*tp[n];om[n-1]=om[n-1]-2*n*E*Z*J+Fnew*Z;vel[n]=vnext(n-1)
  th[n+1],r,pr1=particular(thermal(n+1),tp[n+1]);ck(f'n{n}_recomputed_T_residue',r==0,str(r))
  om[n],r,pr2=particular(vort(n,th[n+1]),tp[n]*Y);ck(f'n{n}_recomputed_V_residue',r==0,str(r));vel[n+1]=vnext(n)
  # Recompute transport defects and separately check Poisson construction consistency.
  for l in range(1,n+2):
   d=B*th[l].der()-(8*l+2*l*Bd)*th[l]-thermal(l);exact_zero(f'n{n}_full_T{l}',d,lower=min(0,d.val()))
  for j in range(0,n+1):
   d=B*om[j].der()-((2*j+1)*(4+Bd)+1)*om[j]-vort(j,th[j+1]);exact_zero(f'n{n}_full_V{j}',d,lower=min(0,d.val()))
   d=F(2*j+2)*vel[j+1]+om[j]+vel[j].der().der()/F(2*j+1);exact_zero(f'n{n}_poisson_update_consistency{j}',d,lower=min(0,d.val()))
  for label,fields in [('T',th),('O',om),('v',vel)]:
   ck(f'n{n}_{label}_analytic_jets',all(j.val()>=0 for j in fields.values()))
  rec=dict(n=n,E=str(E),F=str(Fnew),fixed_residue_T=str(rT),fixed_residue_O=str(rO),residue_known_high=[precT,precO,pr1,pr2],seconds=time.monotonic()-begin,theta_leading=[min(th[n].d),str(th[n].d[min(th[n].d)])],omega_leading=[min(om[n-1].d),str(om[n-1].d[min(om[n-1].d)])])
  records.append(rec);checkpoint('RUNNING');coefficient_dump();print(json.dumps(rec),flush=True)
 d=checkpoint('COMPLETE');coefficient_dump();print(json.dumps({k:v for k,v in d.items()if k not in ['checks','records']},indent=2),flush=True)
except BaseException as e:
 checkpoint('FAILED '+type(e).__name__+': '+str(e));raise
