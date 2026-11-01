"""Finite higher jets of the rational-exponent tuning curve."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import argparse,json,sys,time
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb,ctx
import sympy as sp
from formal_parameter_jet import JetField,poisson,quotient
from pure_cartesian_ball import Tuning,ball,refine_root
from parameter_regularization_slope import order6_bderivative

def pack(v):
    m,e=v.mid().man_exp();r,re=v.rad().man_exp()
    return [str(m),int(e),str(r),int(re)]
def unpack(v):
    m,e,r,re=v
    mid=arb(int(m))*arb(2)**e;rad=arb(int(r))*arb(2)**re
    return mid+arb(0,rad)

def prefix(betas):
    J=len(betas)-1;N=3*(J+1);coeff=[]
    for d,v in enumerate(betas):
        row=[arb(0)]*7;row[0],row[6]=-v/2,v/2
        if not d:row[2],row[4]=-arb(1)/2,arb(1)/2
        coeff.append(row)
    f={1:JetField(mpq(1,3),-1,-3,coeff)}
    counts=dict(support_zero_checks=0,compatible_simple_divisions=0,poisson_jet_coefficient_checks=0,ordered_products=0)
    g={1:poisson(f[1],1,counts)}
    for n in range(2,N+1):
        total=JetField(1-mpq(2*n,3),-n,order=J)
        for i in range(1,n):
            total=total+g[i].derivative()*f[n-i].derivative(True)-g[i].derivative(True)*f[n-i].derivative()
            counts['ordered_products']+=1
        factor=quotient([ball(mpq(1,3)),arb(-1)],[ball(mpq(2,3)),arb(1)],total.order)
        f[n]=total.scale([v/(n-1) for v in factor]);g[n]=poisson(f[n],n,counts)
    assert g[N].order==0
    return f,g,counts

def run():
    ap=argparse.ArgumentParser();ap.add_argument('--max-jet',type=int,default=12);ap.add_argument('--roots',default='1,2');ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    ctx.prec=2048;start=time.monotonic();root=Path('research/159_higher_parameter_jets');out=root/'verification'
    algpath=Path('research/119_tuned_rational_series/verification/algebraic_roots.json');num=Path('research/119_tuned_rational_series/verification/algebraic_numeric_values.json')
    alg=json.loads(algpath.read_text());data=json.loads(num.read_text());P=sp.Poly(sp.sympify(alg['sturm_sequence'][0]),sp.Symbol('b'),domain=sp.QQ);co=[str(v) for v in reversed(P.all_coeffs())]
    summaries=[]
    for index in map(int,args.roots.split(',')):
        old=data['rows'][index-1];b,I=refine_root(co,old['root_interval'],2176)
        solver=Tuning(1,3);ft,gt,hs=solver.prefix(b,3*(args.max_jet+1))
        Ob=order6_bderivative(b);C=Ob/12;betas=[b];rows=[]
        dest=out/f'root{index}_checks.json'
        if args.resume and dest.exists():
            previous=json.loads(dest.read_text());rows=previous['rows'];betas.extend(unpack(row['beta_exact_dyadic']) for row in rows)
        for j in range(1,args.max_jet+1):
            if j>1:C=C*hs[j-2]['sigma']/(6*(j+1))
            if j<len(betas):continue
            levelstart=time.monotonic();n=3*(j+1);q=2*j
            ff,gg,c0=prefix(betas+[arb(0)]);H0=gg[n].sine(q);Hstar=hs[j-1]['H']
            observed=None
            if j in [1,2,3,6,9,12,16,20,24,30]:
                _,gone,_=prefix(betas+[arb(1)]);observed=gone[n].sine(q)-H0
                assert observed.overlaps(C),('slope',index,j,str(observed),str(C))
            assert not C.contains(0)
            beta=(Hstar-H0)/C;assert not beta.contains(0)
            f,g,c1=prefix(betas+[beta]);comparisons=0
            for order in range(1,n+1):
                for m in range(1,4*order,2):
                    assert f[order].sine(m).overlaps(ft[order].sine(m)),('density',index,j,order,m)
                    comparisons+=1
                for m in range(2,4*order+1,2):
                    assert g[order].sine(m).overlaps(gt[order].sine(m)),('stream',index,j,order,m)
                    comparisons+=1
            ratio=None if j==1 else abs(beta/betas[-1]);factorialroot=(abs(beta)/arb(factorial(j)))**(arb(1)/j)
            text=lambda v:None if v is None else v.str(85,radius=True)
            row=dict(j=j,spatial_order=n,beta=text(beta),beta_exact_dyadic=pack(beta),predicted_slope=text(C),observed_slope=text(observed),slope_check=observed is not None,ratio_abs=text(ratio),ratio_over_j=text(None if ratio is None else ratio/j),factorial_normalized_root=text(factorialroot),constant_comparisons=comparisons,counts_zero=c0,counts_tuned=c1,actual_level_elapsed_s=time.monotonic()-levelstart)
            betas.append(beta);rows.append(row)
            result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),root_index=index,root_interval=I,arithmetic_bits=2048,max_jet=j,all_finite_checks_pass=True,rows=rows,actual_invocation_elapsed_s=time.monotonic()-start,scope='Finite jets only; no parameter convergence or divergence conclusion.')
            dest.write_text(json.dumps(result,indent=2)+'\n')
            print(json.dumps(dict(root=index,j=j,beta=beta.str(35,radius=True),ratio_over_j=text(None if ratio is None else ratio/j),level_elapsed_s=row['actual_level_elapsed_s'],elapsed_s=time.monotonic()-start)),flush=True)
        summaries.append(dict(root_index=index,max_jet=len(rows),last_beta=rows[-1]['beta']))
    for name in ['higher_parameter_jets.py','formal_parameter_jet.py','pure_cartesian_ball.py','parameter_regularization_slope.py','fixed_shape_parameter_limit.py']:
        (root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log'}
    (out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
    print(json.dumps(dict(all_finite_checks_pass=True,roots=summaries,actual_invocation_elapsed_s=time.monotonic()-start)),flush=True)
if __name__=='__main__':
    try:run()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(v.filename).name,line=v.lineno) for v in traceback.extract_tb(exc.__traceback__)])
        Path('research/159_higher_parameter_jets/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
