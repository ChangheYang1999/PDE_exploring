"""Exact audit of both independent geometric model certificates and all dependencies."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,sys,math
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_series_operands'
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def dy(x):return Q.from_float(float(x))
v=read(S/'evidence/verdict.json');assert v['status']=='CONFIRMED_CONTEMPORARY_SERIES_OPERANDS_AND_DIRECT_GEOMETRY';pins=dict(v['files']);assert len(pins)==255
for s,h in pins.items():assert sha(B/s)==h,s
part=read(B/'research/middle_residual/evidence/partition_exact.json');pts=[];end=None
for z in part['spans']:
 a,b=Q(z['a_exact']),Q(z['b_exact']);n=z['count'];assert n>0 and a<b and z['first_cell']==len(pts)
 if end is not None:assert end==a
 pts.extend(a+(b-a)*Q(i,n) for i in range(n));end=b
pts.append(end);assert len(pts)==7810
cover=read(B/'research/localized_forcing/evidence/coverage.json');assert list(map(Q,cover['local_points']))==pts[4096:4110] and cover['partition_sha256']==sha(B/'research/middle_residual/evidence/partition_exact.json')
rows=read(S/'evidence/blocks.json');expected=[(ci,q,bs,bp) for ci in range(4096,4109) for q in range(16) for bs in range(2) for bp in range(2)];assert len(rows)==len(expected)==832
raw=read(B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json');p1,p2=map(dy,raw['x_star_bracket']);theta=dy(raw['theta_max']);assert 0<p1<p2 and 0<theta<Q(1,100)
with np.load(S/'evidence/operands.npz',allow_pickle=False) as f:arr={k:f[k].copy() for k in f.files}
assert arr['indices'].shape==(832,4) and list(map(tuple,arr['indices']))==expected
for m in ['q','uq']:
 for k in ['mid','rad']:assert arr[m+'_'+k].shape==(832,13,9) and np.isfinite(arr[m+'_'+k]).all()
 assert (arr[m+'_rad']>=0).all() and arr[m+'_rem'].shape==(832,) and np.isfinite(arr[m+'_rem']).all() and (arr[m+'_rem']>0).all()
engines={k:read(D/'evidence'/('iv_finite.json' if k=='iv' else 'arb.json')) for k in ['arb','iv']}
assert engines['iv']['endpoint_checks']==391040 and engines['iv']['special_value_rejections']==6;stats={};budgets=[];coordinates=[]
for k,z in engines.items():
 assert z['status']==('PASS_ARB512_PHYSICAL_GEOMETRIC_MODELS' if k=='arb' else 'PASS_IV160_PHYSICAL_GEOMETRIC_MODELS')
 assert z['blocks']==832 and z['models']==1664 and z['coefficient_projection_tests']==194688 and not z['failures'] and len(z['records'])==832
 for s,h in z['pins'].items():assert sha(B/s)==h,s
 ratios=[];margins=[];nex=0;positive_budget_checks=0
 for i,(row,record,key) in enumerate(zip(rows,z['records'],expected)):
  assert tuple(row[s] for s in ['ci','q','bs','bp'])==key and record['index']==i and tuple(record['key'])==key
  ci,q,bs,bp=key;H,W,w,wk,h,hk=map(dy,[row[s] for s in ['H','W','w','wk','h','hk']]);assert H==32*hk and W==2*wk and 64*hk>=h>=pts[ci+1]-pts[ci] and 8*wk>=2*w
  tb,tr=map(dy,[row['tb'],row['tb_rad']]);assert tb-tr<=pts[ci]<=tb+tr
  T=pts[ci]+bs*H;A=theta*Q(2*q+1,32)-w+(4*bp+2)*wk;M=max(abs(A-W),abs(A+W));assert (Q(record['T_exact']),Q(record['A_exact']),Q(record['M_exact']))==(T,A,M)
  assert 0<H<Q(1,1000) and 0<W<Q(1,1000) and M<Q(1,100)
  assert set(record['models'])=={'q','uq'}
  for m,d in record['models'].items():
   total,R,e,margin,rel,big=map(Q,[d[s] for s in ['coefficient_excess_sum','analytic_remainder_upper','saved_budget','margin','relative_margin','largest_weighted_excess']]);assert total>=big>=0 and R>0 and e==dy(arr[m+'_rem'][i])>0
   assert margin==e-total-R>0 and rel==margin/e and total+R<Q(11,250)*e
   n=d['positive_excess_coefficients'];assert type(n) is int and 0<=n<=117;nex+=n
   wit=d['largest_excess_witness']
   if wit is None:assert big==0 and n==0
   else:
    ii,jj,l,u,ex=wit;l,u,ex=map(Q,[l,u,ex]);assert 0<=ii<=12 and 0<=jj<=8 and l<=u and ex>0 and n>0
    mid,rad=map(dy,[arr[m+'_mid'][i,ii,jj],arr[m+'_rad'][i,ii,jj]]);assert ex==max(Q(0),mid-rad-l,u-mid-rad) and big==ex*H**ii*W**jj
   ratios.append((total+R)/e);margins.append(rel);positive_budget_checks+=1
   if k=='arb':budgets.append(e)
  if k=='arb':coordinates.append([*key,str(T),str(A),str(M)])
 assert max(ratios)==Q(z['maximum_budget_ratio']) and min(margins)==Q(z['minimum_relative_margin']) and nex==z['positive_excess_coefficients']
 stats[k]={'strict_budget_checks':positive_budget_checks,'maximum_budget_ratio':str(max(ratios)),'minimum_relative_margin':str(min(margins)),'positive_excess_coefficients':nex,'public_strict_ratio_ceiling':'11/250'}
# Match all geometrical records across the two independently generated lists.
for a,b in zip(engines['arb']['records'],engines['iv']['records']):
 for s in ['index','key','T_exact','A_exact','M_exact']:assert a[s]==b[s]
# Exact independent algebraic checks of the two Taylor-coefficient constructions.
es=[Q(1)];ds=[Q(1)]
for i in range(1,13):es.append(es[-1]/i);ds.append(2*ds[-1]/i)
cs=[(Q(1),Q(0)),(Q(0),Q(-1))]
for j in range(2,9):cs.append(tuple(-c/Q(j*(j-1)) for c in cs[-2]))
trig=[(1,0),(0,-1),(-1,0),(0,1)]
for i in range(13):assert es[i]==Q(1,math.factorial(i)) and ds[i]==Q(2**i,math.factorial(i))
for j in range(9):assert cs[j]==tuple(Q(c,math.factorial(j)) for c in trig[j%4])
for p in [S/'evidence/verdict.json',B/'research/localized_forcing/evidence/coverage.json',B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json',*sorted(D.glob('*.md')),*sorted((D/'code').glob('*.py')),D/'evidence/proof_first.json',D/'evidence/arb.json',D/'evidence/iv.json',D/'evidence/iv_finite.json',D/'evidence/conventions.json']:
 pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FINITE_GEOMETRIC_AUDIT_MODEL_REVIEW_PENDING','prior_pins_rehashed':255,'blocks':832,'models_per_engine':1664,'coefficients_per_engine':194688,'exact_partition_points':7810,'independently_saved_local_points':14,'coordinate_checks':1664,'recurrence_identities':35,'source_bracket_exact':[str(p1),str(p2)],'theta_max_exact':str(theta),'minimum_saved_budget':str(min(budgets)),'maximum_saved_budget':str(max(budgets)),'engines':stats,'scope':'Only physical geometric function inclusions, uniform p and full rectangle. No derivative-remainder or composed forcing assertion.','pins':dict(sorted(pins.items()))}
(D/'evidence/finite_audit_repaired.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(pins),out['prior_pins_rehashed'],{k:float(Q(s['maximum_budget_ratio'])) for k,s in stats.items()})
