"""Serialize audited result320 data without changing any numerical definition."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import csv, io, json, hashlib, os
R=Path('research/accurate_map_final_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
fmt=lambda v:'undefined' if v is None else format(v,'.11g')
def write_csv(path,rows):
 keys=list(rows[0]);buf=io.StringIO();w=csv.DictWriter(buf,fieldnames=keys);w.writeheader();w.writerows(rows);path.write_text(buf.getvalue())
def comp_summary(rows):
 defined=[z for z in rows if z['empirical_pass'] is not None]
 def maxfield(k):return max((float(Fraction(z[k])) for z in rows if z[k] is not None),default=None)
 return dict(selected=len(rows),criterion_defined=len(defined),criterion_pass=sum(z['empirical_pass'] for z in defined),criterion_undefined=len(rows)-len(defined),max_residual_spread_over_abs_B_R=maxfield('spread_over_abs_B_R'),max_residual_spread_over_B_Nf=maxfield('spread_over_B_Nf'),component_scope='V1,V2 are comparable complete velocities. Tail-only components have different cutoffs in A/B/C.')
def main():
 p=V/'FINAL_CHECKS.json';d=json.loads(p.read_text());assert d['status']=='PASS_FINITE_ACCURATE_MAP_FINAL_REQUIRES_MODEL_REVIEW' and not d['synthetic_only'];assert d['count']==len(d['checks']) and all(z['passed']for z in d['checks'])
 e=json.loads((V/'FINAL_CHECK_EXECUTION_RESULT.json').read_text());assert e['returncode']==0
 for pid in [e['wrapper_pid'],e['timeout_pid']]:assert not Path('/proc',str(pid)).exists()
 for path,h in d['bindings'].items():assert sha(path)==h,path
 c=json.loads((V/'candidate/COMPLETE.json').read_text());o=d['outputs'];t=now();reg=[];ext=[];ss=[]
 for state in o['states']:
  tag=state['tag'];raw=next(z for z in c['states']if z['tag']==tag);m=json.loads((V/'candidate'/(tag+'_LOCAL_MP.json')).read_text());diag=[x for z in m['results'] for x in z['diagnostics']]
  mp=dict(points=len(m['results']),components=len(diag),precision_failed=sum(not z['precision_pass']for z in diag),max_precision_scaled=max(z['precision_scaled']for z in diag),max_double_abs=max(z['double_abs']for z in diag),max_double_pure_relative=max(z['double_pure_relative']for z in diag if z['double_pure_relative']is not None),both_zero=sum(z['both_zero']for z in diag))
  for rr in state['regions']:
   for metric,z in rr['metrics'].items():reg.append(dict(tag=tag,region=rr['region'],region_count=rr['count'],metric=metric,**z))
  for extent,rrs in state['extents'].items():
   for rr in rrs:
    for metric,z in rr['metrics'].items():ext.append(dict(tag=tag,extent=extent,region=rr['region'],region_count=rr['count'],metric=metric,**z))
  ss.append(dict(tag=tag,N=state['N'],M=state['M'],source_sha256=state['source_sha256'],points=state['points'],regions=state['regions'],center=state['center'],center_exact_nonzero=state['center_exact_nonzero'],center_gauss_minus_exact=state['gauss_minus_exact'],extent_rounding=raw['extent_rounding'],comparisons=comp_summary(state['comparisons']),local_MP=mp))
 angular=[]
 for z in o['angular']:
  raw=next(x for x in c['angular']if x['tag']==z['tag']);sums=[{k:v for k,v in x.items()if k!='fit_coefficients'}for x in z['summary']]
  angular.append(dict(tag=z['tag'],rows=raw['rows'],summary=sums,QR=z['QR'],comparisons=comp_summary(raw['comparisons'])))
 summary=dict(status='AUDITED_FINITE_OUTPUTS_INTERPRETATION_REVIEW_PENDING',generated_utc=t,final_checker_sha256=sha(p),check_count=d['count'],scalar_assertion_count=d['scalar_assertion_count'],worker_finished_utc=c['finished_utc'],checker_finished_utc=d['finished_utc'],states=ss,angular=angular,function_comparisons=o['function_comparisons'],scope=o['scope'])
 (V/'RESULT_SUMMARY.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n');write_csv(V/'REGIONAL_MAXIMA.csv',reg);write_csv(V/'EXTENT_MAXIMA.csv',ext)
 lines=['# Independent accurate-map audit: results awaiting final review','',f'Generated {t}. The accepted independent final checker completed at {d["finished_utc"]}: {d["count"]} check entries and {d["scalar_assertion_count"]} scalar comparisons passed. Actual model review and the interpretation decision are still pending. Primary IPM remains UNRESOLVED.','',
 'Read PROOF.md, FINAL_CHECKER_PROOF.md and RESULT_PRESENTATION_PROOF.md first. These eight saved states are smooth finite auxiliary hydrostatic trial densities with c=2, radial map exponent P=2 and L=1. The independent Cartesian generator uses the saved binary64 coefficients. Their full physical vertical inverse solves -Phi_yy=g_x. It is not the primary elliptic inverse -Delta psi=rho_x. Near-unit origin slopes and axis coefficients describe the trials, not a permissible normalization of arbitrary primary IPM profiles.','',
 'We evaluated 826 physical probes per state, including both axes, irregular between-node points and nominal radii from 10^-6 to 10^7. There are also 1148 angular rows for each of B and G128. Every row uses the complete B infinite-tail inverse. A/C rules are repeated at all predeclared selected rows; three physical extent restrictions (100, 10^4, 10^7) retain the same full inverse. No finite wall or independent harmonic strain is imposed.','',
 'The residual and denominators are R=(2x+V1)g_x+(2y+V2)g_y-g, Nf=|(2x+V1)g_x|+|(2y+V2)g_y|+|g| and Nv=|g|+|xg_x+yg_y|+|V1g_x+V2g_y|. The finite arithmetic check treats stored binary64 local jets and velocities as exact operands, then checks the reported rounded values. It does not enclose the analytic inverse. Ratios with zero denominators are undefined and excluded from ratio maxima. Nv need not majorize |R| because its dilation term omits the factor 2.','',
 'The physical-radius regions are core [0,0.1), sub [0.1,1), annulus [1,100), far [100,infinity). The far table means only the sampled portion of that region. Each state has regional counts 304,76,120,326. Each has 20,5,8,22 undefined Rf ratios on the horizontal axis, respectively. The corresponding Nv counts and all maxima, locations, signed R, Nf and Nv appear in verification/REGIONAL_MAXIMA.csv. Separate absolute and ratio maxima generally occur at different points.','',
 '|State|Size|Core max Rf|Sub max Rf|Annulus max Rf|Far max Rf|','|---|---|---:|---:|---:|---:|']
 for s in ss:lines.append('|'+s['tag']+'|'+str(s['N'])+' x '+str(s['M'])+'|'+'|'.join(fmt(z['metrics']['Rf']['value'])for z in s['regions'])+'|')
 lines+=['','|State|Core max |R||Sub max |R||Annulus max |R||Far max |R||','|---|---:|---:|---:|---:|']
 # Escape vertical bars in column labels so the Markdown table has the declared columns.
 lines[-2]='|State|Core max abs R|Sub max abs R|Annulus max abs R|Far max abs R|'
 for s in ss:lines.append('|'+s['tag']+'|'+'|'.join(fmt(z['metrics']['absR']['value'])for z in s['regions'])+'|')
 lines+=['','|State|Core max Rv|Sub max Rv|Annulus max Rv|Far max Rv|','|---|---:|---:|---:|---:|']
 for s in ss:lines.append('|'+s['tag']+'|'+'|'.join(fmt(z['metrics']['Rv']['value'])for z in s['regions'])+'|')
 lines+=['','The independent grids differ from the producer grids, so their maxima need not coincide. State B has far Rf about0.60 and state C about0.18 on independent probes despite small logged discrete node residuals. These are unresolved trials, not strong numerical YES evidence. The G80/G96/G112/G128 annular maxima decrease on this fixed probe set; their far maxima are not monotone from G80 to G96. Neither observation establishes convergence.','',
 'At nominal extent100, the physical hypot mask excludes index435 that the nominal-radius mask includes: 509 versus510 points. At 10^4 and10^7 the masks agree (645 and826). verification/EXTENT_MAXIMA.csv contains each regional absolute/Rf/Rv maximum on all three physical extent restrictions. The extent comparison samples the same mathematical inverse, rather than changing a closure.','',
 'Exact center computation uses rational expansion in ordinary powers of the compact coordinate, independent of the candidate-stage Chebyshev product integral. The exact values agree. Let a=g_y(0), b be the x^2 y coefficient, e the y^3 coefficient, E=e/a, and D=1+cH. K is the positive-axis leading coefficient of g/y^(1/2). The finite decimals below present exact nonzero rational D values, not enclosed physical parameters.','',
 '|State|a|D|E|b|b-6E|Exact axis Rf limit (rounded)|','|---|---:|---:|---:|---:|---:|---:|']
 for s in ss:lines.append('|'+s['tag']+'|'+'|'.join(fmt(s['center'][k])for k in ['a','delta','E','b','B_minus_6E','axis_limit'])+'|')
 lines+=['','Every one of the eight exact stored trial representations has a nonzero a and D. Thus none can be an exact auxiliary hydrostatic profile, already by its linear origin relation. This is an exact exclusion of these saved trials only. It does not exclude a limiting family or any primary IPM profile. The exact cubic residual coefficient is e(2+3D)-ab/3, recorded along with K and cH in verification/RESULT_SUMMARY.json and candidate/*_CENTER.json.','',
 '|State|Selected A/C points|Empirical criterion passes/defined|Undefined criterion|Largest spread/abs R_B|Largest spread/Nf_B|','|---|---:|---:|---:|---:|---:|']
 for s in ss:
  z=s['comparisons'];lines.append('|'+s['tag']+'|'+str(z['selected'])+'|'+str(z['criterion_pass'])+'/'+str(z['criterion_defined'])+'|'+str(z['criterion_undefined'])+'|'+fmt(z['max_residual_spread_over_abs_B_R'])+'|'+fmt(z['max_residual_spread_over_B_Nf'])+'|')
 lines+=['','The predeclared empirical criterion is spread<=0.01 abs R_B and spread<=10^-8 Nf_B at fixed local jets. It is undefined at zero R_B or zero Nf_B. These finite sensitivities do not bound quadrature or representation error. V1/V2 comparisons use complete velocities; tail-only components use different cutoff radii in A/B/C, so their differences are not errors in a common tail integral. All selected local-jet72/108 decimal precision criteria pass. This320 run did not perform MP inverse-integrand replay. That distinction matters when interpreting small sampled residuals.','',
 '|State|Radius|Dense max Rf|Direct collocation max Rf|Sign changes|Dominant fitted k|','|---|---:|---:|---:|---:|---:|']
 for a in angular:
  for z in a['summary']:lines.append('|'+a['tag']+'|'+'|'.join(fmt(z[k])for k in ['radius','dense_max','collocation_direct_max','sign_changes','dominant_k'])+'|')
 lines+=['','On the verifier angular grid there are 255 dense interior angles and32 direct collocation angles at each radius. The collocation rays lie in the dense set, and the direct and interpolated maxima coincide here; that coincidence is not independent validation of interpolation. The cosine fits were checked through a separately assembled QR solve and normal equations.','',
 'A discrepancy is retained: the producer recorded31 sign changes for B at radius3, while the independent scan on its different sample has6. Both give dominant fitted k=33 there. At radii30,300,3000 the independent scan reproduces32 sign changes and dominant k=32; the much smaller collocation-ray values are consistent with angular aliasing in these finite records. Neither the cause of the radius3 disagreement nor an aliasing mechanism is established. G128 has the recorded dominant k=22,27,2 at the three larger radii, which does not exclude other aliasing.','',
 'For function comparisons h=g_old-g_new, the following annular metric is max |h|/sqrt(1+r). The common set has19649 points and the shifted set18659, with separately specified nominal-radius masks. All four function metrics and five regional summaries are in verification/RESULT_SUMMARY.json. The last half-open far interval excludes nominal radius10^7. The ordered relative metric uses the explicitly named second-state denominator; the pure relative metric is symmetric with value0 when both functions vanish.','',
 '|Ordered pair|Common annular weighted density difference|Shifted difference|','|---|---:|---:|']
 fs=o['function_comparisons'];assert [z['grid']for z in fs]==['common','shifted']
 for a,b in zip(fs[0]['records'],fs[1]['records']):
  assert a['pair']==b['pair'];aa=next(z for z in a['regions']if z['region']=='annulus');bb=next(z for z in b['regions']if z['region']=='annulus');lines.append('|'+':'.join(a['pair'])+'|'+fmt(aa['metrics']['weighted_density']['value'])+'|'+fmt(bb['metrics']['weighted_density']['value'])+'|')
 lines+=['','The three consecutive G-sequence differences are not monotone. The small E:G96 difference compares two rules at one resolution. The G128:S160 and S128:G128 values distinguish these saved functions; they do not prove that either family converges to a solution.','',
 'The producer-record audit of solver budgets, stopping messages and printed residuals is separate and bound in verification/PRINTED_RECORD_CHECKS.json. Those files describe records, not authenticated historical executions or independently recomputed raw solver residuals. Result323 verifies finite arithmetic and selected local jets in the all-node S160/G128 exports while retaining producer inverse values. Result318 independently recomputes all-node192/224 velocities and residuals. Result320 must not be cited as an independent all-node inverse audit of S160 or G128.','',
 'Reproduction: launch_accurate_map_audit.py admitted and recorded the completed worker after318 ceased; run_accurate_map_audit.py produced the pointwise arrays; check_accurate_map_final.py performed the separate arithmetic audit; render_accurate_map_results.py serialized these results. Accepted design manifests, manufactured tests, original execution logs, coefficients and code hashes are preserved under verification/. This report requires the actual final results review and a binding manifest before its verdict can be CONFIRMED.']
 (R/'RESULTS_DRAFT.md').write_text('\n'.join(lines)+'\n')
 manifest=dict(status='SERIALIZED_AUDITED_OUTPUTS_REVIEW_PENDING',utc=t,bindings={str(x):sha(x)for x in [p,V/'FINAL_CHECK_EXECUTION_RESULT.json',R/'RESULT_PRESENTATION_PROOF.md',Path(__file__),V/'RESULT_SUMMARY.json',V/'REGIONAL_MAXIMA.csv',V/'EXTENT_MAXIMA.csv',R/'RESULTS_DRAFT.md']},regional_rows=len(reg),extent_rows=len(ext))
 (V/'PRESENTATION_BINDINGS.json').write_text(json.dumps(manifest,indent=2)+'\n');print(manifest['status'],len(reg),len(ext),t)
if __name__=='__main__':main()
