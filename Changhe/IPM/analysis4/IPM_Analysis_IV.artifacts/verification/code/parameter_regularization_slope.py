"""Check the unique first profile derivative and finite parameter approaches."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb,ctx
import sympy as sp
from pure_cartesian_ball import Tuning,ball,refine_root,sine
from fixed_shape_parameter_limit import DField,adv,poisson

def order6_bderivative(b):
    delta=mpq(2,3);v=sine(1-delta,1,arb(1))+sine(1-delta,3,b);d=sine(1-delta,3,arb(1))
    assert v.lo==d.lo
    f={1:DField(1-delta,0,v.lo,v.poly,d.poly)};g={1:poisson(f[1])}
    for n in range(2,7):
        total=DField(1-n*delta,0)
        for i in range(1,n):total=total+adv(g[i],f[n-i])
        f[n]=total.scale(ball((1-delta)/(delta*(n-1))))
        if n<6:g[n]=poisson(f[n])
    return f[6].sine(1,True)

def prefix(delta,b):
    solver=Tuning(int(delta.numerator),int(2*delta.denominator));assert solver.delta==delta
    f={1:sine(1-delta,1,arb(1))+sine(1-delta,3,b)};g={1:solver.poisson(f[1],1)}
    for n in range(2,10):f[n]=solver.order(n,f,g);g[n]=solver.poisson(f[n],n)
    return f,g

def run():
    ctx.prec=1536;start=time.monotonic();root=Path('research/152_parameter_regularization_slope');source=Path('research/151_fixed_shape_parameter_limit/verification/checks.json');data=json.loads(source.read_text())
    alg=json.loads(Path('research/119_tuned_rational_series/verification/algebraic_roots.json').read_text());bvar=sp.Symbol('b');P=sp.Poly(sp.sympify(alg['sturm_sequence'][0]),bvar,domain=sp.QQ);coeff=[str(v) for v in reversed(P.all_coeffs())];dcoeff=[str(176703765525000*v) for v in reversed(P.diff().all_coeffs())]
    rows=[];text=lambda v:v.str(65,radius=True)
    for row in data['rows']:
        b,I=refine_root(coeff,row['root_interval'],128);Ob=arb(0)
        for v in reversed(dcoeff):Ob=Ob*b+ball(mpq(v))
        Ob/=35818438656000000;db=order6_bderivative(b);assert db.overlaps(Ob) and not Ob.contains(0)
        Hlim=arb(row['H6_limit']);Hstar=arb(row['H6_tuned']);residue=arb(row['stream9_pole_residue']);sigma=arb(row['sigma2']);slope=12*(Hstar-Hlim)/Ob;assert not slope.contains(0)
        samples=[]
        for power in [30,60,100]:
            for sign in [-1,1]:
                t=mpq(sign,2**power);delta=mpq(2,3)+t
                ff,gf=prefix(delta,b);fc,gc=prefix(delta,b+slope*ball(t))
                scaled=ball(t)*gf[9].sine(4);error=scaled-residue
                assert abs(error)<ball(abs(t)*10000)
                assert abs(gc[6].sine(2)-Hstar)<ball(abs(t)*10000)
                assert abs(gc[9].sine(4))<100
                samples.append(dict(power=power,sign=sign,delta=str(delta),fixed_stream9=text(gf[9].sine(4)),fixed_scaled_stream9=text(scaled),scaled_residue_error=text(error),curve_stream6=text(gc[6].sine(2)),curve_stream9=text(gc[9].sine(4)),finite_error_bound=str(abs(t)*10000),all_checks_pass=True))
        item=dict(root_index=row['root_index'],root_interval=I,Ob_polynomial=text(Ob),Ob_cartesian=text(db),Ob_overlap=True,db_ddelta=text(slope),db_dc=text(slope/9),curve_limiting_harmonic=text(Hlim+Ob*slope/12),limiting_harmonic_matches=(Hlim+Ob*slope/12).overlaps(Hstar),samples=samples)
        assert item['limiting_harmonic_matches'];rows.append(item)
        print(json.dumps({k:item[k] for k in ['root_index','Ob_polynomial','db_ddelta','db_dc','limiting_harmonic_matches']}),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,arithmetic_bits=1536,source_sha256=sha256(source.read_bytes()).hexdigest(),rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Finite analytic slope criterion and finite approach checks; no all-order parameter family is asserted.')
    (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['parameter_regularization_slope.py','fixed_shape_parameter_limit.py','pure_cartesian_ball.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
if __name__=='__main__':
    try:run()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/152_parameter_regularization_slope/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
