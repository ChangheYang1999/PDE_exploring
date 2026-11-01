"""Exact complex bidisk response and compatible-family certificates."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import json
import time
import sys
sys.dont_write_bytecode = True
import sympy as sp
from general_component_radius import certificate, stringify

BASE = Path('research/137_larger_compatible_shape_disks')
START = time.monotonic()
b, tau, x, k, w = sp.symbols('b tau x k w')


def terms(expr):
    return {(i,j): F(str(c)) for (i,j),c in sp.Poly(expr,x,tau,domain=sp.QQ).terms()}


def bounds(coeffs,h,t0,excluded=(0,0)):
    return sum((abs(c)*h**i*t0**j for (i,j),c in coeffs.items() if (i,j)!=excluded), F(0))


def save(name,data):
    (BASE/'verification'/name).write_text(json.dumps(stringify(data),indent=2)+'\n')
    print(json.dumps({'stage':name,'actual_elapsed_s':time.monotonic()-START}),flush=True)


def main():
    obstruction=sp.sympify(json.loads(Path('research/125_explicit_compatible_shape/verification/obstruction_polynomial.json').read_text())['expression'])
    source=Path('research/136_three_mode_responses/verification')
    small={r['k']:sp.sympify(r['sigma']) for r in json.loads((source/'small_responses.json').read_text())['rows']}
    symbolic=json.loads((source/'symbolic_response.json').read_text())
    numerator=sp.sympify(symbolic['numerator'])
    denominator=sp.sympify(symbolic['denominator'])
    shifted_den=sp.Poly(denominator.subs(k,10+w),w,domain=sp.QQ)
    den={degree[0]:F(str(value)) for degree,value in shifted_den.terms()}
    assert all(value>0 for value in den.values()) and den[0]>0
    roots=json.loads(Path('research/120_tuned_explicit_radius/verification/response_bound.json').read_text())['rows']
    rows=[]
    for root,lower in zip(roots,[F(1,100000),F(1,2000)]):
        lo,hi=map(F,root['interval']);mid=(lo+hi)/2;width=(hi-lo)/2
        center=sp.Rational(mid.numerator,mid.denominator)
        circle=terms(obstruction.subs(b,center+x))
        derivative=circle[(1,0)]
        finite={kk:terms(small[kk].subs(b,center+x)) for kk in range(2,10)}
        full=sp.Poly(numerator.subs({k:10+w,b:center+x}),w,x,tau,domain=sp.QQ)
        tail={}
        for (degree,i,j),value in full.terms():
            tail.setdefault(degree,{})[(i,j)]=F(str(value))
        assert set(den)<=set(tail)
        trials=[]
        for power in range(0,101):
            t0=F(1,2**power);h=2*t0
            circle_bound=bounds(circle,h,t0,excluded=(1,0))
            circle_ratio=circle_bound/(abs(derivative)*h)
            finite_margins={kk:abs(co.get((0,0),F(0)))-bounds(co,h,t0)-lower for kk,co in finite.items()}
            tail_margins={degree:-co.get((0,0),F(0))-bounds(co,h,t0)-lower*den.get(degree,F(0))
                          for degree,co in tail.items()}
            finite_ok=min(finite_margins.values())>0
            tail_ok=min(tail_margins.values())>0
            success=width<h and circle_ratio<1 and finite_ok and tail_ok
            trials.append({'power':power,'circle_ratio':circle_ratio,'finite_pass':finite_ok,
                           'tail_pass':tail_ok,'passes':success})
            if success:
                break
        assert success
        norm=1+abs(mid)+h+t0
        a=F(-(-norm.numerator*1000//norm.denominator),1000)
        assert a>=norm
        radius=certificate('larger_shape_root_'+str(root['root_index']),3,a,F(14),lower)
        row={'root_index':root['root_index'],'root_interval':root['interval'],'center':mid,
             't0':t0,'h':h,'dyadic_parameter_power':power,'response_lower':lower,
             'circle_ratio':circle_ratio,'finite_response_signs':{str(kk):1 if co.get((0,0),F(0))>0 else -1 for kk,co in finite.items()},'finite_response_margins':{str(kk):value for kk,value in finite_margins.items()},
             'tail_coefficient_margins':{str(degree):value for degree,value in tail_margins.items()},
             'norm_bound_before_rounding':norm,'a':a,'radius_certificate':radius,'trials':trials}
        rows.append(row)
        save('checks.partial.json',{'rows':rows})
        print(json.dumps({'root_index':root['root_index'],'parameter_power':power,
                          'circle_ratio_approx':float(circle_ratio),'radius_power':radius['exterior_radius_power'],
                          'actual_elapsed_s':time.monotonic()-START}),flush=True)
    save('checks.json',{'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
                       'all_checks_pass':True,'denominator_shift_coefficients':{str(degree):value for degree,value in den.items()},
                       'rows':rows,'actual_elapsed_s':time.monotonic()-START})
    for name in ('larger_shape_disks.py','general_component_radius.py'):
        (BASE/'sources'/name).write_bytes(Path('code',name).read_bytes())
    manifest={}
    for p in BASE.rglob('*'):
        if p.is_file() and p.name!='MANIFEST.json':
            data=p.read_bytes();manifest[str(p.relative_to(BASE))]={'bytes':len(data),'sha256':sha256(data).hexdigest()}
    (BASE/'verification/MANIFEST.json').write_text(json.dumps({'files':manifest},indent=2)+'\n')


if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        import traceback
        save('FAILURE.json',{'error_type':type(exc).__name__,'error':str(exc),
                             'frames':[{'file':Path(f.filename).name,'line':f.lineno} for f in traceback.extract_tb(exc.__traceback__)]})
        raise SystemExit(1)
