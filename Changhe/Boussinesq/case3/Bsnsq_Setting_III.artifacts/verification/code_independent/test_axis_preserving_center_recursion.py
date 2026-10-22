"""Own exact packet122 check of center corrections with fixed g1 and g3."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
from time import monotonic
import json,hashlib
import sympy as sp
import exact_bivariate as P
import formal_center_recursion as C

root=Path('research/122_global_axis_first_order_realization/verification')

def right_inverse_fix_g1(H,n):
    D={}
    for i in range(1,n+1,2):
        j=n-i
        v=(-H.get((i,j),Q(0))-(j+2)*(j+1)*D.get((i,j+2),Q(0)))/((i+1)*(i+2))
        if v:D[i+2,j]=v
    assert P.scale(P.lap(D),-1)==P.clean(H)
    return D

def axis_series(beta,a0,base,N):
    g1={j:v for (i,j),v in base.items() if i==1}
    b=g1.copy();b[1]=b.get(1,Q(0))+beta
    mu=1+3*beta/2;M=2*beta+1
    aa={0:a0};qq={}
    for k in range(N+1):
        if k:
            aa[k]=sum((3*i-k-1)*b.get(i,Q(0))*aa.get(k-i+1,Q(0)) for i in range(2,k+2))/(mu*k)
        qq[k]=(2*aa[k]-sum((k-2*i+1)*b.get(i,Q(0))*qq.get(k-i+1,Q(0)) for i in range(2,k+2)))/(mu*k+M-mu)
    return aa,qq

def expression(poly,x,y):
    return sum(sp.Rational(v.numerator,v.denominator)*x**i*y**j for (i,j),v in poly.items())

def one(bs,avs,N):
    beta,a0=Q(bs),Q(avs);base,par=C.base_stream(beta,a0,N+2)
    aa,qq=axis_series(beta,a0,base,N-1)
    qe={j:v for (i,j),v in P.scale(P.lap(base),-1).items() if i==1}
    strip={(3,j):-(qq[j]-qe.get(j,Q(0)))/6 for j in range(N)}
    psi=P.add(base,strip);initial=psi.copy();initial_theta=C.temperature(beta,a0,psi,N+1)
    _,RO=P.pde(beta,psi,initial_theta,N)
    assert not {k:v for k,v in RO.items() if k[0]==1},RO
    stages=[];l=(beta-2)/2;mu=1+3*beta/2
    for n in range(2,N+1):
        th=C.temperature(beta,a0,psi,n+1)
        defect=P.homogeneous(P.pde(beta,psi,th,n)[1],n)
        assert all(i!=1 for i,j in defect)
        dO={k:-v/(k[0]*l+k[1]*mu+1) for k,v in defect.items()}
        D=right_inverse_fix_g1(dO,n)
        assert all(i>=5 for i,j in D)
        psi=P.add(psi,D);theta=C.temperature(beta,a0,psi,n+1)
        f,g=P.pde(beta,psi,theta,n+1)
        assert not P.trunc(f,n+1) and not P.trunc(g,n)
        assert {k:v for k,v in psi.items() if k[0] in [1,3]}=={k:v for k,v in initial.items() if k[0] in [1,3]}
        stages.append({'degree':n+2,'D':P.serialize(D),'divisible_by_x5':True,'g1_g3_unchanged':True})
    theta=C.temperature(beta,a0,psi,N+1)
    data={'parameters':par,'max_residual_degree':N,'initial_psi':P.serialize(initial),'psi':P.serialize(psi),'theta':P.serialize(theta),'stages':stages,
          'axis_a':{str(k):str(v) for k,v in aa.items()},'axis_Q':{str(k):str(v) for k,v in qq.items()}}
    path=root/('axis_center_b'+bs.replace('/','_')+'_N'+str(N)+'.json');path.write_text(json.dumps(data,indent=2)+'\n')
    # Independent symbolic differentiation, from serialized exact coefficients.
    re=json.loads(path.read_text());load=lambda rows:{(v['x_power'],v['y_power']):Q(v['coefficient']) for v in rows}
    ps=load(re['psi']);th=load(re['theta'])
    x,y=sp.symbols('x y');expr=expression(ps,x,y);tt=expression(th,x,y);bb=sp.Rational(beta.numerator,beta.denominator)
    w1=bb*x-sp.diff(expr,y);w2=bb*y+sp.diff(expr,x)
    oo=-sp.diff(expr,x,2)-sp.diff(expr,y,2)
    ff=sp.Poly(sp.expand(w1*sp.diff(tt,x)+w2*sp.diff(tt,y)-(bb-2)*tt),x,y)
    gg=sp.Poly(sp.expand(w1*sp.diff(oo,x)+w2*sp.diff(oo,y)+oo-sp.diff(tt,x)),x,y)
    assert all(sum(k)>N+1 for k,v in ff.terms() if v)
    assert all(sum(k)>N for k,v in gg.terms() if v)
    return {'beta':bs,'a0':avs,'N':N,'certificate':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'symbolic_PDE_check':True,'all_corrections_divisible_x5':True,
            'first_nonzero_correction':next((z for z in stages if z['D']),None)}

if __name__=='__main__':
    t0=monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','cases':[]}
    for bs,avs,N in [('4','1',12),('9','1',10),('25/9','3/2',10)]:
        ans=one(bs,avs,N);out['cases'].append(ans);print(bs,N,'CONFIRMED',flush=True)
    out.update(status='CONFIRMED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=monotonic()-t0)
    out['code_hashes']={n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['test_axis_preserving_center_recursion.py','formal_center_recursion.py','exact_bivariate.py']}
    (root/'center_recursion_tests.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
