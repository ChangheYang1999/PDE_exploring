#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.time();s,z,c,q0,b1,b2,d1,d2=sp.symbols('s z c q0 b1 b2 d1 d2')
    p=z/2+d1*s*z+d2*z**3;q=q0+b1*s+b2*z*z
    e=-8*sp.diff(p,s)-4*s*sp.diff(p,s,2)-sp.diff(p,z,2)
    ws=2*s*(c-sp.diff(p,z));wz=c*z+2*p+2*s*sp.diff(p,s)
    rq=q+ws*sp.diff(q,s)+wz*sp.diff(q,z)-2*sp.diff(p,z)*q
    re=(1+c)*e+ws*sp.diff(e,s)+wz*sp.diff(e,z)-2*q*sp.diff(q,z)
    qs=sp.expand(rq).coeff(s,1).coeff(z,0);qzz=sp.expand(rq).coeff(s,0).coeff(z,2)
    ez=sp.expand(re).coeff(s,0).coeff(z,1)
    expected=4*(c-sp.Rational(1,2))*(c+1)*b1+((c+1)**2+q0*q0)*b2
    substituted=ez.subs({d1:(c-sp.Rational(1,2))*b1/q0,d2:(c+1)*b2/(3*q0)})
    defects=[sp.simplify(qs+2*q0*d1-2*(c-sp.Rational(1,2))*b1),
             sp.simplify(qzz+6*q0*d2-2*(c+1)*b2),sp.simplify(-q0*substituted/4-expected)]
    checks=[{'name':name,'symbolic_defect':str(d),'passed':d==0} for name,d in zip(['q_s_coefficient','q_z2_coefficient','curvature_relation'],defects)]
    result={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'all_passed':all(r['passed'] for r in checks),'coefficients':{'q_s':str(qs),'q_z2':str(qzz),'eta_z':str(ez)},
            'source_sha256':{'tests/test_source_curvature.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    (ROOT/'results/source_curvature_tests.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
