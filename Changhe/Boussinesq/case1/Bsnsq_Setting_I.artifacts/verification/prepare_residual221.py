from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimized plan prohibited')
r=Path('research/interval_residual221');dest=r/'verification/plan.json'
if dest.exists():raise RuntimeError('plan exists')
paths=set()
def sha(p):p=Path(p).resolve();paths.add(p);return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):sha(p);return json.loads(Path(p).read_text())
for p in [__file__,'code/run_residual221.py','code/replay_residual221.py','code/interval_residual221.py','code/dyadic_root220.py','code/root220_replay_arithmetic.py',r/'PROOF.md',r/'RUNNER_PROOF.md',r/'RUNNER_REVIEW_PROOF.md',r/'PRELAUNCH_PROOF.md','PROMPT.md']:sha(p)
for name,count in [('machinery',387),('composition',45),('interval_base',523),('interval_composition',137),('rational_replay',4350),('source_gx',68)]:
 j=read(r/f'verification/{name}.json')
 if j['check_count']!=count or not j['status'].startswith('PASS_'):raise RuntimeError(('machinery',name))
 for p,h in j['hashes'].items():
  if sha(p)!=h:raise RuntimeError(('machinery pin',p))
pre=read(r/'verification/prelaunch.json')
if pre['status']!='PASS_FINAL_RESIDUAL_PRELAUNCH_DIAGNOSTICS':raise RuntimeError('prelaunch status')
for p,h in pre['hashes'].items():
 if sha(p)!=h:raise RuntimeError(('prelaunch pin',p))
tables=read('candidate_audits/core32_focused218/verification/tables.json')
if tables['status']!='PASS_EXACT_SAVED_DECIMAL_REGIONAL_ORDERING':raise RuntimeError('completed selection')
for p,h in tables['hashes'].items():
 if sha(p)!=h:raise RuntimeError(('table pin',p))
rootplan=read('research/implicit_root220/verification/plan.json');rs=read('research/implicit_root220/verification/replay_summary.json');rp=Path('research/implicit_root220/certificates/replay.jsonl')
if rs['status']!='COMPLETE_FINITE_ROOT_REPLAY' or rs['total']!=2366 or rs['certified']!=2366 or rs['failed'] or rs['plan_sha256']!=sha('research/implicit_root220/verification/plan.json')or rs['output_sha256']!=sha(rp):raise RuntimeError('complete independent roots')
for p,h in rootplan['hashes'].items():
 if sha(p)!=h:raise RuntimeError(('root pin',p))
rootrecords={(v['name'],v['index']):v for v in map(json.loads,rp.read_text().splitlines())};sources=[];count=0
regions=[['focused_origin_region',0,169],['focused_intermediate',169,338],['focused_outer',338,507],['broad',507,1183]];quantities=['prompt_ratio','grouped_ratio','R','D']
for src in rootplan['sources']:
 rows=[v for v in tables['rows']if v['name']==src['name']and v['region']in ['focused_origin_region','focused_intermediate','focused_outer','broad']]
 if len(rows)!=4:raise RuntimeError('four regions')
 reasons={}
 for row in rows:
  if set(row['maxima'])!=set(quantities):raise RuntimeError('exact four quantities')
  for key in quantities:
   cell=row['maxima'][key];reasons.setdefault(cell['index'],[]).append([row['region'],key])
 raw={}
 for seg in src['raw_segments']:
  if sha(seg['path'])!=seg['sha256']:raise RuntimeError('raw pin')
  raw.update({v['index']:v for v in map(json.loads,Path(seg['path']).read_text().splitlines())})
 if sorted(raw)!=list(range(1183)):raise RuntimeError('complete raw set')
 for idx,v in raw.items():
  x,y=map(F,v['coordinate_exact_dyadics'])
  if x<=0 or y<=0 or v['status']!='COMPUTED' or v['dps']!=130 or v['source_sha256']!=src['source_sha256']:raise RuntimeError('finite strictly positive source grid')
  for key in quantities+['eta']:F(v['fields'][key])
 for label,lo,hi in regions:
  matches=[v for v in rows if v['region']==label]
  if len(matches)!=1:raise RuntimeError('exactly one row per region')
  row=matches[0]
  if row['point_count']!=hi-lo:raise RuntimeError('region count')
  for key in quantities:
   idx=max(range(lo,hi),key=lambda i:abs(F(raw[i]['fields'][key])))
   if row['maxima'][key]['index']!=idx or F(row['maxima'][key]['absolute_value'])!=abs(F(raw[idx]['fields'][key])):raise RuntimeError('table ordering and earliest tie')
 selected=[]
 for idx in sorted(reasons):
  old=rootrecords[src['name'],idx];v=raw[idx]
  if old['status']!='CERTIFIED' or old['source_sha256']!=src['source_sha256']:raise RuntimeError('selected root')
  selected.append({'index':idx,'reasons':reasons[idx],'coordinate_exact_dyadics':v['coordinate_exact_dyadics'],'eta_hint':v['fields']['eta'],'old_l':old['l'],'old_h':old['h'],'scalar_fields':{k:v['fields'][k]for k in ['R','D','N','N2','prompt_ratio','grouped_ratio']}})
 sources.append({**src,'selected':selected});count+=len(selected)
now=datetime.now(timezone.utc).isoformat();j={'utc':now,'status':'PINNED_DATA_INFORMED_FINITE_SELECTION_NOT_RESIDUAL_CERTIFICATE','total':count,'sources':sources,'trial_bits':[160,140,120],'regions':regions,'quantities':quantities,'tie_rule':'smallest index','domain':'strictly positive x and y; finite saved quantities only','first_bits':400,'second_bits':512,'scope':'Finite data-informed maxima witnesses only. Independent root endpoints and interval arithmetic replay; no independently regenerated fourth derivatives or continuum bound.','hashes':{str(p):sha(p)for p in sorted(paths)},'relative_paths':{str(p):str(p.relative_to(Path.cwd()))if p.is_relative_to(Path.cwd())else str(p)for p in sorted(paths)}};dest.write_text(json.dumps(j,indent=2)+'\n');print(now,j['status'],count,len(paths))
