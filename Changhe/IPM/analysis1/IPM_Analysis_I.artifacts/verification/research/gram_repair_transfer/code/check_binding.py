from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_repair_transfer';R=B/'research/gram_conforming_repair'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
v=read(R/'evidence/verdict.json');a=read(R/'evidence/compute.json');b=read(R/'evidence/independent.json');sc=read(D/'evidence/compute.json');rows=[];pins={}
for p in [R/'PROOF.md',R/'evidence/compute.json',R/'evidence/independent.json',R/'evidence/summary.json']:
 n=str(p.relative_to(B));check(v['files'][n]==sha(p),'explicit132membership');pins[n]=sha(p)
for x,y,z in zip(a['records'],b['records'],sc['records'],strict=True):
 check(x['M']==y['M']==z['M'] and x['N']==y['N']==len(x['columns'])==len(y['columns']),'radial count');knots=set();pieces=0
 for c,d in zip(x['columns'],y['columns'],strict=True):
  check(c['column_index']==d['column_index'] and c['pieces']==d['pieces'],'same exact repair record')
  for p in c['pieces']:
   l,r=F(p['a_exact']),F(p['b_exact']);check(l<r and -5<l<r<9,'finite log support away from infinite endpoints');knots.update([l,r]);pieces+=1
 check(z['N']==x['N']*x['M'] and F(z['delta_exact'])==F(x['public']['uniform_single_column_relative_broken_energy_upper']),'application parameters')
 rows.append({'M':x['M'],'radial_columns':x['N'],'angular_modes':list(range(x['M'])),'real_angular_factor':'cos(2*m*theta)','columns':z['N'],'pieces':pieces,'common_log_partition_endpoints':len(knots),'smallest_log_endpoint_exact':str(min(knots)),'largest_log_endpoint_exact':str(max(knots)),'support_enclosure':'exp(-5) < r < exp(9), hence a compact annulus with inner radius strictly positive','quadratic_error_term_exact':z['eta_squared_exact']})
for p in [R/'evidence/verdict.json',D/'evidence/compute.json',D/'evidence/independent.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_POSITIVE_INNER_RADIUS_COMMON_SUBDIVISION_AND_REAL_MODE_BINDING','records':rows,'files':pins,'scope':'Exact support/mode/application binding. No actual Gram eigenvalue, quadrature or operator claim.'}
p=D/'evidence/binding.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'records':rows}))
