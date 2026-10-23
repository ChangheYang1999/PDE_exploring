from pathlib import Path
from datetime import datetime,timezone
import math,json,hashlib,sys
ROOT=Path('verification');R=ROOT/'research/primary_fresh_sample';V=R/'verification'
assert not sys.flags.optimize and Path.cwd().resolve()==ROOT and not(V/'INPUTS.json').exists()
def vdc(n):
 z=0.;w=.5
 while n:z+=w*(n%2);n//=2;w*=.5
 return z
points=[]
def add(x,y,group,index):points.append(dict(hex=[x.hex(),y.hex()],decimal=[repr(x),repr(y)],group=group,index=index))
for i in range(64):
 r=10**(-6+18*(i+.5)/64);t=(math.pi/2)*(.01+.98*vdc(i+1));add(r*math.cos(t),r*math.sin(t),'log_polar',i)
for i in range(16):
 r=10**(-4+12*(i+.5)/16);e=1e-6*(1+i%3)
 for g,t in [('near_horizontal',e),('near_vertical',math.pi/2-e)]:add(r*math.cos(t),r*math.sin(t),g,i)
for i,(x,y)in enumerate([(0.,0.),(0.,1e-6),(0.,1.),(1e-6,0.),(1.,0.)]):add(x,y,'exact_axes',i)
assert len(points)==len(set(tuple(p['hex'])for p in points))==101
old=json.loads((ROOT/'research/primary_common_mp_sample/verification/INPUTS.json').read_text());states=old['states'];bindings={}
for s in states:
 for key in ['source','exact_input']:
  p=Path(s[key]);h=hashlib.sha256(p.read_bytes()).hexdigest();assert h==s[key+'_sha256'];bindings[str(p)]=h
for p in [Path(__file__).resolve(),R/'PROOF.md']:bindings[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
out=dict(status='FROZEN_PROSPECTIVE101_SAMPLE',utc=datetime.now(timezone.utc).isoformat(),states=states,points=points,bindings=bindings,scope='No candidate evaluations used to select these fixed deterministic binary64 points.')
(V/'INPUTS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['utc'])
