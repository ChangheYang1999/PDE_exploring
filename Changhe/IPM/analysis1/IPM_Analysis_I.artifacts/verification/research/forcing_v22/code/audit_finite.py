"""Bind the two complete finite checks without asserting physical model validity."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys,gzip,math
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1]
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
prior_path=B/'research/forcing_composed_cutoff/evidence/verdict.json';prior=read(prior_path)
assert prior['status']=='CONFIRMED_V21_FINITE_COMPONENTS_PHYSICAL_FORCING_OPEN'
pins=dict(prior['files']);assert len(pins)==208
for f,h in pins.items():assert sha(B/f)==h,f
assert sha(D/'PROOF.md')==read(D/'evidence/proof_first.json')['sha256']
manifest=read(D/'evidence/snapshot_manifest.json');assert len(manifest['files'])==33
for k,v in manifest['files'].items():
 p=B/v['snapshot'];assert sha(p)==v['snapshot_sha256']
 content=gzip.decompress(p.read_bytes()) if v['compressed_gzip'] else p.read_bytes()
 assert len(content)==v['bytes'] and hashlib.sha256(content).hexdigest()==v['source_sha256'],k
 del content
names=['linkage','source_geometry','aggregate_arb','aggregate_exact_iv','pointwise_series','cutoff_extrema','calculus']
v={k:read(D/('evidence/'+k+'.json')) for k in names}
assert all(z['status'].startswith('PASS') for z in v.values())
l=v['linkage'];assert l['rows']==43949 and l['prior_pins_rehashed']==208 and l['part_count']==26 and l['coverage_pairs']==208
assert l['geometry_field_equalities']==219745 and l['geometry_boxes_inherited']==106496 and l['omitted_inherited']==62547
assert l['classifications']=={'inside':26079,'transition':16502,'straddle':1368}
g=v['source_geometry'];assert g['canonical_points_checked']==7810 and g['local_endpoint_equalities']==52
assert g['constants']['prior']==g['constants']['v22'] and g['source_constant_assignments_identical']
assert g['source_bodies']['cart_derivative_table']=='ABSENT_BOTH_NO_INHERITED_CLAIM'
for name,z in g['external_inputs'].items():
 assert z['checks_before_and_after'] and sha(Path(z['path']))==z['sha256'] and Path(z['path']).stat().st_size==z['bytes']
assert g['partition_sha256']==sha(B/'research/middle_residual/evidence/partition_exact.json')
for name,h in g['source_sha256'].items():assert sha(D/'source/src'/name)==h
merged_sha=manifest['files']['runs/forcing/v22_p9_merged.json']['source_sha256']
a,e=v['aggregate_arb'],v['aggregate_exact_iv'];assert a['row_count']==e['row_count']==43949 and a['row_order_sha256']==e['row_order_sha256']
assert a['source_sha256']==e['source_sha256']==merged_sha
comparisons=0;ceilings={'1':['0.7759','893.16','1.5700'],'500':['1.8107','1638.56','3.5769']}
for lam in ['1','500']:
 for k in ['J3','J4']:
  q=Q(e['results'][lam][k+'_exact']);z=a['results'][lam][k];assert Q(z['lower'])<=q<=Q(z['upper']);comparisons+=2
 for k in ['N3','N4','N31']:
  x,y=a['results'][lam][k],e['results'][lam][k];assert max(Q(x['lower']),Q(y['lower']))<=min(Q(x['upper']),Q(y['upper']));comparisons+=1
 j3,j4=[Q(e['results'][lam][k+'_exact']) for k in ['J3','J4']];c3,c4,c31=map(Q,ceilings[lam])
 assert j3<c3**2 and j4<c4**2 and j3**9*j4<c31**20
 assert Q(e['results'][lam]['saved_I3_margin'])>0 and Q(e['results'][lam]['saved_I4_margin'])>0
p=v['pointwise_series'];assert p['rows']==43949 and p['pointwise_checks_per_engine']==137235 and p['series_blocks']==p['tail_checks_per_engine']==331
assert p['classifications']==l['classifications'] and p['series_occurrences']==l['series_occurrences']==38445 and p['fallback_blocks']==43
assert Q(p['largest_saved_ratio'])<Q(3,5) and Q(p['tail_squared_relative_slack_min'])>0 and p['data_sha256']==merged_sha
c=v['cutoff_extrema'];assert c['rows']==43949 and c['checks']==263694 and c['inside']==26079 and c['transition']==17870 and c['failure_count']==0 and not c['partial']
assert c['data_sha256']==merged_sha
# Four early completed batches used the stronger original dmin>=0 assertion.
# Verify that the only program change was the harmless interval-domain assertion.
old=(D/'code/check_cutoff_exact_nonnegative_d0.py').read_text();new=(D/'code/check_cutoff_exact.py').read_text()
assert old.count('assert 0<=d0<=d1 and d0<rout')==1
assert old.replace('assert 0<=d0<=d1 and d0<rout','assert d0<=d1 and d1>=0 and d0<rout')==new
failure=read(D/'evidence/cutoff_full_bernstein_assertion_failure.json');assert failure['code_sha256']==sha(D/'code/check_cutoff_exact_nonnegative_d0.py')
assert len(failure['rows_failing_assertion'])==1 and failure['rows_failing_assertion'][0]['index']==20999
ranges=[];position=0;totalchecks=0;totalinside=0;subdivisions={}
# Select using explicit digit fields; assertion-failure records are not accepted.
chunk_paths=sorted(p for p in (D/'evidence').iterdir() if p.suffix=='.json' and len(p.stem.split('_'))==5 and p.stem.split('_')[:3]==['cutoff','full','bernstein'] and all(x.isdigit() for x in p.stem.split('_')[3:]))
for path in chunk_paths:
 z=read(path);assert z['status']=='PASS_V22_SIX_CUTOFF_FULL_POLYNOMIAL_BERNSTEIN' and z['failure_count']==0 and not z['failures']
 assert z['data_sha256']==merged_sha and z['start_index']==position and z['end_index']>position and z['rows']==z['end_index']-position
 assert z['checks']==6*z['rows'] and z['total_rows']==43949
 assert z['inside']+sum(z['subdivisions_used'].values())==z['rows']
 ranges.append({'start':position,'end':z['end_index'],'file':str(path.relative_to(B)),'sha256':sha(path),'engine_sha256':sha(D/'code'/('check_cutoff_exact_nonnegative_d0.py' if z['end_index']<=19000 else 'check_cutoff_exact.py'))})
 position=z['end_index'];totalchecks+=z['checks'];totalinside+=z['inside']
 for k,count in z['subdivisions_used'].items():subdivisions[k]=subdivisions.get(k,0)+count
assert position==43949 and totalchecks==263694 and totalinside==26079 and len(ranges)==9
cal=v['calculus'];assert cal['source_sha256']==g['source_sha256']['cert_forcing2.py'] and cal['cartesian_multiindices']==15 and cal['cartesian_table_entries']==30
assert cal['zeta_derivatives']==4 and cal['scalar_composition_orders']==5 and cal['leibniz_expressions']==7 and cal['binomial_ratio_checks']==16 and cal['centering_binomial_checks']==91
assert cal['leibniz_term_counts']==dict(f=1,fx=2,fy=2,lapf=6,lapfx=10,lapfy=10,lap2f=19)
raw=read(D/'source/runs/forcing/v22_p9_merged.json');negative=[i for i,z in enumerate(raw['cells']) if z['dmin']<0];assert negative==[20999]
assert Q.from_float(raw['cells'][20999]['dmin'])==-Q(1,2**1074) and Q.from_float(raw['cells'][20999]['dmax'])<Q(231,8000)
h=read(D/'evidence/cutoff_hessian_bounds_checked.json');assert h['status']=='PASS_AUXILIARY_HESSIAN_EXPORT_WITH_PROVED_CONSTANT_ZEROS' and h['rows']==len(h['T2F'])==43949
assert h['old_sha256']==sha(D/'evidence/cutoff_hessian_bounds.json') and h['data_sha256']==merged_sha and h['code_sha256']==sha(D/'code/check_hessian_export.py')
assert h['constant_zero_repairs']==26079 and h['checks']==43949
for z,row in zip(h['T2F'],raw['cells']):assert math.isfinite(z) and 0<=z<=row['T2F']
for group in ['source/src','source/runs/forcing','code','evidence']:
 for path in sorted((D/group).iterdir()):
  if path.is_file() and path.name not in ['finite_audit.json','verdict.json','review_packet.json']:pins[str(path.relative_to(B))]=sha(path)
for path in sorted(D.iterdir()):
 if path.is_file() and path.suffix=='.md':pins[str(path.relative_to(B))]=sha(path)
for path in [prior_path,D/'source/NUM_REPORT.md']:pins[str(path.relative_to(B))]=sha(path)
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_V22_FINITE_AUDIT_REVIEW_PENDING_PHYSICAL_OPEN',prior_pins=208,snapshots=33,source_data_sha256=merged_sha,cross_engine_comparisons=comparisons,row_count=43949,part_pairs=208,geometry_cases_inherited_each_engine=106496,geometry_field_equalities=219745,canonical_partition_points=7810,pointwise_checks_each_engine=137235,series_tails_each_engine=331,cutoff_checks_each_engine=263694,nonconstant_cutoff_rows=17870,inside_cutoff_rows=26079,exact_cutoff_ranges=ranges,exact_cutoff_subdivisions=subdivisions,harmless_negative_distance_lower_endpoint=20999,conditional_strict_norm_ceilings=ceilings,external_inputs=g['external_inputs'],pins=dict(sorted(pins.items())),scope='Conditional finite theorem only, PROOF and mandatory addenda. H0/H1/H2 and all physical forcing conclusions OPEN. In particular the five nonlinear residual jets need their own physical construction audit beyond the queued P/R value-model audit101. The unretained B3 derivative suprema have separate unresolved ancestry.')
(D/'evidence/finite_audit.json').write_text(json.dumps(out,indent=2)+'\n')
packet={k:z for k,z in out.items() if k!='pins'};packet['finite_audit_sha256']=sha(D/'evidence/finite_audit.json');packet['pin_count']=len(pins)
(D/'evidence/review_packet.json').write_text(json.dumps(packet,indent=2)+'\n');print(out['utc'],out['status'],len(pins),'pins',comparisons,'cross engine comparisons')
