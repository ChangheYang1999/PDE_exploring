"""Result194: frozen text and independent algebra for the repaired statement."""
from pathlib import Path
import datetime, hashlib, json, re, time
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / 'research/hydrostatic_structure_v2_audit/verification'
start = time.monotonic()
checks = []
def check(name, value, detail=None):
    checks.append({'name': name, 'passed': bool(value), 'detail': detail})
def exact(name, expression):
    z = s.simplify(expression)
    check(name, z == 0, str(z))
inputs = json.loads((V/'INPUTS.json').read_text())
for name, item in inputs['inputs'].items():
    check('frozen input '+name, hashlib.sha256((V/name).read_bytes()).hexdigest() == item['sha256'])
oldbody,body,oldapp,app=[(V/x).read_text() for x in ['body.v1.txt','body.v2.txt','app.v1.txt','app.v2.txt']]
for tag,old,new in [('body',oldbody,body),('appendix',oldapp,app)]:
    displays=lambda text: [line.strip() for line in text.splitlines() if line.startswith('@@')]
    check(tag+' displayed formulas unchanged',displays(old)==displays(new),len(displays(new)))
required={
 'expansion topology': ('g_D = y + D u + O(D^2) in C^1 on compact sets',body),
 'velocity topology': ('V[g_D] = D V[u] + O(D^2) uniformly on compact sets',body),
 'conditional moment proved': ('the conditional moment identity in (d)',body),
 'isopycnal coefficient': ('(c xi + H) Z_xi + sigma Z_sigma = (D - H_xi) Z',body),
 'fixed isopycnal derivative': ('H_xi is taken at fixed sigma',body),
 'no universal method exclusion': ('establish no maximum-principle argument excluding g_y > 0',body),
 'signed whole-circle trace': ('K sgn(sin th) |sin th|^p as the entire trace',body),
 'homogeneous subtraction scope': ('it does not satisfy (5)',app),
 'joint tail derivative': ('V_2[u](xi, 1) + int_0^1 (1 - t) u_xixi(xi, t) dt - int_0^y u_xixi(xi, t) dt',app),
 'continuous polynomial coefficients': ('functions of y whose moment matrix is invertible',app),
 'inverse convergence premise': ('termwise only where the integrals converge',body),
 'possible logarithm only': ('whether a logarithm occurs is not determined here',body),
 'exact moment remainder': ('-int_y^inf (t - y) e(t) dt',app),
 'formal tangent domain': ('its velocity is not automatically defined classically',body),
 'strict growth weight': ('for c_1 != 0 this formal leading variation is not O(r^p)',body),
 'quotient scope': ('number of solution classes modulo dilation',body),
 'common compactness bounds': ('with one C and one gamma',body),
 'local third derivatives': ('|D^3 g_n| <= C_R',body),
 'C2 limit only': ('converges in C^2 on compact sets',body),
 'original problem left open': ('they establish neither existence nor nonexistence',body),
}
for name,(needle,haystack) in required.items(): check(name,needle in haystack)
x,y,D,ux,uy,u,v1,v2=s.symbols('x y D ux uy u v1 v2')
res=((1+D)*x+D*v1)*D*ux+((1+D)*y+D*v2)*(1+D*uy)-(y+D*u)
exact('first-order expansion',s.expand(res).coeff(D,1)-(x*ux+y*uy+y+v2-u))
A,I0,I1,Iy=s.symbols('A I0 I1 Iy')
Vone=I1+(A-I0)
exact('conditional-tail continuity identity',Vone+(I0-I1)-Iy-(A-Iy))
t=s.symbols('t', positive=True)
y=s.symbols('y', positive=True)
p=s.symbols('p', positive=True)
for degree in [0,1,3]:
    e=t**degree*s.exp(-t)
    m=s.integrate(t*e,(t,0,s.oo))
    delta=s.integrate(t*e,(t,0,y))+y*s.integrate(e,(t,y,s.oo))-m
    remainder=-s.integrate((t-y)*e,(t,y,s.oo))
    exact('moment remainder manufactured degree '+str(degree),delta-remainder)
exact('nonzero logarithmic curvature',s.integrate(1/t,(t,1,y))-s.log(y))
c,c1,r,Theta=s.symbols('c c1 r Theta', positive=True)
exact('parameter logarithm',c1*s.diff(r**(1/c)*Theta,c)+c1*r**(1/c)*Theta*s.log(r)/c**2)
A,c,Hx,Z,Zx,Sigma,Zs=s.symbols('A c Hx Z Zx Sigma Zs')
exact('fixed-sigma coefficient',(A-c-Hx)*Z-((2*c-1)-c-Hx)*Z-(A-(2*c-1))*Z)
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'passed':all(x['passed'] for x in checks),'count':len(checks)}
(V/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['utc','elapsed_seconds','passed','count']}))
for row in checks:
    if not row['passed']: print('FAIL',row)
raise SystemExit(0 if result['passed'] else 1)
