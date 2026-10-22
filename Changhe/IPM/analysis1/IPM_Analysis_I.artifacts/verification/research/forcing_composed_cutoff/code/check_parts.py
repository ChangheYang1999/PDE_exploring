"""Authenticate all snapshots and compare complete part coverage and exact rows."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from datetime import datetime,timezone
import hashlib,json,gzip,sys,time
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];start=time.monotonic()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1048576),b''):h.update(v)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
manifest=read(D/'evidence/snapshot_manifest.json');nbytes=0
for name,r in manifest['files'].items():
 p=B/r['snapshot'];assert sha(p)==r['snapshot_sha256'];v=p.read_bytes();v=gzip.decompress(v) if r['compressed_gzip'] else v
 assert len(v)==r['bytes'] and hashlib.sha256(v).hexdigest()==r['source_sha256'];nbytes+=len(v)
x=read(D/'source/runs/forcing/v21_p9_merged.json');meta=['green','trial','delta','cutoff','cutoff_smoothness','cutoff_poly_step','s','KSUB','ntheta','KP','Qs','Qp','nbs','nbp','Kser','theta_max','radial_cells_cover','x_star_bracket','n_angular_cells','code_version','done']
cover=set();rows=[];reg=Counter();sup={b:{k:0 for k in x['sup_D_eps'][b]} for b in ['B94','B3']};worst={k:0 for k in x['worst_series']};results={l:{k:Q(0) for k in ['I3','I4']} for l in x['results']};areas={b:Q(0) for b in ['B94','B3']};partinfo=[]
for name in x['merged_from']:
 p=D/'source'/name;p=p.with_suffix(p.suffix+'.gz');y=json.loads(gzip.decompress(p.read_bytes()))
 assert all(y[k]==x[k] for k in meta) and y['partial'] and len(y['chunk'])==1 and y['n_radial_cells']==1
 assert y['radial_cells']==[y['chunk'][0]]*2
 own={(ci,q) for ci in y['chunk'] for q in range(y['qchunk'][0],y['qchunk'][1]+1)};assert not cover&own and len(own)==8;cover|=own
 assert all((r['ci'],r['q']) in own for r in y['cells'])
 count=Counter(r['regime'] for r in y['cells']);assert len(y['cells'])==y['n_subcells_in_support'] and sum(y['regime_count'][k] for k in ['inside','transition','straddle','outside'])==8*64*8
 for k in ['inside','transition','straddle']:assert count[k]==y['regime_count'][k]
 reg.update(y['regime_count']);rows+=y['cells']
 for b in sup:
  for k in sup[b]:sup[b][k]=max(sup[b][k],y['sup_D_eps'][b][k])
  areas[b]+=Q.from_float(y['area_sum'][b])
 for k in worst:worst[k]=max(worst[k],y['worst_series'][k])
 for l in results:
  for k in results[l]:results[l][k]+=Q.from_float(y['results'][l][k])
 partinfo.append({'name':name,'coverage':sorted(own),'rows':len(y['cells'])})
assert len(partinfo)==26 and cover=={(ci,q) for ci in range(4096,4109) for q in range(16)}
assert rows==x['cells'] and len(rows)==43949 and dict(reg)==x['regime_count'] and sup==x['sup_D_eps'] and worst==x['worst_series']
assert not x['partial'] and x['chunk']==list(range(4096,4109)) and x['radial_cells']==x['radial_cells_cover']==[4096,4108] and x['qchunk']==[0,15]
for l in results:
 for k in results[l]:assert results[l][k]<=Q.from_float(x['results'][l][k])
for b in areas:assert areas[b]<=Q.from_float(x['area_sum'][b])
# Exact second regime check: do not rely on an Arb comparison or rounded sigmas.
regimechecks=0
for r in rows:
 assert 0<=r['bs']<2 and 0<=r['bp']<2 and 0<=r['ks']<32 and 0<=r['kp']<4
 a,b=map(Q.from_float,[r['dmin'],r['dmax']]);s=(a-Q(231,8000))*Q(4000,33);t=(b-Q(231,8000))*Q(4000,33)
 assert Q.from_float(r['sigma'][0])<=s<=t<=Q.from_float(r['sigma'][1])
 if r['regime']=='inside':assert b<=Q(231,8000)
 if r['regime']=='transition':assert Q(231,8000)<=a<=b<=Q(297,8000)
 regimechecks+=1
prior=read(B/'research/localized_forcing/evidence/verdict.json');assert len(prior['files'])==139
for f,h in prior['files'].items():assert sha(B/f)==h,f
published={r.split()[1]:r.split()[0] for r in (D/'source/runs/forcing/SHA256.txt').read_text().splitlines()}
versions={n:{'published':published[n],'current_snapshot':manifest['files'][n]['source_sha256'],'equal':published[n]==manifest['files'][n]['source_sha256']} for n in ['src/cert_forcing.py','src/cert_forcing2.py','src/cert_resid.py','runs/forcing/v21_p9_merged.json','runs/forcing/v11_p9_merged.json']}
assert not versions['src/cert_forcing.py']['equal'] and not versions['src/cert_forcing2.py']['equal']
assert all(versions[n]['equal'] for n in ['src/cert_resid.py','runs/forcing/v21_p9_merged.json','runs/forcing/v11_p9_merged.json'])
missing=sorted(set(['G0','G1','G2F','GL','GL1','GL2','T0','T1','T2F','TL','TL1','TL2'])-set(rows[0]))
assert all(set(r)==set(rows[0]) for r in rows)
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_V21_PARTS_AND_PROVENANCE_SCOPE','snapshots':len(manifest['files']),'original_bytes':nbytes,'part_count':len(partinfo),'cell_angle_pairs':len(cover),'exact_row_count':len(rows),'regime_checks':regimechecks,'regimes':dict(reg),'prior_pins_checked':len(prior['files']),'source_versions':versions,'missing_row_fields':missing,'individual_series_operands_present':False,'parts':partinfo,'scope':'Data and current-source separation explicit. No historical execution or physical model certification.'}
(D/'evidence/parts.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],out['missing_row_fields'])
