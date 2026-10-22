"""Independent reversed FLINT rational reduction of saved inner cells."""
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q
from datetime import datetime,timezone
import json,hashlib,argparse
R=Path(__file__).resolve().parents[3];E=R/'research/inner_derivative_cells_v2/evidence'
a=argparse.ArgumentParser();a.add_argument('tag',choices=['smoke','full']);tag=a.parse_args().tag
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[json.loads(x) for x in (E/(tag+'_rows.jsonl')).read_text().splitlines()];head,*rows=rows
s=json.loads((E/(tag+'_summary.json')).read_text());audit=json.loads((E/(tag+'_audit.json')).read_text())
indices=[0,15,43] if tag=='smoke' else list(range(44))
assert [r['cell'] for r in rows]==head['indices']==s['indices']==audit['indices']==indices
assert s['full_inner']==(tag=='full') and audit['status']=='PASS_COMPLETE_INNER_SAVED_OUTPUT_AUDIT'
assert s['rows_sha256']==audit['rows_sha256']==sha(E/(tag+'_rows.jsonl'))
partition=[(F(-5)+F(j,5),F(-5)+F(j+1,5)) for j in range(15)]+[(F(-2)+F(j,10),F(-2)+F(j+1,10)) for j in range(19)]+[(F(-1,10)+F(j,100),F(-1,10)+F(j+1,100)) for j in range(10)]
for r in rows:
 for key in ['arb','iv']:
  z=r[key];assert (F(z['left_exact']),F(z['right_exact']))==partition[r['cell']]
  for x in z['norm_squares']:assert 0<=F(x['lower_exact'])<=F(x['upper_exact'])
records=[]
for j in range(2):
 maxima=[max(Q(r[k]['norm_squares'][j]['upper_exact']) for k in ['iv','arb']) for r in rows]
 total=sum(reversed(maxima),Q(0));assert total==Q(s['cell_squares_upper_exact'][j])
 tail=Q(str(F(['0.000002273735','0.000035059554'][j])))**2
 assert tail==Q(s['accepted_tail_squares_upper_exact'][j])
 combined=total+tail;assert combined==Q(s['combined_squares_upper_exact'][j])
 ceil=Q(str(F(s['norms']['strict_decimal_ceilings'][j])));assert ceil>0 and ceil*ceil>combined
 idx=indices[max(range(len(rows)),key=lambda i:maxima[i])];assert idx==audit['maximum_contribution_cells'][j]
 for engine in ['arb512','iv200']:
  z=s['norms'][engine][j];lo,hi=Q(z['lower_exact']),Q(z['upper_exact']);assert 0<lo<=hi<ceil and lo*lo<=combined<=hi*hi
 records.append({'norm_index':j,'cell_sum_exact':str(total),'tail_square_exact':str(tail),'combined_square_exact':str(combined),'strict_ceiling':s['norms']['strict_decimal_ceilings'][j],'positive_ceiling_square_margin_exact':str(ceil*ceil-combined),'maximizing_cell':idx})
counts={}
for key,percell in [('coefficient_overlap_checks',17226),('derivative_input_checks',324136),('cross_method_input_jet_checks',62688)]:
 counts[key]=sum(r['iv'][key] for r in rows);assert counts[key]==len(indices)*percell==s['all_'+key]
pins={str(p.relative_to(R)):sha(p) for p in [E/(tag+'_rows.jsonl'),E/(tag+'_summary.json'),E/(tag+'_audit.json'),Path(__file__).resolve()]}
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_INNER_FLINT_REVERSED_SUMS_AND_ROOT_SQUARE_BRACKETS','full_inner':tag=='full','indices':indices,'counts':counts,'records':records,'files':pins,'scope':'Saved rational reduction and exact partition endpoints only. Smoke is not a cover. Separate complete engines, actual reviews and final gates required.'}
out=E/(tag+'_own_reduction.json');assert not out.exists();out.write_text(json.dumps(v,indent=2)+'\n');print(v['utc'],v['status'],counts)
