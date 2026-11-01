"""Exact common-potential reconstruction for Q5/Q7, h2 single harmonics."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from extremal_single_exact import ExactSingle,poisson,coefficient,L,Q,Poly,parse
ROOT=Path('research/251_seven_nine_potential_logs')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def clone(base):
 c=object.__new__(ExactSingle);c.__dict__=base.__dict__.copy()
 for key in ['F','G','FX','FY','GX','GY']:setattr(c,key,getattr(base,key).copy())
 return c
def continuation(base,H):
 c=clone(base);n0=base.period;c.setg(n0,base.G[n0]+parse(Q(-2),{'2':[str(H)]}))
 for n in range(n0+1,2*n0+1):
  c.setf(n,c.density(n))
  if n<2*n0:c.setg(n,poisson(c.F[n]))
 return c,coefficient(c.F[2*n0],5)
def main():
 start=time.monotonic();ctx.prec=768;rows=[]
 for period in [5,7]:
  begin=time.monotonic();base=ExactSingle(2,period);base.initialize();f=base.F[period]
  maxk=(f.M-1)//2;D={maxk+1:Q(0)}
  for k in range(maxk,0,-1):D[k]=(coefficient(f,2*k+1)-k*D[k+1])/(k+1)
  M=2*maxk;cs=[Q(0)]*(2*M+1)
  for k,v in D.items():
   if v:
    a=-v/(4*k*k);cs[M+2*k]+=a/2;cs[M-2*k]+=a/2
  pure=L(Q(0),M,[Poly(cs)]);g=pure.X().Y().scale(-1);beta=coefficient(g,2)
  assert beta==D[2]/8 and ((pure.X().X()-pure.Y().Y()).Y()-f).zero()
  zero,R=continuation(base,Q(0));one,V=continuation(base,Q(1));sigma=V-R;assert sigma
  H=-R/sigma;corrected,obstruction=continuation(base,H);assert obstruction==0
  lam=beta-H;assert lam
  potential=pure+L(Q(0),0,[Poly([Q(0)]),Poly([lam])]);target=base.G[period]+parse(Q(-2),{'2':[str(H)]})
  assert ((potential.X().X()-potential.Y().Y()).Y()-f).zero()
  assert (potential.X().Y().scale(-1)-target).zero()
  row=dict(Q=period,h=2,mode=period+2,beta_pure_exact=str(beta),R1_exact=str(R),sigma1_exact=str(sigma),H_Q_exact=str(H),lambda_exact=str(lam),lambda_sign=1 if lam>0 else -1,exact_tuned_obstruction_zero=True,exact_density_reconstruction=True,exact_stream_reconstruction=True,actual_elapsed_s=time.monotonic()-begin)
  for name,v in [('beta_pure',beta),('R1',R),('sigma1',sigma),('H_Q',H),('lambda',lam)]:row[name+'_display']=arb(str(v)).str(55,radius=True)
  rows.append(row);print(json.dumps({k:v for k,v in row.items() if not k.endswith('_exact')}),flush=True)
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 for name in ['seven_nine_potential_logs.py','extremal_single_exact.py','laurent_log_audit.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps(dict(checked_at_utc=out['checked_at_utc'],all_checks_pass=True,elapsed_s=out['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)
