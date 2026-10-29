#!/usr/bin/env python3
"""Exact rational audit of the independently derived formal S1 recurrence."""
from pathlib import Path
import datetime,hashlib,json,time
import sympy as S
ROOT=Path(__file__).resolve().parents[1];s,x=S.symbols('s x');checks=[]
def check(name,passed,detail=None):
    row={'name':name,'passed':bool(passed)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)
def coefficients(p):return S.Poly(S.expand(p),s,x).as_dict()
def weight(p,n):return sum(v*s**j*x**k for (j,k),v in coefficients(p).items() if 2*j+k==n)
def lap(p):return 8*S.diff(p,s)+4*s*S.diff(p,s,2)+S.diff(p,x,2)
def residuals(p,q,c):
    ws=2*s*(c-S.diff(p,x));wz=c*x+2*p+2*s*S.diff(p,s)
    eta=-lap(p)
    return (S.expand(q+ws*S.diff(q,s)+wz*S.diff(q,x)-2*S.diff(p,x)*q),
            S.expand((1+c)*eta+ws*S.diff(eta,s)+wz*S.diff(eta,x)-2*q*S.diff(q,x)))
def build(c,K,axis,degree):
    p=x/2;q=K;a=2*c-1;delta=c+1
    for d in range(2,degree+1):
        rq,re=residuals(p,q,c);F=coefficients(weight(rq,d-1));H=coefficients(weight(re,d-2))
        new={(0,d):axis.get(d,S.Integer(0))}
        for j in range(d//2):
            k=d-2-2*j;D=a*j+delta*(k+1);A=4*(j+1)*(j+2);B=(k+1)*(k+2)
            new[j+1,k]=S.factor(-S.Rational(B,A)*(1+4*K*K/(D*D))*new[j,k+2]
                +(2*K*(k+1)*F.get((j,k+1),0)/D+H.get((j,k),0))/(D*A))
        P=sum(v*s**j*x**k for (j,k),v in new.items());Q=S.Integer(0)
        for j in range((d-1)//2+1):
            k=d-1-2*j;Q+=(2*K*(k+1)*new.get((j,k+1),0)-F.get((j,k),0))/(a*j+delta*k)*s**j*x**k
        p+=P;q+=Q
        rq,re=residuals(p,q,c)
        check(f'full_q_residual_c{c}_weight{d-1}',all(v==0 or 2*j+k>d-1 for (j,k),v in coefficients(rq).items()))
        check(f'full_eta_residual_c{c}_weight{d-2}',all(v==0 or 2*j+k>d-2 for (j,k),v in coefficients(re).items()))
    return S.expand(p),S.expand(q)
def main():
    start=time.time();exception=None
    try:
        for c in [S.Rational(101,200),S.Rational(3,5),S.Rational(37,50)]:
            axis={2:S.Rational(1,30),3:-S.Rational(1,70),4:S.Rational(1,120),5:S.Rational(1,250),6:-S.Rational(1,1000)}
            build(c,S.Rational(7,10),axis,6)
        p,q=build(S.Rational(3,5),S.Integer(1),{5:S.Integer(1)},5)
        expected_q=1+S.Rational(25,16)*x**4-S.Rational(21075,4352)*s*x*x+S.Rational(2732725,591872)*s*s
        expected_p=x/2+x**5-S.Rational(1405,512)*s*x**3+S.Rational(546545,591872)*s*s*x
        check('lead_quartic_q_sample',S.expand(q-expected_q)==0)
        check('lead_quintic_phi_sample',S.expand(p-expected_p)==0)
        A=S.Rational(25,16);B=-S.Rational(21075,4352);C=S.Rational(2732725,591872);disc=B*B-4*A*C
        check('definite_quartic_zero_Hessian_example',A>0 and C>0 and disc<0,{'discriminant':str(disc)})
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'exception':exception,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'all_passed':exception is None and all(v['passed'] for v in checks)}
    (ROOT/'results/s1_formal_jet_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
