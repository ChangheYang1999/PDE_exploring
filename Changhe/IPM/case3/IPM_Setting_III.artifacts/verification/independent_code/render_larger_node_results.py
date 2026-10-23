"""Render a review draft from completed independently checked finite records."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import json, hashlib, sys
if sys.flags.optimize: raise SystemExit('optimized Python prohibited')
sys.set_int_max_str_digits(1000000)
R=Path('research/hydrostatic_larger_node_audit'); V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read_gate(name,status):
 p=V/name; d=json.loads(p.read_text())
 if d['status']!=status or d['count']!=len(d['checks']) or not all(z['passed']for z in d['checks']) or d['synthetic_only']:
  raise ValueError('actual complete gate required: '+name)
 for path,h in d['bindings'].items():
  if sha(path)!=h:raise ValueError('changed binding '+path)
 return d
def fmt(x):
 return 'undefined' if x is None else format(float(F(x)) if isinstance(x,str) else float(x),'.12g')
def main():
 out=R/'RESULTS_DRAFT.md'
 if out.exists():raise ValueError('preserve existing draft before rerendering')
 d=read_gate('FINAL_ARITHMETIC_CHECKS.json','PASS_FINITE_LARGER_NODE_ARITHMETIC_REQUIRES_FINAL_REVIEW')
 p=read_gate('PRINTED_COMPARISON_CHECKS.json','PASS_FINITE_PRINTED_COMPARISONS')
 q=d['outputs'];lines=['# Larger-node independent finite audit: review draft','',
  'Generated '+datetime.now(timezone.utc).isoformat()+'. Verdict OPEN pending actual final model review and independent resolution.',
  '', 'This result uses the auxiliary hydrostatic vertical inverse. It is not a full-plane elliptic IPM candidate or a certified integral-error estimate.', '',
  'Arithmetic check: '+str(d['count'])+' assertion entries and '+str(d['scalar_assertion_count'])+' scalar assertions. Counts include repeated binding and bookkeeping checks.',
  'Printed comparison: '+str(p['count'])+' assertion entries.',
  'All selected MP precision diagnostics passed: '+str(q['precision_diagnostics_passed'])+'.','']
 for s,ps in zip(q['states'],p['outputs']['states']):
  if s['N']!=ps['N']:raise ValueError('state order')
  lines += ['## N='+str(s['N'])+', M='+str(s['M']),'',
   'Source: `'+s['source']['path']+'`, SHA256 `'+s['source']['sha256']+'`. '+str(s['points'])+' points.', '',
   '| Region | Count | max abs(R) | max abs(R)/Nf | max abs(R)/Nv |',
   '|---|---:|---:|---:|---:|']
  for r in s['regional_summaries']:
   lines.append('| '+r['region']+' | '+str(r['count'])+' | '+' | '.join(fmt(r['metrics'][m]['value'])for m in ['absR','Rf','Rv'])+' |')
  lines += ['', 'Undefined pointwise ratio counts by region (Rf,Rv): '+json.dumps([(r['region'],r['metrics']['Rf']['undefined_count'],r['metrics']['Rv']['undefined_count'])for r in s['regional_summaries']])+'. First index on ties.', '', 'At each maximizing row below the two denominators and signed R refer to that row, not to independently maximized operands.', '',
   '| Region | Metric | Index | x | y | R | Nf | Nv |','|---|---|---:|---:|---:|---:|---:|---:|']
  for r in s['regional_summaries']:
   for m in ['absR','Rf','Rv']:
    z=r['metrics'][m]
    if z['index'] is None:lines.append('| '+r['region']+' | '+m+' | undefined | | | | | |');continue
    lines.append('| '+r['region']+' | '+m+' | '+str(z['index'])+' | '+' | '.join(fmt(t)for t in [z['x'],z['y'],*z['fields'][:3]])+' |')
  cs=s['selected_comparisons'];passed=sum(z['empirical_pass']is True for z in cs)
  lines += ['', 'Selected A/B/C comparisons: '+str(passed)+'/'+str(len(cs))+' satisfy the predeclared empirical criteria. Largest spread/abs(R_B): '+fmt(max(F(z['spread_over_abs_B_R'])for z in cs if z['spread_over_abs_B_R']is not None))+'. Largest spread/Nf_B: '+fmt(max(F(z['spread_over_B_Nf'])for z in cs if z['spread_over_B_Nf']is not None))+'. These are finite rule comparisons, not error bounds.', '',
   'Local selected MP count: '+str(s['selected_count'])+'. Failed diagnostic locations: `'+json.dumps(s['local_failed_locations'])+'`. Both-zero pure-relative undefined counts: `'+json.dumps(s['local_both_zero_counts'])+'`.', '',
   '| Local jet component | Largest double/MP pure-relative discrepancy | both-zero at maximizing record |', '|---|---:|---|']
  for z in s['local_comparison']['double_pure_relative_maxima']:
   lines.append('| '+str(z['component'])+' | '+fmt(z['relative'])+' | '+str(z['both_zero'])+' |')
  for w in s['witnesses']:
   lines += ['', 'Complete B-geometry MP witness index '+str(w['index'])+', (x,y)=('+fmt(w['x'])+','+fmt(w['y'])+'), '+str(w['nodes'])+' quadrature nodes. Precision diagnostic passed: '+str(w['precision_diagnostic_passed'])+'.',
    'Signed fixed-jet velocity-induced residual change / stored B Nf: '+fmt(w['residual_change']['total_over_stored_B_Nf'])+'. All exact six-component and four-pairing identities remain in FINAL_ARITHMETIC_CHECKS.json.',
    'Integrand both-zero undefined counts: `'+json.dumps(w['both_zero_counts'])+'`; failed locations: `'+json.dumps(w['failed_locations'])+'`.']
  lines += ['', 'Producer raw solver Fmax '+fmt(s['producer_raw_Fmax'])+' is unverified metadata. Printed argmax geometrically compatible: '+str(ps['printed_argmax_geometrically_compatible'])+'; compatible reconstructed indices: `'+json.dumps(ps['compatible_node_indices'])+'`. This is not authentication of historical maximizing arrays.', '',
   'The full finite-difference proxy array was not saved; its maximum is a provenance-backed selector only.', '']
 lines += ['## Exact center comparisons','',
  'The center applications and exact defining source coefficients are rebound by the final arithmetic checker. The following are rounded displays; the large exact rational values remain in the bound center evidence and FINAL_ARITHMETIC_CHECKS.json:', '',
  '| N | a0 | cH | D | axis limit | B core Rf | B core / axis limit |', '|---|---:|---:|---:|---:|---:|---:|',
  *['| '+str(z['N'])+' | '+' | '.join(fmt(z[k])for k in ['a','cH','delta','core_axis_limit','B_core_max','B_core_to_center_limit'])+' |'for z in q['center_comparisons']], '',
  'Primary IPM endpoint UNRESOLVED. No uniform or continuum claim follows from these finite calculations. T_end has not been declared by this result.', '']
 out.write_text('\n'.join(lines));print('WROTE_REVIEW_DRAFT',sha(out))
if __name__=='__main__':main()
