#!/usr/bin/env python3
"""Recompute the retained pressure refinement reductions without field evaluation."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, math
ROOT=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser();p.add_argument('audit',type=Path);p.add_argument('--reference',type=Path,required=True);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--samples',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
if a.output.exists() or not a.output.resolve().is_relative_to(ROOT):raise ValueError('Fresh local output required')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def flat(x):
 for v in x:
  if isinstance(v,list):yield from flat(v)
  else:yield float(v)
def delta(x,y):
 u=list(flat(x));v=list(flat(y));assert len(u)==len(v)
 return max(abs(i-j)for i,j in zip(u,v))
checks=[]
def check(name,cond,**kw):checks.append(dict(name=name,passed=bool(cond),**kw))
def equal(name,x,y):check(name,math.isclose(x,y,rel_tol=2e-13,abs_tol=2e-15),recomputed=x,retained=y)
d=json.loads(a.audit.read_text());ref=json.loads(a.reference.read_text())
check('completed',d['phase']==ref['phase']=='complete')
check('candidate_hash',d['candidate_sha256']==ref['candidate_sha256']==sha(a.candidate))
check('reference_hash',d['reference_sha256']==sha(a.reference))
check('samples_hash',d['samples_sha256']==ref['samples_sha256']==sha(a.samples))
for rel,h in d['source_sha256'].items():check('source_hash '+rel,sha(ROOT/rel)==h)
check('same_twenty_points',d['points_r_z']==ref['points_r_z'] and len(d['points_r_z'])==20)
N=d['angular_bound']['maximum_saved_element_nmax'];D=d['angular_bound']['bulk_source_maximum_degree'];check('degree_bound',D==2*N+2)
oldp=ref['green_refinements'][-1]['pressure'];oldg=ref['green_refinements'][-1]['gradient']
check('three_levels',len(d['levels'])==3)
for i,row in enumerate(d['levels']):
 check('full_bandwidth '+str(i),row['lmax']>=D and 2*row['nangle']-1>=D+row['lmax'])
 check('finite_values '+str(i),all(math.isfinite(x)for x in flat([row['pressure'],row['gradient']])))
 equal('pressure_change '+str(i),delta(row['pressure'],oldp),row['change_from_previous']['pressure'])
 equal('gradient_change '+str(i),delta(row['gradient'],oldg),row['change_from_previous']['gradient'])
 equal('direct_pressure '+str(i),delta(row['pressure'],ref['direct_newton_values'][-1]['pressure']),row['difference_from_fine_direct']['pressure'])
 for item,control in zip(row['direct_gradient_comparisons'],ref['direct_gradient_checks']):
  check('direct_gradient_index',item['point_index']==control['point_index'])
  check('direct_gradient_step',item['h']==control['steps'][-1]['h'])
  equal('direct_gradient_error',delta(row['gradient'][item['point_index']],control['steps'][-1]['gradient']),item['max_abs_error'])
 oldp,oldg=row['pressure'],row['gradient']
s=d['saved_sample_comparison'];u=s['reconstructed_pressure'];v=s['exported_pressure'];errors=[x-y for x,y in zip(u,v)]
check('sample_lengths',len(u)==len(v)==len(s['R'])==len(s['mu'])==s['count']==765)
equal('sample_max',max(map(abs,errors)),s['max_abs_error'])
equal('sample_rms',math.sqrt(sum(x*x for x in errors)/len(errors)),s['rms_error'])
check('sample_worst',s['worst_index']==max(range(len(errors)),key=lambda i:abs(errors[i])))
result=dict(completed_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED' if all(x['passed']for x in checks)else'REFUTED',check_count=len(checks),checks=checks,audit_sha256=sha(a.audit),collector_sha256=sha(Path(__file__)),scope='Retained finite-point reductions and input identities. No uniform pressure error or new independent integral evaluation.')
a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='checks'},indent=2))
if result['verdict']!='CONFIRMED':raise SystemExit(1)
