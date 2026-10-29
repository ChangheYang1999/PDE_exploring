#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'exploration'))
from s1_constrained import ConstrainedProblem

def main():
    started=time.perf_counter();rows=[];rng=np.random.default_rng(281958)
    def check(name,error,tolerance):
        row=dict(name=name,error=float(error),tolerance=tolerance,passed=bool(error<=tolerance));rows.append(row)
        print(json.dumps(row),flush=True)
    for c,q0 in [(.505,.25),(.60,1.),(.74,4.)]:
        for pole in [False,True]:
            key=f'{c:g}_{q0:g}_{pole}'
            p=ConstrainedProblem(c,q0,pole=pole,nradial=9,nangle=10,rmax_power=3)
            x,_=p.seed();x+=.12*rng.normal(size=len(x));f=p.field(x)
            check(key+'_S1',max(abs(f.phi.evaluate(0,0,0,1)-.5),abs(f.q.evaluate(0,0)-q0)),2e-13)
            b=float(f.phi.evaluate(0,0,1,1));h=float(f.phi.evaluate(0,0,0,3))/6
            fs=float(f.q.evaluate(0,0,1,0));gz=float(f.q.evaluate(0,0,0,2))/2
            e=-8*b-6*h
            check(key+'_q_r2',abs((2*c-1)*fs-2*q0*b),4e-12)
            check(key+'_q_z2',abs(2*(1+c)*gz-6*q0*h),4e-12)
            check(key+'_eta_z',abs(2*(1+c)*e-4*q0*gz),4e-12)
            if pole:
                alpha=(1-c)/c
                E=sum(t.coefficient*(alpha*(3-alpha)+4*t.j) for t in f.phi.terms if abs(2*t.beta-t.j-alpha)<1e-12)
                B=sum(t.coefficient for t in f.q.terms if abs(2*t.beta-t.j-alpha-1)<1e-12)
                check(key+'_pole',abs(c*E+2*q0*B),2e-12)
            check(key+'_projection',np.max(abs(p.project(p.lift(x))-x)),2e-13)
            direction=rng.normal(size=len(x));direction/=np.linalg.norm(direction)
            analytic=p.evaluate(x)[1]@direction;errors=[]
            for step in [1e-3,3e-4,1e-4]:
                fd=(p.evaluate(x+step*direction)[0]-p.evaluate(x-step*direction)[0])/(2*step)
                errors.append(float(np.linalg.norm(fd-analytic)/np.linalg.norm(analytic)))
            check(key+'_JVP',min(errors),3e-8)
            rows[-1]['step_errors']=errors
    paths=[Path(__file__),ROOT/'exploration/s1_constrained.py',ROOT/'exploration/s1_pilot.py',ROOT/'src/independent_fields.py']
    result=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-started,
                checks=rows,all_passed=all(x['passed'] for x in rows),
                source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (ROOT/'results/s1_constrained_tests.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_passed':result['all_passed'],'checks':len(rows),'elapsed_seconds':result['elapsed_seconds']}))
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
