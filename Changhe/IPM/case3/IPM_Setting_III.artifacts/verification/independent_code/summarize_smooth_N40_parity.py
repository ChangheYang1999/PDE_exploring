"""Error attribution for the two fixed near-axis witnesses of result148."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
mp.mp.dps=120
root=Path('research/smooth_N40_refinement_audit/verification/parity');raw=json.loads((root/'AUDIT.json').read_text());assert raw['status']=='COMPUTED'
rows=[];prec=[]
for i,p in enumerate(raw['points']):
 a,b=p['MP'];prec.append({k:str(abs(mp.mpf(a[k])-mp.mpf(b[k])))for k in ['rho','U1','U2','rho_x','rho_y','R','Nf','Nv','R_Nf','R_Nv']})
 x=mp.mpf(p['x']);y=mp.mpf(p['y']);rho=mp.mpf(b['rho']);gx=mp.mpf(b['rho_x']);gy=mp.mpf(b['rho_y']);ux=mp.mpf(b['U1']);uy=mp.mpf(b['U2']);exactR=mp.mpf(b['R'])
 for r in p['rows']:
  row={'point_index':i+1,'point':[p['x'],p['y']],'level':r['level'],'relative_h':r['interpolation']['relative_h'],'MP':b,'raw':r['raw'],'corrected':r['corrected'],'errors':{}}
  for k in ['raw','corrected']:
   v=r[k];uh,vh=map(mp.mpf,v['U']);gxh,gyh=map(mp.mpf,v['gradient']);rh=mp.mpf(v['rho']);termU=(uh-ux)*gx+(vh-uy)*gy;termD=(mp.mpf('2.5')*x+uh)*(gxh-gx)+(mp.mpf('2.5')*y+vh)*(gyh-gy);termR=-(rh-rho);difference=mp.mpf(v['R'])-exactR
   row['errors'][k]={name:mp.nstr(z,45)for name,z in {'U1_error':uh-ux,'U2_error':vh-uy,'velocity_contribution_to_R_error':termU,'derivative_contribution_to_R_error':termD,'density_contribution_to_R_error':termR,'actual_R_error':difference,'float_residual_evaluation_remainder':difference-termU-termD-termR}.items()}
  rows.append(row)
s={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED improvement at two fixed points; monotone convergence and uniform accuracy OPEN','audit_sha256':hashlib.sha256((root/'AUDIT.json').read_bytes()).hexdigest(),'precision_absolute_differences':prec,'rows':rows,'scope':raw['scope']}
(root/'SUMMARY.json').write_text(json.dumps(s,indent=2)+'\n')
lines=['# N40 near-axis parity audit','',s['utc'],'','The degree-three interpolation in y^2 improves the raw Cartesian vertical velocity at both fixed witnesses. It is constructed only from the independently implemented Cartesian inverse and does not use the high-precision reference. The horizontal velocity and eighth-order Cartesian density differences remain unchanged.','',
'| point | quadrature level | relative h | raw normalized residual | corrected normalized residual | MP normalized residual | corrected U2 error |', '|---:|---:|---:|---:|---:|---:|---:|']
for r in rows:lines.append(f"| {r['point_index']} | {r['level']} | {r['relative_h']} | {r['raw']['R_Nf']:.8g} | {r['corrected']['R_Nf']:.8g} | {float(r['MP']['R_Nf']):.8g} | {float(r['errors']['corrected']['U2_error']):.8g} |")
lines+=['','Point1=(0.00800986137674711,1.7256723212410504e-10); point2=(0.00309218611001119,3.09218611001119e-11). Quadrature level1=(40 radial,256 angular,144 exterior,outer factor4); level2=(64,512,224,8). The interpolation radii are h=relative_h times |x|, then h/2,h/4,h/8. The density difference relative step is0.00075.','',
'The raw normalized discrepancies range from9.45e-7 to1.45e-5; corrected values range from2.82e-13 to2.21e-10. Both step and quadrature-order refinement are nonmonotone. The reference values are1.64121007e-13 and6.95830470e-14. Therefore improvement at these points is CONFIRMED, but the parity procedure has not demonstrated accuracy at the reference residual scale everywhere. The interpolation remainder has an unmeasured fourth derivative constant; no interval certificate is claimed.','',
'SUMMARY.json retains absolute R, Nf, Nv, all velocities/derivatives and the exact multiprecision decomposition of the residual error into velocity, density derivative, density value and floating point residual-evaluation contributions. AUDIT.json retains every parity sample and weight and the75/110-digit comparisons. The original literal finite field is unchanged; there is no endpoint or sequence-convergence claim.']
(root/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(s['utc'],len(rows),'rows')
