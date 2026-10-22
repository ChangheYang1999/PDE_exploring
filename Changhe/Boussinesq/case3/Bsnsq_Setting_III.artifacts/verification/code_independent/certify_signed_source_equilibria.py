"""Exact Fraction interval certificate, no floating arithmetic in verdicts."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
V=Path('research/238_signed_source_axis_equilibria/verification')
inputs=json.loads((V/'input.json').read_text());N=inputs['taylor_even_order']
class I:
 def __init__(self,a,b=None):self.a=F(a);self.b=F(a if b is None else b);assert self.a<=self.b
 def __add__(self,o):
  if not isinstance(o,I):o=I(o)
  return I(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,o):return self+-o if isinstance(o,I) else self+I(-F(o))
 def __rsub__(self,o):return I(o)+-self
 def __mul__(self,o):
  if not isinstance(o,I):o=I(o)
  p=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b];return I(min(p),max(p))
 __rmul__=__mul__
 def __truediv__(self,o):
  if not isinstance(o,I):o=I(o)
  assert o.a*o.b>0
  return self*I(1/o.b,1/o.a)
 def __rtruediv__(self,o):return I(o)/self
 def encode(self):return {'lower':str(self.a),'upper':str(self.b),'decimal_display_only':[float(self.a),float(self.b)]}
def poly(z,n):
 term=F(1);total=term
 for k in range(1,n+1):term*=(-z)/k;total+=term
 return total
def eneg(z):
 assert z.a>=0
 return I(max(F(0),poly(z.b,N+1)),min(F(1),poly(z.a,N)))
def B(a,S):return (1-eneg(a*S))/S
def Bp(a,S):return ((1+a*S)*eneg(a*S)-1)/(S*S)
t0=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'input_sha256':hashlib.sha256((V/'input.json').read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest(),'checks':[],'intervals':[]}
beta=F(inputs['beta']);height=F(inputs['upper_height']);au=F(inputs['upper_exponent']);al=F(inputs['lower_exponent']);relative=F(inputs['lower_relative_amplitude']);strain=F(inputs['strain'])
fu=1/(4*au*au);fl=relative/(4*al*al);cu=-2*fu*height*Bp(au,I(height*height));A=strain/cu
u0=fu*B(au,I(height*height))+fl*al
def phi(y):return beta*y+A*(fu*B(au,(y-height)*(y-height))+fl*B(al,y*y)-u0)
def dp(y):return beta+A*(2*fu*(y-height)*Bp(au,(y-height)*(y-height))+2*fl*y*Bp(al,y*y))
for index,pair in enumerate(inputs['brackets']):
 l,r=map(F,pair);left=phi(I(l));right=phi(I(r));d=dp(I(l,r));row={'bracket':pair,'phi_left':left.encode(),'phi_right':right.encode(),'phi_prime_over_bracket':d.encode(),'horizontal_eigenvalue':(2*beta-d).encode()};out['intervals'].append(row)
 if index==0:tests=[('left negative',left.b<0),('right positive',right.a>0),('vertical derivative >2',d.a>2),('vertical derivative <3',d.b<3),('horizontal positive',(2*beta-d).a>0)]
 else:tests=[('left positive',left.a>0),('right negative',right.b<0),('vertical derivative >-4',d.a>-4),('vertical derivative <-2',d.b<-2),('horizontal positive',(2*beta-d).a>0)]
 out['checks'] += [{'name':str(index)+': '+n,'pass':bool(q)} for n,q in tests]
out['checks'] += [{'name':'positive normalization denominator','pass':bool(cu.a>0)},{'name':'even Taylor order','pass':N%2==0},{'name':'distinct intervals and center','pass':F(inputs['brackets'][0][1])<F(inputs['brackets'][1][0])<F(inputs['brackets'][1][1])<0}]
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,all_passed=all(q['pass'] for q in out['checks']),normalization_A=A.encode(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(V/'certificate.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out['intervals']:print(r['bracket'],r['phi_left']['decimal_display_only'],r['phi_right']['decimal_display_only'],r['phi_prime_over_bracket']['decimal_display_only'])
print('PASS',sum(q['pass'] for q in out['checks']),'/',len(out['checks']),out['started_utc'],out['ended_utc'],out['elapsed_seconds'])
if not out['all_passed']:raise SystemExit('certificate rejected')
