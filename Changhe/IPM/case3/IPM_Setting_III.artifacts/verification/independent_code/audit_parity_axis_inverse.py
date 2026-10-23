from pathlib import Path
from datetime import datetime,timezone
import argparse,json,math,hashlib
from log_radius_inverse import LogRadiusQCheckpoint,LogTailInverse
from direct_inverse import Quadrature,cartesian_gradient
from parity_axis_inverse import interpolate_vertical
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);ap.add_argument('--output-tag');ap.add_argument('--include-fd-worst',action='store_true');args=ap.parse_args()
assert json.loads(Path('research/parity_inverse_verification/verification/checks.json').read_text())['status']=='PASS'
model=LogRadiusQCheckpoint(args.snapshot);chart=json.loads((Path('evidence/complementary_charts')/(args.tag+'_dense_peaks')/'diagnostic.json').read_text())
assert model.meta['sha256']==chart['sha256']
allpoints=chart['rows'][-1]['points'];candidates=[p for p in allpoints if p['x']>0 and 0<p['y']/p['x']<.001 and 1e-14<math.hypot(p['x'],p['y'])<1e10]
if not candidates:raise RuntimeError('No near-horizontal-axis points')
# Separate the actual ratio maximum and the smallest-angle cancellation witness.
selected=[]
for key in [lambda p:p['R_Nf'],lambda p:-p['y']/p['x']]:
 p=max(candidates,key=key)
 if (p['x'],p['y']) not in [(q['x'],q['y'])for q in selected]:selected.append(p)
if args.include_fd_worst:
 fd=json.loads((Path('evidence/q_evaluations')/(args.tag+'_dense_peaks')/'q2.json').read_text())
 assert fd['metadata']['sha256']==chart['sha256'] and fd.get('finished_utc')
 lookup={(p['x'],p['y']):p for p in candidates}
 for quantity in ['R_Nf','R_Nv']:
  available=[p for p in fd['points']if(p['x'],p['y'])in lookup and p['residuals'][-1].get(quantity)is not None]
  if not available:continue
  p=max(available,key=lambda p:abs(p['residuals'][-1][quantity]-lookup[p['x'],p['y']][quantity]))
  selected_point=lookup[p['x'],p['y']]
  if(p['x'],p['y'])not in[(q['x'],q['y'])for q in selected]:selected.append(selected_point)
rows=[];dest=Path('evidence/parity_axis_inverse')/(args.output_tag or args.tag);dest.mkdir(parents=True,exist_ok=True)
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),source=args.snapshot,sha256=model.meta['sha256'],rows=rows,scope='Independent direct canonical inverse using parity interpolation of U2/y. Angular values are comparison data only. No uniform error or exact profile certificate.')
for level,(nr,nt,ne,of) in [(1,(40,256,144,4.)),(2,(64,512,224,8.))]:
 core=model.L*2**(-model.kappa);inv=LogTailInverse(model.rho,Quadrature(nr,nt,ne,of,core,model.p,16*model.L,model.kappa))
 for p in selected:
  x,y=p['x'],p['y'];raw=inv.velocity(x,y);rho=float(model.rho(x,y));gx,gy=map(float,cartesian_gradient(model.rho,x,y,.00075,0.))
  for h in [.008,.004,.002]:
   est=interpolate_vertical(inv,x,y,h);ux,uy=float(raw[0]),est['u2'];tx=(model.cl*x+ux)*gx;ty=(model.cl*y+uy)*gy;R=tx+ty-rho;nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*gx+y*gy)+abs(ux*gx+uy*gy)
   row=dict(level=level,x=x,y=y,ratio_y_x=y/x,interpolation=est,U=[ux,uy],raw_U=raw.tolist(),rho=rho,gradient=[gx,gy],abs_R=abs(R),Nf=nf,Nv=nv,R_Nf=abs(R)/nf,R_Nv=abs(R)/nv,angular_R_Nf=p['R_Nf'],angular_R_Nv=p['R_Nv'],angular_U_over_r=p['U_over_r'])
   rows.append(row);result['updated_utc']=datetime.now(timezone.utc).isoformat();(dest/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in row.items() if k not in ['interpolation','angular_U_over_r']},default=float),flush=True)
result['finished_utc']=datetime.now(timezone.utc).isoformat();(dest/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
