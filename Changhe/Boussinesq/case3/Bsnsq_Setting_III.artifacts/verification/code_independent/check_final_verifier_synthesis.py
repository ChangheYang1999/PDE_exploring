#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,csv,hashlib,itertools,json,time
p=Path('research/348_final_verifier_synthesis');v=p/'verification';t0=datetime.now(timezone.utc);tick=time.monotonic();checks=[]
def sha(q):return hashlib.sha256(q.read_bytes()).hexdigest()
def ck(n,test,detail=None):checks.append(dict(name=n,passed=bool(test),detail=detail))
f=json.loads((v/'freeze.json').read_text());ck('proof_before_checks',datetime.fromisoformat(f['prepared_utc'])<t0);ck('proof_hash',sha(p/'PROOF.md')==f['proof_sha256'])
inputs={}
for z in f['inputs']:
 q=p/z['copy'];ck('input_hash_'+z['source'],sha(q)==z['sha256']);ck('input_size_'+z['source'],q.stat().st_size==z['bytes']);inputs[z['source']]=q
rows=list(csv.DictReader(inputs['../numerics/artifacts/consolidated_residuals.csv'].open()));groups={}
for r in rows:groups.setdefault((r['folder'],r['label']),[]).append(r)
regions={'0-0.03','0.03-0.3','0.3-3','3-30','30-300','300-1e8'}
observed_regions=sorted({r['region'] for r in rows})
# Validate the literal schema rather than silently changing a region label.
ck('six_literal_regions',set(observed_regions)==regions,observed_regions)
expected=set(itertools.product(['self','transport'],['F','G','Theta','Omega'],regions))
ck('5904_records',len(rows)==5904);ck('123_entries',len(groups)==123);ck('62_folders',len({a for a,b in groups})==62)
for key,rr in groups.items():
 keys=[(r['kind'],r['field'],r['region']) for r in rr];ck('cartesian_product_'+str(key),len(keys)==48 and set(keys)==expected)
 for r in rr:
  for name in ['max_abs','max_ratio','zero_normalizers','infinite_ratios','points']:ck('nonnegative_'+str(key)+'_'+r['kind']+'_'+r['field']+'_'+r['region']+'_'+name,float(r[name])>=0)
controls={('farfield_grid_20261020T1930','S0'),('farfield_grid_20261020T1930','manufactured_picard')}
ck('two_manufactures_named',controls<=set(groups));forced=set(groups)-controls;ck('121_forced_entries',len(forced)==121)
ranges={}
for field,expected_range in [('F',(.693002738,1.)),('G',(.412113426,.993766813))]:
 vals=[max(float(r['max_ratio']) for r in groups[key] if r['kind']=='self' and r['field']==field) for key in sorted(forced)]
 ranges[field]=[min(vals),max(vals)];ck('B2_range_'+field,all(abs(a-b)<1e-9 for a,b in zip(ranges[field],expected_range)),ranges[field])
selected=[]
for K in [24,32,40]:
 key=('215_equal_count_resolution_audit','eqb_K'+str(K));rr=groups[key]
 ck('equal_budget_metadata_'+str(K),all(float(r['meta_K'])==K and float(r['meta_Nt'])==56 and float(r['meta_beta'])==3.0113961 and float(r['meta_lam'])==.95 for r in rr))
 for kind in ['self','transport']:
  z=dict(K=K,kind=kind,beta=3.0113961,Nt=56,lam=.95)
  for field in ['F','G','Theta','Omega']:
   z[field]={name:max(float(r[name]) for r in rr if r['kind']==kind and r['field']==field) for name in ['max_abs','max_ratio']}
  selected.append(z)
inv=json.loads(inputs['verification/cartesian_inverse_manufactured.json'].read_text());ck('manufactured_six_points',len(inv['points'])==6)
irecs=inv['records'];ck('18_inverse_records',len(irecs)==18);ck('three_inverse_radii',set(r['radius'] for r in irecs)=={8.,16.,32.});ck('three_inverse_orders',set(r['order'] for r in irecs)=={12,20,32})
inverse_summary={}
for name in ['gaussian','slow_stream']:
 r32=[r for r in irecs if r['field']==name and r['order']==32];ck('three_order32_'+name,len(r32)==3)
 inverse_summary[name]=dict(max_order32_absolute_error=max(r['max_absolute_error'] for r in r32),truncated_order32_by_radius={str(r['radius']):r['truncated_max_absolute_error'] for r in r32})
ck('manufactured_order32_below8e15',all(r['max_order32_absolute_error']<8e-15 for r in inverse_summary.values()))
ck('slow_finite_box_errors_over1',all(x>1 for x in inverse_summary['slow_stream']['truncated_order32_by_radius'].values()))
# Exact arithmetic controls for the elementary identities proved in PROOF.md.
for beta in [Q(1,2),Q(2),Q(3),Q(7,2)]:
 for a0 in [Q(-3),Q(1),Q(2,3)]:
  c=1+beta/2;b0=4*a0/beta
  ck(f'center_temperature_{beta}_{a0}',2*(beta-c)*a0==(beta-2)*a0)
  ck(f'center_vorticity_{beta}_{a0}',(beta-c+1)*b0==2*a0)
  ck(f'negative_strain_shift_{beta}_{a0}',2*(beta-c-1)*a0!=(beta-2)*a0)
imports={}
for source,q in inputs.items():
 if not source.endswith('.py'):continue
 tree=ast.parse(q.read_text());names=[]
 for node in ast.walk(tree):
  if isinstance(node,ast.Import):names += [a.name for a in node.names]
  if isinstance(node,ast.ImportFrom):names.append(node.module or '')
 imports[source]=sorted(set(names))
 ck('static_no_numerics_import_'+source,not any('numerics' in n or n.startswith('picard') for n in names))
# Reject inference that a tiny manufactured absolute residual forces every ratio tiny.
res=json.loads(inputs['verification/residual_manufactured.json'].read_text())
ck('manufactured_degenerate_ratio_visible',any(max(z['cartesian']['normalized_Theta'])==1. for z in res['polynomial_control']))
ck('no_denominator_floor_source','denominator!=0' in inputs['code_independent/finite_difference.py'].read_text())
summary=dict(started_utc=t0.isoformat(),ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,code_sha256=sha(Path(__file__)),proof_sha256=f['proof_sha256'],passed=sum(x['passed'] for x in checks),total=len(checks),checks=checks,forced_ranges=ranges,equal_budget_rows=selected,inverse_summary=inverse_summary,static_imports=imports,scope='Finite transcription, source and elementary identity controls. Not a new inverse computation, continuum residual certificate, final-time certificate, or general B2 endpoint.')
(v/'checks.json').write_text(json.dumps(summary,indent=2)+'\n')
(v/'selected_rows.json').write_text(json.dumps(selected,indent=2)+'\n')
print(json.dumps({k:z for k,z in summary.items() if k not in ['checks','static_imports','equal_budget_rows']},indent=2));print('FAILED',[x for x in checks if not x['passed']]);raise SystemExit(0 if all(x['passed'] for x in checks) else 1)
