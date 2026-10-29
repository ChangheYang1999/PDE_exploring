#!/usr/bin/env python3
"""Exact identities supporting the prescribed-field positive-strain proof."""
from pathlib import Path
import datetime,time
import sympy as sp
import mpmath as mp
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter();rows=[];exception=None
    def exact(name,value):
        value=sp.factor(value);rows.append({'name':name,'remainder':str(value),'passed':value==0})
        if value!=0:raise AssertionError((name,value))
    try:
        v,t,B,p=sp.symbols('v t B p',positive=True);beta=(1-p)/2;d=p+beta
        F=(1+v+B*t)**beta/(2*(1+v+t)**d)
        exact('radial portrait factor',sp.diff(F,v)/F-beta/(1+v+B*t)+d/(1+v+t))
        exact('strict radial portrait lower bound decomposition',1+v*sp.diff(F,v)/F-(1-d)-beta*v/(1+v+B*t)-d*(1+t)/(1+v+t))
        A=(1+B*t)**beta/(1+t)**d
        exact('axis amplification interval numerator',sp.diff(A,t)/A-(beta*B-d-p*B*t)/((1+B*t)*(1+t)))
        L,s,z=sp.symbols('L s z',positive=True)
        phi=z*(1+s/L**2+B*z*z)**beta/(2*(1+s/L**2+z*z)**d)
        exact('source p_s',sp.diff(phi,s,z).subs({s:0,z:0})+p/(2*L**2))
        exact('source p_z',sp.diff(phi,z,3).subs({s:0,z:0})/6-(beta*B-d)/2)
        w,wp,h,e,delta=sp.symbols('w wp h e delta',nonzero=True)
        hp=(wp-delta)*h/w;ep=(2*h*hp-delta*e)/w;J=w*e-2*h*(h-1)
        exact('axis invariant differential equation',wp*e+w*ep-2*hp*(2*h-1)-hp*J/h)
        exact('axis g equation',hp/w-h*wp/w**2+delta*h/w**2)
        exact('positive exponent dominance',1+beta-(sp.Rational(1,2)+beta/(2*p))-(sp.Rational(1,2)+beta*(1-1/(2*p))))
        K=sp.symbols('K',real=True)
        ps=-p/(2*L**2);pz=(beta*B-d)/2
        exact('cubic closure equivalence',8*L**2*(ps+sp.Rational(3,4)*pz*(1+K*K/delta**2))-3*(1+K*K/delta**2)*(L**2*(beta*B-d)-4*p/(3*(1+K*K/delta**2))))
        mp.mp.dps=55
        for zz in ['.2','1','4']:
            znum=mp.mpf(zz);value=mp.quad(lambda r:r**3/(r*r+znum*znum)**mp.mpf('2.5'),[0,znum,mp.inf]);error=abs(value-2/(3*znum))
            rows.append({'name':'radial strain kernel integral z='+zz,'error':mp.nstr(error,25),'passed':error<mp.mpf('1e-45')})
            if not rows[-1]['passed']:raise AssertionError(rows[-1])
    except Exception as error:
        import traceback;traceback.print_exc();exception=repr(error)
    result={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_passed':exception is None,
            'case_count':len(rows),'rows':rows,'exception':exception,'wall_seconds':time.perf_counter()-start,
            'source_sha256':sha256(Path(__file__)),'proof_sha256':sha256(ROOT.parent/'research/t1_positive_strain/PROOF.md')}
    atomic_json(ROOT/'results/t1_positive_strain_tests.json',result)
    print(result['all_passed'],len(rows),result['wall_seconds'],flush=True)
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
