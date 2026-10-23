"""Stdlib-only compilation of completed independent diagnostics, no new evaluations."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json
now=datetime.now(timezone.utc).isoformat()
files=sorted(Path('evidence').glob('q_exact_jets*/diagnostic.json'))
rows=[]
for p in files:
 for r in json.loads(p.read_text())['rows']:
  q=dict(r);q['diagnostic_file']=str(p);rows.append(q)
lines=['# Exact finite-state center audit',f'Updated {now}. {len(rows)} frozen coefficient formulas.','', 'All displayed decimal values come from exact rational arithmetic on the stored binary coefficients and parameters. Complete fractions, witnesses and source hashes are in the diagnostics listed in ALL_STATES.json. The proof is ../../research/finite_q_exact_jets/PROOF.md. With rc=L*2^(-kappa), all cubic and quartic coefficients displayed below have been multiplied by rc^2. No exact-profile or nearby-solution assertion is made.', '', '| state | ell | a | delta=ell+c-1 | rc^2 b | rc^2 e | rc^2 q1 | rc^2 q2 | axis gradient relative excess |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for r in rows:
 e=r['exact'];w=r['largest_witness'];vals=[e[k]['approx']for k in ['ell','a','delta','b_core','e_core','q1_core','q2_core']]
 assert Fraction(e['poisson']['exact'])==0
 lines.append('| '+Path(r['metadata']['source']).name+' | '+' | '.join(f'{v:.11g}'for v in vals)+' | '+(f"{w['relative_excess']['approx']:.9g}"if w else'none in this witness set')+' |')
fixed=[r for r in rows if Path(r['metadata']['source']).name.startswith('qfixF_cl')]
assert all(Fraction(r['exact']['q2_core']['exact'])<0 for r in fixed)
negative=sum(Fraction(r['exact']['q2_core']['exact'])<0 for r in rows)
nonzero=sum(Fraction(r['exact']['delta']['exact'])!=0 for r in rows)
lines+=['',f'Every Poisson quartic identity is exactly zero. The center defect is nonzero in {nonzero}/{len(rows)} states. The quartic q2 is negative in {negative}/{len(rows)} states; in particular it is negative in all {len(fixed)} fixed-ell1.1/1.2 states. Positive q2 occurs in several drifting states, so the latter sign statement must not be generalized to the full archive.', '', '| state | rc^2 actual R_x2y | rc^2 actual R_y3 | rc^2 jet elimination | source SHA256 |','|---|---:|---:|---:|---|']
for r in rows:
 e=r['exact'];lines.append('| '+Path(r['metadata']['source']).name+' | '+' | '.join(f"{e[k]['approx']:.11g}"for k in ['actual_R_x2y_core','actual_R_y3_core','jet_elimination_core'])+' | '+r['metadata']['sha256']+' |')
base=Path('evidence/q_exact_jets');(base/'SUMMARY.md').write_text('\n'.join(lines)+'\n');(base/'ALL_STATES.json').write_text(json.dumps({'utc':now,'rows':rows},indent=2)+'\n')
wr=[]
for p in sorted(Path('evidence/q_weighted').glob('*/diagnostic.json')):
 d=json.loads(p.read_text())
 if d.get('status')!='COMPUTED':continue
 q={'tag':p.parent.name,'diagnostic':str(p),'metadata':d['metadata'],'a':d['a'],'delta':d['delta'],'weights':[]}
 for m in [2.5,3.]:
  rr=[x for x in d['rows']if x['m']==m];best=rr[-1]
  q['weights'].append({'m':m,'baseline':best})
  ref=Path('evidence/q_weighted_refinement')/p.parent.name/'diagnostic.json'
  if ref.exists():
   rd=json.loads(ref.read_text());rv=[x for x in rd['rows']if x['m']==m]
   if rv:
    q['weights'][-1]['refinement']=rv;q['weights'][-1]['refinement_file']=str(ref);q['weights'][-1]['refinement_complete']=rd.get('status')=='COMPUTED'
 q['strain']=d['strain_samples'][-1];wr.append(q)
lines=['# Independent weighted diagnostics of archived finite Q states',f'Updated {now}. {len(wr)} completed baseline audits.','', 'E_m=||F||_m/||h||_m, h=rho-a*y and F=R-a*(ell+c-1)*y. When delta is nonzero, the raw R has infinite norm for m>=2, so it must not replace F here. Canonical inverse and density are implemented independently of the producer. Exact rational bounds control omitted radial tails. Retained-annulus quadrature is not an interval enclosure. Baseline rows have inverse order128; the sharper fixed-N96 refinements use order256 when complete.', '', '| tag | ell | a | baseline E2.5 | baseline E3 | sampled sigma | sigma-D |', '|---|---:|---:|---:|---:|---:|---:|']
for q in wr:
 sig=q['strain']['sigma']['sampled_max'];ell=q['metadata']['cl'];E=[z['baseline']['E']for z in q['weights']]
 lines.append(f"| {q['tag']} | {ell:.10g} | {q['a']:.10g} | {E[0]:.10g} | {E[1]:.10g} | {sig:.12g} | {sig-(ell-1):.8g} |")
lines+=['', 'The strain column uses each baseline finite grid and is a lower estimate of the global supremum. Refined local maxima and their locations are in ../q_local_refinement/SUMMARY.md.', '', '| tag | m | refined E128 | refined E192 | refined E256 | final identity defect | exact tail F^2 / computed h norm^2 | completion |', '|---|---:|---:|---:|---:|---:|---:|---|']
for q in wr:
 for w in q['weights']:
  if 'refinement' not in w:continue
  rr=w['refinement'];v={r['inverse_order']:r for r in rr};last=rr[-1]
  lines.append(f"| {q['tag']} | {w['m']} | "+' | '.join(f"{v[o]['E']:.12g}"if o in v else'pending' for o in [128,192,256])+f" | {last['identity_defect']:.5g} | {last['tail_F_over_quadrature_h']:.5g} | "+('complete'if w['refinement_complete']else'in progress')+' |')
lines+=['', 'Exact tails do not bound retained-annulus integration error, and an energy identity can hold while the residual norm is still underresolved. The explicit inverse/radial/angular orders and windows are in ALL_STATES.json, along with source diagnostics and hashes. Differences from baseline to refined values separate quadrature error at one frozen state from differences between coefficient counts. No norm here establishes proximity to an exact solution.']
base=Path('evidence/q_weighted');(base/'SUMMARY.md').write_text('\n'.join(lines)+'\n');(base/'ALL_STATES.json').write_text(json.dumps({'utc':now,'rows':wr},indent=2)+'\n')
print(json.dumps({'utc':now,'exact_states':len(rows),'delta_nonzero':nonzero,'q2_negative':negative,'weighted_states':len(wr)}))
