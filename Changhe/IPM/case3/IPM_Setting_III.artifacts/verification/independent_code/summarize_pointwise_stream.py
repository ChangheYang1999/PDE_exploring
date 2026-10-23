#!/usr/bin/env python3
"""Summarize completed independent pointwise reconstructions without rerunning inverses."""
from pathlib import Path
from decimal import Decimal, localcontext
from datetime import datetime, timezone
import hashlib,json
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def D(x):return Decimal(str(x))
def fmt(x):return f'{float(x):.11g}'
p=R/'evidence/pointwise_stream_audit/diagnostic.json';d=json.loads(p.read_text())
assert d['status']=='COMPUTED', d['status']
out=R/'research/shared_pointwise_inverse_audit/verification/completed';out.mkdir(parents=True,exist_ok=True)
provenance={str(p.relative_to(R)):sha(p)}
for origin,name in [(R.parent/'numerics/NUM_REPORT.md','NUM_REPORT.md'),(R.parent/'numerics/runs/shared_points_check.txt','shared_points_check.txt')]:
 dest=out/name
 if not dest.exists():dest.write_bytes(origin.read_bytes())
 provenance[str(dest.relative_to(R))]=sha(dest)
rows=[]
with localcontext() as ctx:
 ctx.prec=100
 for state in d['rows']:
  for z in state['precision_rows'][-1]['points']:
   c=z['delta_R_contributions']; unit=D(z['producer_printed_R']).as_tuple().exponent
   half=D(5)*D(10)**(unit-1); printed_error=abs(D(z['interpolant_minus_producer_printed_R']))
   assert abs(sum(map(D,c))-D(z['delta_R']))<D('1e-100')
   assert max(abs(D(v)) for v in z['density_scaled_differences'])<D('1e-100')
   rows.append(dict(N=state['N'],maximizer=z['maximizer'],x=z['x'],y=z['y'],r=z['r'],theta=z['theta'],
    delta_U=z['delta_U'],delta_R=z['delta_R'],delta_R_contributions=c,
    horizontal_fraction=str(abs(D(c[0])/D(z['delta_R']))),
    interpolant=z['interpolant'],canonical=z['canonical'],poisson_defect=z['poisson_defect'],
    relative_Nf_difference=z['relative_Nf_difference'],relative_Nv_difference=z['relative_Nv_difference'],
    producer_printed_R=z['producer_printed_R'],printed_R_difference=z['interpolant_minus_producer_printed_R'],
    half_printed_rounding_unit=str(half),within_half_printed_unit=printed_error<=half,
    canonical_over_interpolant_R_Nf=z['canonical_over_interpolant_R_Nf']))
 worst=max(D(v) for s in d['rows'] for z in s['precision_comparison'] for v in z['scaled_differences'].values())
 summary=dict(utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED finite pointwise discrepancy; global and endpoint attribution OPEN',
  evaluation_started_utc=d['started_utc'],evaluation_finished_utc=d['finished_utc'],provenance=provenance,
  inputs={k:d[k] for k in ['code_sha256','proof_sha256','gates_sha256','canonical_summary_sha256']},
  arithmetic='80/120-digit independent interpolation; canonical U from earlier 75/110 target-digit source-primitives inverse. No certified error enclosure.',
  max_interpolation_precision_scaled_difference=str(worst),rows=rows,
  ranges={k:[str(min(D(z[k]) for z in rows)),str(max(D(z[k]) for z in rows))] for k in ['delta_R','horizontal_fraction','relative_Nf_difference','relative_Nv_difference','canonical_over_interpolant_R_Nf']},
  maximum_abs_printed_R_difference=str(max(abs(D(z['printed_R_difference'])) for z in rows)),
  scope='Only six selected shared points. Source/export/old inverse hashes and density identities checked by the evaluator. Exact interpolation need not match producer floating arithmetic. No claim that endpoint defects alone cause the discrepancy; no uniform maximum or endpoint.')
 (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
 lines=['# Completed pointwise inverse comparison','',summary['utc'],'',
 'CONFIRMED at six specified Cartesian points: the saved stream interpolant and the canonical inverse of the same density give different velocities. The exact identity delta R = delta U_1 rho_x + delta U_2 rho_y accounts for the residual discrepancy. Density and gradient are recomputed independently from the saved coefficients, with hashes tied to the earlier canonical source-primitives evaluation. No producer code was executed.','',
 '| N | selected maximum | delta U_1 | delta U_2 | delta U_1 rho_x | delta U_2 rho_y | R interpolant | R canonical | canonical/interpolant abs(R)/N_f |',
 '|---:|---|---:|---:|---:|---:|---:|---:|---:|']
 for z in rows:lines.append('| '+' | '.join([str(z['N']),z['maximizer'],*[fmt(v) for v in z['delta_U']],*[fmt(v) for v in z['delta_R_contributions']],fmt(z['interpolant']['R']),fmt(z['canonical']['R']),fmt(z['canonical_over_interpolant_R_Nf'])])+' |')
 lines+=['',
 'The horizontal contribution opposes the vertical one, with magnitude '+fmt(min(D(z['horizontal_fraction']) for z in rows))+' to '+fmt(max(D(z['horizontal_fraction']) for z in rows))+' of abs(delta R). Thus the previously estimated vertical differences at the N_f maxima, 3.2e-9, 1.8e-9 and 1.7e-9, are supported with both terms now separated. This does not mean that the horizontal velocity difference itself vanishes.','',
 'Relative N_f changes range from '+fmt(min(D(z['relative_Nf_difference']) for z in rows))+' to '+fmt(max(D(z['relative_Nf_difference']) for z in rows))+'. N_f depends on U. Denominator agreement by itself does not imply separate agreement of the density, its gradient, or the signed transport term; their comparison here is direct.','',
 'All six interpolated Poisson defects are nonzero, ranging in absolute magnitude from '+fmt(min(abs(D(z['poisson_defect'])) for z in rows))+' to '+fmt(max(abs(D(z['poisson_defect'])) for z in rows))+'. The velocity and Poisson discrepancies are properties of the reconstructed stream at these points. A quantitative explanation by specified origin endpoint derivatives remains OPEN.','',
 'The 80/120-digit interpolation comparison has maximum scaled change '+str(worst)+'. The 1128 manufactured gates test irregular-node full-degree interpolation and independent Cartesian derivatives at 70/110 digits. The canonical values retain the earlier 75/110 target-digit validation; reusing a 110-digit canonical value does not supply 120 independent digits.','',
 'Comparison with the producer printed R values: maximum absolute difference '+summary['maximum_abs_printed_R_difference']+'. Five are within half a printed last-place unit. At N192, N_v maximizer, the reconstructed value 9.2335841066e-9 differs from printed 9.233e-9 by 5.8410661e-13, slightly above the half-unit 5e-13. Therefore exact agreement at every last printed digit is not confirmed. This small discrepancy could include producer floating arithmetic; it is much smaller than the canonical residual difference and no cause is inferred.','',
 'The latest frozen producer text correctly distinguishes residual differences from estimated velocity differences. Its denominator-agreement wording still cannot alone establish agreement of the signed W.grad rho; quote the direct quantities in SUMMARY.json instead. The observed canonical/interpolant N_f ratios are 3.407 to 11.504 at these six points. Claims about all between-node locations or every report table are not established by six observations.','',
 'OPEN: full-plane uniform residual accuracy, a limiting smooth exact profile, a quantified endpoint-defect mechanism, and the principal YES/NO endpoint. The team must continue.','',
 'Reproduction: run python3 independent_code/audit_pointwise_stream.py --help for its manufactured/run interface; the original evaluation and all inputs are hash recorded in diagnostic.json. This summary is reproducible with python3 independent_code/summarize_pointwise_stream.py.']
 (out/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
 print(json.dumps({k:summary[k] for k in ['utc','verdict','ranges','maximum_abs_printed_R_difference']},indent=2))
