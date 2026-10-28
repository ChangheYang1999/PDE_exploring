"""Independent symbolic and quadrature checks. Diagnostics, not a certificate."""
from pathlib import Path
from datetime import datetime, timezone
import importlib.util, hashlib, json, random
import sympy as sp
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
mp.mp.dps=65
z,c,a=sp.symbols('z c a', nonzero=True)
bc=-1/((c*c-a*a)*(z-c))-2*c*sp.log(z-c)/(c*c-a*a)**2+sp.log(z-a)/(2*a*(a-c)**2)-sp.log(z+a)/(2*a*(a+c)**2)
assert sp.cancel(sp.diff(bc,z)-1/((z-c)**2*(z*z-a*a)))==0
X,Y=sp.symbols('X Y',real=True);ar=sp.symbols('ar',positive=True)
V=2*ar*X*Y/(sp.pi*((X*X-Y*Y-ar*ar)**2+4*X*X*Y*Y))
k=lambda u:(u*u-Y*Y)/(2*sp.pi*(u*u+Y*Y)**2)
assert sp.cancel(sp.diff(V,Y)-(k(X-ar)-k(X+ar)))==0
spec=importlib.util.spec_from_file_location('cert',ROOT/'code/certify_axis_clamp_layercake.py');cert=importlib.util.module_from_spec(spec);spec.loader.exec_module(cert)
def ball(x):return cert.arb(str(x))
def in_ball(v,b):return mp.mpf(str(b.lower()))<=v<=mp.mpf(str(b.upper()))
# Decimal serialization is deliberately checked through a looser decimal ball.
def checked(v,b):
 lo=mp.mpf(b.lower().str(65,radius=False));hi=mp.mpf(b.upper().str(65,radius=False))
 assert lo-mp.mpf('1e-60')<=v<=hi+mp.mpf('1e-60'),(str(v),str(b))
 return float(max(abs(v-lo),abs(v-hi)))
a=mp.mpf('.5');rt2=mp.sqrt(2);rt3=mp.sqrt(3)
def vv(x,y):return -a/mp.pi*mp.im(1/((x+1j*y)**2-a*a))
def ll(m,d,lo,hi=mp.inf):return mp.quad(lambda x:vv(x,m*x+d),[lo,hi])
def positive(u,s,b):
 ans=0;lo=max(u,s);hi=a-rt2*s
 if lo<hi:ans+=ll(-1,hi,lo,hi)
 d1=-a-rt2*s;d2=((rt3-1)*b-a-2*s)/rt3;cross=(d2-d1)/(1-1/rt3)
 lo=max(u,a+rt2*s,a-(rt3-1)*b+2*s)
 if lo<cross:ans+=ll(1,d1,lo,cross)
 ans+=ll(1/rt3,d2,max(lo,cross));return 2*ans

def negative(u,s,b):
 left=a+b-s/rt2;right=a+b-s/2;ans=0
 if u<left:ans+=ll(1,-a+rt2*s,u,left)
 low=max(u,left)
 if low<right:ans+=mp.quad(lambda x:vv(x,b+mp.sqrt(s*s-(x-a-b)**2)),[low,right])
 ans+=ll(1/rt3,((rt3-1)*b-a+2*s)/rt3,max(u,right));return 2*ans
rng=random.Random(628031);rows=[]
for j in range(48):
 alpha=mp.mpf(rng.choice(['.25','.5','.75','.9']));b=mp.mpf(rng.choice(['.2','.35','.75','1.5']));t=mp.exp(mp.mpf(str(rng.uniform(-7,4))));cc=mp.power(2,alpha-1)
 U=lambda v:mp.power(v/cc,1/alpha)
 if j%3==0:part='plus';u=U(t);s=U(t+mp.mpf('.5'));val=positive(u,s,b);encl=cert.positive_mass(ball(u),ball(s),ball(b))
 elif j%3==1:
  t=t/(1+t)/2;part='mid';u=U(t);s=U(mp.mpf('.5')-t);val=positive(u,s,b);encl=cert.positive_mass(ball(u),ball(s),ball(b))
 else:part='minus';u=U(t+mp.mpf('.5'));s=U(t);val=negative(u,s,b);encl=cert.negative_mass_magnitude(ball(u),ball(s),ball(b))
 err=checked(val,encl);rows.append(dict(part=part,alpha=str(alpha),b=str(b),t=str(t),quadrature=str(val),arb=str(encl),comparison_tolerance=err))
result=dict(time_utc=datetime.now(timezone.utc).isoformat(),symbolic_kernel_derivative='PASS',symbolic_arc_primitive_derivative='PASS',quadrature_cases=len(rows),status='PASS; numerical comparisons are diagnostics only',rows=rows,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'code/certify_axis_clamp_layercake.py']})
p=ROOT/'11_lattice_pole_constraints/axis_clamped_layercake/verification/primitive_crosscheck.json';p.write_text(json.dumps(result,indent=2)+'\n');print(p);print(result['status'])
