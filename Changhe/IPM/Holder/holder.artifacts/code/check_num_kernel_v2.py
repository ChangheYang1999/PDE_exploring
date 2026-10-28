"""Independent algebra and geometric checks of the numerical lane kernel revision."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,random
import sympy as sp
from flint import arb,ctx
ctx.prec=160
ROOT=Path(__file__).resolve().parents[1]
x,y=sp.symbols('x y',real=True)
A=x*x+y*y;B=(x-1)**2+y*y
N=A*(3*x*x-y*y)-2*x*A-4*x**3+4*x*x-x
assert sp.expand((x-1)*A*A-x*B*B-N)==0
rng=random.Random(2042801);checks=0
for _ in range(2000):
    xx=arb(rng.randint(-10000,10000))/137;yy=arb(rng.randint(1,10000))/139
    aa=xx*xx+yy*yy;bb=(xx-1)**2+yy*yy
    direct=yy*((xx-1)/bb**2-xx/aa**2)/arb.pi()
    nn=aa*(3*xx*xx-yy*yy)-2*xx*aa-4*xx**3+4*xx*xx-xx
    combined=yy*nn/(arb.pi()*bb**2*aa**2)
    # Independent midpoint coordinates, complex dipole, imaginary part.
    from flint import acb
    w=acb(xx-arb(1)/2,yy)
    alternate=-(w/(arb.pi()*(w*w-arb(1)/4)**2)).imag
    assert direct.overlaps(combined) and alternate.overlaps(combined)
    checks+=1
# Hessian eigenvalues of d^alpha on a vertex regime follow directly by differentiation.
al=sp.symbols('alpha',positive=True);r=sp.symbols('r',positive=True)
H=sp.hessian((x*x+y*y)**(al/2),(x,y)).subs({x:r,y:0})
assert sp.simplify(H[0,0]-al*(al-1)*r**(al-2))==0
assert sp.simplify(H[1,1]-al*r**(al-2))==0
paths=['05_team_audit/numerical_certificate_v2/source/certify_lb.py','05_team_audit/numerical_certificate_v2/source/zcurve.py','code/check_num_kernel_v2.py']
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),kernel_polynomial_identity='exactly zero',kernel_arb_comparisons=checks,hessian_eigenvalues=['alpha*(alpha-1)*r^(alpha-2)','alpha*r^(alpha-2)'],status='Exact symbolic identities and independent Arb comparisons passed',source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
(ROOT/'data/num_kernel_v2_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
