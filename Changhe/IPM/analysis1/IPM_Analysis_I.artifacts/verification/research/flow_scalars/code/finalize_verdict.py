"""Final exact source, evidence, projection and whole-review binding."""
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/flow_scalars';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for z in iter(lambda:f.read(2**20),b''):h.update(z)
 return h.hexdigest()
def load(n):return json.loads((E/n).read_text())
c=load('checks.json');a=load('saved_audit.json');m=load('metadata_audit.json');p=load('projection_audit.json')
assert c['status']=='PASS_FINITE_RECONSTRUCTED_SCALARS_ONLY' and a['status']=='PASS_FRESH_ALL_SCALARS' and m['status']=='PASS_METADATA_AND_FULL_EXPORTED_ENDPOINTS'
assert a['producer_checks_sha256']==sha(E/'checks.json') and a['array_sha256']==c['array_sha256']==sha(E/'scalar_arrays.npz')
for f,h in c['files'].items():assert sha(f)==h,f
assert a['self_sha256']==sha(D/'code/audit_saved.py')
assert m['self_sha256']==sha(D/'code/check_metadata.py') and m['addendum_sha256']==sha(D/'ADDENDUM.md') and m['arrays_sha256']==c['array_sha256'] and m['checks']==96945
assert Q(m['max_rounded_ode_x_exact'])<=1
assert p['checks_sha256']==sha(E/'checks.json') and p['counts_sha256']==sha(E/'review_counts.json') and p['constants']==444 and p['status']=='PASS_PROJECTION_AND_INDEPENDENT_CONSTANT_TARGETS'
for f,h in load('execution_source_pins.json').items():assert sha(B/f)==h,f
for reg,v in m['regions'].items():
 f=B.parent/'ipmA-num/data'/('cert_green.npz' if reg=='middle' else 'cert_'+reg+'_green.npz');assert v['npz_sha256']==c['files'][str(f)]
assert all(v['returncode']==0 for v in load('serial_runtime.json')['steps']) and load('metadata_runtime.json')['returncode']==0
assert load('review_counts.json')=={k:v for k,v in c.items() if k!='constants'}
expected={f'inv_{j}':Q(1,j) for j in range(1,14)}
expected.update({f'inv4n_{n}':Q(1,4*n) for n in range(1,262)})
expected['cl']=1/Q(1615536043799051,9007199254740992)
expected.update({f'Bern_{r}_{i}':Q(math.comb(r,i),math.comb(12,i)) if i<=r else Q(0) for r in range(13) for i in range(13)})
assert len(c['constants'])==len(expected)==444 and {v['name'] for v in c['constants']}==set(expected)
for v in c['constants']:
 q=expected[v['name']];m0,r0=map(lambda s:Q(float.fromhex(s)),[v['mid_hex'],v['rad_hex']]);assert Q(v['exact'])==q and m0-r0<=q<=m0+r0
assert c['counts']['positive_cell_width_and_ode_hypothesis']==a['counts']['cells']==19389
assert c['counts']['exact_power_upper_comparisons']==a['counts']['fresh_rational_power_upper']==523503
assert c['counts']['rational_constant_contains']==a['counts']['fresh_constant_contains']==444
assert sum(v['r_hull_bitwise_matches_to_recorded'] for v in c['regions'].values())==19389
for name in ['serial_runtime.json','metadata_runtime.json']:
 run=load(name)
 assert run.get('resumed_worker',False) or run.get('resumed_utc') or run.get('resume_utc'),(name,run)
files={};reviews={}
for tag in ['flow_scalars_proof','flow_scalars_closure','flow_scalars_final']:
 path=B/'notes/reviews';meta=json.loads((path/(tag+'_metadata.json')).read_text());request=(path/(tag+'_request.txt')).read_text();ans=(path/(tag+'_response.md')).read_text();raw=json.loads((path/(tag+'_response.json')).read_text())
 assert meta['actual_response_model']==raw['model']=='claude-opus-5-5' and meta['stop_reason']==raw['stop_reason']=='end_turn' and len(ans)>200
 assert ans=='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n'
 assert hashlib.sha256(request.encode()).hexdigest()==meta['input_sha256']
 marker='\n\nFILE '+meta['files'][0]+'\n';assert request.count(marker)==1
 rebuilt=request.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in meta['files']);assert rebuilt==request,tag
 if tag=='flow_scalars_final':assert 'FINAL VERDICT: ACCEPT_STATED_SCALAR_SCOPE' in ans[:150]
 reviews[tag]={k:meta[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  f=path/(tag+'_'+suffix);files[str(f.relative_to(B))]=sha(f)
for f in D.rglob('*'):
 if f.is_file() and f.name!='verdict.json':files[str(f.relative_to(B))]=sha(f)
for f,h in c['files'].items():files[f]=h
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FINITE_SCALAR_SCOPE_ONLY','scope':'All19389 finite cells: middle7809 outer8948 inner2632. Reconstructed scalar operations and exact radial geometry only.','confirmed':['Exact partition point containment and cell-width upper bounds.','All444 scalar rational constants enclose independently reconstructed exact targets.','All523503 h powers dominate exact powers; rounded maximal ODE522 step at most1.','Whole start-ball exponentials and whole reciprocal E intervals enclosed, checked by exact endpoint and independent interval engines.','Both exact partition radial endpoints and whole exported end-ball radius enclosed by rlo/rhi.','Rational mu image of full radial interval enclosed.','Nf261 all coefficient NPY headers, bases, hsub and partition metadata checked.'],'counts':c['counts'],'fresh_counts':a['counts'],'metadata_checks':m,'projection_check':'Exact JSON projection after removing only constants; independent complete444-name target reconstruction in finalizer. No byte-identity claim.','reviews':reviews,'open':['Full radial Taylor and ODE models, truncation/tail and exponential tolerances','Common Taylor variable anchoring and application of h powers','Matrix products and historical runtime arithmetic','Angular coefficient coverage outside independently audited subset','Full cell_bounds, field inequalities and historical aggregate provenance','Any full IPM inverse or decisive YES/NO endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
