"""Independent exact symbolic differential replay of the far-axis formula.
Construct raw homogeneous G_j, expand only after construction, apply physical
operators, then extract the residual's linear physical-y coefficient.
No imports from the certificate/evaluator or teammate code.
"""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
from pathlib import Path
import sympy as S
import json,datetime,hashlib,time
OUT=Path('research/logarithmic_far_compatibility/verification');OUT.mkdir(exist_ok=True)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic()
q,s=S.symbols('q s',positive=True);e,a,c1,c2=S.symbols('e a c1 c2');p=S.symbols('p00 p01 p02 p10 p11 p12 p20 p21 p22');p00,p01,p02,p10,p11,p12,p20,p21,p22=p
F=q**6+(e/s)**6;w=(e/s)**2*F**(-S.Rational(1,3))
P0=p00+p01*w+p02*w*w;P1=p10+p11*w+p12*w*w;P2=p20+p21*w+p22*w*w
raw=[q**3*e*F**S.Rational(1,3)*P0,c1*q**3*e*F**S.Rational(1,6)*P1,q**3*e*(c2*P1+c1*c1*P2/2)]
# Degree <=5 suffices for the linear-e coefficient after at most three eta derivatives.
G=[S.series(z,e,0,6).removeO().expand() for z in raw]
print(now(),'raw homogeneous series constructed',flush=True)
def tr(z):
 z=S.expand(z)
 return S.Add(*(v*e**k[0] for k,v in S.Poly(z,e).terms() if k[0]<6))
def mx(z):return S.diff(z,q)/(3*q*q)
A=S.diff(mx(G[0]),e);B=mx(mx(G[0]));invA=S.series(1/A,e,0,6).removeO().expand();b=tr(B*invA)
def dx(z):return tr(mx(z)-b*S.diff(z,e))
def dy(z):return tr(invA*S.diff(z,e))
psi0=-G[1];psi1=tr(-2*G[2]+mx(G[1])*S.diff(G[1],e)*invA)
omega0=-dx(dx(psi0))-dy(dy(psi0));omega1=-dx(dx(psi1))-dy(dy(psi1))
C=tr(-omega1-dy(psi0)*dx(omega0)+dx(psi0)*dy(omega0)+a*b)
# At e=0, physical y=0; partial_y=1/A partial_e. Divide by physical x=q^3.
axis=S.factor(S.diff(C,e).subs(e,0)/A.subs(e,0)/q**3*q**8)
if any(axis.has(v) for v in [q,p02,p12,p22]):raise ArithmeticError('Unexpected dependence in axis limit')
print(now(),'exact physical-operator axis coefficient extracted',flush=True)
h=S.Rational(5,3)*p00
Ksymbol=S.factor((axis-2*a/(3*h)).subs({c1:1,c2:S.Symbol('alpha')/2}))
if S.simplify(axis-(c1*c1*Ksymbol.subs(S.Symbol('alpha'),2*c2/(c1*c1))+2*a/(3*h)))!=0:raise ArithmeticError('c1/c2 homogeneity failed')
source=json.loads((OUT/'axis_exact.json').read_text());rows=[]
for r in source['rows']:
 vals={p00:S.Rational(r['p']['(0, 0)']),p01:S.Rational(r['p']['(0, 1)']),p10:S.Rational(r['p']['(1, 0)']),p11:S.Rational(r['p']['(1, 1)']),p20:S.Rational(r['p']['(2, 0)']),p21:S.Rational(r['p']['(2, 1)']),s:S.Rational(r['s']),S.Symbol('alpha'):3}
 value=Ksymbol.subs(vals)
 if value!=S.Rational(r['K']):raise ArithmeticError('Exact source coefficient disagreement '+r['label'])
 rows.append({'label':r['label'],'source_sha256':r['source_sha256'],'exact_rational_K_agrees':True})
report=dict(utc=now(),seconds=time.monotonic()-start,status='CONFIRMED_EXACT_SYMBOLIC_REPLAY',axis_expression=str(axis),K_expression=str(Ksymbol),higher_angular_coefficients_absent=True,homogeneity_c1_c2=True,rows=rows,hashes={str(z):hashlib.sha256(Path(z).read_bytes()).hexdigest() for z in [__file__,OUT/'axis_exact.json']},scope='Exact formal local expansion of analytic homogeneous fields at x>0, physical differential operators, and source rational coefficient identities. Global chart certificates remain separate. No sampling or quadrature inference.')
(OUT/'axis_symbolic.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
