"""Independent Fourier-polynomial jet audit, without the lead's monomial code."""
import json
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
A,a=s.symbols('A a0');cl=(A+1)/2;eps=(A-1)/2

def put(v,k,value):
    if k>0:v[k]=v.get(k,0)+value
    elif k<0:v[-k]=v.get(-k,0)-value

def jet_matrix(n):
    odd=list(range(1,n+1,2)); cols=[]
    for k in odd:
        forcing={};put(forcing,k+1,s.Rational(n-k,2));put(forcing,k-1,s.Rational(n+k,2))
        chi={m:-f/((n+1)**2-m*m) for m,f in forcing.items() if m<n+1}
        velocity={}
        for m,c in chi.items():
            put(velocity,m+1,s.Rational(n+1-m,2)*c);put(velocity,m-1,s.Rational(n+1+m,2)*c)
        transport={k:cl*n-1};put(transport,k+2,eps*(n-k)/2);put(transport,k-2,eps*(n+k)/2)
        cols.append(s.Matrix([s.expand(transport.get(j,0)+a*velocity.get(j,0)) for j in odd]))
    return s.Matrix.hstack(*cols)

expected={3:a-4*A,5:3*a*a-(38*A+26)*a+128*A*(A+1),7:(a-8*A-4)*(a*a-(18*A+30)*a+96*A*A+192*A)}
rows=[]
for n in [3,5,7,9]:
    m=jet_matrix(n);det=s.factor(m.det());ratio=s.factor(det/expected[n]) if n in expected else None
    row={'degree':n,'matrix':[[str(v) for v in row] for row in m.tolist()],'determinant':str(det),'ratio_to_lead_polynomial':str(ratio) if ratio is not None else None,'same_zero_set_for_A_gt_1':bool(ratio is not None and not ratio.has(a) and s.ask(s.Q.nonzero(ratio),s.Q.positive(A-1)) is not False)}
    rows.append(row); print(json.dumps(row),flush=True)
x,y=s.symbols('x y');f=s.Function('f')(x,y)
D=lambda g:A*x*s.diff(g,x)+y*s.diff(g,y)
lap=lambda g:s.diff(g,x,2)+s.diff(g,y,2)
identity=s.simplify(lap(D(f)-f)-(D(lap(f))+lap(f)+(2*A-2)*s.diff(f,x,2)))
result={'utc':datetime.now(timezone.utc).isoformat(),'laplacian_commutator_remainder':str(identity),'polynomial_jets':rows}
Path('research/indicial/verification/symbolic.json').write_text(json.dumps(result,indent=2)+'\n')
