"""Canonical density moments at every original exact spline knot."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,gzip,hashlib,time,resource,itertools
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from types import SimpleNamespace
import numpy as np
from flint import arb,ctx,fmpq,fmpq_mat
from modal_setup import setup,exact_poly
from fast_moments import aa,integral
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/middle_residual/evidence'
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import export_ball

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def fq(v):return fmpq(v.numerator,v.denominator)
def main():
 ctx.prec=384;ctx.threads=1;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic();z=setup();t=z['t'];knots=sorted(set(t));S=len(knots)-1;M=z['M'];assert M==260
 gp=BASE.parent/'ipmA-num/data/cert_green.npz';assert sha(gp)=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1';gg=np.load(gp,allow_pickle=False);groups=[(int(i),len(list(v))) for i,v in itertools.groupby(gg['parent'])];assert [i for i,n in groups]==list(range(S));counts=[n for i,n in groups];tb=[]
 for (a,b),n in zip(zip(knots[:-1],knots[1:]),counts):assert n>0;tb.extend(a+(b-a)*F(j,n) for j in range(n))
 tb.append(knots[-1]);assert len(tb)==7810
 for i,v in enumerate(tb):m=F.from_float(float(gg['tb'][i]));r=F.from_float(float(gg['tb_rad'][i]));assert r>=0 and m-r<=v<=m+r
 del gg
 dummy=SimpleNamespace(t=t,deg=7);polys=[];ileft=[];jright=[None]*S;iv=list(z['iv']);jv=list(z['jv'])
 for i,(a,b) in enumerate(zip(knots[:-1],knots[1:])):
  sp,C=exact_poly(dummy,a,b);assert t[sp]<=a<b<=t[sp+1];T=C*fmpq_mat([[fq(v) for v in row] for row in z['sd'][sp-7:sp+1]])
  p=[[aa(F(str(T[q,j]))) for q in range(8)] for j in range(M+2)];assert all(v==0 for v in p[-1]);polys.append(p);ileft.append(list(iv));h=b-a;cache={}
  for n in range(1,M+2):rate=-(2*n+4);iv[n-1]=aa(rate*h).exp()*iv[n-1]+integral(p[n-1],h/2,h,rate,True,cache)
  if i%100==0:emit(stage='forward_knots',span=i,total=S,seconds=time.monotonic()-start)
 for i in reversed(range(S)):
  a,b=knots[i:i+2];h=b-a;jright[i]=list(jv);cache={}
  for n in range(1,M+2):rate=4-2*n;jv[n-1]=aa(rate*h).exp()*jv[n-1]+integral(polys[i][n],-h/2,h,rate,False,cache)
  if i%100==0:emit(stage='backward_knots',span=i,total=S,seconds=time.monotonic()-start)
 paths={'source':Path(__file__),'setup':Path(__file__).parent/'modal_setup.py','fast_moments':Path(__file__).parent/'fast_moments.py','input':BASE/'data_exact/modal_v2.json','normalization':z['zpath'],'Cox':BASE/'research/canonical_inverse/code/exact_audit.py','ball_transport':BASE/'research/ball_transport/code/dyadic_ball.py'};hashes={k:sha(p) for k,p in paths.items()}
 header={'type':'header','utc':utc(),'spans':S,'cells':len(tb)-1,'degree':7,'stream_modes':261,'precision_bits':384,'hashes':hashes,'comparison_grid_sha256':sha(gp),'scalars_exact':{k:str(v) for k,v in z['sc'].items()}}
 destination=E/'original_knots.jsonl.gz';tmp=E/'original_knots.partial.jsonl.gz';ci=0
 with gzip.open(tmp,'wt',compresslevel=3) as f:
  f.write(json.dumps(header,separators=(',',':'))+'\n')
  for i,(a,b) in enumerate(zip(knots[:-1],knots[1:])):
   record={'type':'span','span':i,'first_cell':ci,'count':counts[i],'a_exact':str(a),'b_exact':str(b),'polynomial_mid_exact':str((a+b)/2),'density_polynomials':[[export_ball(v) for v in p] for p in polys[i]],'i_left':list(map(export_ball,ileft[i])),'j_right':list(map(export_ball,jright[i]))};f.write(json.dumps(record,separators=(',',':'))+'\n');ci+=counts[i]
  assert ci==7809;f.write(json.dumps({'type':'complete','spans':S,'cells':ci,'utc':utc()})+'\n')
 tmp.replace(destination);out={'utc':utc(),'status':'COMPUTED_REQUIRES_AUDIT','spans':S,'cells':ci,'hashes':hashes,'output_sha256':sha(destination),'output_bytes':destination.stat().st_size,'seconds':time.monotonic()-start};(E/'knot_manifest.json').write_text(json.dumps(out,indent=2)+'\n');emit(stage='done',**out)
if __name__=='__main__':main()
