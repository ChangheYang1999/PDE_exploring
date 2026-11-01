"""Prove the ordering used to report finite floating-fit maxima."""
from pathlib import Path
import json,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from certificate_admission import stamp,ref
ctx.prec=768
result=[]
for topic,Qs in [('290_floating_order_doubling',[7,8]),('303_period_nine_ten_floating_extensions',[9,10])]:
 base=Path('research')/topic/'verification'
 for Q in Qs:
  inputs=sorted(base.glob(f'Q{Q}_root[0-9]*.json'))
  data=[json.loads(p.read_text()) for p in inputs]
  candidates=[(d['root_index'],r) for d in data for r in d['same_window_changes'] if r['channel']=='density']
  if not candidates: continue
  best=max(candidates,key=lambda v:float(arb(v[1]['absolute_relative_A_change']).mid()))
  checked=0
  for other in candidates:
   if other is best:continue
   assert arb(best[1]['absolute_relative_A_change'])>arb(other[1]['absolute_relative_A_change']),(Q,best,other)
   checked+=1
  result.append(dict(Q=Q,root=best[0],window_lower=best[1]['window_lower'],absolute_relative_A_change=best[1]['absolute_relative_A_change'],strict_interval_comparisons=checked,inputs=[ref(p) for p in inputs]))
out=Path('research/303_period_nine_ten_floating_extensions/verification/maxima_latest.json')
out.write_text(json.dumps(dict(at=stamp(),all_checks_pass=True,groups=result,scope='Strict ordering of finite fit statistics only.'),indent=2)+'\n')
print(json.dumps([dict(Q=r['Q'],root=r['root'],comparisons=r['strict_interval_comparisons']) for r in result]))
