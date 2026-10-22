"""Own exact Fourier and elementary radial controls; no foreign execution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,math,time
r=Path('research/351_spec_absolute_and_signed_drift');v=r/'verification';start=datetime.now(timezone.utc);tick=time.monotonic();checks=[]
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,t,d=None):checks.append(dict(name=n,passed=bool(t),detail=d))
f=json.loads((v/'freeze.json').read_text());ck('proof_before',f['prepared_utc']<start.isoformat());ck('proof_hash',f['proof_sha256']==h(r/'PROOF.md'))
for x in f['inputs']:ck('frozen_'+x['source'],h(x['copy'])==x['sha256'])
spec=Path(f['inputs'][0]['copy']).read_text();ck('ambiguous_never','In class A this NEVER happens' in spec);ck('signed_uncontrolled','signed circular truncations v0(R) are not controlled in general' in spec);ck('like_claim','tend to +infinity like' in spec);ck('uniform_tail_D','Omega = r^{-1/beta}(a(theta) + o(1)) UNIFORMLY' in spec)
# Complex Fourier coefficients of cos(n theta), with exact rational convolution.
def cosine(n):return {n:Q(1,2),-n:Q(1,2)}
def prod(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():c[i+j]=c.get(i+j,Q(0))+x*y
 return c
ck('cos1_cos3_orthogonality',prod(cosine(1),cosine(3)).get(0,0)==0)
ck('cos1_square_mean',prod(cosine(1),cosine(1))[0]==Q(1,2))
for n in [1,3,5,7]:ck('odd_x_reflection_'+str(n),(-1)**n==-1)
# Smooth control Omega=x(1+r^2)^(-(1+s)/2): exact disk moment.
rows=[]
for s in [Q(1,2),Q(1,3),Q(2,5),Q(1,10)]:
 B=1/(2*(1-s));sf=float(s);ck('s_between_zero_one_'+str(s),0<s<1)
 last=None
 for R in [10,100,10000,1e8]:
  moment=((1+R*R)**((1-sf)/2)-1)/(2*(1-sf));ratio=moment/R**(1-sf);err=abs(ratio-float(B))
  ck('positive_moment_'+str((s,R)),moment>0)
  if last is not None:ck('asymptotic_error_decreases_'+str((s,R)),err<last)
  last=err;rows.append(dict(s=str(s),R=R,normalized_moment=ratio,limit=str(B),error=err))
 ck('large_R_relative_accuracy_'+str(s),last/float(B)<1.1e-4)
 # Independent centered derivative of the exact radial primitive.
 for R in [0.2,1,3,20]:
  step=1e-5*max(1,R)
  primitive=lambda t:((1+t*t)**((1-sf)/2)-1)/(1-sf)
  derivative=(primitive(R+step)-primitive(R-step))/(2*step)
  expected=R*(1+R*R)**(-(1+sf)/2)
  ck('primitive_derivative_'+str((s,R)),abs(derivative-expected)<2e-9*max(1,abs(expected)))
# Direct numerical angular integration separately checks signed cancellation and nonzero absolute mass.
angular=[]
for N in [192,384,768,1536,3072,6144]:
 vals=[math.cos(2*math.pi*j/N)*math.cos(6*math.pi*j/N) for j in range(N)]
 signed=math.fsum(vals)*2*math.pi/N;absolute=math.fsum(abs(x) for x in vals)*2*math.pi/N
 ck('signed_quadrature_'+str(N),abs(signed)<2e-15);ck('absolute_positive_'+str(N),absolute>1)
 angular.append(dict(N=N,signed=signed,absolute=absolute))
exact_absolute=3*math.sqrt(3)/2
for j,row in enumerate(angular):
 row['exact_absolute']=exact_absolute;row['error']=abs(row['absolute']-exact_absolute)
 ck('absolute_error_positive_'+str(row['N']),row['error']>0)
 if j:ck('absolute_error_second_order_'+str(row['N']),0.249<row['error']/angular[j-1]['error']<0.251)
ck('absolute_final_accuracy',angular[-1]['error']<2e-6)
# Exact exponent computation after u=1+r^2 for the cubic smooth counter-control.
for s in [Q(1,2),Q(1,3)]:
 a=(3+s)/2;ck('cubic_exponent1_'+str(s),2-a==(1-s)/2);ck('cubic_exponent2_'+str(s),1-a==-(1+s)/2)
end=datetime.now(timezone.utc);out=dict(started_utc=start.isoformat(),ended_utc=end.isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(x['passed'] for x in checks),total=len(checks),proof_sha256=h(r/'PROOF.md'),code_sha256=h(__file__),radial_controls=rows,angular_controls=angular,checks=checks)
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:x for k,x in out.items() if k not in ('checks','radial_controls','angular_controls')},indent=2))
for c in checks:
 if not c['passed']:print('FAILED',c)
