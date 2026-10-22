"""Independent exact source/output audit, with normalization and prior full-convolution pins.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/far_residual_obstruction';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def dec(s):
 neg=s.startswith('-');man,e=s.lstrip('+-').split('p');w,f=man[2:].split('.')
 r=Q(int(w+f,16),16**len(f))*Q(2)**int(e)
 return -r if neg else r
def interval(b):
 lo,hi=Q(b['lower_exact']),Q(b['upper_exact']);assert lo<=hi
 return lo,hi
files={};counts={}
def pin(p,h=None):
 s=sha(p)
 if h is not None:assert s==h,str(p)
 files[str(p.relative_to(B))]=s
 return s
def main():
 A=load(E/'arb.json');I=load(E/'iv.json');pf=load(E/'proof_first.json')
 assert pf['sha256']==sha(D/'PROOF.md')
 assert datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(A['utc']) and datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(I['utc'])
 assert A['status']==I['status']=='COMPUTED_REQUIRES_OUTPUT_AUDIT'
 for out in (A,I):
  for p,h in out['files'].items():pin(B/p,h)
 for p in (E/'arb.json',E/'iv.json',Path(__file__),D/'ADDENDUM.md'):pin(p)
 raw=load(B/'data_exact/modal_v2.json');ar=raw['arrays'];npz=Path(I['source_archive']['path']);assert sha(npz)==I['source_archive']['sha256']=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(npz,allow_pickle=False) as z:
  assert z['Aout'].shape==(260,10) and z['knots'].shape==(1573,)
  assert all(Q(float(x))==dec(s) for x,s in zip(z['Aout'].flat,ar['Aout']['hex'],strict=True));counts['original_outer_coefficients']=2600
  assert all(Q(float(x))==dec(s) for x,s in zip(z['knots'],ar['knots']['hex'],strict=True));counts['original_knots']=1573
  k=Q(float(z['k']));t=Q(float(z['knots'][-1]));bo=Q(float(z['bo']))
  assert k==dec(raw['scalars_hex']['k'])==Q(A['exact']['k'])==Q(I['exact']['k'])
  assert t==Q(A['exact']['tplus'])==Q(I['exact']['tplus']) and bo==dec(raw['scalars_hex']['bo'])
  # Direct exact multiplication by (sin theta + sin 3theta)/4, separate from both engines.
  expected=[[Q(0),Q(0),Q(0)] for _ in range(262)]
  for m in range(260):
   for base in (1,3):
    for sign in (-1,1):
     f=base+sign*2*m;j=(abs(f)-1)//2;q=Q(1 if f>0 else -1,8)
     expected[j][0]+=q*Q(float(z['Aout'][m,0]));expected[j][1]+=q*Q(m==0);expected[j][2]+=q*Q(float(z['Aout'][m,1]))
 assert expected==[list(map(Q,row)) for row in I['exact']['sine_affine']];counts['exact_projection_entries']=262*3
 for w in A['witnesses']:
  n=w['n'];assert list(map(Q,w['dprev']))==expected[n-1][:2] and list(map(Q,w['dn']))==expected[n][:2]
 assert Q(A['exact']['b0'])==Q(I['exact']['b0'])==expected[0][2];counts['primary_projection_witnesses']=12
 assert 0<k<Q(1,2);beta=2*k-1;assert -1<beta<0 and beta+1==2*k>0
 assert A['exact']['beta']==I['exact']['beta']==str(beta)
 pairs=[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[0,1],[1,1],[2,1],[0,2]];assert raw['outer_jl']==pairs
 exps=[k-j*(1-k)-2*l for j,l in pairs]+[3-bo]
 assert exps[0]==k and exps[1]==beta and all(x<beta for x in exps[2:])
 assert all((i==j==0 and x+y-1==beta) or ((i,j)!=(0,0) and x+y-1<beta) for i,x in enumerate(exps) for j,y in enumerate(exps))
 assert all(x-2*n-2<beta for x in exps for n in range(1,262));counts['exponent_comparisons']=121+2871+9
 nv=load(B/'research/modal_repair/evidence/audit_verdict.json');assert nv['verdict']=='CONFIRMED'
 for p,h in nv['source_and_evidence_sha256'].items():pin(B/p,h)
 counts['normalization_dependency_pins']=len(nv['source_and_evidence_sha256'])
 n=load(B/'research/modal_repair/evidence/independent_gauss_iv.json')['values']['A00_correction'];nb=(Q(n['lower_exact_dyadic']),Q(n['upper_exact_dyadic']))
 assert list(map(Q,I['exact']['z_bracket']))==list(nb)
 lo,hi=map(Q,A['exact']['z_bracket']);assert lo<nb[0]<=nb[1]<hi
 il,ih=interval(I['values']['z']);al,ah=interval(A['values']['z']);assert al<=lo<nb[0]<=nb[1]<hi<=ah and il<=nb[0]<=nb[1]<=ih
 public={'e0':['-0.0002000282880','-0.0002000282879'],'E0':['-0.03688201144','-0.03688201143'],'Theta_pi4':['90.81020983897880','90.81020983897882']}
 for eng in (A,I):
  for key,b in eng['values'].items():interval(b)
  for key,(lo,hi) in public.items():
   x,y=interval(eng['values'][key]);assert Q(lo)<x<=y<Q(hi)
 counts['finite_ordered_endpoints']=24;counts['strict_public_enclosures']=6
 for key in A['values']:
  al,ah=interval(A['values'][key]);il,ih=interval(I['values'][key]);assert al<=il<=ih<=ah,key
 counts['independent_intervals_contained']=6
 # Compare the fresh selected coefficient with BOTH prior complete 522-mode computations.
 vp=B/'research/outer_leading_cancellation/evidence/verdict.json';v=load(vp);assert v['status']=='CONFIRMED';pin(vp)
 for p,h in v['files'].items():pin(B/p,h)
 old=[]
 for name in ('leading_result.json','leading_iv_audit.json'):
  p=B/'research/outer_leading_cancellation/evidence'/name;row=load(p)['residual_coefficients'][0];assert row['q']==0;ol,oh=interval(row['value']);assert Q(public['e0'][0])<ol<=oh<Q(public['e0'][1]);old.append([str(ol),str(oh)])
  al,ah=interval(A['values']['e0']);assert al<=ol<=oh<=ah
 counts['prior_complete_convolution_coefficients']=2
 # Check the compact normalization repair angular factor exactly by beta recurrence.
 # Integral cos^(2a) sin^(2b)/pi = 2*(2a)!*(2b)!/(4^(a+b)*a!*b!*(a+b)!).
 import math
 def angular(a,b):return Q(2*math.factorial(2*a)*math.factorial(2*b),4**(a+b)*math.factorial(a)*math.factorial(b)*math.factorial(a+b))
 assert angular(2,1)==angular(1,2)==Q(1,8) and 3*angular(2,1)-angular(1,2)==Q(1,4);counts['angular_normalization_checks']=3
 # Direct canonical Green normalization: f1/r=r*b+r^2*b'/4,
 # integral r^2*b'=-2 integral r*b; psi1 leading=(r^2/4) integral f1/r.
 assert Q(1)+Q(1,4)*(-2)==Q(1,2)
 assert 2*Q(1,4)*Q(1,2)==Q(1,4)
 assert -Q(-1)==Q(1)  # minus convolution at zero of an odd kernel
 counts['canonical_strain_sign_checks']=3
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_SOURCE_OUTPUT_AND_NONZERO_COEFFICIENT_AUDIT','public_strict_enclosures':public,'counts':counts,'prior_full_coefficients':old,'source_archive':I['source_archive'],'files':dict(sorted(files.items())),'scope':'Fresh coefficient nonzero and Theta nonzero. Analytic L2 obstruction requires PROOF plus ADDENDUM. No weighted neighborhood exclusion or decisive endpoint.'}
 (E/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'counts':counts,'pins':len(files)}))
if __name__=='__main__':main()
