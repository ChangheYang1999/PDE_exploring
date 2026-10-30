from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib,json,time
import sympy as S
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((ROOT/'data/manifest.json').read_text())
assert sha(ROOT/'PROOF.md')==manifest['proof_sha256']
for rel,digest in manifest['files'].items():assert sha(ROOT/rel)==digest,rel
params=json.loads((ROOT/'data/parameters.json').read_text());conv=lambda x:arb(Q(x).numerator)/Q(x).denominator
c=Q(params['c']);q=1/c-4;delta=1-1/c;aq=-q;Etest=(-q-1)/(2*(-q)*(-q-3));D=1-c*(q-delta)
assert Etest>Q(785064,1000000)
# Homogeneous velocity, local dipole sign, exact tail coefficients.
x,y=S.symbols('x y',positive=True);z=S.symbols('z',real=True);a=S.symbols('a',positive=True);m=S.symbols('m',real=True)
r2=x*x+y*y;psi=y*r2**((z+1)/2)/(a*(z+1)*(z+3))
wx=S.diff(psi,x,y);wy=-S.diff(psi,x,x)
wantx=x*r2**((z-1)/2)*(1+(z-1)*y*y/r2)/(a*(z+3))
wanty=-y*r2**((z-1)/2)*(1+(z-1)*x*x/r2)/(a*(z+3))
assert S.simplify(wx-wantx)==0 and S.simplify(wy-wanty)==0
K1=-x*y/(S.pi*r2**2);K2=(x*x-y*y)/(2*S.pi*r2**2);psid=-m*y/(2*S.pi*r2)
assert S.simplify(S.diff(psid,x,y)+m*S.diff(K1,y))==0
assert S.simplify(-S.diff(psid,x,x)+m*S.diff(K2,y))==0
assert S.simplify((-1/(z+3)+1/(z+1))/(2*a)-1/(a*(z+1)*(z+3)))==0
u,v=S.symbols('u v',positive=True)
assert S.factor(1/u-2/(u+v)+1/(u+2*v)-2*v*v/(u*(u+v)*(u+2*v)))==0
Aa=conv(aq);pi=arb.pi();moment_beta=pi*arb(4).gamma()*(Aa-3).gamma()/(Aa*(Aa+1).gamma())
moment_exact=6*pi/(Aa*Aa*(Aa-1)*(Aa-2)*(Aa-3));assert moment_beta.overlaps(moment_exact)
C,Qa,Dt,Dd=map(conv,(c,q,delta,D));alpha=-2*Qa-2;E=conv(Etest)
shape=2*Dt*Dt/(alpha*(alpha+Dt)*(alpha+2*Dt));assert shape>0
rows=[]
for name,angle in params['angles'].items():
 ep=json.loads((ROOT/'data'/f'{name}_endpoint.json').read_text())
 A={int(k):Q(v) for k,v in ep['F12'].items()};P={int(k):Q(v) for k,v in ep['P'].items()};th={int(k):Q(v) for k,v in ep['Theta0'].items()}
 ns=set(A)|set(P);proj=sum(A.get(n,0)**2 for n in ns)-sum(A.get(n,0)*P.get(n,0) for n in ns)**2/sum(P.get(n,0)**2 for n in ns)
 B=(pi*conv(proj)).sqrt()/(4*C);angle_a=conv(angle)
 def evaltr(cf,der=False):return sum(conv(v)*n*(n*angle_a).cos() if der else conv(v)*(n*angle_a).sin() for n,v in cf.items())
 av,ad,pv,pd=evaltr(A),evaltr(A,True),evaltr(P),evaltr(P,True)
 H0=abs(Qa*(av*pd-ad*pv))/(4*C*(Qa*Qa*pv*pv+pd*pd).sqrt());assert H0>999745
 g0=sum(n*v for n,v in th.items());s=1/c+2;v0=abs((s-1)*sum(n*v/(s*s-n*n) for n,v in th.items()))
 result={'candidate':name,'H_point':str(H0),'versions':{}}
 for label,vel in [('without_velocity_asymptotic',Q(0)),('with_velocity_asymptotic',v0)]:
  r0=((2*pi).sqrt()*H0*(conv(vel)+E*conv(g0))/(Dd*B))**(1/Dt)
  base=B*r0**(Qa+1);crude=base/alpha.sqrt();sharp=base*shape.sqrt()
  assert sharp<crude
  comparisons={label:bool(crude<conv(beta)) for label,beta in params['betas'].items()};assert all(comparisons.values())
  result['versions'][label]={'r0':str(r0),'crude_cap':str(crude),'delta_shape_cap':str(sharp),'crude_below_named_radius':comparisons}
 rows.append(result)
out={'completed_utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(ROOT/'data/manifest.json'),'q':str(q),'Etest_exact':str(Etest),'Etest':str(E),'moment_exact':str(moment_exact),'symbolic_checks':{'homogeneous_velocity_components':2,'dipole_components':2,'Green_coefficient':True,'shape_integral':True},'cap_shape_improvement_factor':str((alpha*shape).sqrt()),'rows':rows,'status':'Independent proof and exact arithmetic complete; Opus review pending'}
(ROOT/'verification/result.json').write_text(json.dumps(out,indent=2)+'\n')
print('Etest',E.str(18))
for row in rows:
 v=row['versions']['without_velocity_asymptotic'];print(row['candidate'],'crude',arb(v['crude_cap']).str(10),'delta',arb(v['delta_shape_cap']).str(10))
print('PASS',out['completed_utc'],out['elapsed_s'])
