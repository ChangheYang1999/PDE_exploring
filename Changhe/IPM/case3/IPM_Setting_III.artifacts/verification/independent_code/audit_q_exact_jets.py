from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import argparse,json,math
from q_exact_jets import jets,axis_gradient,pack
from q_checkpoint_reader import QCheckpoint

ap=argparse.ArgumentParser();ap.add_argument('--paths-file',required=True);ap.add_argument('--out',default='evidence/q_exact_jets');args=ap.parse_args()
assert json.loads(Path('research/finite_q_exact_jets/verification/checks.json').read_text())['status']=='PASS'
rows=[];out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
for path in json.loads(Path(args.paths_file).read_text()):
 model=QCheckpoint(path);j=jets(model.coeff,model.kappa,model.cl)
 cert={key:val for key,val in j.items() if not key.endswith('_polynomial')}
 witnesses=[]
 for k in range(4,37,2):
  s=F(1,2**k);gy,gx=axis_gradient(j,s)
  lograd=math.log(model.L)-model.kappa*math.log(2.)+math.log(float(s))/2-model.kappa*math.log1p(-float(s))
  for axis,g in [('y',gy),('x',gx)]:
   excess=abs(g)-abs(j['a'])
   if excess>0:
    witnesses.append(dict(axis=axis,sigma=s,gradient=g,excess=excess,relative_excess=excess/abs(j['a']) if j['a'] else None,
                          approximate_log10_radius=lograd/math.log(10.)))
 best=max(witnesses,key=lambda v:v['excess']) if witnesses else None
 row=dict(utc=datetime.now(timezone.utc).isoformat(),metadata=model.meta,exact=pack(cert),
          gradient_witnesses=pack(witnesses),largest_witness=pack(best),
          canonical_strain_strictly_above_origin_on_y_axis=bool(j['c']<0 and j['q2_core']<0),
          origin_strain_strictly_above_D=bool(abs(j['c'])>j['ell']-1),
          scope='Exact arithmetic for this frozen finite coefficient formula. Compact witness coordinate and gradient inequality exact; printed radius approximate. Quartic signs give a qualitative continuous strain excess, without a certified location or global upper bound. No exact profile is asserted.')
 rows.append(row)
 result=dict(updated_utc=row['utc'],status='COMPUTED_EXACT',rows=rows)
 (out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(utc=row['utc'],source=path,a=float(j['a']),c=float(j['c']),delta=float(j['delta']),
                      b_core=float(j['b_core']),e_core=float(j['e_core']),q1_core=float(j['q1_core']),q2_core=float(j['q2_core']),
                      witness=pack(best),strain_excess=row['canonical_strain_strictly_above_origin_on_y_axis'])),flush=True)
