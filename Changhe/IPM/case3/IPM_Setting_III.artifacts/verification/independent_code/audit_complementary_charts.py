"""Off-grid endpoint-safe independent inverse and analytic density derivative.

Primary Cartesian FD8/real-space outputs remain separate and are cross-checked.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,math,hashlib
import numpy as np
from complementary_inverse_charts import SmoothAngular,ComplementaryQ,point_fields

ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);ap.add_argument('--kind',choices=['smooth','Q'],required=True);ap.add_argument('--points-file',required=True);ap.add_argument('--orders',default='64,128,192');args=ap.parse_args()
model=(SmoothAngular if args.kind=='smooth' else ComplementaryQ)(args.snapshot)
points=json.loads(Path(args.points_file).read_text());dest=Path('evidence/complementary_charts')/args.tag;dest.mkdir(parents=True,exist_ok=True)
nonzero=[(float(x),float(y)) for x,y in points if x or y]
logs=np.array([math.log(math.hypot(x,y)) for x,y in nonzero]);angles=np.array([math.atan2(y,x) for x,y in nonzero])
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),source=args.snapshot,sha256=hashlib.sha256(Path(args.snapshot).read_bytes()).hexdigest(),kind=args.kind,a=model.a,c=model.c,delta=model.cl+model.c-1,ell=model.cl,rows=[])
if hasattr(model,'exact_c'):result['exact_c']=str(model.exact_c)
for order in map(int,args.orders.split(',')):
 data=point_fields(model,logs,angles,order)
 for p,(x,y) in zip(data,nonzero):
  p['x']=x;p['y']=y;p['abs_R']=abs(p['R_over_r'])*math.hypot(x,y)
  p['Nf']=p['Nf_over_r']*math.hypot(x,y);p['Nv']=p['Nv_over_r']*math.hypot(x,y)
  if y==0:p['R_Nf']=None;p['R_Nv']=None
 summary={}
 for region,lo,hi in [('all',0,float('inf')),('center',0,.01),('core',.01,1.),('middle',1.,100.),('far',100.,float('inf'))]:
  subset=[p for p in data if lo<=math.hypot(p['x'],p['y'])<hi];row={}
  for field in ['abs_R','R_Nf','R_Nv']:
   good=[p for p in subset if p[field] is not None]
   if good:
    q=max(good,key=lambda p:p[field]);row[field]={'maximum':q[field],'x':q['x'],'y':q['y'],'chart':q['chart'],'Nf':q['Nf'],'Nv':q['Nv']}
  summary[region]=row
 result['rows'].append(dict(order=order,points=data,summary=summary));result['updated_utc']=datetime.now(timezone.utc).isoformat()
 (dest/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(order=order,utc=result['updated_utc'],summary=summary)),flush=True)
result['finished_utc']=datetime.now(timezone.utc).isoformat();result['scope']='Finite sample diagnostics of the whole-plane inverse, complementary charts, independent analytic differentiation. Neither a certified uniform residual nor a nearby-profile theorem. Exact x-axis ratios omitted, origin analytically zero. Candidate center computed from coefficients, not imposed.'
(dest/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
