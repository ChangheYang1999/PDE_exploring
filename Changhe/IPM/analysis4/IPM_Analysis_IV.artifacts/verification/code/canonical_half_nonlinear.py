"""Full selected nonlinear sums using signed Cartesian Laurent derivatives."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,pickle,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,arb_poly,ctx
from stream_precision_audit import unpack
ROOT=Path('research/291_canonical_half_finite')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def text(x):return x.str(40,radius=True)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--orders',default='8,12,20,40,80,160,300');a=ap.parse_args();orders=list(map(int,a.orders.split(',')))
 start=time.monotonic();ctx.prec=768;zero=arb(0)
 manifest=json.loads((ROOT/'verification/input_manifest.json').read_bytes());p=Path(manifest['source']);raw=p.read_bytes();assert sha256(raw).hexdigest()==manifest['source_sha256'];state=pickle.loads(raw);del raw
 assert (state['A'],state['B'])==('1','2')
 values={field:{n:[[arb(*unpack(v)) for v in col] for col in state[field][n]] for n in range(1,max(orders)+1)} for field in ['f','g']};del state
 rows=[]
 for n in orders:
  begin=time.monotonic();stride=4*n+5;M=2*n+2
  def derivative(field,i,which):
   cols=values[field][i];shift=2*i+1;radial=arb(1+(field=='g'))-arb(i)/2
   out=[zero for _ in range(stride*(len(cols)-1)+2*shift+1)]
   for degree,col in enumerate(cols):
    for j,amplitude in enumerate(col):
     m=2*j+(field=='f')
     if m==0:assert amplitude.is_zero();continue
     for sign in [1,-1]:
      freq=sign*m;v=sign*amplitude/4;pos=stride*degree+shift+freq
      out[pos-1]+=(radial+freq)*v
      out[pos+1]+=(radial-freq)*v*(1 if which=='X' else -1)
      if degree:
       out[pos-1-stride]+=degree*v
       out[pos+1-stride]+=degree*v*(1 if which=='X' else -1)
   return arb_poly(out)
  def expected():
   cols=values['f'][n];out=[zero for _ in range(stride*(len(cols)-1)+2*M+1)]
   for degree,col in enumerate(cols):
    for j,value in enumerate(col):
     m=2*j+1;v=value/2;pos=stride*degree+M
     out[pos+m]+=(n-1)*v;out[pos-m]-=(n-1)*v
     if degree:out[pos+m-stride]-=2*degree*v;out[pos-m-stride]+=2*degree*v
   return arb_poly(out)
  total=arb_poly()
  for i in range(1,n):
   j=n-i
   total+=derivative('g',i,'X')*derivative('f',j,'Y')-derivative('g',i,'Y')*derivative('f',j,'X')
   if i%25==0:print(json.dumps(dict(at=now(),n=n,through_pair=i,elapsed_s=time.monotonic()-begin)),flush=True)
  target=expected();res=total-target;failed=[j for j,v in enumerate(res.coeffs()) if not v.contains(0)];assert not failed,(n,failed[:10])
  norm=sum(map(abs,target.coeffs()),zero);error=sum(map(abs,res.coeffs()),zero)
  row=dict(n=n,ordered_pairs=n-1,kronecker_stride=stride,checked_coefficients=len(res),all_contain_zero=True,relative_residual=text(error/norm),actual_elapsed_s=time.monotonic()-begin);rows.append(row)
  result=dict(at=now(),all_checks_pass=True,complete_requested_orders=len(rows)==len(orders),source_sha256=manifest['source_sha256'],bits=768,orders=rows,actual_elapsed_s=time.monotonic()-start,scope='Finite coefficient residual consistency in supplied balls, using independent Cartesian derivatives.')
  (ROOT/'verification/nonlinear_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(row),flush=True)
 for name in ['canonical_half_nonlinear.py','stream_precision_audit.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':
 try:main()
 except Exception as e:
  d=dict(at=now(),type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)]);(ROOT/'verification/NONLINEAR_FAILURE.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d),flush=True);raise SystemExit(1)
