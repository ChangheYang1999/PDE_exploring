"""Extract exact scalar geometry without importing or executing the N8 producer."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_geometry';E=D/'evidence';ctx.prec=128;ctx.threads=1
G=B.parent/'ipmA-num/data/cert_green.npz';PART=B/'research/middle_residual/evidence/partition_exact.json'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def aq(a):m,e=a.man_exp();return F(int(m))*F(2)**int(e)
def end(a):return [str(aq(a.lower())),str(aq(a.upper()))]
def succ(a):return math.nextafter(a,math.inf)
U=2.**-53;beta=succ(U/(1-U))
def width(m0,r0,m1,r1):
 m=m1-m0;r=succ(succ(succ(r0+r1)+succ(beta*abs(m))))
 return succ(abs(m)+r)
part=json.loads(PART.read_text());points=[]
for sp in part['spans']:
 a,b=F(sp['a_exact']),F(sp['b_exact']);n=sp['count'];assert sp['first_cell']==len(points)
 points.extend(a+(b-a)*i/n for i in range(n))
points.append(F(part['spans'][-1]['b_exact']));assert len(points)==7810
assert sha(G)==part['grid_sha256']=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
with np.load(G) as z:tm=z['tb'];tr=z['tb_rad']
assert tm.shape==tr.shape==(7810,) and np.all(np.isfinite(tm)) and np.all(np.isfinite(tr)) and np.all(tr>=0)
files={str(p.relative_to(B)) if p.is_relative_to(B) else str(p):sha(p) for p in [G,PART,Path(__file__),D/'PROOF.md',E/'proof_first.json']}
out={'utc':datetime.now(timezone.utc).isoformat(),'runs':{},'files':files}
for tag in ['full','fine0165']:
 source=B/f'research/n8_source_bounds/evidence/cert_n8_{tag}.json';data=json.loads(source.read_text());files[str(source.relative_to(B))]=sha(source)
 pmn,pmx=map(float,data['x_star_bracket']);p0=.5*(pmn+pmx);pr=pmx-p0
 assert F(p0)-F(pr)==F(pmn) and F(p0)+F(pr)==F(pmx)
 R3=3*data['delta_max'];xs=arb(p0,pr);theta=((arb(R3)/xs).asin())*arb('1.000001');dtheta=theta/data['ntheta'];th=[dtheta*i for i in range(data['ntheta']+1)]
 assert float(theta.mid())==data['theta_max']
 thlo=np.array([float(v.lower()) for v in th[:-1]]);thhi=np.array([float(v.upper()) for v in th[1:]])
 angle=[{'index':i,'lo_exact':end(th[i].union(th[i+1]))[0],'hi_exact':end(th[i].union(th[i+1]))[1],'mask_lo_float_exact':str(F(float(thlo[i])))} for i in range(data['ntheta'])]
 K=data['KSUB'];ci0,ci1=data['radial_cells'];radial=[];endpoint_checks=0;counts={d:0 for d in data['deltas']};masks=[]
 for ci in range(ci0,ci1+1):
  for j in [ci,ci+1]:assert F(float(tm[j]))-F(float(tr[j]))<=points[j]<=F(float(tm[j]))+F(float(tr[j]));endpoint_checks+=1
  h=width(float(tm[ci]),float(tr[ci]),float(tm[ci+1]),float(tr[ci+1]));assert F(h)>=points[ci+1]-points[ci]
  assert h==data['cells'][ci-ci0]['h'] and float(tm[ci])==data['cells'][ci-ci0]['t_a']
  ta=arb(float(tm[ci]),float(tr[ci]));hk=arb(h)/K;rlo=[];rhi=[]
  for k in range(K):
   tc=(ta+hk*k).union(ta+hk*(k+1));rr=tc.exp();rlo.append(float(rr.lower()));rhi.append(float(rr.upper()))
   radial.append({'ci':ci,'k':k,'ta_mid_exact':str(F(float(tm[ci]))),'ta_rad_exact':str(F(float(tr[ci]))),'cell_left_exact':str(points[ci]),'cell_right_exact':str(points[ci+1]),'h_up_exact':str(F(h)),'t_lo_exact':end(tc)[0],'t_hi_exact':end(tc)[1],'mask_rlo_float_exact':str(F(rlo[-1])),'mask_rhi_float_exact':str(F(rhi[-1]))})
  R1=np.array(rlo)[:,None];R2=np.array(rhi)[:,None];cos=np.cos(thlo[None,:]);rc=np.clip(p0*cos,R1,R2)
  dm=np.sqrt(np.maximum(rc**2+p0**2-2*rc*p0*cos,0.))
  dm=np.where(thlo[None,:]==0.,np.where((R1<=p0)&(p0<=R2),0.,np.minimum(abs(R1-p0),abs(R2-p0))),dm)
  for d in data['deltas']:
   cutoff=3*float(d)*(1+1e-6);mask=dm<=cutoff;counts[d]+=int(mask.sum());masks.append({'ci':ci,'delta':d,'cutoff_float_exact':str(F(cutoff)),'omitted_per_radial':[np.flatnonzero(~v).tolist() for v in mask]})
 assert counts=={d:v['ncells'] for d,v in data['deltas'].items()},(tag,counts)
 out['runs'][tag]={'p_min_exact':str(F(pmn)),'p_max_exact':str(F(pmx)),'p0_exact':str(F(p0)),'epsilon_exact':str(F(pr)),'delta_max_exact_decimal':str(F(str(data['delta_max']))),'R3_float_exact':str(F(R3)),'theta_cap_exact':end(theta),'selected_first_exact':str(points[ci0]),'selected_last_exact':str(points[ci1+1]),'K':K,'ntheta':data['ntheta'],'radial_cells':[ci0,ci1],'endpoint_checks':endpoint_checks,'counts':counts,'radial':radial,'angular':angle,'masks':masks}
(E/'geometry_inputs.json').write_text(json.dumps(out,indent=1)+'\n')
print(json.dumps({'utc':out['utc'],'status':'EXPORTED_GEOMETRY_MASKS_COUNTS_MATCH','runs':{k:{'counts':v['counts'],'radial':len(v['radial']),'angular':len(v['angular']),'endpoint_checks':v['endpoint_checks']} for k,v in out['runs'].items()},'sha256':sha(E/'geometry_inputs.json')}))
