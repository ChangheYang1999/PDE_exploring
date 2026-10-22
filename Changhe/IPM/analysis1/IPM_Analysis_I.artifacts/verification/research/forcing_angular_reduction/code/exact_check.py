"""Independent exact rational midpoint/radius expansion; iv120 factor check."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,time,sys
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];iv.dps=120;start=time.monotonic();pins={}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p):pins[str(p.relative_to(B))]=sha(p)
def ff(x):return F.from_float(float(x))
def vf(x):return iv.mpf(x.numerator)/x.denominator
reg=json.loads((D/'evidence/regeneration.json').read_text());assert reg['status']=='REGENERATED_INPUTS_REQUIRING_TWO_ENGINE_AUDIT'
pin(D/'evidence/regeneration.json');factor=D/'evidence/factors.npz';pin(factor);assert pins[str(factor.relative_to(B))]==reg['pins'][str(factor.relative_to(B))]
with np.load(factor,allow_pickle=False) as z:
 w=ff(z['w']);fac=[[ff(t) for t in row] for row in z['remfac']];nu=list(map(ff,z['nu']))
assert nu==list(map(F,range(1,1046,2))) and len(fac)==5 and all(len(row)==523 for row in fac)
assert w>0 and all(t>0 for row in fac for t in row)
factor_margins=[];factor_iv=0
for j in range(5):
 for n in range(523):
  rhs=F((2*n+1)**(j+9),362880)*w**9
  slack=fac[j][n]-rhs;assert slack>=0;factor_margins.append(slack/fac[j][n])
  assert vf(fac[j][n])>=iv.mpf(2*n+1)**(j+9)*vf(w)**9/362880;factor_iv+=1
pairs=[(i,j) for i in range(5) for j in range(5-i)];threshold=F(523,2**1021)
rows=[];mode_count=0;coef_count=0;pow_count=0;min_e=None;min_r=None;min_raw=None;max_raw=None
for ci in range(4096,4109):
 p=D/'evidence'/f'cell_{ci}.npz';pin(p);assert pins[str(p.relative_to(B))]==reg['pins'][str(p.relative_to(B))]
 with np.load(p,allow_pickle=False) as z:
  assert int(z['ci'])==ci and list(map(tuple,z['pairs'].tolist()))==pairs
  h=ff(z['h']);hp=list(map(ff,z['hpow']));m=z['coef_mid'].copy();r=z['coef_rad'].copy();rem=z['rem'].copy();sup=z['epsSup'].copy();native=list(map(ff,z['r2_native']));raw=list(map(ff,z['sum_native']))
 assert h>0 and len(hp)==27 and m.shape==r.shape==(5,523,13) and rem.shape==sup.shape==(5,523) and len(native)==len(raw)==15
 for q,t in enumerate(hp):assert t>=h**q>=0;pow_count+=1
 Es=[[ff(t) for t in row] for row in sup]
 for i in range(5):
  for n in range(523):
   mids=list(map(ff,m[i,n]));rads=list(map(ff,r[i,n]));er=ff(rem[i,n]);E=Es[i][n]
   assert all(t>=0 for t in rads) and er>=0 and E>=0
   # Separate sums deliberately differ from the direct Arb accumulation.
   midpoint_sum=sum((abs(x)*t for x,t in zip(mids,hp)),F(0))
   radius_sum=sum((x*t for x,t in zip(rads,hp)),F(0))
   bound=midpoint_sum+(radius_sum+er);slack=E-bound;assert slack>=0,(ci,i,n,slack)
   ratio=slack/E if E else F(0)
   min_e=ratio if min_e is None else min(min_e,ratio);mode_count+=1;coef_count+=len(mids)
 for k,(i,j) in enumerate(pairs):
  s=sum((x*y for x,y in zip(Es[i],fac[j])),F(0));slack=native[k]-s;assert slack>=0 and native[k]>0
  assert raw[k]>threshold
  ratio=slack/native[k];min_r=ratio if min_r is None else min(min_r,ratio)
  min_raw=raw[k] if min_raw is None else min(min_raw,raw[k]);max_raw=raw[k] if max_raw is None else max(max_raw,raw[k])
  rows.append({'ci':ci,'i':i,'j':j,'S_exact':str(s),'r2_exact':str(native[k]),'slack_exact':str(slack),'relative_slack_exact':str(ratio),'native_sum':str(raw[k])})
assert mode_count==33995 and coef_count==441935 and pow_count==351 and factor_iv==2615 and len(rows)==195
pin(Path(__file__));pin(D/'PROOF.md');pin(D/'evidence/proof_first.json')
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_REGENERATED_ANGULAR_REDUCTION_EXACT_IV','iv_digits':120,'radial_mode_checks':mode_count,'coefficient_entries':coef_count,'factor_checks':len(factor_margins),'factor_iv_checks':factor_iv,'power_checks':pow_count,'reduction_checks':len(rows),'subnormal_threshold_checks':len(rows),'subnormal_threshold_exact':str(threshold),'min_model_relative_slack_exact':str(min_e),'min_r2_relative_slack_exact':str(min_r),'min_factor_relative_slack_exact':str(min(factor_margins)),'min_native_sum_exact':str(min_raw),'max_native_sum_exact':str(max_raw),'rows':rows,'pins':pins,'scope':'Regenerated finite arithmetic only, physical model validity and absent historical operands OPEN.'}
(D/'evidence/exact_iv.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],'seconds');print('minimum_relative_slacks',float(min_e),float(min_r),'native_range',float(min_raw),float(max_raw))
