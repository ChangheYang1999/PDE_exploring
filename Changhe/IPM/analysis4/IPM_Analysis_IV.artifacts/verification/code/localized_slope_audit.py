"""Independent pairwise regression audit of the reported localized-weight slopes."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
import json,time
ctx.prec=640;start=time.monotonic()
root=Path('research/104_divisor_localized_criterion')
raw=(root/'verification/targeted_weights_N315.json').read_bytes();data=json.loads(raw)
other=json.loads((root/'verification/summary_N315.json').read_text())
rows={r['n']:r for r in data['rows']};slopes=[]
for end in [150,200,250,280,300,315]:
 for residue in [0,1,2]:
  ns=[n for n in range(end-26,end+1) if n%3==residue];N=len(ns)
  ys=[arb(rows[n]['log10_E']) for n in ns]
  den=N*sum(n*n for n in ns)-sum(ns)**2
  slope=(N*sum((n*y for n,y in zip(ns,ys)),arb(0))-sum(ns)*sum(ys,arb(0)))/den
  same=[r for r in other['slopes'] if r['window_end']==end and r['residue']==residue]
  if same:assert len(same)==1 and slope.overlaps(arb(same[0]['slope_per_order']))
  if end==315:
   reported=['-0.671','-0.599','-0.599'][residue]
   assert abs(slope-arb(reported))<arb('.0005')
  slopes.append(dict(window_end=end,residue=residue,orders=ns,slope=slope.str(35,radius=True),summary_overlap=bool(same)))
positive=[n for n,r in rows.items() if arb(r['targeted_weight'])>0]
above=[n for n,r in rows.items() if arb(r['targeted_weight'])>arb(r['density_norm'])]
assert min(positive)==7 and min(above)==196
assert all(arb(r['targeted_weight'])<arb(1)/arb(4)**n for n,r in rows.items())
winner=max(rows,key=lambda n:float(arb(rows[n]['E_root']).mid()))
assert winner==314 and all(arb(rows[winner]['E_root'])>arb(r['E_root']) for n,r in rows.items() if n!=winner)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),input_sha256=sha256(raw).hexdigest(),slopes=slopes,all_quarter_power_bounds=True,first_positive=7,first_E_above_M=196,strict_maximum_root_order=winner,strict_maximum_root=rows[winner]['E_root'],actual_elapsed_s=time.monotonic()-start,scope='Recomputes summaries from retained interval weights; does not independently generate coefficients or re-evaluate all scalar inverses.')
(root/'verification/slope_audit.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/localized_slope_audit.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result),flush=True)
