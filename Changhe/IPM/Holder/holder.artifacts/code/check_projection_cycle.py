"""Exact algebra and small independent Arb cycles; no optimization."""
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
from flint import arb, ctx
ctx.prec=256
root=Path(__file__).resolve().parents[1]
u,v,b=s.symbols('u v b',positive=True)
f=b*(u*u-v*v)**(b-1)*(u*u+v*v)**(-b/2)
curl=s.diff(-f*v,u)-s.diff(f*u,v)
expected=2*b*b*u*v*(u*u-v*v)**(b-1)*(u*u+v*v)**(-1-b/2)
assert s.simplify(curl/expected)==1
# The squared singular values of [[sin,2cos],[0,-sin]] are (1+-cos)^2.
t=s.symbols('t',real=True)
lam=s.symbols('lam')
J=s.Matrix([[s.sin(t),2*s.cos(t)],[0,-s.sin(t)]])
char=(J.T*J-lam*s.eye(2)).det()
assert s.trigsimp(s.expand(char-(lam-(1+s.cos(t))**2)*(lam-(1-s.cos(t))**2)))==0
assert Q(108,1000)/(2*Q(71,100)**2)>Q(1,40)

def A(q): return arb(q.numerator)/q.denominator

def enc(x): return dict(display=str(x),lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()))
def target(p):
    x,y=p; d=x*x+y*y
    return (2*x*y*y/d,2*x*x*y/d)
def d2(p,q): return sum((x-y)**2 for x,y in zip(p,q))
vertices=[(Q(2,5),Q(1,10)),(Q(4,5),Q(1,10)),(Q(4,5),Q(1,5)),(Q(2,5),Q(1,5))]
n=8
points=[tuple(vertices[k][j]+Q(i,n)*(vertices[(k+1)%4][j]-vertices[k][j]) for j in range(2)) for k in range(4) for i in range(n)]
targets=list(map(target,points))
rows=[]
for alpha in [Q(1,2),Q(3,4),Q(9,10)]:
    old=arb(0); new=arb(0)
    for i,p in enumerate(points):
        old += A(d2(p,targets[i]))**(A(alpha)/2)
        new += A(d2(p,targets[(i+1)%len(points)]))**(A(alpha)/2)
    gain=old-new
    assert gain>0
    nn=(Q(10625)/alpha).__ceil__(); eps=alpha/(150000*nn); delta=alpha*alpha*eps*eps/12500
    rows.append(dict(alpha=str(alpha),old_cost=enc(old),new_cost=enc(new),point_cycle_saving=enc(gain),general_analytic_n=nn,general_epsilon=str(eps),general_delta=str(delta),general_delta_display=str(A(delta))))
proof=root/'08_improved_upper_bounds/local_projection/internal_cycle/PROOF.md'
rec=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),verdict='ALGEBRA AND SMALL CYCLES PASS; general proof pending independent cross-read',n=8,source_points=[[str(x),str(y)] for x,y in points],target_points=[[str(x),str(y)] for x,y in targets],rows=rows,identities=['curl positive identity','Jacobian squared singular values','source density lower bound'],sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),proof]})
(root/'08_improved_upper_bounds/local_projection/internal_cycle/verification/cycle_certificate.json').write_text(json.dumps(rec,indent=2)+'\n')
for r in rows: print(r['alpha'],r['point_cycle_saving']['display'],r['general_delta_display'])
print(rec['timestamp_utc'])
