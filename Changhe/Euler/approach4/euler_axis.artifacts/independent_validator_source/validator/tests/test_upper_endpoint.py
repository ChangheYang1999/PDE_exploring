#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import sympy as S
import numpy as np
from independent_farfield import angular_data
from independent_second_order import second_forcing
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.time();mu=S.symbols('mu');s2=1-mu**2;alpha=S.Rational(1,3);rows=[]
    def check(name,condition,detail=None):
        row={'name':name,'passed':bool(condition)}
        if detail is not None:row['detail']=detail
        rows.append(row)
    fr=2*mu;C=alpha-2
    nr=S.expand(-alpha*fr**2-s2*C*S.diff(fr,mu)-s2*C*C)
    V=S.expand((1-alpha)*fr*C+mu*C*C)
    Q=(mu**2-1)/6;gr=S.expand(nr-2*alpha*Q);D=S.expand(V-S.diff(Q,mu))
    check('first_pressure_equation',S.expand(-(2*alpha*(2*alpha-1)*Q+S.diff(s2*S.diff(Q,mu),mu))-(1-2*alpha)*nr+S.diff(s2*V,mu))==0)
    H=S.expand(-(3*alpha+1)*fr*gr-s2*(C*S.diff(gr,mu)+D*S.diff(fr,mu))-2*s2*C*D)
    polar=S.expand(-(2*alpha+1)*fr*D+C*(mu*D-s2*S.diff(D,mu))+C*gr-alpha*gr*C+D*(mu*C)+D*fr)
    source=S.expand(-3*alpha*H-S.diff(s2*polar,mu))
    check('local_degree_one_forcing_vanishes',S.integrate(mu*source,(mu,-1,1))==0)
    fz=mu*fr-s2*C;gz=mu*gr-s2*D
    moment=S.simplify(S.Rational(3,2)*S.integrate(mu*H-fz*gr-gz*fr,(mu,-1,1)))
    check('dipole_boundary_moment',moment==S.Rational(136,135),str(moment))
    check('selected_pressure_dipole',moment/3==S.Rational(136,405),str(moment/3))
    computed=second_forcing(float(alpha),[1.],[0.]);data=computed['first'];x=np.linspace(-1,1,19)
    error=max(np.max(np.abs(data['Q'](x)-S.lambdify(mu,Q,'numpy')(x))),np.max(np.abs(computed['N'][0](x)-S.lambdify(mu,H,'numpy')(x))))
    check('floating_angular_route',error<2e-13,float(error))
    paths=[Path(__file__),ROOT/'src/independent_farfield.py',ROOT/'src/independent_second_order.py']
    result={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':rows,'all_passed':all(r['passed'] for r in rows),'scope':'Formal coefficients at c_l=3/4, outside the campaign target. No exact profile constructed.',
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (ROOT/'results/upper_endpoint_tests.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
