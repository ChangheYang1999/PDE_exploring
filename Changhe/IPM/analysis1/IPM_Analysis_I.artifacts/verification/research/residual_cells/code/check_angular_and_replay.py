"""Exact trigonometric fixture and zero-radius export audit of the executed source."""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,arb_poly,arb_mat,ctx
import certify_cells as c
ctx.prec=384;ctx.threads=1;B=Path(__file__).resolve().parents[3];E=B/'research/residual_cells/evidence'
Q=16;tc=c.aa(F(3,7));h=c.aa(F(1,1000));base=2*Q+1
rho=c.exp_poly([arb(1)],3,tc,h,Q);D=c.tmscale(rho,arb(3));H=rho
A=c.tmscale(c.exp_poly([arb(1)],4,tc,h,Q),arb(-2));C=c.tmscale(c.exp_poly([arb(1)],4,tc,h,Q),arb(6));em2=c.exp_poly([arb(1)],-2,tc,h,Q)
P=c.tmscale(c.mul(em2,c.tmadd(A,C),Q),arb(-1)/2);Qf=c.tmscale(c.mul(em2,c.tmadd(C,c.tmscale(A,arb(-1))),Q),arb(1)/2)
ld=c.angular([D],[1],1,True,Q);lh=c.angular([H],[1],1,False,Q);lp=c.angular([P],[2],2,False,Q);lq=c.angular([Qf],[2],2,True,Q)
lin=c.tmscale(rho,arb(3)*c.aa(F(5,2))-1);ll=c.angular([lin],[1],1,True,Q);poly=lp[0]*ld[0]+lq[0]*lh[0]+arb_poly([arb(0)]*(2*base)+list(ll[0]))
E5=c.exp_poly([arb(1)],5,tc,h,Q);expected=[c.add(lin[0],c.scale(E5[0],arb(5))),c.scale(E5[0],arb(-1))];got=[[poly[(3-nu)*base+j]-poly[(3+nu)*base+j] for j in range(Q+1)] for nu in (1,3)]
for row,truth in zip(got,expected):
 for v,w in zip(row,truth):assert v.overlaps(w)
_,Bern=c.bernstein_matrix(Q);betas=arb_mat(got)*Bern.transpose();remainder=c.product_tail(lp,ld)+c.product_tail(lq,lh)+ll[2]+sum((c.upper(poly[i*base+j]) for i in range(7) for j in range(Q+1,2*Q+1)),arb(0));bound=sum((max(c.upper(betas[i,j]) for j in range(Q+1)) for i in range(2)),arb(0))+remainder
for z in [F(-1),F(-7,13),F(0),F(5,7),F(1)]:
 t=tc+h*c.aa(z);true_W=abs((arb(3)*c.aa(F(5,2))-1)*(3*t).exp()+5*(5*t).exp())+(5*t).exp();assert true_W.upper()<=bound.upper()
meta={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','fixture':'rho=e^(3t)sin(theta),psi=e^(4t)sin(2theta), exact E=(3cl-1)e^(3t)sin(theta)+e^(5t)(5sin(theta)-sin(3theta))','coefficients':34,'whole_bound_point_checks':5,'source_sha256':c.sha(__file__),'implementation_sha256':c.sha(Path(c.__file__))}
(E/'angular_fixture.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta),flush=True)
original=c.ff;calls=0
def checked_ff(x):
 global calls
 assert x.rad()==0,'Nonzero-radius number sent to midpoint-only dyadic exporter';calls+=1;return original(x)
c.ff=checked_ff
sys.argv=[c.__file__,'--degree','16','--tag','q16_replay'];c.main()
(E/'zero_radius_replay.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','zero_radius_export_assertions':calls,'implementation_sha256':c.sha(Path(c.__file__)),'wrapper_sha256':c.sha(__file__),'result_sha256':c.sha(E/'q16_replay_result.json')},indent=2)+'\n')
