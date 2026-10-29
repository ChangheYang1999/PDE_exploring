#!/usr/bin/env python3
"""Freeze and check primary F1/F5 data, without running primary software."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,csv,hashlib,json,math,shutil,time
ROOT=Path(__file__).resolve().parent;LANE=ROOT.parent;NUM=LANE.parent/'e4-num/axisymmetric_euler_24h'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def readcsv(p):
 with p.open(newline='') as f:return list(csv.DictReader(f))
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists() or not out.is_relative_to(LANE):raise ValueError('Fresh local output required')
 out.mkdir(parents=True);start=time.perf_counter();inputs={}
 def freeze(path,name=None):
  path=path.resolve();before=sha(path);dest=out/(name or path.name);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,dest)
  if sha(path)!=before or sha(dest)!=before:raise RuntimeError('Input changed while freezing')
  inputs[str(path)]=before;return dest
 mapping=readcsv(freeze(NUM/'FAILURE_MAP.csv'));byid={r['job_id']:r for r in mapping}
 # Independently recover every outer radius from the saved job configuration.
 # Names are not a reliable geometry contract (e.g. t1seedRm5).
 geometry={}
 for row in mapping:
  cfg=json.loads(freeze(NUM/'runs'/row['job_id']/'job.json','jobs/'+row['job_id']+'.json').read_text())['cfg']
  geometry[row['job_id']]=float(cfg['shells'][-1][0]) if cfg.get('shells') else float(cfg['R1'])
 plots={}
 for f in ['F1_residual_vs_resolution','F5_cl_continuation']:
  plots[f]=readcsv(freeze(NUM/'figures'/f'{f}.csv'));freeze(NUM/'figures'/f'{f}.png')
  caption=NUM/'figures'/('F1_caption.txt' if f.startswith('F1') else 'F5_caption.txt')
  if caption.exists():freeze(caption)
 for f in ['figures_F1_F5.py','failure_map.py']:freeze(NUM/'scripts'/f)
 tests=[];labels=[];missing=[];scopes=[]
 def check(name,ok,**data):tests.append(dict(name=name,passed=bool(ok),**data))
 validation_cache={}
 def validation(jid):
  if jid not in validation_cache:
   path=NUM/'runs'/jid/'validation.json'
   if not path.exists():return None
   value=json.loads(freeze(path,f'validation/{jid}.json').read_text());candidates=[]
   for row in value.get('shells',[]):
    for key,v in row.items():
     if key.startswith('rho_') and isinstance(v,(int,float)) and math.isfinite(v):
      pieces=key.split('_');eq=pieces[1]
      if eq in ['Mr','Mt','Mz','q','eta','div']:candidates.append((v,eq,row['k'],'_'.join(pieces[2:])))
   for key,v in value.get('origin',{}).items():
    if key.startswith('rho_') and isinstance(v,(int,float)) and math.isfinite(v):candidates.append((v,key[4:],'origin','origin'))
   maximum=max(candidates);validation_cache[jid]=(value,maximum)
  return validation_cache[jid]
 for plot,rows in plots.items():
  for i,row in enumerate(rows):
   jid=row['job_id']
   if not jid:
    if plot.startswith('F1') and (row['series']=='S1 continuation ladder (verifier)' or row['series'].startswith('independent single-source ladder')):
     if row['D']:
      level={24:0,36:1,48:2}[int(row['D'])]
     else:
      level=int(row['level'].split()[1]);check(f'{plot}_{i}_independent_basis_counts',row['level']==['level 0 (4/3/2)','level 1 (6/4/3)','level 2 (8/5/4)'][level])
     local=ROOT/f'results/s1_refinement_c074_q2/L{level}/summary.json';data=json.loads(freeze(local,f's1/L{level}.json').read_text())
     check(f'{plot}_{i}_rounded_s1',abs(float(row['rho_max'])-data['aggregate']['rho_max'])<=.005,quoted=float(row['rho_max']),actual=data['aggregate']['rho_max'])
     scopes.append(dict(plot=plot,row=i,note='S1 continuation values rounded to two decimals; exact source copied. Dominant-equation label is blank.'))
    else:missing.append(dict(plot=plot,row=i,job_id=jid))
    continue
   source=byid.get(jid)
   if source is None:missing.append(dict(plot=plot,row=i,job_id=jid));continue
   check(f'{plot}_{i}_rho_matches_map',float(row['rho_max'])==float(source['rho_max']))
   if row.get('kind')=='floor_per_cl_level' or plot.startswith('F1'):check(f'{plot}_{i}_B2',source['B2']=='True')
   val=validation(jid)
   if val is None:missing.append(dict(plot=plot,row=i,job_id=jid,note='validation.json missing'));continue
   full,mx=val
   check(f'{plot}_{i}_rho_matches_validation',abs(float(row['rho_max'])-full['rho_max'])<1e-12*max(1,abs(full['rho_max'])))
   check(f'{plot}_{i}_aggregate_is_max',abs(mx[0]-full['rho_max'])<1e-12*max(1,abs(full['rho_max'])))
   if row.get('dominant_eq'):
    ok=row['dominant_eq']==mx[1]
    labels.append(dict(plot=plot,row=i,job_id=jid,quoted_equation=row['dominant_eq'],actual_equation=mx[1],actual_shell=mx[2],actual_set=mx[3],rho_max=mx[0],equation_correct=ok))
   if row.get('kind')=='floor_per_cl_level':
    cl=float(row['cl']);D=int(row['D']);eligible=[]
    for s in mapping:
     if s['B2']!='True' or not s['level'].startswith(f'D{D}n') or round(float(s['cl_final']),4)!=cl:continue
     sj=s['job_id']
     if geometry[sj]!=10:continue
     eligible.append(float(s['rho_max']))
    check(f'{plot}_{i}_floor_is_minimum',bool(eligible) and min(eligible)==float(row['rho_max']))
 # Freeze time is for this snapshot, not the generation time of the mutable source plots.
 record=dict(script_sha256=sha(Path(__file__)),completed_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,inputs_sha256=inputs,tests=tests,all_scalar_checks_pass=all(r['passed'] for r in tests),label_checks=labels,incorrect_equation_labels=[r for r in labels if not r['equation_correct']],missing=missing,scope_notes=scopes,scope='Scalar/label audit of primary validation records and plotted CSV; no new Euler residual computation.')
 (out/'audit.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:record[k] for k in ['completed_utc','wall_seconds','all_scalar_checks_pass','missing']}));print('scalar checks',len(tests),'wrong equation labels',len(record['incorrect_equation_labels']))
if __name__=='__main__':main()
