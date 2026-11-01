"""Compare finite profile statistics by strict interval separation."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from flint import arb,ctx
ctx.prec=640;start=time.monotonic()
root=Path('research/96_profile_family_audit/verification/20261031T071730Z');summary=json.loads((root/'checks.json').read_text());assert summary['complete']
original_path=Path('research/91_candidate_checkpoint_audit/verification/N390_20261031T065156Z/checks.json');original=json.loads(original_path.read_text());oldrows={r['n']:r for r in original['fields']['f']['rows']}
original_root=arb(oldrows[200]['l2_root']);original_smooth=((arb(oldrows[200]['log10_l2_norm'])-arb(oldrows[190]['log10_l2_norm']))*arb(10).log()/10).exp()
rows=[];shear={};text=lambda x:x.str(32,radius=True)
for case in summary['cases']:
 data=json.loads((root/(case['tag']+'.json')).read_text());by_n={r['n']:r for r in data['rows']};r100=arb(by_n[100]['f']['l2_root']);r200=arb(by_n[200]['f']['l2_root']);smooth=arb(data['smoothed_ten_step_l2_ratio'])
 item={k:data[k] for k in ['tag','family','exact_low_order_inclusions','coefficient_count','poisson_coefficient_checks','uncertain_zero_midpoints','nonexact_balls_containing_zero']};item.update(root100=text(r100),root200=text(r200),ten_step_ratio200=text(smooth))
 if case['family']=='shear':shear[case['K']]=(r100,r200,smooth)
 else:
  assert r200>original_root and smooth>original_smooth
  item.update(original_has_strictly_smaller_root200=True,original_has_strictly_smaller_ten_step_ratio200=True)
 rows.append(item)
keys=sorted(shear)
for a,b in zip(keys,keys[1:]):
 for j in range(3):assert shear[a][j]>shear[b][j]
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),source_path=str(root),original_source_path=str(original_path),original_source_sha256=sha256(original_path.read_bytes()).hexdigest(),original_root200=text(original_root),original_ten_step_ratio200=text(original_smooth),shear_tested_K=keys,strict_decrease_across_tested_K_for_each_statistic=True,total_low_order_inclusions=sum(r['exact_low_order_inclusions'] for r in rows),total_coefficient_balls=sum(r['coefficient_count'] for r in rows),total_poisson_checks=sum(r['poisson_coefficient_checks'] for r in rows),cases=rows,actual_elapsed_s=time.monotonic()-start)
(root/'finite_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/profile_family_comparison.py.txt').write_bytes(Path(__file__).read_bytes())
(root/'sources/numerics_report_at_comparison.md').write_bytes(Path('../a4-num/FARFIELD_NUMERICAL_EXPERIMENTS.md').read_bytes())
print(json.dumps(result),flush=True)
