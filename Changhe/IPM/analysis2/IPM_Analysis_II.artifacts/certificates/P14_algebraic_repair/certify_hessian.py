"""Stream exact repaired-reference Hessian integration without enormous JSON polynomials."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]/'11_residual_norms/verification'))
from compact_norms import construct,norm,Q,ctx
ctx.prec=640
name=sys.argv[1] if len(sys.argv)>1 else 'algebraic_n12_m10_k8'
start=time.monotonic();meta,D=construct(name,write=False,max_order=2,encode=False)
print('POLYNOMIALS',len(D),'total',sum(len(v) for v in D.values()),'max_degree',max(p.degree() for v in D.values() for p in v.values()),flush=True)
res=norm(D,2,Q(meta['delta']),weight=True,N=56)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,'metadata':meta,'hessian_norm':res,'seconds':time.monotonic()-start,'scope':'Constructed exact weighted Hessian integral. Separate Cartesian and u-coordinate audit pending.'}
(HERE/(name+'_hessian.json')).write_text(json.dumps(out,indent=2)+'\n')
print('DONE seconds',out['seconds'],flush=True)
