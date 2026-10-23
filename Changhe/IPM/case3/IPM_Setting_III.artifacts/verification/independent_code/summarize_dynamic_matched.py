"""Finite evidence tables from the independent matched-time audit."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,math,hashlib

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='matched_main');args=ap.parse_args()
 root=Path('research/dynamic_local_reconstruction/verification')/args.tag;source=root/'AUDIT.json';d=json.loads(source.read_text());assert d['status']=='COMPUTED'
 rows=sorted(d['states'],key=lambda r:(r['tau'],r['N']));checks=[]
 lines=['# Independent matched-time state audit','',f"Updated {datetime.now(timezone.utc).isoformat()}. Input SHA256 {hashlib.sha256(source.read_bytes()).hexdigest()}.",'',
 'These are reconstructed saved densities, not a newly integrated trajectory. The inverse includes the entire exterior. Scalar polynomial derivatives, direct Cartesian finite differences, logarithmic Green quadrature and repeated multiprecision primitive inversion are independent of the producer implementation. All maxima below are sampled; no uniform error bound or continuum convergence is inferred.','',
 '| tau | N | canonical c | a_star | center defect | core max abs R_star | core max R/Nf | annulus max R/Nf | I_1 | I_10 | I_100 |','|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
 for r in rows:
  assert r['status']=='COMPUTED';grid=r['grid'][-1]['summary'] if r['grid'] else None
  vals=[r['tau'],r['N'],r['canonical_c'],r['a0star'],r['normalized_center_defect']]
  vals += [grid['core']['abs_R']['maximum'],grid['core']['R_Nf']['maximum'],grid['annulus']['R_Nf']['maximum']] if grid else [None]*3
  vals += r['moments'][-1]['values'][1:]
  lines.append('| '+' | '.join('NA' if x is None else f'{x:.10g}' for x in vals)+' |')
  for p in r['points']:
   f=p['multiprecision'][-1]['fields'];rr=math.hypot(*p['point']);q=p['quadrature_fields']
   qe={};qe['rho']=abs(q['rho_over_r']*rr-float(f['rho']));qe['gradient']=max(abs(q['gradient'][i]-float(f['gradient'][i]))for i in range(2));qe['U']=max(abs(q['U_over_r'][i]*rr-float(f['U'][i]))for i in range(2))
   checks.append({'tau':r['tau'],'N':r['N'],'point':p['point'],'quadrature_abs_errors':qe,'precision_Rstar_abs_difference':p['precision_Rstar_abs_difference'],'best_FD_error':max(min(t['absolute_errors'][j]for t in p['finite_difference'])for j in range(2))})
 lines+=['','At the horizontal-axis point (3,0), both residual denominators vanish by parity. The ratio is left undefined rather than reported as zero.','',
 '| tau | N | point | rho_star | grad_x rho_star | grad_y rho_star | U1_star | U2_star | R_star | Nf_star | Nv_star |','|---:|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|']
 for r in rows:
  for p in r['points']:
   f=p['multiprecision'][-1]['fields'];vals=[float(f['rho_star'])]+list(map(float,f['gradient_star']))+list(map(float,f['U_star']))+[float(f[k])for k in ['R_star','Nf_star','Nv_star']]
   lines.append('| '+f"{r['tau']} | {r['N']} | {p['point']} | "+' | '.join(f'{v:.10g}'for v in vals)+' |')
 out={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checks':checks,'maximum_quad_error_by_field':{k:max(c['quadrature_abs_errors'][k]for c in checks)for k in ['rho','gradient','U']},'maximum_best_FD_error':max(c['best_FD_error']for c in checks),'max_precision_Rstar_discrepancy':max(float(c['precision_Rstar_abs_difference'])for c in checks)}
 lines+=['','## Empirical evaluator checks','',json.dumps({k:v for k,v in out.items()if k!='checks'},indent=2),'',
 'The quadrature discrepancies and finite-difference errors are comparisons, not certified enclosures. The exact polynomial field is defined by the stored binary coefficients and the separately recorded binary basis shifts. Missing producer shift metadata remains a reproducibility qualification. A small center defect does not make these nonstationary states profiles.']
 (root/'SUMMARY.md').write_text('\n'.join(lines)+'\n');(root/'COMPARISONS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='checks'}))
if __name__=='__main__':main()
