"""Exact certificate for the profile-specific compensated velocity bound."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time, sys
import sympy as S
from flint import arb, ctx, fmpq as Q
from geometry import derive, velocity, dot
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1]
start=time.monotonic();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==m['proof_sha256']
for name,digest in m['inputs'].items():assert sha(B/name)==digest,name
par=json.loads((B/'data/parameters.json').read_text());ctx.prec=par['bits_for_displays'];E=Q(par['Eprof'])
checks=[]
def identity(name,x):
    z=S.cancel(S.trigsimp(S.expand_trig(S.expand(x))))
    assert z==0,(name,z)
    checks.append(name)
r=S.symbols('r',positive=True)
theta,p=S.symbols('theta p',real=True)
n=S.symbols('n',integer=True,positive=True)
f=r**p*S.sin(n*theta)
dx=lambda x:S.cos(theta)*S.diff(x,r)-S.sin(theta)*S.diff(x,theta)/r
dy=lambda x:S.sin(theta)*S.diff(x,r)+S.cos(theta)*S.diff(x,theta)/r
# Differentiate a generic polar mode without using the coefficient code.
w1=(dx(dy(f))/r**(p-2)).expand()
w2=(-dx(dx(f))/r**(p-2)).expand()
cs=S.cos(n*theta);sn=S.sin(n*theta)
cminus=cs*S.cos(2*theta)+sn*S.sin(2*theta)
cplus=cs*S.cos(2*theta)-sn*S.sin(2*theta)
sminus=sn*S.cos(2*theta)-cs*S.sin(2*theta)
splus=sn*S.cos(2*theta)+cs*S.sin(2*theta)
t1=((p+n)*(p+n-2)*cminus-(p-n)*(p-n-2)*cplus)/4
t2=-(p*p-n*n)*sn/2-((p+n)*(p+n-2)*sminus+(p-n)*(p-n-2)*splus)/4
identity('generic mixed Hessian formula',w1-t1)
identity('generic negative xx Hessian formula',w2-t2)
identity('homogeneous Poisson coefficient',(S.diff(f,r,2)+S.diff(f,r)/r+S.diff(f,theta,2)/r**2)/r**(p-2)-(p*p-n*n)*sn)
x,y=S.symbols('x y',real=True)
rr=x*x+y*y
psi=-y/(2*S.pi*rr)
k1=-x*y/(S.pi*rr**2);k2=(x*x-y*y)/(2*S.pi*rr**2)
identity('dipole first component',S.diff(psi,x,y)+S.diff(k1,y))
identity('dipole second component',-S.diff(psi,x,2)+S.diff(k2,y))
# A direct Cartesian first-sine fixture, independent of polar differentiation.
q0=Q(-7,2);p0=q0+2
fxy=y*rr**((S.Rational(p0.p,p0.q)-1)/2)
for xv,yv in ((S.Rational(3,5),S.Rational(4,5)),(S.Rational(4,5),S.Rational(3,5))):
    denom=S.Rational(p0.p,p0.q)**2-1
    got=[S.diff(fxy,x,y).subs({x:xv,y:yv})/denom,-S.diff(fxy,x,2).subs({x:xv,y:yv})/denom]
    vg=velocity({1:Q(1)},p0)
    z=xv+S.I*yv
    expected=[sum(S.Rational(v.p,v.q)*S.re(S.expand(z**k)) for k,v in vg[0].items()),sum(S.Rational(v.p,v.q)*S.im(S.expand(z**k)) for k,v in vg[1].items())]
    for i in range(2):identity('Cartesian first-sine fixture '+str((xv,yv,i)),got[i]-expected[i])
rows=[]
ar=lambda v:arb(v.p)/v.q
for name in par['candidates']:
    j=json.loads((B/f'data/{name}_endpoint.json').read_text())
    q,pv,ss,va,vb,t=derive(j)
    assert -5<q<-3
    l1=sum((abs(v) for v in t.values()),Q(0))
    assert l1<E*E,(name,str(l1))
    assert all(n%2==0 for n in t)
    checks.append(name+' positive Gram determinant and exact cosine l1 bound')
    rows.append({'candidate':name,'q':str(q),'p':str(pv),'S11':str(ss[0]),'S12':str(ss[1]),'S22':str(ss[2]),
      'det_S':str(ss[0]*ss[2]-ss[1]**2),'V_A':[{str(n):str(v) for n,v in d.items()} for d in va],
      'V_P':[{str(n):str(v) for n,v in d.items()} for d in vb],
      'trace_cosine_coefficients':{str(n):str(v) for n,v in t.items()},'trace_l1_exact':str(l1),
      'trace_l1_display':ar(l1).str(60),'sqrt_trace_l1_display':ar(l1).sqrt().str(60),
      'strictly_below_Eprof_squared':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'proof_sha256':m['proof_sha256'],
 'manifest_sha256':sha(B/'data/manifest.json'),'checker_sha256':sha(Path(__file__)),'geometry_sha256':sha(B/'code/geometry.py'),
 'Eprof':str(E),'precision_for_displays':ctx.prec,'checks':checks,'check_count':len(checks),'rows':rows,
 'certificate':'exact rational coefficient-sum bound; Arb only for displays','status':'PASS finite checks; analytic theorem OPEN independent review',
 'finite_radius_remainder_claimed':False,'foreign_code_executed':False}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
for row in rows:print(row['candidate'],row['trace_l1_display'],row['sqrt_trace_l1_display'])
