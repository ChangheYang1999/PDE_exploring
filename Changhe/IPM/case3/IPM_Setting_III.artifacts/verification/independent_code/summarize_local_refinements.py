"""Stdlib-only compilation of all completed local refinement diagnostics."""
from pathlib import Path
from datetime import datetime,timezone
import json
now=datetime.now(timezone.utc).isoformat();rows=[]
for p in sorted(Path('evidence/q_local_refinement').glob('*/diagnostic.json')):
 d=json.loads(p.read_text())
 if d.get('status')!='COMPUTED':continue
 rr=[r for r in d['rows']if r['inverse_order']==256];best={name:max(rr,key=lambda r:r[name]['value'])for name in ['q','gradient','strain']}
 q=dict(tag=p.parent.name,source=str(p),metadata=d['metadata'],a=d['a'],c=d['c'],best={k:v[k]for k,v in best.items()})
 q['q_excess']=q['best']['q']['value']-1;q['gradient_relative_excess']=q['best']['gradient']['value']/abs(d['a'])-1;q['strain_excess']=q['best']['strain']['value']-(d['metadata']['cl']-1)
 rb=best['strain'];prev=next(r for r in d['rows']if r['grid']==rb['grid']and r['inverse_order']==192)
 q['strain_maximum_order192_256_difference']=rb['strain']['value']-prev['strain']['value'];rows.append(q)
lines=['# Independent local refinement of Q density and strain',f'Updated {now}. {len(rows)} completed states.','', 'Each row gives maxima over explicit finite neighborhoods, with the canonical inverse at order256. These are lower estimates of global suprema. The order comparison changes the inverse quadrature on the same local grid; it compares sampled maxima and does not certify integration error. Complete grids and source hashes are in the individual diagnostics. Density q=rho/(a*y) is extended to y=0 by its derivative.', '', '| state | ell | a | max q - 1 | max gradient / abs(a) - 1 | sampled sigma - D | sigma order256 - order192 |','|---|---:|---:|---:|---:|---:|---:|']
for q in rows:lines.append('| '+q['tag']+' | '+' | '.join(f'{z:.12g}'for z in [q['metadata']['cl'],q['a'],q['q_excess'],q['gradient_relative_excess'],q['strain_excess'],q['strain_maximum_order192_256_difference']])+' |')
lines+=['', '| state | quantity | log10 radius | angle in radians |','|---|---|---:|---:|']
for q in rows:
 for name,loc in q['best'].items():lines.append(f"| {q['tag']} | {name} | {loc['log10_radius']:.14g} | {loc['theta']:.14g} |")
lines+=['', 'A strict sampled excess over D contradicts a claim that this finite field is globally capped, subject to numerical accuracy. An absence of sampled excess never proves a cap. Exact rational density-gradient witnesses and center/quartic coefficients are separately recorded in ../q_exact_jets/SUMMARY.md.']
base=Path('evidence/q_local_refinement');(base/'SUMMARY.md').write_text('\n'.join(lines)+'\n');(base/'SUMMARY.json').write_text(json.dumps({'utc':now,'rows':rows},indent=2)+'\n');print(json.dumps({'utc':now,'states':len(rows)}))
