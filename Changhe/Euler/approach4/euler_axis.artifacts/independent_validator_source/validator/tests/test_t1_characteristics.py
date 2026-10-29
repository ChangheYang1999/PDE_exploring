#!/usr/bin/env python3
"""Analytic seed derivatives, exact local identities and transport gradients."""
import datetime,json,time
from pathlib import Path
import numpy as np
import sympy as sp
from t1_characteristics import seed_jets,transport_points
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]
checks=[]

def check(name,error,tolerance):
    row={'name':name,'error':float(error),'tolerance':tolerance,'passed':bool(np.isfinite(error) and error<=tolerance)};checks.append(row)
    if not row['passed']:raise AssertionError(row)

def exact(name,expr):check(name,float(sp.factor(expr)!=0),0)

def main():
    start=time.perf_counter();exception=None
    try:
        c,ps,pz,K=sp.symbols('c ps pz K',nonzero=True);eps=c-sp.Rational(1,2);delta=1+c
        A=ps/eps;B=3*pz/delta;E=6*pz/delta**2
        exact('source radial swirl coefficient',2*eps*A-2*ps)
        exact('source axial swirl coefficient',2*delta*B-6*pz)
        exact('source eta coefficient',2*delta*E-4*B)
        exact('elliptic source closure',(-8*ps-6*pz-K*K*E).subs(ps,-3*pz*(1+K*K/delta**2)/4))
        v,n,u=sp.symbols('v n u',positive=True);cv=(2*n+3)/(4*n);hu=2*n*(v**3-1)/((2*n+3)-2*n*v**3)
        exact('radial implicit derivative',hu-(v**3-1)/(2*cv-v**3))
        exact('radial swirl constant term',(1-v**3)+(2*cv-v**3)*hu)
        h,hp=sp.symbols('h hp',positive=True)
        exact('radial swirl angular term',6*(h**sp.Rational(3,2)/2)*hp-4*(sp.Rational(3,4)*sp.sqrt(h)*hp)*h)
        r=np.array([.001,.13,.7,1.8,4.]);z=np.array([.002,.8,.4,2.1,3.]);step=2e-5
        for cl in [.55,.6,.74]:
            d=seed_jets(r,z,cl)
            for axis in ['r','z']:
                rp=r+step if axis=='r' else r;rm=r-step if axis=='r' else r
                zp=z+step if axis=='z' else z;zm=z-step if axis=='z' else z
                plus=seed_jets(rp,zp,cl);minus=seed_jets(rm,zm,cl)
                derivative=(plus['a']-minus['a'])/(2*step)
                check(f'forcing derivative {cl} {axis}',np.max(np.abs(derivative-d['a_'+axis])),8e-9)
                wrp=rp*plus['log_r_speed'];wrm=rm*minus['log_r_speed']
                wzp=zp*plus['log_z_speed'];wzm=zm*minus['log_z_speed']
                check(f'W_r derivative {cl} {axis}',np.max(np.abs((wrp-wrm)/(2*step)-d['Dr'+axis])),8e-9)
                check(f'W_z derivative {cl} {axis}',np.max(np.abs((wzp-wzm)/(2*step)-d['Dz'+axis])),8e-9)
            radial=(r*r*d['log_r_speed']+z*z*d['log_z_speed'])/(r*r+z*z)
            check(f'proved radial lower bound {cl}',np.max(np.maximum(cl-.5-radial,0)),0)
        r=np.array([.2,.8,2.]);z=np.array([.3,.6,1.]);step=1e-4
        rr=np.concatenate([r,r+step,r-step,r,r]);zz=np.concatenate([z,z,z,z+step,z-step])
        value=transport_points(rr,zz,.74,rtol=3e-12,atol=2e-14)
        base=value['h'][:3];hr=(value['h'][3:6]-value['h'][6:9])/(2*step)
        hz=(value['h'][9:12]-value['h'][12:15])/(2*step)
        check('characteristic h_r versus point differences',np.max(np.abs(hr-value['h_r'][:3])),2e-7)
        check('characteristic h_z versus point differences',np.max(np.abs(hz-value['h_z'][:3])),2e-7)
        check('endpoint return accuracy',value['endpoint_log_error'],2e-9)
        d=seed_jets(r,z,.74)
        residual=r*d['log_r_speed']*value['h_r'][:3]+z*d['log_z_speed']*value['h_z'][:3]-d['a']*base
        check('independent characteristic swirl equation',np.max(np.abs(residual)),2e-9)
        fine=transport_points(r,z,.74,source_radius=1e-6,rtol=3e-12,atol=2e-14)
        for key in ['h','h_r','h_z','e']:
            check('source radius refinement '+key,np.max(np.abs(fine[key]-value[key][:3])),2e-9)
    except Exception as error:
        import traceback;traceback.print_exc();exception=repr(error)
    result={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_passed':exception is None,'case_count':len(checks),
            'checks':checks,'exception':exception,'wall_seconds':time.perf_counter()-start,
            'source_sha256':{name:sha256(ROOT/name) for name in ['tests/test_t1_characteristics.py','src/t1_characteristics.py']},
            'proof_sha256':sha256(ROOT.parent/'research/t1_prescribed/PROOF.md')}
    atomic_json(ROOT/'results/t1_characteristic_tests.json',result)
    print(json.dumps({k:result[k] for k in ['all_passed','case_count','wall_seconds','exception']}),flush=True)
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
