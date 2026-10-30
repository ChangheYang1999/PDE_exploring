"""Independent local Cartesian Taylor audit of the frozen scaled field engine."""
from pathlib import Path
from datetime import datetime, timezone
from math import comb, factorial
from hashlib import sha256
import importlib.util, json, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('frozen_n4_scaled_fields',BASE/'source/fields.py')
F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
DEGREE=4
ONE={(0,0):Q(1)}

def add(*terms):
    out={}
    for term in terms:
        for key,v in term.items():out[key]=out.get(key,Q(0))+v
    return {k:v for k,v in out.items() if v}

def scale(a,c):return {k:v*c for k,v in a.items() if v*c}

def mul(a,b):
    out={}
    for (i,j),u in a.items():
        for (k,l),v in b.items():
            if i+j+k+l<=DEGREE:
                key=i+k,j+l;out[key]=out.get(key,Q(0))+u*v
    return {k:v for k,v in out.items() if v}

def power(a,n):
    assert isinstance(n,int) and n>=0
    out=ONE
    for _ in range(n):out=mul(out,a)
    return out

def relative_power(a,e):
    a0=a.get((0,0),Q(0));assert a0>0
    h=scale(add(a,{(0,0):-a0}),1/a0)
    term=ONE;out=ONE;coefficient=Q(1)
    for k in range(1,DEGREE+1):
        term=mul(term,h);coefficient*=Q(e-k+1)/k
        out=add(out,scale(term,coefficient))
    return out

def integral_power(a,n):
    if n>=0:return power(a,n)
    return scale(relative_power(a,Q(n)),a[0,0]**n)

def harmonic(x,y,m):
    re,im=ONE,{}
    for _ in range(2*m):re,im=add(mul(re,x),scale(mul(im,y),-1)),add(mul(re,y),mul(im,x))
    return re

def ar(q):
    q=Q(q);return arb(q.numerator)/arb(q.denominator)

def cartesian(data,xs,ys):
    x0,y0=Q(xs),Q(ys);x={(0,0):x0,(1,0):Q(1)};y={(0,0):y0,(0,1):Q(1)}
    r2=add(mul(x,x),mul(y,y));S=add(r2,ONE)
    c=Q(data.get('cl_exact',data.get('cl')));delta=1-1/c
    result={(i,j):arb(0) for i in range(5) for j in range(5-i)}
    for g in data['generators']:
        j,m=int(g['j']),int(g['m']);kind,*ss=g['spec'];w=int(ss[0]);n=0 if kind=='mono' else int(ss[1]);q=int(ss[2]) if kind in ['legq','legqs'] else 0;R=Q(ss[3]) if kind=='legqs' else Q(1)
        p=(3+1/c-j*delta)/2-m
        localS=relative_power(S,p);den=add(r2,{(0,0):R*R});shifted={}
        for k in range(n+1):
            coef=Q((-1)**(n+k)*comb(n,k)*comb(n+k,k))*R**(2*q)
            term=mul(integral_power(r2,w+k),integral_power(den,-w-q-k))
            shifted=add(shifted,scale(term,coef))
        local=mul(mul(harmonic(x,y,m),localS),shifted)
        factor=ar(Q(g['coef']))*ar(S[0,0])**ar(p)
        for key,value in local.items():result[key]+=factor*ar(value)
    d={(i,j):a*factorial(i)*factorial(j) for (i,j),a in result.items()}
    out={'rho':-d[2,1]-d[0,3],'u1':-d[1,2],'u2':d[2,1],'rho_x':-d[3,1]-d[1,3],'rho_y':-d[2,2]-d[0,4]}
    out['residual']=(ar(c*x0)+out['u1'])*out['rho_x']+(ar(c*y0)+out['u2'])*out['rho_y']-out['rho']
    out.update({f'chi_{i}_{j}':a for (i,j),a in d.items()})
    return out

def main():
    start=time.monotonic();ctx.prec=2048
    digest=lambda p:sha256(Path(p).read_bytes()).hexdigest()
    manifest=json.loads((BASE/'verification/source_manifest.json').read_text())
    assert all(digest(BASE/p)==h for p,h in manifest.items())
    fixtures=json.loads((BASE/'data/fixtures.json').read_text());peer=json.loads((BASE/'source/N4_fields.json').read_text())
    assert peer['all_passed'] and peer['rational_arithmetic_checks'] and all(peer['candidate007_exact_field_comparisons'].values())
    Rat=F.Rat;a=Rat(Poly([3,-2,0,5]),(3,1));b=Rat(Poly([-2,7,1]),(1,2))
    denom=F.LINEARS[0]**3*F.LINEARS[1]
    quot=Rat(a.P.derivative()*denom-a.P*denom.derivative(),(6,2))
    assert a.derivative()==quot and (a+b)-b==a and a*0==0
    rational_checks=0
    for t in [Q(0),Q(1,4),Q(3,4),Q(1)]:
        assert (a+b).exact_value(t)==a.exact_value(t)+b.exact_value(t)
        assert (a*b).exact_value(t)==a.exact_value(t)*b.exact_value(t)
        assert (a*F.TR**3).divide_t(3).exact_value(t)==a.exact_value(t)
        rational_checks+=3
    try:a.divide_t(1)
    except AssertionError:pass
    else:raise AssertionError('invalid origin division accepted')
    try:F.rational(0.1)
    except TypeError:pass
    else:raise AssertionError('float coefficient accepted')
    points=[('1/2','1/3'),('3','4'),('60','80'),('-3/5','7/4'),('0','1/2'),('2','0')]
    rows=[];total=0
    for index,data in enumerate(fixtures):
        model=F.ScaledRadial(data);mixed=0
        for x in range(1,5):
            for y in range(1,5-x):
                alt=model.differentiate(model.deriv(x-1,y),x+y-1,'s' if y%2 else 'c','x')
                assert alt==model.deriv(x,y);mixed+=1
        for x in range(5):
            for y in range(5-x):model.fields[f'chi_{x}_{y}']=(model.deriv(x,y),x+y,'s' if y%2 else 'c')
        checks=[]
        for xs,ys in points:
            own=cartesian(data,xs,ys);other=model.evaluate(xs,ys)
            flags={k:v.overlaps(other[k]) for k,v in own.items()}
            assert len(flags)==21 and all(flags.values()),(index,xs,ys,flags)
            total+=len(flags)
            checks.append({'point':[xs,ys],'overlaps':flags,'independent_values':{k:v.str(80) for k,v in own.items()}})
        rows.append({'fixture':index,'mixed_derivatives_exact':mixed,'points':checks})
        print('fixture',index,'126 scalar comparisons passed',flush=True)
    paths=[Path(__file__),BASE/'PROOF.md',BASE/'verification/source_manifest.json',BASE/'data/fixtures.json',BASE/'source/fields.py',BASE/'source/N4_fields.json']
    out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'inputs':{str(p.relative_to(BASE)):digest(p) for p in paths},'scalar_comparisons':total,'rational_point_checks':rational_checks,'quotient_rule_exact':True,'invalid_t_division_rejected':True,'float_input_rejected':True,'manufactured':rows,'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED N4-191 algebra and independent Cartesian fixtures; candidate-level moments remain separate'}
    with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('DONE',out['utc'],total,'scalar comparisons',out['elapsed_seconds'],'seconds',flush=True)
if __name__=='__main__':main()
