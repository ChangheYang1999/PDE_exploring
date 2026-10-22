from pathlib import Path
from fractions import Fraction as F
import sys,os,json
sys.dont_write_bytecode=True
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import numpy as np
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_scaling_rank_one';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='99cbccd132ab68569fdfdcd438b36fca0ceaa82740f3ff822c84ac13121813a1'
parent='research/weak_axis_compact_higher_orders/evidence/verdict.json';pv=p.load(R/parent);pins=dict(pv['files']);p.pin(pins,parent,'391cd45cbabe7d3540327fe38a9ecb079ff3d80f982f21749b79f55200ae2710');p.rehash(pins)
raw=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(raw)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(raw,allow_pickle=False) as z:
 k,bi,bo=[F.from_float(float(z[n].item())) for n in ['k','bi','bo']];C=[F.from_float(float(z['Aout'][m,0])) for m in range(260)];shape=list(z['Aout'].shape)
assert shape==[260,10] and 0<k<F(1,2) and C[1]!=0 and bi>50 and bo>120
actual={'k':k,'bi':bi,'bo':bo,'leading_cosine_m1':C[1],'Euler_leading_cosine_m1':k*C[1],'membership_lower':1+k,'axis_limit':F(5,2),'strain_limit':F(2),'s':F(153,50),'center_margin_at_upper':6-F(5,2)-F(153,50),'weight3over2_far_margin':F(3,2)-1-k,'weight3over2_residual_margin':F(3,2)-2*k,'outer_log_gap':bo+k-3,'nonlocal_to_rank_gap':F(4)}
pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)];exponents=[k-3-j*(1-k)-2*l for j,l in pairs];gaps=[k-3-e for e in exponents]
assert gaps[0]==0 and all(t>0 for t in gaps[1:]) and all(actual[n]>0 for n in ['center_margin_at_upper','weight3over2_far_margin','weight3over2_residual_margin','outer_log_gap'])
x,y,sigma,beta,b,q,kk=S.symbols('x y sigma beta b q k');aa=S.Function('a')(x,y);v1=S.Function('v1')(x,y);v2=S.Function('v2')(x,y);Q=S.Function('Q')(x,y)
rho=x*x*y*aa;G=x*S.diff(rho,x)+y*S.diff(rho,y);U1=-sigma*x+x*v1;U2=sigma*y+y*v2;B=sigma*(-2*x*S.diff(aa,x)+4*y*S.diff(aa,y))/3+v1*(2*aa+x*S.diff(aa,x))+v2*(aa+y*S.diff(aa,y))
checks={'Euler_density_factor':S.expand(G-x*x*y*(3*aa+x*S.diff(aa,x)+y*S.diff(aa,y))),'strain_cubic_cancellation':S.expand(U1*S.diff(rho,x)+U2*S.diff(rho,y)+sigma*G/3-x*x*y*B)}
for pp in range(5):
 for qq in range(5-pp):
  f=S.diff(x*x*Q,y,qq);Cq=S.diff(Q,y,qq)
  for _ in range(pp):f=x*S.diff(f,x)+beta*f;Cq=x*S.diff(Cq,x)+(beta+2)*Cq
  checks[f'factor_p{pp}_q{qq}']=S.expand(f-x*x*Cq)
checks['center_shell']=S.expand((5-2*b)+1+2*(3-q)-2*(6-b-q));checks['far_shell']=S.expand((5-2*b)+1+2*(kk-2-q)-2*(kk+1-b-q));checks['far_divergence_endpoint']=S.expand((2*kk-2*b+1)+1-2*(1+kk-b));checks['axis_divergence_endpoint']=S.expand((4-2*b)+1-2*(S.Rational(5,2)-b));checks['far_rank_vs_nonlocal']=S.expand(kk-(kk-4)-4);assert all(t==0 for t in checks.values())
out={'start_utc':start,'utc':p.now(),'status':'PASS_EXACT_NONZERO_LEADING_COEFFICIENT_AND_SCALING_IDENTITIES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'Aout_shape':shape,'actual':{n:str(v) for n,v in actual.items()},'all_260_leading_cosines':list(map(str,C)),'outer_exponents':list(map(str,exponents)),'exterior_gaps':list(map(str,gaps)),'symbolic_identities':{n:str(v) for n,v in checks.items()},'normalization_support':'Only m=0 changes; Aout[1,0] is unchanged. This property is inherited from the canonical normalization proof.','scope':'Exact dyadic coefficient and finite algebra; no new quadrature, interval norm enclosure, angular sampling, matching computation, or Sobolev theorem from finite checks.'};p.write(E/'check.json',out);print(json.dumps({n:out[n] for n in ['start_utc','utc','status','parent_pin_count','actual','symbolic_identities']}))
