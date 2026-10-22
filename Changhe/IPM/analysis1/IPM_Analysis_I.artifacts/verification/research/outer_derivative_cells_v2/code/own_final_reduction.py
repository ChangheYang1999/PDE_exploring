"""Independent FLINT rational reduction of all completed exterior rows."""
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[3];E=R/'research/outer_derivative_cells_v2/evidence'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[json.loads(x) for x in (E/'full_rows.jsonl').read_text().splitlines()];head,*rows=rows
s=json.loads((E/'full_summary.json').read_text());a=json.loads((E/'full_audit.json').read_text());assert len(rows)==89 and [r['cell'] for r in rows]==list(range(89)) and head['indices']==list(range(89))
assert s['full_exterior'] and a['status']=='PASS_COMPLETE_EXTERIOR_SAVED_OUTPUT_AUDIT';assert s['rows_sha256']==a['rows_sha256']==sha(E/'full_rows.jsonl')
for j,row in enumerate(rows):
 for key in ['arb','iv']:
  z=row[key];assert F(z['left_exact'])<F(z['right_exact'])
  if j:assert F(rows[j-1][key]['right_exact'])==F(z['left_exact'])
  assert F(z['left_exact'])==F(row['arb']['left_exact']) and F(z['right_exact'])==F(row['arb']['right_exact'])
  for x in z['norm_squares']:assert 0<=F(x['lower_exact'])<=F(x['upper_exact'])
assert F(rows[0]['arb']['left_exact'])==0 and F(rows[-1]['arb']['right_exact'])==17
records=[]
for j in range(2):
 maxima=[max(Q(r[k]['norm_squares'][j]['upper_exact']) for k in ['iv','arb']) for r in rows]
 total=sum(reversed(maxima),Q(0));assert total==Q(s['cell_squares_upper_exact'][j]);tail=Q(s['accepted_tail_squares_upper_exact'][j]);combined=total+tail;assert combined==Q(s['combined_squares_upper_exact'][j])
 ceil=Q(str(F(s['norms']['strict_decimal_ceilings'][j])));assert ceil>0 and ceil*ceil>combined
 idx=max(range(89),key=lambda i:maxima[i]);assert idx==a['maximum_contribution_cells'][j]
 for engine in ['arb512','iv200']:
  z=s['norms'][engine][j];lo,hi=Q(z['lower_exact']),Q(z['upper_exact']);assert 0<lo<=hi<ceil and lo*lo<=combined<=hi*hi
 records.append({'norm_index':j,'cell_sum_exact':str(total),'tail_square_exact':str(tail),'combined_square_exact':str(combined),'strict_ceiling':s['norms']['strict_decimal_ceilings'][j],'positive_ceiling_square_margin_exact':str(ceil*ceil-combined),'maximizing_cell':idx})
checks=sum(r['iv']['coefficient_overlap_checks'] for r in rows);jets=sum(r['iv']['derivative_input_checks'] for r in rows);assert checks==89*17226==s['all_coefficient_overlap_checks'] and jets==89*445005==s['all_derivative_input_checks']
pins={str(p.relative_to(R)):sha(p) for p in [E/'full_rows.jsonl',E/'full_summary.json',E/'full_audit.json',Path(__file__).resolve()]}
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_ALL89_FLINT_REVERSED_SUMS_AND_ROOT_SQUARE_BRACKETS','cells':89,'coefficient_overlap_checks':checks,'derivative_input_checks':jets,'records':records,'files':pins,'scope':'Saved rational output reduction and endpoint coverage, not fresh integration. Complete actual review, later own adjudication and final gate still required.'}
(E/'own_final_reduction.json').write_text(json.dumps(v,indent=2)+'\n');print(v['utc'],v['status'],checks,jets)
