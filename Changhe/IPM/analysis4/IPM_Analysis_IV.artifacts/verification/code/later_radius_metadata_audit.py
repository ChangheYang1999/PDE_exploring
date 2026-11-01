"""Check the printed density-column precision monitor and reset ancestry."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,pickle,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);N=p.parse_args().N
root=Path('research/266_later_conditional_continuations')/f'N{N}'
start=time.monotonic();ctx.prec=512
source=Path('../a4-num/ckpt/log_sin1_c3_from329.pkl');raw=source.read_bytes();digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
prior=json.loads((root/'verification/checks.json').read_text());assert prior['all_checks_pass']
assert digest==prior['source_sha256']
table=(root/'sources/peer_table.md').read_text();printed={}
for line in table.splitlines():
 cells=[x.strip() for x in line.split('|')[1:-1]]
 if cells and cells[0].isdigit():printed[int(cells[0])]=cells
ancestry=[{'n':n,'reset_at':row['radii_reset_at']} for n,row in state['stats'].items() if row.get('radii_reset_at') is not None]
assert not ancestry or min(x['reset_at'] for x in ancestry)==329
rows=[]
for n in range(N-9,N+1):
 assert int(printed[n][1])==n%3
 monitor=[];pivots=[];skipped=[];skipped_radius=arb(0);total_norm=arb(0);uncertain_pivots=[]
 for q,values in enumerate(state['f'][n]):
  col=[arb(*unpack(v)) for v in values]
  total_norm+=sum((abs(v) for v in col),arb(0))
  if not col or all(v.mid().is_zero() for v in col):
   if any(not v.is_zero() for v in col):skipped.append(q);skipped_radius+=sum((v.rad() for v in col),arb(0))
   continue
  win=max(range(len(col)),key=lambda j:abs(col[j].mid()))
  pivot=col[win]
  if pivot.contains(0):
   uncertain_pivots.append(dict(q=q,pivot=pivot.str(15,radius=True)));skipped_radius+=sum((v.rad() for v in col),arb(0));continue
  radius=max((v/pivot).rad() for v in col)
  monitor.append(radius);pivots.append(win)
 value=max(monitor).log()/arb(10).log()
 original=state['stats'][n]['log10_rad_over_max'];assert abs(float(printed[n][7])-original)<0.05001
 reconstructed_match=not uncertain_pivots and abs(float(value.mid())-original)<1e-6
 rows.append(dict(n=n,printed=printed[n][7],finite_pivot_monitor=value.str(42,radius=True),producer_statistic=original,full_monitor_reconstructed=reconstructed_match,uncertain_pivots=uncertain_pivots,checked_column_pivots=len(pivots),zero_midpoint_uncertain_columns=skipped,skipped_radius_over_plain_norm=(skipped_radius/total_norm).str(42,radius=True)))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,full_monitor_reconstructed=all(r['full_monitor_reconstructed'] for r in rows),target_order=N,source_sha256=digest,bits=512,rows=rows,printed_radius_comparisons=len(rows),residue_class_comparisons=len(rows),top_level_reset=state.get('radii_reset_at'),earliest_reset_ancestor=min((x['n'] for x in ancestry),default=None),recorded_ancestor_reset_orders=sorted(set(x['reset_at'] for x in ancestry)),metadata_retains_reset=bool(ancestry or state.get('radii_reset_at')),external_reset_provenance=['research/160_interval_midpoint_precision/PROOF.md','research/189_reset350_conditional_audit/PROOF.md'],scope='Finite precision-monitor reproduction, conditional on the stored midpoint reset. The monitor is not the relative error of the canonical sequence.',actual_elapsed_s=time.monotonic()-start)
(root/'verification/radius_metadata_checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ('later_radius_metadata_audit.py','unpack_dyadic4.py'):(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
for name in ('logff.py','table_511b.py'):(root/'sources'/('producer_'+name)).write_bytes(Path('../a4-num/code',name).read_bytes())
print(json.dumps(result),flush=True)
