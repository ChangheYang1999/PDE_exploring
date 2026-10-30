"""Exact finite checks for the analytic moment-resolved endpoint theorem."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import time
import sympy as sp
from flint import fmpq as Q, arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 768
B = Path(__file__).resolve().parents[1]
start = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
ar = lambda q: arb(Q(q).p) / arb(Q(q).q)
tw = lambda q: arb(2) ** ar(q)

# Work with pi*K. The omitted constant is put back in the proof.
x, y = sp.symbols('x y', real=True)
s = x*x+y*y
K = sp.Matrix([-x*y/s**2, (x*x-y*y)/(2*s**2)])
J = K.jacobian([x,y])
assert all(sp.factor(v) == 0 for v in J.T*J-sp.eye(2)/s**3)
D = sp.Matrix([(x**3-3*x*y*y)/s**3, (3*x*x*y-y**3)/s**3])
assert all(sp.factor(v) == 0 for v in -K.diff(y)-D)
z, w, t = sp.symbols('z w t')
assert sp.factor(sp.diff(1/(2*(z+t*w)**2),t,3).subs(t,0)+12*w**3/z**5)==0
assert Q(12)*2**5/6 == 64

c = Q(4076476460239181,2251799813685248)
g = 1/c
delta = 1-g
q = g-4
assert -4<q<-3 and -5<q<-3 and 1-c*q==4*c
# q = qstar forces all displayed error exponents below the leading one.
assert q-delta<q and q-4<q and 2*q-1<q
E = ar(Q(1,2))+tw(-q)+tw(3-q)+tw(q+2)/ar(-q)+tw(-q-2)/ar(-q-3)+tw(2-q)/ar(q+5)
assert E > 0
expected = {
    '007':'bcd0e49225807ba313dfb86ec386b4d3d3411bdcb233072d5047e84cc27ec58b',
    '013':'3a2cf49c387db2fd95e7174a2b5f58103201857f01ba875e391b88714ab96471',
    '014':'8168bf8b326124bc720cc992a5fbe0300d9b1250eb9f4e862b0f2ce38b53b6ce',
}

def dec(d):
    return {int(n): Q(a) for n,a in d.items() if Q(a)}

def put(d,n,a):
    if n<0:
        n,a=-n,-a
    if n and a:
        d[n]=d.get(n,Q(0))+a
        if not d[n]:
            del d[n]

def dot(a,b):
    return sum((v*b.get(n,Q(0)) for n,v in a.items()),Q(0))

rows=[]
for name in ['007','013','014']:
    path=B/f'data/{name}_endpoint.json'
    assert sha(path)==expected[name]
    raw=json.loads(path.read_text())
    assert Q(raw['c'])==c
    A=dec(raw['F12']); T=dec(raw['Theta0']); T12=dec(raw['Theta12']); P=dec(raw['P'])
    assert A=={n:-4*c*v for n,v in T12.items()}
    fresh={}
    for n,v in T.items():
        put(fresh,n+2,v*(g+n)/2)
        put(fresh,n-2,v*(g-n)/2)
    assert fresh==P and P
    lam=dot(A,P)/dot(P,P)
    assert lam==Q(raw['lambda'])
    R={n:A.get(n,Q(0))-lam*P.get(n,Q(0)) for n in set(A)|set(P)}
    R={n:v for n,v in R.items() if v}
    assert R==dec(raw['projection_residual']) and R and dot(R,P)==0
    n,m=raw['nonzero_determinant']['modes']
    det=A.get(n,Q(0))*P.get(m,Q(0))-A.get(m,Q(0))*P.get(n,Q(0))
    assert det and det==Q(raw['nonzero_determinant']['value'])
    assert dot(R,R)==dot(A,A)-dot(A,P)**2/dot(P,P)>0
    distance=(arb.pi()*ar(dot(R,R))).sqrt()
    tail_floor=distance/ar(4*c)
    # A heuristic decimal proposes a rational integer; only the interval check accepts it.
    floor=Q(int(float(tail_floor))-1)
    assert tail_floor>ar(floor)
    rows.append({'candidate':name,'exact_data_sha256':sha(path),'nonzero_determinant_modes':[n,m],
                 'nonproportional_exact':True,'projection_orthogonal_exact':True,
                 'angular_distance':distance.str(110),'forced_tail_angular_floor':tail_floor.str(110),
                 'strict_integer_lower':str(floor),
                 'scope':'Requires a reference satisfying all endpoint residual and gradient hypotheses (5).'})

out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,
     'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),
     'kernel_checks':{'jacobian_conformal_norm':True,'S1_dipole_sign':True,'third_derivative_coefficient':True},
     'qstar_exact':str(q),'E_qstar':E.str(110),'rows':rows,
     'verdict':'Exact kernel and angular checks CONFIRMED; new analytic theorem OPEN independent Opus review.'}
with (B/'verification/result.json').open('x') as f:
    json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
