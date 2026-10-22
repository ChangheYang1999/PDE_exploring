"""Exact rational Machin bounds. No floating transcendental functions."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

def bounds():
 def atan(q):
  z=F(1,q);s=sum(((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(100)),F(0));return s,s+z**201/F(201)
 a,b=atan(5);c,d=atan(239);lo,hi=16*a-4*d,16*b-4*c
 if not (F(3)<lo<hi<F(22,7)):raise ValueError('rational order')
 if (F(120,119)-F(1,239))/(1+F(120,119*239))!=1:raise ValueError('Machin identity')
 return lo,hi
if __name__=='__main__':
 p=Path(__file__).resolve();D=p.parents[1];lo,hi=bounds()
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'EXACT_RATIONAL_MACHIN_BOUNDS','terms_each':100,'atan_denominators':[5,239],'lower':str(lo),'upper':str(hi),'width':str(hi-lo),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((D/'PROOF.md').read_bytes()).hexdigest()}
 with (D/'evidence/pi_bounds.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['lower','upper','width']}))
