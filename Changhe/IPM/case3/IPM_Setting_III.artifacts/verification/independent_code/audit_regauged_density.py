"""Independent literal-field gauge and half-widths, using only saved numeric data."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Fr
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
import mpmath as mp
from scipy.optimize import brentq
from q_local_checkpoint import QLocalCheckpoint
from q_high_precision_density import MPQDensity
from q_mp_primitives import mf
root=Path('research/regauged_density_audit/verification');root.mkdir(parents=True,exist_ok=True)
source=Path('evidence/q_exact_jets/R1_SUMMARY.json');prior=json.loads(source.read_text());rows=[];states=[];start=time.monotonic()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
out=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',code_sha256=sha(__file__),proof_sha256=sha(root.parent/'PROOF.md'),source_summary_sha256=sha(source),states=rows)
def save():(root/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
for N in [64,96,128,160,192]:
 old=next(x for x in prior['rows']if x['tag']==f'R1C_CL3P0_N{N}');q=QLocalCheckpoint(old['source']);assert q.meta['sha256']==old['sha256'];cc=q.exact_coefficients()
 a=float(sum(c*(-1)**j for j,c in enumerate(cc[0])));K=float(sum((-1)**k*sum(c) for k,c in enumerate(cc))/2)*q.L**(1/q.kappa);l=(a/K)**q.kappa
 states.append((q,a,K,l,cc));r=dict(N=N,source=q.meta['source'],source_sha256=q.meta['sha256'],a=a,actual_K=K,actual_exponent=1-1/q.kappa,dilation_length=l,report_idealized_length=(a/10)**1.5,axis={});rows.append(r);save()
 def axis(X,kaxis):
  t,s,w=q.coordinates(np.asarray(X)/l);value=np.zeros_like(t);power=np.ones_like(t)
  for k in range(q.M):value+=power*q.polynomial(k,t);power*=s*(-1 if kaxis=='y' else 1)
  return w*value/a
 for kaxis in ['x','y']:
  grid=np.geomspace(1e-3,1e4,1400);values=axis(grid,kaxis);idx=np.flatnonzero(values<=.5);assert len(idx)
  fine=np.geomspace(1e-5,1e4,4097);vf=axis(fine,kaxis);i=int(np.flatnonzero(vf<=.5)[0]);assert i>0
  bracket=[float(fine[i-1]),float(fine[i])];cross=brentq(lambda x:float(axis(x,kaxis)-.5),*bracket,xtol=2e-13,rtol=1e-14)
  assert abs(float(axis(cross,kaxis)-.5))<1e-11
  r['axis'][kaxis]=dict(producer_grid_first_below=float(grid[idx[0]]),producer_grid_preceding=float(grid[idx[0]-1]),producer_grid_ratio=float(grid[1]/grid[0]),independent_bracket=bracket,bracketed_crossing=cross,crossing_residual=float(axis(cross,kaxis)-.5),crossing_over_sqrt_a=cross/np.sqrt(a))
 print(json.dumps(dict(N=N,a=a,K=K,length=l,widths=r['axis'])),flush=True);save()
for label,nx,ny in [('reported_grid',61,60),('finer_grid',122,121)]:
 xi=np.linspace(0,3,nx);y=np.linspace(.05,3,ny);xx,yy=np.meshgrid(xi,y,indexing='ij');vals=[]
 for q,a,K,l,cc in states:vals.append(l/a*q.rho(np.sqrt(a)*xx/l,yy/l))
 ref=vals[-1]
 for r,g in zip(rows,vals):
  delta=abs(g-ref);ii=np.unravel_index(np.argmax(delta),delta.shape);r[label]=dict(grid=[nx,ny],max_abs_difference_from_N192=float(delta[ii]),xi=float(xx[ii]),y=float(yy[ii]),g=float(g[ii]),g192=float(ref[ii]))
 save()
mp_rows=[]
for precision in [60,90]:
 with mp.workdps(precision):
  models=[MPQDensity(cc,Fr(q.L),Fr(q.kappa),Fr(q.cl))for q,a,K,l,cc in states]
  for i,((q,a,K,l,cc),r) in enumerate(zip(states,rows)):
   point=r['reported_grid'];xi,y=point['xi'],point['y']
   values=[]
   for j in [i,4]:
    aq=mf(states[j][1]);lq=mf(states[j][3]);X=mp.sqrt(aq)*mf(xi)/lq;Y=mf(y)/lq;rr=mp.sqrt(X*X+Y*Y);th=mp.atan2(Y,X);v=models[j].at(rr,th)
    values.append(lq/aq*rr*v[0])
   delta=abs(values[0]-values[1]);err=abs(delta-mf(point['max_abs_difference_from_N192']))
   mp_rows.append(dict(N=q.N,precision=precision,xi=xi,y=y,MP_difference=mp.nstr(delta,precision),double_difference_error=mp.nstr(err,12)))
 out['MP_checks']=mp_rows;save()
out.update(status='COMPUTED',finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save()
