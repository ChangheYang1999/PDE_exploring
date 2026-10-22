"""Complete new-source provenance and transfer of unchanged, audited physical geometry."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter,defaultdict
from datetime import datetime,timezone
import json,gzip,hashlib,sys,ast,math,time
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];P=B/'research/forcing_composed_cutoff';tic=time.monotonic()
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def key(r):return (r['ci'],r['q'],32*r['bs']+r['ks'],4*r['bp']+r['kp'])
manifest=read(D/'evidence/snapshot_manifest.json');original_bytes=0
for n,r in manifest['files'].items():
 p=B/r['snapshot'];assert sha(p)==r['snapshot_sha256'];raw=p.read_bytes();raw=gzip.decompress(raw) if r['compressed_gzip'] else raw;assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['source_sha256'];original_bytes+=len(raw)
published={r.split()[1]:r.split()[0] for r in (D/'source/runs/forcing/SHA256.txt').read_text().splitlines()}
for n in ['src/cert_forcing.py','src/cert_forcing2.py','src/cert_resid.py','runs/forcing/v22_p9_merged.json']:assert published[n]==manifest['files'][n]['source_sha256'],n
old=read(P/'source/runs/forcing/v21_p9_merged.json');cur=read(D/'source/runs/forcing/v22_p9_merged.json');meta=['green','trial','delta','cutoff','cutoff_smoothness','cutoff_poly_step','s','KSUB','ntheta','KP','Qs','Qp','nbs','nbp','Kser','theta_max','radial_cells_cover','x_star_bracket','n_angular_cells','n_radial_cells','radial_cells','chunk','qchunk','partial']
assert all(old[n]==cur[n] for n in meta)
oldrows={key(r):r for r in old['cells']};assert len(oldrows)==len(old['cells'])==43949
geometry_fields=['dmin','dmax','area','sigma','regime'];same_geometry=same_present=0;comparisons=Counter();series=defaultdict(set);block_rems=defaultdict(set);parent_rems=defaultdict(set);newrows={};class_count=Counter();series_row_count=0
req=['G0','G1','G2F','GL','GL1','GL2','T0','T1','T2F','TL','TL1','TL2','F0','F1','FL','FL1','FL2','rem_D','rem_lap','rem_f','rem_tau','series']
for r in cur['cells']:
 k=key(r);assert k in oldrows and k not in newrows;newrows[k]=r;o=oldrows[k];assert all(r[n]==o[n] for n in geometry_fields);same_geometry+=len(geometry_fields)
 assert 4096<=r['ci']<=4108 and 0<=r['q']<16 and 0<=r['bs']<2 and 0<=r['bp']<2 and 0<=r['ks']<32 and 0<=r['kp']<4
 assert all(n in r for n in req)
 for n in req[:17]:assert isinstance(r[n],(int,float)) and math.isfinite(r[n]) and r[n]>=0
 assert set(r['rem_D'])=={f'{a}_{b}' for a in range(5) for b in range(5-a)} and len(r['rem_lap'])==4
 assert all(math.isfinite(v) and v>=0 for v in [*r['rem_D'].values(),*r['rem_lap']])
 parent=(r['ci'],r['q']);block=(*parent,r['bs'],r['bp']);parent_rems[parent].add(json.dumps([r['rem_D'],r['rem_lap']],sort_keys=True,separators=(',',':')))
 for n in ['G0','GL2']:
  comparisons[n+('_equal' if r[n]==o[n] else ('_increased' if r[n]>o[n] else '_decreased'))]+=1;same_present+=1
 for n in ['F0','F1','FL','FL1','FL2']:comparisons[n+('_equal' if r[n]==o[n] else '_changed')]+=1
 class_count[r['regime']]+=1
 vals=r['series'];assert (vals is None)==(r['rem_f'] is None)==(r['rem_tau'] is None)==(r['tau_sup'] is None)
 if vals is not None:
  assert len(vals)==3 and all(math.isfinite(v) and v>=0 for v in vals) and vals[0]>0 and vals[1]<.6 and vals[2]>0
  assert len(r['rem_f'])==len(r['rem_tau'])==7 and all(math.isfinite(v) and v>=0 for v in r['rem_f']+r['rem_tau']);series[block].add(tuple(vals));series_row_count+=1
  block_rems[block].add(json.dumps([r['rem_f'],r['rem_tau']],separators=(',',':')))
 else:assert r['regime']!='transition'
 if r['regime']=='inside':assert Q.from_float(r['dmax'])<=Q(231,8000)
 elif r['regime']=='transition':assert Q.from_float(r['dmin'])>=Q(231,8000) and Q.from_float(r['dmax'])<=Q(297,8000)
 else:assert r['regime']=='straddle'
assert set(newrows)==set(oldrows) and len(newrows)==43949 and same_geometry==219745 and same_present==87898
assert all(len(v)==1 for v in series.values()) and all(len(v)==1 for v in block_rems.values()) and all(len(v)==1 for v in parent_rems.values())
# Reconstruct the complete current merge from all independently snapshotted parts.
partmeta=meta[:meta.index('n_radial_cells')]+['code_version','done'];coverage=set();rows=[];counts=Counter();maxima={b:{k:0 for k in cur['sup_D_eps'][b]} for b in ['B94','B3']};worst={k:0 for k in cur['worst_series']};sums={l:{k:Q(0) for k in ['I3','I4']} for l in cur['results']};areas={b:Q(0) for b in cur['area_sum']};part_rows=[]
for name in cur['merged_from']:
 p=D/'source'/name;p=p.with_suffix(p.suffix+'.gz');z=json.loads(gzip.decompress(p.read_bytes()));assert all(z[n]==cur[n] for n in partmeta),name
 own={(ci,q) for ci in z['chunk'] for q in range(z['qchunk'][0],z['qchunk'][1]+1)};assert len(own)==8 and not own&coverage;coverage|=own;assert z['partial'] and z['n_radial_cells']==1 and z['radial_cells']==[z['chunk'][0]]*2
 assert len(z['cells'])==z['n_subcells_in_support'] and all((r['ci'],r['q']) in own for r in z['cells'])
 rc=Counter(r['regime'] for r in z['cells']);assert all(rc[k]==z['regime_count'][k] for k in ['inside','transition','straddle'])
 assert sum(z['regime_count'][k] for k in ['inside','transition','straddle','outside'])==8*64*8
 rows+=z['cells'];counts.update(z['regime_count']);part_rows.append([name,len(z['cells'])])
 for b in maxima:
  for k in maxima[b]:maxima[b][k]=max(maxima[b][k],z['sup_D_eps'][b][k])
  areas[b]+=Q.from_float(z['area_sum'][b])
 for k in worst:worst[k]=max(worst[k],z['worst_series'][k])
 for l in sums:
  for k in sums[l]:sums[l][k]+=Q.from_float(z['results'][l][k])
assert len(part_rows)==26 and coverage=={(ci,q) for ci in range(4096,4109) for q in range(16)} and rows==cur['cells']
assert dict(counts)==cur['regime_count'] and maxima==cur['sup_D_eps'] and worst==cur['worst_series']
for l in sums:
 for k in sums[l]:assert sums[l][k]<=Q.from_float(cur['results'][l][k])
for b in areas:assert areas[b]<=Q.from_float(cur['area_sum'][b])
# Changed generator metadata is not covered by an older source proof; only identify exact unchanged bodies here.
unchanged={}
for file,names in [('cert_forcing.py',['cart_from_polar','finish']),('cert_forcing2.py',['cart_derivative_table','Recentre','add_const'])]:
 ot=ast.parse((P/'source/src'/file).read_text());nt=ast.parse((D/'source/src'/file).read_text())
 for name in names:
  aa=[n for n in ot.body if getattr(n,'name',None)==name];bb=[n for n in nt.body if getattr(n,'name',None)==name]
  if not aa or not bb:continue
  assert len(aa)==len(bb)==1 and ast.dump(aa[0],include_attributes=False)==ast.dump(bb[0],include_attributes=False)
  unchanged[file+':'+name]=hashlib.sha256(ast.dump(bb[0],include_attributes=False).encode()).hexdigest()
prior=read(P/'evidence/verdict.json');assert len(prior['files'])==208
for f,h in prior['files'].items():assert sha(B/f)==h,f
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_V22_PROVENANCE_UNCHANGED_PHYSICAL_GEOMETRY_AND_ROW_STRUCTURE','snapshots':len(manifest['files']),'original_bytes':original_bytes,'published_source_data_hashes_match':True,'rows':len(newrows),'geometry_field_equalities':same_geometry,'geometry_boxes_inherited':106496,'omitted_inherited':62547,'uniform_block_series':len(series),'series_occurrences':series_row_count,'uniform_parent_remainders':len(parent_rems),'uniform_block_remainders':len(block_rems),'required_new_fields':req,'classifications':dict(class_count),'comparisons_to_v21':dict(comparisons),'part_count':26,'coverage_pairs':208,'part_rows':part_rows,'prior_pins_rehashed':208,'unchanged_source_bodies':unchanged,'scope':'New pinned pair, exact geometry transfer, metadata and complete row structure only. Remainder fields and scalar triples do not attest missing full models or historical runtime.'}
(D/'evidence/linkage.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],len(series),series_row_count)
