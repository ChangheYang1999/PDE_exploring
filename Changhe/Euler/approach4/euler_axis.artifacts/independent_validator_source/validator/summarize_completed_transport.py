#!/usr/bin/env python3
"""Small immutable analysis of already completed independent transport records."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import numpy as np
ROOT=Path(__file__).resolve().parent.parent; BASE=ROOT/'axisymmetric_euler_24h'; RES=BASE/'results'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(name):
 p=RES/name;d=json.loads(p.read_text());assert d['phase']=='complete'
 for s,h in d['source_sha256'].items():
  p0=ROOT/s if s.startswith(('axisymmetric_euler_24h/','research/'))else BASE/s
  assert sha(p0)==h,(p0,h)
 return d
def maxi(x):return float(np.max(np.abs(x)))
def delta(x,y):return maxi(np.array(x)-np.array(y))
source=load('ladder_l1_source_transport.json')
summary={'created_utc':datetime.now(timezone.utc).isoformat(),'source_l1':{'candidate_sha256':source['candidate_sha256'],'source':source['source'],'wall_seconds':source['elapsed_seconds'],'cpu_seconds':source['cpu_seconds'],'completed_utc':source['updated_utc'],'point_count':len(source['points']),'levels':[]}}
for lev in source['levels']:
 row={'rtol':lev['rtol'],'nfev':lev['summary']['nfev'],'cutoffs':[]}
 for cut in lev['completed_cutoffs']:
  c=cut['comparison']; row['cutoffs'].append({'T':c['cutoff'],'max_identity_error':c['maximum_cutoff_identity_error'],'sets':[{k:s[k]for k in ['name','q_relative_difference','q_compensated_relative_difference','cutoff_identity_max_error','terminal_distance_max']}|{'rho_q':{tag:s[tag]['q']['rho']for tag in ['saved','transported','compensated']},'rho_eta':{tag:s[tag]['eta']['rho']for tag in ['saved','transported','compensated']}}for s in c['sets']]})
 summary['source_l1']['levels'].append(row)
coarse,tight=[l['completed_cutoffs'][-1]for l in source['levels']]
summary['source_l1']['tolerance_change_T48']={k:delta(coarse['transport'][k],tight['transport'][k])for k in ['q','gradient_q']}
summary['source_l1']['tight_cutoff_changes']=[]
for a,b in zip(source['levels'][-1]['completed_cutoffs'],source['levels'][-1]['completed_cutoffs'][1:]):
 ta,tb=a['transport']['cutoff'],b['transport']['cutoff'];a0=source['source']['a0']
 summary['source_l1']['tight_cutoff_changes'].append({'from':ta,'to':tb,'raw_q_max_change':delta(a['transport']['q'],b['transport']['q']),'compensated_q_max_change':delta(np.exp(a0*ta)*np.array(a['transport']['q']),np.exp(a0*tb)*np.array(b['transport']['q'])),'gradient_q_max_change':delta(a['transport']['gradient_q'],b['transport']['gradient_q'])})
summary['repaired_time_crosscheck']=[]
names=['ladder_l1_source_transport.json']
for level,normal,tightname in [(1,'strain_time_l1_retry.json','strain_time_l1_tight.json'),(2,'strain_time_l2.json','strain_time_l2_tight_retry.json')]:
 d,t=load(normal),load(tightname);names.extend([normal,tightname]);assert d['references']==t['references']
 row={'level':level,'candidate_sha256':d['candidate_sha256'],'radii':sorted(set(x['radius']for x in d['references'])),'mu':sorted(set(x['mu']for x in d['references'])),'points':len(d['references']),'normal_rtol':d['transport']['rtol'],'tight_rtol':t['transport']['rtol'],'normal_wall_seconds':d['wall_seconds'],'tight_wall_seconds':t['wall_seconds'],'normal_completed_utc':d['updated_utc'],'tight_completed_utc':t['updated_utc'],'cutoffs':[]}
 for c in d['cutoff_rows']+t['cutoff_rows']:
  row['cutoffs'].append({'T':c['cutoff'],'q_max_absolute_difference':maxi(c['q_absolute_difference']),'q_max_relative_difference':maxi(c['q_relative_difference']),'qz_max_absolute_difference':maxi(c['qz_absolute_difference']),'qz_max_scaled_difference':maxi(c['qz_scaled_difference']),'max_terminal_a':maxi(c['terminal_a'])})
 row['tolerance_change_T64']={k:delta(d['cutoff_rows'][-1][k],t['cutoff_rows'][-1][k])for k in ['q','q_z']}
 row['T48_to_T64_change']={k:delta(d['cutoff_rows'][-2][k],d['cutoff_rows'][-1][k])for k in ['q','q_z']}
 summary['repaired_time_crosscheck'].append(row)
summary['input_sha256']={name:sha(RES/name)for name in names};summary['script_sha256']=sha(Path(__file__))
summary['scope']='Saved-field finite cutoff transport and sampled cross-formulation agreement. No global error bound, accepted Euler approximation, or rigorous infinite-cutoff enclosure.'
out=RES/('transport_completed_summary_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')+'.json');out.write_text(json.dumps(summary,indent=2)+'\n')
print(out.relative_to(ROOT));print(json.dumps({k:v for k,v in summary['source_l1'].items()if k in ['point_count','tolerance_change_T48','tight_cutoff_changes']},indent=2));print(json.dumps(summary['repaired_time_crosscheck'],indent=2))
