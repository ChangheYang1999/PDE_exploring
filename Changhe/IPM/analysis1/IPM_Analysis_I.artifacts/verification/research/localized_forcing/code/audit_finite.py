"""Authenticate the completed finite components without promoting the forcing norm."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
D=Path(__file__).resolve().parents[1];B=D.parents[1]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1024*1024),b''):h.update(c)
 return h.hexdigest()
def read(s):return json.loads((D/'evidence'/s).read_text())
m=read('snapshot_manifest.json');pins={};bytes_total=0;live_changes=[]
for ent in m['sources'].values():
 p=B/ent['snapshot'];assert p.stat().st_size==ent['bytes'] and sha(p)==ent['sha256'];pins[ent['snapshot']]=ent['sha256'];bytes_total+=ent['bytes']
 live=Path(ent['source']);h=sha(live)
 if h!=ent['sha256']:live_changes.append({'source':str(live),'snapshot':ent['sha256'],'current':h})
assert sha(D/'PROOF.md')==m['proof_sha256']
a=read('aggregate_audit.json');assert a['rows']==43949 and a['parts']==13 and a['status']=='CONFIRMED_CONDITIONAL_SAVED_ROW_POSTPROCESSING_ONLY'
assert a['merged_sha256']==m['sources']['runs/forcing/p9_K64_n16_P8_merged.json']['sha256']
assert a['midrad_sha256']==m['sources']['src/midrad.py']['sha256'] and a['new_source_sha256']==m['sources']['src/cert_resid.py']['sha256']
g=read('geometry_arb.json');v=read('geometry_iv.json');assert not g['failure_count'] and not v['failures'] and g['rows_checked']==v['included']==43949 and g['omitted_cells_checked']==v['omitted']==62547
assert g['all_cells']==106496 and g['power_checks']==356
assert g['green_sha256']==v['green_sha256']==sha(Path(g['green_path']))
cover=read('coverage.json');part=B/'research/middle_residual/evidence/partition_exact.json';assert sha(part)==cover['partition_sha256'];assert cover['exact_points']==7810 and len(cover['local_points'])==14 and cover['exact_checks']==71
cut=read('cutoff_extrema.json');assert cut['rows']==43949 and cut['partial'] is False and cut['checks']==219745 and cut['failure_count']==0
paths=sorted((D/'evidence').glob('cutoff_iv_[0-9]*_[0-9]*.json'));start=rows=checks=inside=0
for p in paths:
 c=json.loads(p.read_text());assert c['status']=='PASS_FINITE_CUTOFF_SECOND_METHOD' and c['failure_count']==0 and c['total_rows']==43949 and c['start_index']==start
 assert c['end_index']-c['start_index']==c['rows'];start=c['end_index'];rows+=c['rows'];checks+=c['checks'];inside+=c['inside']
assert len(paths)==8 and start==rows==43949 and checks==219745 and inside==cut['inside']==26079
cart=read('cartesian_identity.json');assert cart['operators']==15 and cart['commutation_checks']==15 and cart['nonzero_Laurent_jet_terms']==404 and cart['source_sha256']==m['sources']['src/cert_forcing.py']['sha256']
pr=read('product_lemma_audit.json');assert pr['K_values']==1023 and pr['coefficient_enclosures']==274 and pr['proof_sha256']==sha(D/'MULTIPLICATION_LEMMA.md')
pos=read('positive_sums.json');assert pos['exact_constant_checks']==16384 and pos['normal_power_products']==5525 and pos['exact_native_integer_powers']==2615
assert F(pos['r2_counterexample']['exact_over_eta'])>F(pos['r2_counterexample']['returned_over_eta'])
reg=read('regularity.json');assert reg['simple_interior_knots']==1557 and reg['degree']==7 and reg['source_sha256']==sha(B/'data_exact/modal_v2.json')
for file,proof in [('positive_sums_proof_first.json','POSITIVE_SUMS.md'),('regularity_proof_first.json','LOCAL_REGULARITY.md')]:assert read(file)['sha256']==sha(D/proof)
pub=read('public_bounds_audit.json');assert pub['failed_ceiling_count']==22 and pub['total']==36
# Current completed component files are pinned. Samples and historical failed
# checker attempts are retained but never counted as completed certificates.
files=list((D/'code').glob('*.py'))+list(D.glob('*.md'))
files += [D/'evidence'/s for s in ['snapshot_manifest.json','aggregate_audit.json','geometry_arb.json','geometry_iv.json','coverage.json','cutoff_extrema.json','cartesian_identity.json','product_lemma_audit.json','positive_sums.json','regularity.json','public_bounds_audit.json','positive_sums_proof_first.json','regularity_proof_first.json']]+paths
for p in files:pins[str(p.relative_to(B))]=sha(p)
for p in [part,B/'data_exact/modal_v2.json',Path(g['green_path'])]:pins[str(p.relative_to(B)) if p.is_relative_to(B) else str(p)]=sha(p)
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FINITE_COMPONENTS_ONLY_FULL_FORCING_OPEN','snapshot_files':len(m['sources']),'snapshot_bytes':bytes_total,'cutoff_second_chunks':len(paths),'cutoff_rows':rows,'cutoff_checks_per_engine':checks,'geometry_total':g['all_cells'],'inward_endpoint_exports':cut['inward_sigma_exports'],'live_source_changes':live_changes,'pins':pins,'open':['canonical finite Green and spline input linkage','full radial residual Taylor models and inherited remainder operations','actual matrix/tensordot/bincount evaluation conditions or independent replacement enclosures','actual angular r2 positive sums without a generic underflow allowance','full polar/Cartesian/Bernstein input-specific composition','per-row missing G2F,T2F for FL1/FL2 arithmetic replay','historical producing-source attestation','physical localized forcing norm and every global a posteriori endpoint'],'scope':'Only named finite geometry, cutoff, aggregation and universal algebra/arithmetic lemmas at their stated hypotheses. Does not accept an actual forcing constant.'}
(D/'evidence/finite_audit.json').write_text(json.dumps(o,indent=2)+'\n');print(o['utc'],o['status'],len(pins),'pins',len(live_changes),'live changes')
