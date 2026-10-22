"""Cross-bind two arithmetic engines, geometry, coverage and source snapshots."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1]
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
prior=read(B/'research/localized_forcing/evidence/verdict.json');pins=dict(prior['files']);assert len(pins)==139
for f,h in pins.items():assert sha(B/f)==h,f
names=['calculus','aggregate_arb','aggregate_exact_iv','geometry_arb','geometry_iv','parts','public','blocks'];v={k:read(D/('evidence/'+k+'.json')) for k in names}
assert all(x['status'].startswith('PASS') for x in v.values())
a,e=v['aggregate_arb'],v['aggregate_exact_iv'];assert a['row_count']==e['row_count']==43949 and a['row_order_sha256']==e['row_order_sha256'];comparisons=0
for lam in ['1','500']:
 for k in ['J3','J4']:
  q=Q(e['results'][lam][k+'_exact']);z=a['results'][lam][k];assert Q(z['lower'])<=q<=Q(z['upper']);comparisons+=2
 for k in ['N3','N4','N31']:
  x,y=a['results'][lam][k],e['results'][lam][k];assert max(Q(x['lower']),Q(y['lower']))<=min(Q(x['upper']),Q(y['upper']));comparisons+=1
for k in ['geometry_arb','geometry_iv']:assert v[k]['included']==43949 and v[k]['omitted']==62547
assert v['parts']['part_count']==26 and v['parts']['cell_angle_pairs']==208 and v['parts']['exact_row_count']==43949 and v['parts']['prior_pins_checked']==139
assert v['parts']['regimes']==dict(v['geometry_arb']['regimes'],outside=62547,fallback_block=43)
assert v['calculus']['cartesian_multiindices']==15 and v['calculus']['cartesian_table_entries']==30 and v['calculus']['leibniz_expressions']==7
assert v['public']['table_count']==42
assert v['blocks']['coordinate_identities']==3744 and v['blocks']['outward_power_checks']==598 and v['blocks']['normal_weight_checks']==6669
# Pin the new result's own finite sources, proofs and outputs; no broad walk.
for group in ['source/src','source/runs/forcing','code','evidence']:
 for p in sorted((D/group).iterdir()):
  if p.is_file() and p.name not in ['finite_audit.json','verdict.json']:pins[str(p.relative_to(B))]=sha(p)
for name in ['PROOF.md','ADDENDUM.md','source/NUM_REPORT_7_10.md']:
 p=D/name;pins[str(p.relative_to(B))]=sha(p)
p=B/'research/localized_forcing/evidence/verdict.json';pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_V21_FINITE_AUDIT_REVIEW_PENDING_PHYSICAL_OPEN','prior_pins':139,'cross_engine_comparisons':comparisons,'row_count':43949,'geometry_each_engine':106496,'regime_checks_exact':43949,'part_pairs':208,'public_upward_displays':42,'new_block_power_checks':598,'new_block_normal_weight_checks':6669,'coordinate_identities':3744,'conditional_norm_ceilings':{'1':['0.7759','893.16','1.5700'],'500':['1.8107','1638.56','3.5769']},'pins':dict(sorted(pins.items())),'scope':'Finite identities, data aggregation and geometry. Physical model validity, individual series scalars and historical source execution OPEN.'}
(D/'evidence/finite_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(pins),'pins')
