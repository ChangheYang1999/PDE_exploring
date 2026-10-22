from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import numpy as np
root=Path('verification/native_axis_K40_checkpoints_20261021T1110Z');now=datetime.now(timezone.utc).isoformat()
queue=json.loads((root/'queue_status.json').read_text());assert queue['status']=='COMPLETE' and all(q['returncode']==0 for q in queue['steps'])
paths=[Path('verification/native_axis_beta3p0315_20261021T0752Z'),root/'K40_beta3p0315',root/'K32_beta3p04',root/'K40_beta3p04']
rows=[];states=[]
for p in paths:
 d=json.loads((p/'results.json').read_text());q=json.loads((p/'quadrature_comparison.json').read_text());m=json.loads((p/'manifest.json').read_text());assert d['status']=='COMPLETE' and q['status']=='COMPLETE'
 assert hashlib.sha256((p/m['snapshot']).read_bytes()).hexdigest()==m['sha256']==d['archive_sha256']==q['archive_sha256']
 label='K'+str(d['metadata']['K'])+'_beta'+str(d['metadata']['beta'])
 def run(kind,axis,epsilon):return next(r for r in d['runs'] if r.get('grid')=='fine' and r['kind']==kind and r['axis']==axis and r['epsilon']==epsilon)
 forced={axis:run('transport',axis,1e-6) for axis in ['up','down']}
 state={'label':label,'root':str(p),'archive_sha256':m['sha256'],'beta':d['metadata']['beta'],'K':d['metadata']['K'],'lambda':d['metadata']['lam'],'center_strain_error':d['center']['strain_error'],'Q_raw_epsilon1e6_R1e8':{axis:r['Q_raw'][3] for axis,r in forced.items()},'Q_raw_epsilon1e6_R1e14':{axis:r['Q_raw'][-1] for axis,r in forced.items()},'max_nested_grid_relative_Q_change':max(r['max_relative_Q_raw_difference'] for r in q['refinement']),'primary_quadrature_failures':{name:len(v['failed']) for name,v in d['quadrature'].items()},'direct_V2_max_difference':max(t['absolute_V2_difference'] for t in q['axis_value_checks']),'direct_dU1dx_max_difference':max(t['absolute_dU1dx_difference'] for t in q['axis_value_checks']),'strict_direct_flags':[{'source':s['source'],'evidence':r} for s in q['quadrature_estimates'] for r in s['values'] if not(r['inner_success'] and r['outer_success'])]}
 states.append(state)
 lines=[f'# Independent axis checkpoint {label}',f'UTC {now}. CONFIRMED as a finite-cutoff diagnostic of the represented forced velocity. Literal B2 profile status remains REFUTED by the separate Cartesian and exact-tail audits.',f"Archive SHA256 {m['sha256']}. Own adaptive full-plane physical-radius inverse uses{d['fine_radii']} radii from1e-8 to1e14 and a nested{d['coarse_radii']}-point grid. A Hermite interpolant of log(v/r), with independently integrated derivative, feeds the adaptive log-radius axis functional. Both half-axes and both self and forced velocities are evaluated. No NUM code is imported or executed.",'| velocity | axis | Q(1e2) | Q(1e6) | Q(1e8) | Q(1e14) |','|---|---|---:|---:|---:|---:|']
 for kind in ['self','transport']:
  for axis in ['up','down']:
   r=run(kind,axis,1e-6);lines.append('| '+kind+' | '+axis+' | '+' | '.join(f'{r["Q_raw"][i]:.12g}' for i in [0,2,3,6])+' |')
 lines+=['','The table uses positive inner normalization epsilon=1e-6. Q_raw is the packet112 functional with the missing inner integral filled by its center power law. It is not an exact axis amplitude normalized at zero: the actual center-strain mismatch is nonzero. No harmonic strain projection is added to the verifier inverse. The R dependence is a measured finite-cutoff effect, not a certified error estimate for R=infinity. An integral-only tail correction does not remove the finite-C_R bias.',f"The center strain defect is{d['center']['strain_error']:.12g}. Across all velocities, half-axes, inner cutoffs and outer cutoffs, the maximum relative coarse/fine Q change is{state['max_nested_grid_relative_Q_change']:.12g}. All primary inverse quadratures report success. The stricter direct comparison flags one seed outer integral at r=.5 as unsuccessful from roundoff, with estimated error6.69e-13 or smaller; it is retained explicitly. These floating-point estimates are not rigorous enclosures.",'| axis | NUM Q_R | own physical trapezoid1200 | own trapezoid19200 | own adaptive log ODE |','|---|---:|---:|---:|---:|']
 for axis in ['up','down']:
  rr=[r for r in q['quadratures'] if r['axis']==axis];a,b=rr[0],rr[-1]
  lines.append(f"| {axis} | {a['numerics_Q_reported']:.12g} | {a['Q_physical_trapezoid']:.12g} | {b['Q_physical_trapezoid']:.12g} | {a['Q_adaptive_log_ODE']:.12g} |")
 lines+=['','This controlled comparison holds the own inverse, inner cutoff1e-4 and outer cutoff1e8 fixed. The physical-radius trapezoid approaches the adaptive value under doubling through1200,2400,4800,9600,19200 points. The NUM comparison also contains velocity/strain-treatment differences, so its entire discrepancy is not assigned to quadrature.',f"The six independently integrated point checks have maximum relative-velocity component difference{state['direct_V2_max_difference']:.12g} and derivative difference{state['direct_dU1dx_max_difference']:.12g} from NUM's transcribed diagnostic. All original values and estimated errors are saved.",'| epsilon | forced upper Q(1e8) | forced lower Q(1e8) |','|---|---:|---:|']
 for eps in [1e-4,1e-6,1e-8]:lines.append(f"| {eps:g} | {run('transport','up',eps)['Q_raw'][3]:.12g} | {run('transport','down',eps)['Q_raw'][3]:.12g} |")
 lines+=['','Reproduce with code_independent/run_native_axis_cutoffs.py and compare_native_axis_quadratures.py on this directory. The inputs bind immutable coefficient and diagnostic snapshots. No fold, asymptotic branch limit, limiting jump, nearby profile or nonexistence endpoint follows.']
 if p.parent==root:
  (p/'SUMMARY.md').write_text('\n\n'.join(lines[:3])+'\n\n'+'\n'.join(lines[3:])+'\n')
  inputs=[{'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(p.iterdir()) if f.is_file() and f.name!='build_inputs.json']
  for name in ['run_native_axis_cutoffs.py','compare_native_axis_quadratures.py','axis_cutoff_functional.py','adaptive_modal_inverse.py','r2_state_values.py','summarize_K40_axis_checkpoints.py']:
   f=Path('code_independent')/name;inputs.append({'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
  (p/'build_inputs.json').write_text(json.dumps({'utc':now,'inputs':inputs},indent=2)+'\n')
comparisons=[]
for beta in [3.0315,3.04]:
 a=next(s for s in states if s['beta']==beta and s['K']==32);b=next(s for s in states if s['beta']==beta and s['K']==40)
 comparisons.append({'beta':beta,'lambda_difference':b['lambda']-a['lambda'],'relative_K40_minus_K32_Q_R':{axis:b['Q_raw_epsilon1e6_R1e8'][axis]/a['Q_raw_epsilon1e6_R1e8'][axis]-1 for axis in ['up','down']}})
out={'utc':now,'verdict':'CONFIRMED_FINITE_CUTOFF_ONLY','states':states,'comparisons':comparisons,'pipeline':queue,'scope':'Neither Q_infinity nor an exact smooth axis amplitude is certified; all literal B2 fields already refuted.'}
(root/'audit_summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# Matched K32/K40 independent axis audit',f'UTC {now}. All six serial audit steps returned0 in{queue["elapsed_seconds"]:.6f}s, ending{queue["ended_utc"]}. The three new archives use own physical-radius full-plane quadrature and adaptive log-radius axis integration; the previously completed K32 beta3.0315 audit is included without rerunning it.','| beta | K | lambda | upper Q_R | lower Q_R | upper Q(1e14) | center strain defect |','|---|---:|---:|---:|---:|---:|---:|']
for s in states:lines.append(f"| {s['beta']} | {s['K']} | {s['lambda']:.15g} | {s['Q_raw_epsilon1e6_R1e8']['up']:.12g} | {s['Q_raw_epsilon1e6_R1e8']['down']:.12g} | {s['Q_raw_epsilon1e6_R1e14']['up']:.12g} | {s['center_strain_error']:.9g} |")
lines+=['','Here R=1e8 and epsilon=1e-6. The own finite-cutoff upper Q changes by about-0.0088 percent at beta3.0315 and-0.0225 percent at beta3.04 when K32 is replaced byK40. Those finite comparisons confirm that these particular diagnostic values move little under this angular refinement. They do not prove a mesh limit, a fold or fate of the component; the runs also have different starting and stopping histories.','For an apples-to-apples quadrature comparison, the separate1200-point physical-radius trapezoid on the own inverse lies near the NUM diagnostic and approaches the own adaptive result under refinement to19200 points. The resulting roughly0.1 percent bias is larger than the K32/K40 difference. The finite-C_R outer-cutoff effect is larger still. Both are recorded in each child SUMMARY, along with inner-normalization dependence and the one strict seed quadrature roundoff flag.','Verdict CONFIRMED for the finite-cutoff calculation and its small finite angular-resolution changes. No exact amplitude at the center or at infinity is certified, and every literal field remains REFUTED as an unforced B2 profile. No NUM code was used.']
(root/'SUMMARY.md').write_text('\n\n'.join(lines[:2])+'\n\n'+'\n'.join(lines[2:])+'\n')
note=f'''## {now} verifier: matched K40 axis checks complete, finite-cutoff agreement only

Own full-plane inverse/adaptive axis functional at epsilon1e-6,R1e8: beta3.0315 upper Q209.94254(K32),209.92410(K40); beta3.04 259.24043(K32),259.18207(K40). Relative changes-0.0088percent/-0.0225percent. Finite pair agreement CONFIRMED; not a mesh limit/fold. NUM's1200pointphysicaltrapezoid has roughly0.1percentbias: with the SAME owninverse, epsilon1e-4,R1e8,K40beta3.04 the1200pointvalue258.87252 approaches259.17239 under refinement; NUM258.86979. The fullNUMdifference alsoincludesstrain/velocitytreatment. Cutoffeffect from1e8to1e14 is larger still. Allactualcenterstrainerrorsnonzero; Q_raw is not an exactzero-normalizedaxisamplitude. Six ownsteps0,315.954440s,end11:14:59.477. All4410primaryinverseintegralsreport success; eachstrictdirectsourcecheckatr.5has roundoff flagwithouterestimate6.69e-13. Full matched summary verification/native_axis_K40_checkpoints_20261021T1110Z/SUMMARY.md. LiteralstatesalreadyREFUTED, no endpoint.

'''
p=Path('NOTES_FOR_TEAM.md');p.write_text(note+p.read_text())
with Path('VERIFY_REPORT.md').open('a') as f:f.write('\n'+note)
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: Published completeownK40axisqueue andmatchedK32comparisons, including allquadrature/cutoff/centerlimitations andsourcehashes. Threechildsummaries+aggregate.6returncodes0.\n')
print(json.dumps({'utc':now,'comparisons':comparisons},indent=2))
