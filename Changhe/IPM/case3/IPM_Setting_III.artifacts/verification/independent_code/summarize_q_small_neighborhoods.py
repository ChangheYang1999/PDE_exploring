"""Read finite neighborhood-grid maxima and their canonical MP re-evaluations."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
import json,hashlib

def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def xy(p):return float(p['x']),float(p['y'])

out=dict(utc=datetime.now(timezone.utc).isoformat(),code_sha256=sha(__file__),rows=[],
 scope='Finite samples. Each reported MP value re-evaluates the corresponding finest-grid maximizer. Maxima of different metrics may occur at different points. No global or continuum bound follows. Both denominators are evaluated without a positive floor. At the x-axis and origin R=Nf=Nv=0 and the ratios are undefined. Exact canonical inverse of the saved smooth density, not the producer stream interpolant.')
lines=['# Canonical residuals in small neighborhoods','',out['utc'],'',out['scope'],'',
 '| N | region | MP absolute R at selected absolute maximum | MP R/Nf at selected normalized maximum | MP R/Nv at selected normalized maximum |',
 '|---:|---|---:|---:|---:|']
for N in [128,160,192]:
 tag=f'R1C_CL3P0_N{N}';p=Path('evidence/q_small_neighborhoods')/tag/'diagnostic.json';mp_path=Path('evidence/q_mp_inverse')/(tag+'_small_neighborhoods')/'diagnostic.json'
 d,mp=read(p),read(mp_path);assert d['status']==mp['status']=='COMPUTED'
 assert d['source_sha256']==mp['source_sha256']==sha(d['source'])
 mr=max(mp['rows'],key=lambda r:r['target_digits']);pts={xy(p):p for p in mr['points']};assert len(pts)==len(mr['points'])
 for zero in [(0.,0.),(1.,0.)]:
  zz=pts[zero];assert all(Decimal(zz[k])==0 for k in ['R','Nf','Nv']);assert zz['R_Nf'] is None and zz['R_Nv'] is None
 selected=max(d['rows'],key=lambda r:r['inverse_order']);row=dict(N=N,source=d['source'],source_sha256=d['source_sha256'],diagnostic=str(p),diagnostic_sha256=sha(p),mp_diagnostic=str(mp_path),mp_diagnostic_sha256=sha(mp_path),sample_levels=[{k:r[k]for k in ['radial_nodes','angular_nodes','inverse_order','physical_radius_range']}for r in d['rows']],regions=[],max_scaled_precision_difference=str(max(Decimal(v)for rr in mp['precision_comparisons']for v in rr['scaled_absolute_differences'].values())),scope=out['scope'])
 for region in selected['regions']:
  rr={k:v for k,v in region.items()if k!='maxima'};rr['selected_maxima']={}
  for metric,peak in region['maxima'].items():
   qp=pts[xy(peak)];value=abs(Decimal(qp['R']))if metric=='abs_R'else Decimal(qp[metric])
   rr['selected_maxima'][metric]=dict(grid=peak,MP=qp,MP_value=str(value),absolute_difference_from_grid=str(abs(value-Decimal(str(peak['value'])))))
  row['regions'].append(rr);values=[rr['selected_maxima'][k]['MP_value']for k in ['abs_R','R_Nf','R_Nv']]
  lines.append(f"| {N} | {rr['name']} | "+' | '.join(f'{float(v):.12g}'for v in values)+' |')
 out['rows'].append(row)
for row in out['rows']:
 lines+=['',f"## N={row['N']}",'',f"Source SHA-256 `{row['source_sha256']}`. Largest scaled difference between MP precision levels: {row['max_scaled_precision_difference']}.",'',
  '| Region and selected metric | x | y | absolute R | Nf | Nv |','|---|---:|---:|---:|---:|---:|']
 for r in row['regions']:
  for metric,q in r['selected_maxima'].items():
   p=q['MP'];lines.append('| '+r['name']+' '+metric+' | '+' | '.join(f'{abs(float(p[k])) if k=="R" else float(p[k]):.13g}'for k in ['x','y','R','Nf','Nv'])+' |')
 lines+=['','The two grids use different radial/angular offsets and inverse quadrature orders. They are sampling levels of the same saved density, not two candidate resolutions. The absolute peaks and normalized peaks above generally differ; the JSON retains both grid levels through the linked diagnostic and all locations and zero-denominator counts.']
root=Path('evidence/q_small_neighborhoods');(root/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n');(root/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines[:35]))
