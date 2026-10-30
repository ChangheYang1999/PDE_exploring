from pathlib import Path
from datetime import datetime,timezone
import numpy as np
import json,hashlib,time
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[1]
def arfloat(x):
 a,b=float(x).as_integer_ratio();return arb(a)/arb(b)
def ratio(x):
 a,b=float(x).as_integer_ratio();return f'{a}/{b}'
def run():
 ctx.prec=384;start=time.monotonic();results=[]
 for M,N in [(59,160),(69,160),(69,192)]:
  nf=2*M+2;z,w=np.polynomial.legendre.leggauss(N);theta=(z+1)*np.pi/4;weights=w*np.pi/4
  freq=2*np.arange(nf)+1;mat=np.sin(freq[:,None]*theta[None,:])*np.sqrt(4/np.pi)
  vals,vecs=np.linalg.eigh((mat*weights)@mat.T);v=np.round(vecs[:,0]*10**12).astype(np.int64)
  exact=arb.pi()/4*sum((arb(int(a))**2 for a in v),arb(0));quad=arb(0)
  for th,wi in zip(theta,weights):
   thb=arfloat(th);value=sum((arb(int(a))*(int(n)*thb).sin() for n,a in zip(freq,v)),arb(0))
   quad+=arfloat(wi)*value*value
  relative=quad/exact
  assert relative>=0 and relative<arb('1e-6'),relative
  row={'M':M,'N':N,'integer_sine_coefficients':[int(a) for a in v],'nodes':[ratio(x) for x in theta],
       'weights':[ratio(x) for x in weights],'floating_eigenvalue':float(vals[0]),
       'quadrature_to_integral_ratio':relative.str(80),'strictly_below_one_millionth':True}
  results.append(row);print(M,N,row['quadrature_to_integral_ratio'],flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
      'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'results':results,
      'elapsed_seconds':time.monotonic()-start,'scope':'Specified frozen binary64 nodes and weights, arbitrary polynomial in allowed harmonic space'}
 (BASE/'verification/witness.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
