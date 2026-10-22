"""Supplementary explicit inherited-input, dimension, chronology and label audit."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_bernstein';S=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
plan=load(D/'data_exact/arithmetic_plan.json');audit=load(D/'evidence/output_audit.json');pins=dict(audit['files']);assert audit['status']=='PASS_COMPLETE_THREE_CELL_BERNSTEIN_RANGE_AUDIT'
for n,h in pins.items():assert sha(B/n)==h
needed=[S/'evidence/output_audit.json',S/'evidence/verdict.json',S/'evidence/label_audit.json']+[S/'evidence'/('%s_%d.json'%(kind,cell)) for cell in [4102,4125,4211] for kind in ['arb','iv']]
for p in needed:
 n=str(p.relative_to(B));assert n in plan['files'] and n in pins and sha(p)==plan['files'][n]==pins[n]
assert pins['research/residual_cell_cauchy/evidence/verdict.json']=='c5ac5d88fde1a9e92925c45af26bdac920841a0378830027d4a9535565c1a04c'
old=load(S/'evidence/output_audit.json');labels=load(S/'evidence/label_audit.json');assert labels['status']=='PASS_EXPLICIT_SAVED_ROW_BINDING_AND_ALL_LABELS' and labels['source_rows_checked']==7809
lengths=0;orders=0;chronology=0
for cell in [4102,4125,4211]:
 for kind in ['arb','iv']:
  obj=load(S/'evidence'/('%s_%d.json'%(kind,cell)));assert obj['cell']==cell and obj['degree']==64 and obj['modes']==522 and len(obj['coefficient_boxes'])==522
  for row in obj['coefficient_boxes']:assert len(row)==65;lengths+=1
 for chunk in range(9):
  p=D/'evidence'/('exact_%d_%d.json'%(cell,chunk));q=D/'evidence'/('subdivision_%d_%d.json'%(cell,chunk));x=load(p);y=load(q);n=str(p.relative_to(B));assert n in y['files'] and sha(p)==y['files'][n]==pins[n]
  assert datetime.fromisoformat(plan['utc'])<datetime.fromisoformat(x['utc'])<datetime.fromisoformat(y['utc'])<datetime.fromisoformat(audit['utc']);chronology+=1
 orig=next(x for x in old['records'] if x['cell']==cell);new=next(x for x in audit['records'] if x['cell']==cell);expected={'W_%d_%d'%(i,j) for i in range(6) for j in range(6-i)};assert set(orig['bounds'])==set(new['bounds'])==expected
 for k in ['left_exact','right_exact','h_exact']:assert orig[k]==new[k]
 for k in expected:
  assert orig['bounds'][k]['tail_upper_exact']==new['bounds'][k]['inherited_tail_upper_exact'] and orig['bounds'][k]['total_upper_exact']==new['bounds'][k]['old_total_upper_exact'];orders+=1
assert (lengths,orders,chronology)==(3132,63,27)
for p in [D/'evidence/output_audit.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():assert sha(B/n)==h
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXPLICIT_INPUT_PINS_DIMENSIONS_CHRONOLOGY_AND_ORDER_BINDING','inherited_paths_explicitly_checked':len(needed),'coefficient_row_dimensions_checked':lengths,'cell_derivative_bindings':orders,'chunk_chronology_and_primary_pins_checked':chronology,'source_saved_row_ids_inherited':7809,'files':dict(sorted(pins.items())),'scope':'Supplementary completed-output guards. No added radial cover or canonical integration.'}
with (D/'evidence/guard_audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:v for k,v in out.items() if k!='files'}))
