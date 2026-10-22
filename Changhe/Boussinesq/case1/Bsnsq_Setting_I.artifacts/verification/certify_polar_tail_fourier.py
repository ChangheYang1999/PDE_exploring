"""Exact rational Fourier next-order PDE defect of frozen32-mode data.

No numerical angle evaluation and no fitting-code imports. The complete proof
and scope are in research/polar_tail_replay/PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,json
import numpy as np
SRC=Path('runs/polar_res3b_verification/source_coefficients.npz')
OUT=Path('candidate_audits/res3b/tail_exact');OUT.mkdir(parents=True,exist_ok=True)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
with np.load(SRC,allow_pickle=False) as z:
 assert float(z['L'])==1. and float(z['beta'])==3.
 ct=z['cT'].reshape(int(z['NT']),int(z['K']));co=z['cO'].reshape(int(z['NO']),int(z['K']))
 saved={k:float(z[k]) for k in ['gamma_T','gamma_O','mu']}
def modes(c,odd):
 a={};b={}
 for i,row in enumerate(c):
  m=2*i+1 if odd else 2*i+2
  cc=[F.from_float(float(v)) for v in row]
  a[m]=sum(cc);b[m]=-2*sum(j*j*v for j,v in enumerate(cc))
 return a,b
FF,GG=modes(ct,True);AA,BB=modes(co,False)
delta=gamma=F(1,3);kappa=F(5,3)
HH={m:v/(m*m-kappa*kappa) for m,v in AA.items()}
DT={};DO={}
def add(out,m,v):
 if not m:return
 if m<0:m,v=-m,-v
 out[m]=out.get(m,F(0))+v
for k,hk in HH.items():
 vr=-k*hk;vp=kappa*hk
 for m,fm in FF.items():
  for j in [m+k,m-k]:add(DT,j,gamma*vr*fm/2)
  for j in [k+m,k-m]:add(DT,j,vp*m*fm/2)
 for m,am in AA.items():
  for j in [m+k,m-k]:add(DO,j,-delta*vr*am/2)
  for j in [k+m,k-m]:add(DO,j,vp*m*am/2)
for m,fm in FF.items():
 for j in [m+1,m-1]:add(DO,j,-gamma*fm/2)
 for j in [1+m,1-m]:add(DO,j,m*fm/2)
for m,v in GG.items():add(DT,m,-v)
for m,v in BB.items():add(DO,m,-v)
N=max(AA);top=F(N)*AA[N]**2/(N*N-kappa*kappa)
assert max(FF)+1<2*N and AA[N]!=0 and DO[2*N]==top and top>0
assert all(m%2 for m in DT) and all(m%2==0 for m in DO)
record=lambda d:{str(k):{'exact':str(v),'approximate':float(v)} for k,v in sorted(d.items())}
largest={}
for name,d in [('DT',DT),('DO',DO)]:
 mode=max(d,key=lambda m:abs(d[m]));v=d[mode]
 largest[name]={'mode':mode,'coefficient':str(v),'coefficient_approximate':float(v),'max_absolute_angular_coefficient_lower_bound_exact':str(abs(v)/2),'max_absolute_angular_coefficient_lower_bound_approximate':float(abs(v)/2)}
report={'utc':now(),'source':str(SRC),'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exponents':'intended exact beta3,delta=gamma=1/3,kappa=5/3,L=1','saved_binary_exponents':saved,'input_endpoint_modes':{k:record(v) for k,v in [('F',FF),('A',AA),('G',GG),('B',BB)]},'DT_modes':record(DT),'DO_modes':record(DO),'top_mode_test':{'N':N,'A_N_exact':str(AA[N]),'DO_2N_exact':str(top),'DO_2N_approximate':float(top),'passed':True},'largest_coefficients':largest,'verdict':'CONFIRMED exact nonzero next-order compatibility coefficients for this stored intended-rational-exponent function; proof review pending','scope':'Exact rejection of this function, no broad A1 exclusion, no residual floor for a changing representation and no normalized Cartesian error bound'}
(OUT/'certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'utc':now(),'top_mode':report['top_mode_test'],'largest_coefficients':largest}),flush=True)
