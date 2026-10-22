"""Every regenerated mode and reduction, using independent direct Arb384 sums."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,time,sys
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];ctx.prec=384
start=time.monotonic();pins={}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p):pins[str(p.relative_to(B))]=sha(p)
def box(x):return {'lower':str(F(str(x.lower().fmpq()))),'upper':str(F(str(x.upper().fmpq()))),'display':str(x)}
reg=json.loads((D/'evidence/regeneration.json').read_text());assert reg['status']=='REGENERATED_INPUTS_REQUIRING_TWO_ENGINE_AUDIT'
pin(D/'evidence/regeneration.json');factor=D/'evidence/factors.npz';pin(factor);assert pins[str(factor.relative_to(B))]==reg['pins'][str(factor.relative_to(B))]
with np.load(factor,allow_pickle=False) as z:w=arb(float(z['w']));nu=z['nu'].copy();fac=z['remfac'].copy()
assert nu.shape==(523,) and np.array_equal(nu,2*np.arange(523)+1) and fac.shape==(5,523)
assert np.isfinite(fac).all() and (fac>0).all() and w>0
factor_checks=0;factor_relative=[]
for j in range(5):
 for n in range(523):
  e=arb(2*n+1)**(j+9)*w**9/362880;b=arb(float(fac[j,n]));assert b>=e,(j,n,b,e)
  factor_relative.append((b-e)/b);factor_checks+=1
outrows=[];model_count=0;coefficient_count=0;power_checks=0;raw_checks=0;min_model=None;min_r2=None
threshold=arb(523)*arb(2)**-1021
pairs=[(i,j) for i in range(5) for j in range(5-i)]
for ci in range(4096,4109):
 p=D/'evidence'/f'cell_{ci}.npz';pin(p);assert pins[str(p.relative_to(B))]==reg['pins'][str(p.relative_to(B))]
 with np.load(p,allow_pickle=False) as z:
  assert int(z['ci'])==ci and list(map(tuple,z['pairs'].tolist()))==pairs
  h=arb(float(z['h']));hp=z['hpow'].copy();m=z['coef_mid'].copy();r=z['coef_rad'].copy();e=z['rem'].copy();E=z['epsSup'].copy();raw=z['sum_native'].copy();rr=z['r2_native'].copy()
 assert len(hp)==27 and m.shape==r.shape==(5,523,13) and e.shape==E.shape==(5,523) and raw.shape==rr.shape==(15,)
 assert h>0
 for x in [hp,m,r,e,E,raw,rr]:assert np.isfinite(x).all()
 for x in [hp,r,e,E,raw,rr]:assert (x>=0).all()
 H=list(map(lambda x:arb(float(x)),hp))
 for q,Hq in enumerate(H):assert Hq>=h**q,(ci,q);power_checks+=1
 for i in range(5):
  for n in range(523):
   bound=arb(float(e[i,n]))
   for q in range(13):bound+=(abs(arb(float(m[i,n,q])))+arb(float(r[i,n,q])))*H[q];coefficient_count+=1
   ei=arb(float(E[i,n]));assert ei>=bound,(ci,i,n,ei,bound)
   rel=(ei-bound)/ei if ei>0 else arb(0)
   if min_model is None or rel.upper()<min_model.upper():min_model=rel
   model_count+=1
 for pos,(i,j) in enumerate(pairs):
  s=arb(0)
  for n in range(523):s+=arb(float(E[i,n]))*arb(float(fac[j,n]))
  native=arb(float(rr[pos]));assert native>=s,(ci,i,j,native,s)
  rawval=arb(float(raw[pos]));assert rawval>threshold;raw_checks+=1
  rel=(native-s)/native
  if min_r2 is None or rel.upper()<min_r2.upper():min_r2=rel
  outrows.append({'ci':ci,'i':i,'j':j,'S':box(s),'r2':str(F.from_float(float(rr[pos]))),'relative_slack':box(rel),'native_sum':str(F.from_float(float(raw[pos])))})
assert model_count==33995 and coefficient_count==441935 and factor_checks==2615 and power_checks==351 and raw_checks==195 and len(outrows)==195
pin(Path(__file__));pin(D/'PROOF.md');pin(D/'evidence/proof_first.json')
output={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_REGENERATED_ANGULAR_REDUCTION_ARB','precision_bits':384,'radial_mode_checks':model_count,'coefficient_entries':coefficient_count,'factor_checks':factor_checks,'power_checks':power_checks,'reduction_checks':len(outrows),'subnormal_threshold_checks':raw_checks,'min_model_relative_slack':box(min_model),'min_r2_relative_slack':box(min_r2),'min_factor_relative_slack':box(min(factor_relative,key=lambda x:float(x.mid()))),'rows':outrows,'pins':pins,'scope':'Regenerated finite operands and outputs only, inherited models and historical arrays OPEN.'}
(D/'evidence/arb.json').write_text(json.dumps(output,indent=2)+'\n');print(output['utc'],output['status'],output['seconds'],'seconds');print('minimum_relative_slacks',output['min_model_relative_slack']['display'],output['min_r2_relative_slack']['display'])
