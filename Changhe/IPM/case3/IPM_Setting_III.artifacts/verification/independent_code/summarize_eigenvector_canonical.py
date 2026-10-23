from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path('research/eigenvector_canonical_audit/verification');rows=[]
def cc(z):return complex(float(z[0]),float(z[1]))
for tag in ['producer_const64','producer_const96','producer_stall64','own_constant64_composite','own_constant96_composite','own_literal64_composite','own_literal64_on96_composite']:
 source=root/tag/'AUDIT.json';d=json.loads(source.read_text());assert d['status']=='COMPUTED'
 lo,hi=d['multiprecision'];H=max(abs(cc(x['direction']['rho']))for x in hi['rows']);ev=complex(*d['info']['lambda_value']);rate=abs(ev.real)*H
 row=dict(tag=tag,lambda_value=d['info']['lambda_value'],sampled_direction_sup=H,sampled_canonical_eigen_residual=max(abs(cc(x['canonical_eigen_residual']))for x in hi['rows']),maximum_double_DF_absolute_error=max(float(x['double_DF_absolute_error'])for x in hi['rows']),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),points=hi['rows'])
 # Decimal differences are computed without rounding both MP answers to binary64.
 from decimal import Decimal,localcontext
 with localcontext() as ctx:
  ctx.prec=120;delta=[]
  for a,b in zip(lo['rows'],hi['rows']):
   dd=[Decimal(a['DF'][k])-Decimal(b['DF'][k])for k in [0,1]];delta.append((dd[0]**2+dd[1]**2).sqrt())
  row['maximum_MP_DF_absolute_change']=str(max(delta))
 row['eigen_residual_over_real_growth_sample_norm']=row['sampled_canonical_eigen_residual']/rate
 row['eigen_residual_over_complex_rate_sample_norm']=row['sampled_canonical_eigen_residual']/(abs(ev)*H)
 row['peak_point_canonical_eigen_residual_over_real_growth']=abs(cc(hi['rows'][5]['canonical_eigen_residual']))/rate
 if tag.startswith('producer_'):
  row['canonical_minus_exported_Jv_over_real_growth_sample_norm']=max(abs(cc(x['canonical_minus_producer_projected_Jv']))for x in hi['rows'])/rate
  row['exported_Jv_eigen_residual_over_real_growth_sample_norm']=max(abs(cc(x['producer_projected_eigen_residual']))for x in hi['rows'])/rate
 rows.append(row)
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='COMPUTED',rows=rows,scope='Eight explicitly listed Cartesian points per state; H is the maximum of the canonical direction density on those points. No continuum operator norm, spectral enclosure, uniform inverse error or profile endpoint.',endpoint='UNRESOLVED')
(root/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# Canonical derivative on the common spectral vectors','',out['scope'],'','| vector | Re lambda | Im lambda | max |E|/(Re lambda H) | peak-point ratio | max double DF error | MP65/95 change |','|:---|---:|---:|---:|---:|---:|---:|']
for r in rows:lines.append('| '+r['tag']+' | '+' | '.join(f'{x:.8g}'for x in r['lambda_value']+[r['eigen_residual_over_real_growth_sample_norm'],r['peak_point_canonical_eigen_residual_over_real_growth'],r['maximum_double_DF_absolute_error']])+f" | {r['maximum_MP_DF_absolute_change']} |")
lines+=['','E=DF(B)h-lambda h uses the full canonical inverse, and the actual literal background and complex direction. H is the finite eight-point direction maximum, not a global norm. The first evaluator uses scalar complex-step radial differentiation, exact angular differentiation and composite interior/polynomial-exact exterior Green quadrature. The second uses exact rational basis conversion and independent multiprecision primitive integration and analytic differentiation. Agreement between these evaluators is empirical and does not supply an interval certificate.','', '| producer vector | canonical DF minus exported Jv, divided by Re lambda H | exported Jv minus lambda h, same denominator |','|:---|---:|---:|']
for r in rows[:3]:lines.append(f"| {r['tag']} | {r['canonical_minus_exported_Jv_over_real_growth_sample_norm']:.8g} | {r['exported_Jv_eigen_residual_over_real_growth_sample_norm']:.8g} |")
lines+=['','The comparison does not isolate projection, inverse or differentiation error. The exported Jv is itself a represented coefficient field and differs from the canonical derivative away from the producer grid. Several residuals already exceed the reported real-growth scale at this small set of points. Neither the producer vectors nor this lane\'s compressed vectors certify continuum eigenvalues. The small evaluator discrepancy supports the interpretation of the residuals as properties of the encoded finite fields, rather than quadrature or differentiation noise at the sampled points. The finite compressed spectra of result176 remain finite-matrix observations.','',f"Computed {out['utc']}. UNRESOLVED: no decisive endpoint."]
(root/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(json.dumps({**out,'rows':[{k:v for k,v in r.items()if k!='points'}for r in rows]},indent=2))
