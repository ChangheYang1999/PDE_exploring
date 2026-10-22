"""Own exact tests for packet127; no lead or NUM code dependency.

All-orders assertions are proved in PROOF.md. Finite cutoff controls here use
an explicit C7 compact polynomial cutoff, so they check derivatives <=3 only
and do not stand in for the smooth Borel construction.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from time import monotonic
import json,hashlib
import sympy as sp
import mpmath as mp
root=Path('research/127_prescribed_disk_full_axis_symbols/verification')
t0=monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING'}
x,y,beta=sp.symbols('x y beta');k=beta-2
# Direct Cartesian coefficient comparisons with independent arbitrary functions.
g={n:sp.Function('g'+str(n))(y) for n in range(1,12,2)}
a={n:sp.Function('a'+str(n))(y) for n in range(2,12,2)}
ps=sum(x**n*v for n,v in g.items());th=sum(x**n*v for n,v in a.items())
w1=beta*x-sp.diff(ps,y);w2=beta*y+sp.diff(ps,x)-sp.Symbol('g10')
om=-sp.diff(ps,x,2)-sp.diff(ps,y,2)
rt=sp.Poly(sp.expand(w1*sp.diff(th,x)+w2*sp.diff(th,y)-k*th),x)
ro=sp.Poly(sp.expand(w1*sp.diff(om,x)+w2*sp.diff(om,y)+om-sp.diff(th,x)),x)
b=beta*y+g[1]-sp.Symbol('g10');A=beta-sp.diff(g[1],y)
w={n:-sp.diff(g[n],y,2)-(n+1)*(n+2)*g[n+2] for n in range(1,10,2)}
for n in range(2,12,2):
    rhs=sum((n-j+1)*sp.diff(g[j],y)*a[n-j+1]-j*g[j]*sp.diff(a[n-j+1],y)for j in range(3,n,2))
    target=b*sp.diff(a[n],y)+(n*A-k)*a[n]-rhs
    assert sp.expand(rt.coeff_monomial(x**n)-target)==0,n
for n in range(1,10,2):
    rhs=(n+1)*a[n+1]+sum((n-j+1)*sp.diff(g[j],y)*w[n-j+1]-j*g[j]*sp.diff(w[n-j+1],y) for j in range(3,n+1,2))
    target=b*sp.diff(w[n],y)+(n*A+1)*w[n]-rhs
    assert sp.expand(ro.coeff_monomial(x**n)-target)==0,n
out['arbitrary_function_Cartesian_recurrences']={'temperature_degrees':[2,4,6,8,10],'vorticity_degrees':[1,3,5,7,9],'confirmed':True}
print('Cartesian recurrences confirmed',flush=True)
# Exact symbol arithmetic over varied beta and every relevant forcing term.
orders=[]
for bs in ['5/2','4','9']:
    bb=Q(bs);alpha=1/bb;D=2-alpha;m=1-2*alpha
    for n in range(2,22,2):
        for j in range(3,n,2):
            r=n-j+1
            assert (D-j-1)+(m-r)==m-n-alpha
            assert (D-j)+(m-r-1)==m-n-alpha
        assert n-(bb-2)/bb==n-m
    for n in range(1,22,2):
        assert m-(n+1)==-n-2*alpha
        for j in range(3,n+1,2):
            r=n-j+1
            assert (D-j-1)+(-r-alpha)==-n-2*alpha
            assert (D-j)+(-r-alpha-1)==-n-2*alpha
        assert (D-n)-2==D-(n+2)==-n-alpha
    orders.append({'beta':bs,'temperature_through':20,'vorticity_through':21,'all_forcing_exponents_confirmed':True})
out['symbol_orders']=orders
# Differentiate the conic cubic correction directly with unspecified f,gamma.
eps=sp.Symbol('eps',positive=True);H=sp.sqrt(1+y*y);z=x/(eps*H)
f=sp.Function('f')(y);Gam=sp.Function('Gamma');v=y/(1+y*y)
actual=sp.diff(f*Gam(z),y,2)
target=sp.diff(f,y,2)*Gam(z)-(2*v*sp.diff(f,y)+sp.diff(v,y)*f)*z*sp.Subs(sp.Derivative(Gam(sp.Symbol('t')),sp.Symbol('t')),sp.Symbol('t'),z)
t=sp.Symbol('t')
target+=v*v*f*(z*sp.Subs(sp.diff(Gam(t),t),t,z)+z*z*sp.Subs(sp.diff(Gam(t),t,2),t,z))
assert sp.simplify(actual-target)==0
out['conic_cutoff_second_y_derivative']=True
# Exact polynomial representation for mixed derivatives and a genuine finite
# weighted supremum bound on all r=y/H and z in [-1,1].
r,z=sp.symbols('r z');mp.mp.dps=45
rows=[];maxerr=0.
for bs in ['5/2','4']:
    alpha=sp.Rational(1)/sp.Rational(bs);D=2-alpha
    for n in [5,7,9]:
        pol0=z**n*(1+r/sp.Integer(10))*(1-z*z)**8
        for i in range(4):
            for j in range(4-i):
                pol=sp.diff(pol0,z,i);order=D-i
                for _ in range(j):
                    pol=sp.expand(order*r*pol+(1-r*r)*sp.diff(pol,r)-r*z*sp.diff(pol,z));order-=1
                pol=sp.Poly(pol,r,z);bound=sum(abs(v)for _,v in pol.terms())
                cert=[{'r_power':ij[0],'z_power':ij[1],'coefficient':str(val)}for ij,val in pol.terms()]
                item={'beta':bs,'n':n,'x_derivatives':i,'y_derivatives':j,'epsilon_power':n-i,'H_power':str(D-i-j),'polynomial':cert,'sup_bound':str(bound)}
                rows.append(item)
                # Verify independent direct Cartesian high-precision differentiation.
                ef=mp.mpf('0.125');yy=mp.mpf('0.75') if j%2 else mp.mpf('-0.75');hh=mp.sqrt(1+yy*yy)
                zz=mp.mpf('0.4');xx=ef*hh*zz;DD=mp.mpf(str(D.p))/int(D.q)
                def F(xx,yy):
                    hh=mp.sqrt(1+yy*yy);zz=xx/(ef*hh)
                    return xx**n*hh**(DD-n)*(1+yy/(10*hh))*(1-zz*zz)**8
                direct=mp.diff(F,(xx,yy),(i,j));rr=yy/hh
                ev=sum(mp.mpf(str(val.p))/int(val.q)*rr**ij[0]*zz**ij[1]for ij,val in pol.terms())
                formula=ef**(n-i)*hh**(DD-i-j)*ev
                er=float(abs(direct-formula)/max(mp.mpf('1e-30'),abs(direct),abs(formula)))
                maxerr=max(maxerr,er);assert er<1e-35,(bs,n,i,j,er)
                assert abs(ev)<=mp.mpf(str(bound.p))/int(bound.q)
path=root/'finite_weighted_conic_certificate.json';path.write_text(json.dumps(rows,indent=2)+'\n')
loaded=json.loads(path.read_text())
for row in loaded:
    bound=sum(abs(Q(t['coefficient'])) for t in row['polynomial'])
    assert bound==Q(row['sup_bound'])
    assert row['epsilon_power']>=row['n']-(row['x_derivatives']+row['y_derivatives'])
out['weighted_conic_controls']={'rows':len(rows),'maximum_45_digit_relative_derivative_error':maxerr,'r_z_box_bound':'sum of absolute rational polynomial coefficients','certificate':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'C7 polynomial cutoff, derivatives through3, not the all-orders smooth construction'}
print('weighted conic controls',len(rows),maxerr,flush=True)
# Extra entered-draft anisotropic example, using closed exact rational formula.
bb=Q(4);q=Q(1);LL=Q(10);c=1+bb/2;eta=9*c*c/(bb*q*q*LL*LL);mu=1+3*bb/2
qp=c*(3*(bb+1)+2*eta)/(bb*(bb+1)*LL*LL)
E=q*(2*bb+4)*mu*(2*bb+1)*qp
assert E==Q(1746927,100000)
out['extra_e432_rational_case']={'beta':'4','q':'1','L':'10','eta':str(eta),'qprime':str(qp),'E_x2y':str(E)}
# The compact-vorticity scope counterexample is a structural exact identity.
F=sp.Function('F')(x,y);uc=-sp.diff(F,y);vc=sp.diff(F,x);oo=-sp.diff(F,x,2)-sp.diff(F,y,2)
assert sp.diff(uc,x)+sp.diff(vc,y)==0
assert -sp.diff(vc,x)+sp.diff(uc,y)==oo
out['compact_stream_perturbation_identity']={'divergence_zero':True,'minus_curl_equal_minus_Laplacian':True,'support_argument':'derivatives preserve compact support; choose smooth odd F with zero gradient at0'}
out.update(status='CONFIRMED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=monotonic()-t0)
out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
