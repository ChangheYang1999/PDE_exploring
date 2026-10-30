"""Cache one exact derivative order; each invocation is a bounded stage."""
import sys,time,json
from pathlib import Path
from flint import fmpq
from pipeline import source,DATA,load,save
from norms import derivative

def run(name,order):
 start=time.monotonic();target=DATA/f'{name}_D{order}.json.gz'
 if target.exists():
  load(name,order);print('existing cache verified',target.name,flush=True);return
 assert 1<=order<=3
 delta=1-1/fmpq(json.loads(source(name).read_text())['cl']);D=load(name,order-1);out={};d=order-1
 print('loaded',d,time.monotonic()-start,flush=True)
 for nx in range(order+1):
  out[order,nx]=derivative(D[d,0],d,'y',delta) if nx==0 else derivative(D[d,nx-1],d,'x',delta)
  if 1<=nx<=d:assert out[order,nx]==derivative(D[d,nx],d,'y',delta)
  print('derived component',nx,time.monotonic()-start,flush=True)
 save(name,order,out,target);print('completed',time.monotonic()-start,flush=True)
if __name__=='__main__':run(sys.argv[1],int(sys.argv[2]))
