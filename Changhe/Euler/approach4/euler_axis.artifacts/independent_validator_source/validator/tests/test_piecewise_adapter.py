#!/usr/bin/env python3
"""Independent symbolic, Cartesian and exported-data checks of the adapter."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
import sympy as sp
from piecewise_adapter import PiecewiseField,spherical_jets
ROOT=Path(__file__).resolve().parents[1]
EXPORT=ROOT/'external_exports/S1_pilot_L0_20261028T2003Z'
ROWS=[]
def check(name,error,tolerance,detail=None):
    row=dict(name=name,error=float(error),tolerance=float(tolerance),passed=bool(np.isfinite(error) and error<=tolerance))
    if detail is not None:row['detail']=detail
    ROWS.append(row);print(json.dumps(row),flush=True)
def main():
    start=time.monotonic();exception=None
    try:
        field=PiecewiseField.load(EXPORT/'coeffs.npz')
        with np.load(EXPORT/'samples.npz',allow_pickle=False) as data:
            d=field.cylindrical(data['r'],data['z'])
            for key,value in [('phi',d['phi'][0,0]),('q',d['q'][0,0]),('Ur',d['U'][:,0]),('Utheta',d['U'][:,1]),('Uz',d['U'][:,2]),('eta',d['eta'])]:
                check('exported_'+key,np.max(abs(value-data[key]))/(1+np.max(abs(data[key]))),1e-12)
        coeff={k:np.zeros_like(v) for k,v in field.coefficients.items()}
        choices={'phi':[(3,2),(2,3),(2,field.alpha)],'q':[(2,1),(3,2),(3,field.alpha+1)]}
        for key in choices:
            for i,target in enumerate(choices[key]):
                labels=field.elements[i].get('labels_'+key,field.elements[i]['labels'])
                hit=[j for j,(n,k) in enumerate(labels) if n==target[0] and abs(k-target[1])<1e-12]
                assert len(hit)==1;coeff[f'{key}_el{i}'][hit[0]]=1.
        fixture=PiecewiseField(field.metadata,coeff)
        s,z=sp.symbols('s z',real=True);t=s+z*z;Rb=sp.Integer(2);Rm=sp.Integer(10)
        x=2*t/Rb**2-1;u=z/sp.sqrt(t);xs=sp.log(t/Rb**2)/sp.log(Rm/Rb)-1
        P2=lambda u:(3*u*u-1)/2;P3=lambda u:(5*u**3-3*u)/2
        formulas={
          'phi':[(5*z**3-3*z*t)/(2*Rb**3)*(2*x*x-1),P2(u)*(4*xs**3-3*xs),P2(u)*(t/Rm**2)**(-sp.Rational(1,3))],
          'q':[(3*z*z-t)/(2*Rb**2)*x,P3(u)*(2*xs*xs-1),P3(u)*(t/Rm**2)**(-sp.Rational(5,6))]}
        points=[(np.array([0.,0.,.01,.6,1.]),np.array([0.,.7,-.6,.2,-1.])),
                (np.array([0.,.1,8.,25.]),np.array([3.,-3.,1.,2.])),
                (np.array([0.,.1,80.,300.]),np.array([12.,-15.,9.,-20.]))]
        for i,(ss,zz) in enumerate(points):
            got=fixture.jets(ss,zz,3,element=i)
            for key in formulas:
                for ab,value in got[key].items():
                    ref=np.asarray(sp.lambdify((s,z),sp.diff(formulas[key][i],s,ab[0],z,ab[1]),'numpy')(ss,zz))
                    check(f'symbolic_{key}_el{i}_d{ab}',np.max(abs(value-ref))/(1+np.max(abs(ref))),2e-11)
        R,m=sp.symbols('R m',real=True,positive=True)
        for i,(radii,angles) in enumerate([(np.array([.2,.7,1.8]),np.array([-1.,.23,1.])),(np.array([2.2,4.4,9.]),np.array([-1.,-.7,1.])),(np.array([11.,20.,50.]),np.array([-1.,.4,1.]))]):
            got=spherical_jets(fixture,radii,angles,3,element=i)
            for key in formulas:
                f=formulas[key][i].subs({s:R**2*(1-m*m),z:R*m},simultaneous=True)
                f=sp.simplify(f)
                for ab,value in got[key].items():
                    ref=np.asarray(sp.lambdify((R,m),sp.diff(f,R,ab[0],m,ab[1]),'numpy')(radii,angles))
                    check(f'spherical_{key}_el{i}_d{ab}',np.max(abs(value-ref))/(1+np.max(abs(ref))),4e-11)
        for point in [np.array([0.,0.,0.]),np.array([.31,-.23,.8]),np.array([.8,1.2,4.]),np.array([10.,7.,12.])]:
            U,J=field.cartesian(point,True);scale=max(1.,np.linalg.norm(point));h=scale*1e-5
            diff=[]
            for j in range(3):
                step=np.eye(3)[j]*h
                diff.append((-field.cartesian(point+2*step)+8*field.cartesian(point+step)-8*field.cartesian(point-step)+field.cartesian(point-2*step))/(12*h))
            check('Cartesian_J_'+str(point.tolist()),np.max(abs(J-np.stack(diff,axis=-1)))/(1+np.max(abs(J))),3e-9)
            d=field.cylindrical(np.hypot(*point[:2]),point[2]);angle=np.arctan2(point[1],point[0]);c,sn=np.cos(angle),np.sin(angle)
            Uc=d['U'];transformed=np.array([c*Uc[0]-sn*Uc[1],sn*Uc[0]+c*Uc[1],Uc[2]])
            check('Cartesian_cylindrical_'+str(point.tolist()),np.max(abs(U-transformed)),3e-13)
            check('Cartesian_divergence_'+str(point.tolist()),abs(np.trace(J)),3e-13)
        points=np.array([[.2,-.3,.7],[0.,0.,0.],[1.,2.,4.],[13.,7.,-11.]])
        U,J=field.cartesian(points,True)
        for L in [.07,2.3]:
            scaled=field.dilate(L);UL,JL=scaled.cartesian(points*L,True)
            check(f'dilation_U_{L}',np.max(abs(UL-L*U))/(1+np.max(abs(L*U))),2e-12)
            check(f'dilation_J_{L}',np.max(abs(JL-J))/(1+np.max(abs(J))),2e-12)
        gauged,gauge=field.reporting_gauge()
        check('leading_norm',abs(gauge['input_leading_squared_norm']/2668.2460780554684-1),1e-12)
        check('reporting_gauge',abs(gauged.reporting_gauge()[1]['input_leading_squared_norm']-1),1e-12)
        # Cache requests for lower derivatives must retain shape and values.
        ss=np.array([[0.,.4],[3.,100.]]);zz=np.array([[0.,1.],[4.,20.]])
        full=field.jets(ss,zz,3);small=field.jets(ss,zz,1)
        check('cache_shape_and_values',max(np.max(abs(small[k][ab]-full[k][ab])) for k in small for ab in small[k]),0.)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    files=[Path(__file__),ROOT/'src/piecewise_adapter.py',ROOT/'src/independent_fields.py',EXPORT/'coeffs.npz',EXPORT/'BASIS.md']
    out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,checks=ROWS,
             exception=exception,all_passed=exception is None and all(x['passed'] for x in ROWS),
             source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
             scope='Adapter implementation checks. These do not establish an Euler solution or interface regularity.')
    (ROOT/'results/piecewise_adapter_tests.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['all_passed','elapsed_seconds','exception']}))
    raise SystemExit(0 if out['all_passed'] else 1)
if __name__=='__main__':main()
