"""Recompute selected complete nodal datasets with the already audited code."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,subprocess,json,os,sys,hashlib
from decimal import Decimal
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'09_uniform_comparison/lead_certificate';OUT=BASE/'verification/recomputed';OUT.mkdir(parents=True,exist_ok=True)
p=argparse.ArgumentParser();p.add_argument('--groups',nargs='+',type=int,required=True);p.add_argument('--kind',choices=['lower','far'],default='lower');a=p.parse_args();checks=[]
for g in a.groups:
 name=f'{a.kind}2_g{g}.json';old=json.loads((BASE/'data'/name).read_text());target=OUT/name
 alphas=','.join(r['alpha'] for r in old['rows'])
 if a.kind=='lower':
  cmd=[sys.executable,str(ROOT/'code/certify_structured_full.py'),'--a',old['a'],'--alphas',alphas,'--step',str(old['cells_per_log_unit']),'--log-lo',str(old['log_lo']),'--log-hi',str(old['log_hi']),'--out',str(target)]
 else:
  cmd=[sys.executable,str(BASE/'source/far_nodes.py'),'--alphas',alphas,'--ref',old['plan_reference_alpha'],'--angles',str(old['angles']),'--radial',str(old['radial_cells']),'--phases',str(old['phase_intervals']),'--umin',old['umin'],'--tries',str(old['plan_trials']),'--out',str(target)]
 with (OUT/f'{a.kind}_g{g}.log').open('w') as log:subprocess.run(cmd,cwd=ROOT,env=os.environ,stdout=log,stderr=subprocess.STDOUT,check=True,timeout=400)
 new=json.loads(target.read_text());assert len(old['rows'])==len(new['rows'])
 identical=old['rows']==new['rows'];shifts=[];contained=True
 for x,y in zip(old['rows'],new['rows']):
  assert x['alpha']==y['alpha']
  if a.kind=='lower':
   lo='safe_decimal_lower_10_places';hi='safe_decimal_upper_10_places'
   ds=[abs(Decimal(x[k])-Decimal(y[k])) for k in [lo,hi]];shifts.extend(ds)
   assert max(ds)<=Decimal('0.000000002')
   contained=contained and Decimal(x[lo])<=Decimal(y[lo]) and Decimal(x[hi])>=Decimal(y[hi])
   assert arb(x['full']).overlaps(arb(y['full']))
  else:
   assert len(x['far_phase_intervals'])==len(y['far_phase_intervals'])
   for u,v in zip(x['far_phase_intervals'],y['far_phase_intervals']):assert arb(u).overlaps(arb(v))
 checks.append(dict(group=g,kind=a.kind,row_count=len(new['rows']),all_rows_identical=identical,original_interval_contains_recomputed=contained if a.kind=='lower' else None,max_decimal_endpoint_change=str(max(shifts,default=Decimal(0))),original_sha256=hashlib.sha256((BASE/'data'/name).read_bytes()).hexdigest(),recomputed_sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
 print(checks[-1],flush=True)
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),checks=checks)
 (OUT/f'comparison_{a.kind}_{"_".join(map(str,a.groups))}.json').write_text(json.dumps(result,indent=2)+'\n')
