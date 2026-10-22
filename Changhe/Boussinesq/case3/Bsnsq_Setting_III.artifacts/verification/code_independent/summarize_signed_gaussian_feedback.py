"""Summarize only finalized independent feedback rows and their saved point data."""
from pathlib import Path
from datetime import datetime,timezone
import json,math,hashlib
from collections import defaultdict
V=Path('research/236_signed_gaussian_feedback/verification')
s=json.loads((V/'feedback_status.json').read_text());out={'created_utc':datetime.now(timezone.utc).isoformat(),'run_status':s['status'],'rows':[],'scope':'Sampled exact-Gaussian forced transport; no interval tail bound and no unforced B2 candidate.'}
for r in s['runs']:
 points=[json.loads(line) for line in Path(r['point_file']).read_text().splitlines()]
 good=[q for q in points if q['status'] in ('COMPLETE','LOCAL_JET')]
 row={k:r[k] for k in ['case','nr','na','L','r_in','rtol','c_out','num_c_out','min_radius','max_radius','point_count','seconds']}
 row['all_points_complete']=len(good)==len(points)
 row['negative_G_count']=sum(q['Omega']<0 for q in good)
 minimum=min(good,key=lambda q:q['Omega']/q['point'][0]);row['sample_min_G']=minimum['Omega']/minimum['point'][0];row['sample_min_point']=minimum['point']
 row['minimum_F']=min(q['Theta']/q['point'][0]**2 for q in good)
 row['sum_from_saved_points']=math.fsum(q['term'] for q in good)
 row['sum_recomputed_equal']=row['sum_from_saved_points']==r['c_out']
 row['point_sha256']=hashlib.sha256(Path(r['point_file']).read_bytes()).hexdigest()
 row['absolute_feedback_difference']=r['c_out']-r['num_c_out']
 # First radial index is largest radius in this compactification. Compare its
 # compensated angular values with those at the next radius; this is a diagnostic.
 ang=defaultdict(dict)
 for q in good:
  if q['i'] in (0,1):ang[q['j']][q['i']]=q
 comps=[]
 for j,pair in ang.items():
  if len(pair)!=2:continue
  vals=[]
  for i in (0,1):
   q=pair[i];rr=math.hypot(*q['point']);vals.append((rr,q['Omega']*rr**(1/r['beta']),q['Theta']/rr**(1-2/r['beta'])))
  comps.append({'angle_index':j,'two_radii_and_compensated_Omega_Theta':vals})
 row['far_tail_samples']=comps
 out['rows'].append(row)
(V/'feedback_aggregate.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
print('STATUS',s['status'],'FINISHED',len(out['rows']))
for r in out['rows']:print(r['case'],r['nr'],r['na'],r['L'],r['c_out'],'negative',r['negative_G_count'],'minG',r['sample_min_G'],'sumexact',r['sum_recomputed_equal'])
