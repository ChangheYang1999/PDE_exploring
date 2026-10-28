from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as S
start=time.monotonic();base=Path(__file__).resolve().parent.parent
x,y=S.symbols('x y',real=True)
inputs=json.loads((base/'evidence/inputs.json').read_text())
assert inputs['potential_gaussian_rate_x']==[1,1] and inputs['potential_gaussian_rate_y']==[1,1]
g=S.Rational(*inputs['g_factor'])*y**3
D=lambda p,z:S.expand(S.diff(p,z)-2*z*p)
D2=lambda p,z:D(D(p,z),z)
a=2*g-D2(g,y);b=D2(D2(g,y),y)-12*D2(g,y)+12*g
vp=S.expand(g+x*x*a/2+x**4*b/24)
dp=S.expand(-D2(vp,x)-D2(vp,y))
u1=S.expand(-D(D(vp,y),x));u2=D2(vp,x)
quot=S.Poly(dp,x,y).exquo(S.Poly(x**4*y,x,y)).as_expr()
assert S.expand(dp-x**4*y*quot)==0
assert S.expand(vp.subs(x,-x)-vp)==0 and S.expand(vp.subs(y,-y)+vp)==0
assert all(i%2==0 and j%2==0 for (i,j),q in S.Poly(quot,x,y).terms())
assert D(u2,y).subs({x:0,y:0})==1
assert min(sum(e) for e,c in S.Poly(dp,x,y).terms())>=5
assert S.expand(D(u1,x)+D(u2,y))==0
# Direct exponential derivatives independently check the polynomial differential replay.
vg=vp*S.exp(-x*x-y*y)
assert S.simplify((-S.diff(vg,x,2)-S.diff(vg,y,2))*S.exp(x*x+y*y)-dp)==0
for deg,expect in [(0,g),(2,-D2(g,y)),(4,D2(D2(g,y),y))]:
 assert S.simplify(S.diff(vg,x,deg).subs(x,0)*S.exp(y*y)-expect)==0
# Independent physical-space strain kernel: exact radial Gamma and angular Beta moments.
def angular(i,j):
 assert i%2==0 and j%2==0
 return 2*S.gamma(S.Rational(i+1,2))*S.gamma(S.Rational(j+1,2))/S.gamma(S.Rational(i+j+2,2))
terms=[]
for (i,j),q in S.Poly(dp,x,y).terms():
 radial=S.gamma(S.Rational(i+j-1,2))/2
 term=S.simplify(q*radial*(3*angular(i+2,j+1)-angular(i,j+3))/S.pi)
 assert term.is_Rational
 terms.append({'powers':[i,j],'integrated_strain':[int(S.numer(term)),int(S.denom(term))]})
strain=sum(S.Rational(*z['integrated_strain']) for z in terms)
assert strain==1
enc=lambda p:[{'powers':list(e),'coefficient':[int(S.numer(c)),int(S.denom(c))]} for e,c in S.Poly(p,x,y).terms()]
polys={'v':enc(vp),'d':enc(dp),'U1':enc(u1),'U2':enc(u2),'P_in_x_y':enc(quot)}
(base/'evidence/exact_polynomials.json').write_text(json.dumps({'meaning':'Every field polynomial is multiplied by exp(-x^2-y^2). P is the quotient d/(x^4 y exp(-r^2)); its powers are even.','polynomials':polys,'strain_terms':terms},indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
deps=[]
for pre in ['123_','126_','165_','167_','174_','177_','181_','190_']:
 deps.append(next(p for p in (base.parent).iterdir() if p.name.startswith(pre))/'PROOF.md')
files=[Path(__file__).resolve(),base/'PROOF.md',base/'evidence/inputs.json',base/'evidence/exact_polynomials.json']+deps
out={'date':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.monotonic()-start,'verdict':'EXACT_IDENTITIES_CONFIRMED; ANALYTIC_HIGH_DOMAIN_OPUS_REVIEW_PENDING','strain_from_velocity':[1,1],'strain_from_kernel_integral':[1,1],'J':[0,1],'zero_vertical_cofactor_trace':True,'minimum_physical_order':min(sum(e) for e,c in S.Poly(dp,x,y).terms()),'polynomial_terms':{n:len(v) for n,v in polys.items()},'files':{str(p):sha(p) for p in files}}
(base/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
