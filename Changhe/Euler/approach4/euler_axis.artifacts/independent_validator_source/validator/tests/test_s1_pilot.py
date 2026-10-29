#!/usr/bin/env python3
from pathlib import Path
import datetime, hashlib, importlib.util, json, time
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
module_path=ROOT/'exploration/s1_pilot.py'
spec=importlib.util.spec_from_file_location('s1_pilot',module_path)
pilot=importlib.util.module_from_spec(spec);spec.loader.exec_module(pilot)

def main():
    started=time.perf_counter();rows=[];rng=np.random.default_rng(296211)
    def check(name,value,tolerance):
        row={'name':name,'error':float(value),'tolerance':tolerance,'passed':bool(value<=tolerance)}
        rows.append(row);print(json.dumps(row),flush=True)
    for c_l,q0 in [(.505,.25),(.60,1.),(.68,2.),(.74,4.)]:
        key=f'c{c_l:g}_q{q0:g}'
        problem=pilot.Problem(c_l,q0,nradial=11,nangle=12,rmax_power=4)
        x,seed=problem.seed();field=problem.field(x)
        check(key+'_S1_strain',abs(field.phi.evaluate(0,0,0,1)-.5),3e-14)
        check(key+'_S1_swirl',abs(field.q.evaluate(0,0)-q0),3e-14)
        delta=c_l+1
        qrr=2*field.q.evaluate(0,0,1,0);qzz=field.q.evaluate(0,0,0,2)
        curvature=4*(c_l-.5)*delta*qrr+(delta**2+q0**2)*qzz
        check(key+'_quadratic_curvature',abs(curvature),4e-12)
        # Direct coefficient extraction checks the intended leading pole sign.
        alpha=field.alpha;k=alpha*(3-alpha)
        A1=sum(t.coefficient for t in field.phi.terms if t.j==1 and abs(2*t.beta-t.j-alpha)<1e-12)
        A3=sum(t.coefficient for t in field.phi.terms if t.j==3 and abs(2*t.beta-t.j-alpha)<1e-12)
        Eplus=(k+4)*A1+(k+12)*A3
        check(key+'_tail_eta_pole',abs(Eplus+.5*(k+4)),1e-12)
        for perturb in [0.,.021]:
            y=x+perturb*rng.standard_normal(len(x));ff=problem.field(y)
            fastq,faste=problem.raw(y);full=ff.reduced(problem.r,problem.z)
            check(key+f'_q_operator_{perturb}',np.max(abs(fastq-full['q'])),3e-12)
            check(key+f'_eta_operator_{perturb}',np.max(abs(faste-full['eta'])),3e-11)
            check(key+f'_constraint_perturbed_{perturb}',max(abs(ff.phi.evaluate(0,0,0,1)-.5),abs(ff.q.evaluate(0,0)-q0)),4e-14)
        y=x+.013*rng.standard_normal(len(x));direction=rng.standard_normal(len(x));direction/=np.linalg.norm(direction)
        analytic=problem.evaluate(y)[1]@direction
        errors=[]
        for step in [3e-4,1e-4,3e-5,1e-5]:
            fd=(problem.evaluate(y+step*direction)[0]-problem.evaluate(y-step*direction)[0])/(2*step)
            errors.append(float(np.linalg.norm(fd-analytic)/max(np.linalg.norm(analytic),1e-30)))
        check(key+'_weighted_JVP',min(errors),2e-7)
        rows[-1]['step_errors']=errors
    result={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'elapsed_seconds':time.perf_counter()-started,'checks':rows,'all_passed':all(r['passed'] for r in rows),
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),module_path,ROOT/'src/independent_fields.py']}}
    (ROOT/'results/s1_pilot_tests.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_passed':result['all_passed'],'checks':len(rows),'elapsed_seconds':result['elapsed_seconds']}))
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
