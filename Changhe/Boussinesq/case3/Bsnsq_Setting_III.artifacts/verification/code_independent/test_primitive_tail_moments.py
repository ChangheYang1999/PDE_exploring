"""Exact and independently differentiated manufactured controls for packet130."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import argparse,json,time,random
import sympy as sp
from primitive_tail_moments import data,repair,source,leading_polynomials,primitive_polynomial,moment,L,D,cheb,serialized
from exact_bivariate import ordinary_stream_jet,diff,lap

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();root=args.root;root.mkdir(exist_ok=True)
tic=time.perf_counter();rng=random.Random(130);rows=[];x,y,z=sp.symbols('x y z',real=True);r=sp.sqrt(x*x+y*y)
sym=lambda p:sum(sp.Rational(a.numerator,a.denominator)*z**j for j,a in enumerate(p))
for beta in [Q(9,4),Q(5,2),Q(3),Q(4),Q(10)]:
    s=1/beta;m=1-2*s;k=2-s;k1=2-2*s
    p=list(map(Q,[1,2,-3,1]));p1=list(map(Q,[-2,1,0,1]));h=source(beta,p,p1)
    P0=x*r**(sp.Rational(1-s)) * sym(p).subs(z,y/r)
    P1=x*r**(sp.Rational(1-2*s)) * sym(p1).subs(z,y/r)
    O0=-sp.diff(P0,x,2)-sp.diff(P0,y,2);O1=-sp.diff(P1,x,2)-sp.diff(P1,y,2)
    F=-O1-sp.diff(P0,y)*sp.diff(O0,x)+sp.diff(P0,x)*sp.diff(O0,y)
    for xx,yy in [(Q(3,5),Q(4,5)),(Q(5,13),-Q(12,13)),(-Q(3,5),Q(4,5))]:
        actual=sp.simplify(F.subs({x:sp.Rational(xx),y:sp.Rational(yy)}))
        expected=sp.Rational(xx)*sym(h).subs(z,sp.Rational(yy))
        assert sp.simplify(actual-expected)==0,(beta,xx,yy)
    # The coefficient recurrence is checked by independent direct Cartesian differentiation.
    # Start with a temperature polynomial, recover its source, then its primitive.
    qp=list(map(Q,[2,-1,3,2]));temp=x*x*r**sp.Rational(m-2)*sym(qp).subs(z,y/r)
    hh=sp.expand((m+(2-m)*z*z)*sym(qp)-z*(1-z*z)*sp.diff(sym(qp),z))
    coeff=list(reversed(sp.Poly(hh,z).all_coeffs()));coeff=list(map(Q,coeff))
    assert moment(m,coeff,1)==moment(m,coeff,-1)==0
    assert primitive_polynomial(m,coeff)==qp
    for xx,yy in [(Q(3,5),Q(4,5)),(Q(5,13),-Q(12,13))]:
        assert sp.simplify(sp.diff(temp,x).subs({x:sp.Rational(xx),y:sp.Rational(yy)})-sp.Rational(xx)*hh.subs(z,sp.Rational(yy)))==0
    # Exact arbitrary coefficient repair, preserving leading stream polynomial and center jets.
    labels=[(i,j,d)for d in [0,1]for i in range(4)for j in range(4)]
    C=[Q(rng.randint(-9,9),11)for _ in labels];new,details=repair(beta,labels,C)
    psi0,_=ordinary_stream_jet(beta,labels,C,[Q(0)]*len(C),6)
    psi1,_=ordinary_stream_jet(beta,labels,new,[Q(0)]*len(C),6)
    for key in [(1,0),(1,1),(3,0),(1,2)]:assert psi0.get(key,Q(0))==psi1.get(key,Q(0)),(beta,key)
    assert data(beta,labels,new)['C_plus']==data(beta,labels,new)['C_minus']==0
    twice,_=repair(beta,labels,new);assert twice==new
    tampered=new.copy();tampered[labels.index((3,0,0))]+=Q(1,13)
    td=data(beta,labels,tampered);assert td['C_plus']!=0 or td['C_minus']!=0
    # Direct symbolic Taylor checks of the two explicit repair functions.
    t=sp.symbols('t');rr=sp.sqrt(1+(t*x)**2+(t*y)**2)
    H0=t*x*rr**sp.Rational(1-2*s)*(1-rr**sp.Rational(-s))**2
    H1=t*t*x*y*rr**sp.Rational(-2*s)*(1-rr**sp.Rational(-s))
    assert sp.series(H0,t,0,5).removeO()==0
    assert sp.series(H1,t,0,4).removeO()==0
    rows.append({'beta':str(beta),'cartesian_source_points':3,'cartesian_primitive_points':2,'exact_repair':serialized(details),'center_jet_equal':True,'idempotence':True,'tamper_detected':True})
# Independent exact algebra of the integral primitive for each monomial.
u=sp.symbols('u',positive=True);mm=sp.symbols('m',real=True)
for j in range(8):
    antiderivative=(1+u*u)**((mm-j)/2)/(mm-j)
    assert sp.simplify(sp.diff(antiderivative,u)-u*(1+u*u)**((mm-2-j)/2))==0
result={'status':'ALL_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-tic,'cases':rows,'monomial_antiderivatives_checked':8,'scope':'Exact rational and symbolic controls, not existence evidence.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['elapsed_seconds'],len(rows),flush=True)
