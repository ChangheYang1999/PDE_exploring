"""Manufactured gate for the independently implemented full Q inverse."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,traceback,math
import mpmath as mp
from q_mp_primitives import MPQPrimitives,chebyshev_power_rows,convert,mf,horner,guard_digits
from q_exact_jets import jets

out=Path('research/q_full_inverse_primitives/verification/manufactured.json');out.parent.mkdir(parents=True,exist_ok=True)
report=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',checks=[],implementation_sha256=hashlib.sha256(Path('independent_code/q_mp_primitives.py').read_bytes()).hexdigest(),test_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
def save():out.write_text(json.dumps(report,indent=2)+'\n')
def check(name,error,tolerance='1e-65',**kw):
    error=abs(error);tol=mp.mpf(tolerance);row=dict(name=name,error=mp.nstr(error,30),tolerance=tolerance,passed=bool(error<tol),**kw);report['checks'].append(row);save();print(json.dumps(row),flush=True);assert error<tol,(name,mp.nstr(error,30),tolerance)

def direct_D(model,j,u):
    t=2*u-1
    get=lambda k:model.density.clenshaw(model.coeff[k],t)[0]if k<model.M else mp.mpf(0)
    return get(0)-u*get(1)/2 if j==0 else (get(j)-u*get(j+1))/2

def direct_H(model,j,u):return (1+(2*model.kappa-1)*u)*direct_D(model,j,u)

save()
try:
    with mp.workdps(120):
        for n in range(14):
            cc=[F(0)]*n+[F(1)]
            for reverse in [False,True]:
                po=[mf(v)for v in convert(cc,chebyshev_power_rows(n,reverse))]
                error=max(abs(horner(po,s)-mp.chebyt(n,1-2*s if reverse else 2*s-1))for s in map(mp.mpf,['.003','.17','.71','.997']))
                check('closed_chebyshev_'+str(n)+'_'+str(reverse),error)
        coeff=[[F((-1)**(j+k)*(j+2),2**(k+3))for k in range(11-j)]for j in range(3)]
        for kap in [F(2),F(7,3),F(11)]:
            model=MPQPrimitives(coeff,F(1),kap,F(5,2));jj=jets(coeff,kap,F(5,2))
            check('center_exact_'+str(kap),model.c-mf(jj['c']))
            for text in ['.003','.37','.8','.999']:
                s=mp.mpf(text);w=1-s;aa,bb=model.moments(s,w)
                for j in [1,2,3]:
                    K=2*model.kappa*(j+1);Kb=2*model.kappa*(j-1)
                    # These integrands use original scalar Clenshaw polynomials,
                    # not the finite primitive coefficients or their recurrence.
                    qa=s**(j-1)/2*mp.quad(lambda v:v**(2*j-1)*(w/(1-s*v))**K*direct_H(model,j-1,s*v),[0,.5,.9,.99,.999,1])
                    qb=s**(j-1)*w/2*mp.quad(lambda v:v**Kb*direct_H(model,j,1-w*v),[0,.5,1])
                    check('interior_quadrature_'+str(kap)+'_'+text+'_'+str(j),(aa[j-1]-qa)/(1+abs(qa)))
                    check('exterior_quadrature_'+str(kap)+'_'+text+'_'+str(j),(bb[j-1]-qb)/(1+abs(qb)))
        for kap in [F(3,2),F(2),F(11)]:
            model=MPQPrimitives([[F(7,4)]],F(3,2),kap,F(5,2))
            check('radial_strain_'+str(kap),model.c+mf(F(7,16)))
        # Exact binary synthetic inputs retain their identity under mp.diff's
        # internal precision increases. Points avoid the piecewise chart join.
        model=MPQPrimitives(coeff,F(1),F(2),F(5,2))
        for x,y in [(mp.mpf('.037'),mp.mpf('.061')),(mp.mpf('.7'),mp.mpf('1.1'))]:
            value=model.at(x,y)
            ux=-mp.diff(lambda v:model.stream(x,v),y)
            uy=mp.diff(lambda v:model.stream(v,y),x)
            source=mp.diff(lambda v:model.rho(v,y),x)
            lap=mp.diff(lambda v:model.stream(v,y),x,2)+mp.diff(lambda v:model.stream(x,v),y,2)
            check('cartesian_stream_velocity_'+str(x),max(abs(ux-value['U'][0]),abs(uy-value['U'][1])),'1e-60')
            check('cartesian_poisson_'+str(x),abs(lap+source)/(1+abs(source)),'1e-60')
            gx=mp.diff(lambda v:model.rho(v,y),x);gy=mp.diff(lambda v:model.rho(x,v),y)
            check('cartesian_density_gradient_'+str(x),max(abs(gx-value['gradient'][0]),abs(gy-value['gradient'][1])),'1e-60')
    coeff2=[[F((-1)**(j+k)*(j+1),2**(k+3))for k in range(19-j)]for j in range(6)]
    points=[('1e-12','1.1'),('.004','1e-10'),('.4','.71'),('40','1.3'),('1e20','.003'),('1e250','1.2')]
    rows=[]
    for target in [80,110]:
        with mp.workdps(target+guard_digits(18,6,11)):
            model=MPQPrimitives(coeff2,1,11,F(11,10));values=[]
            for rt,tt in points:
                r=mp.mpf(rt);theta=mp.mpf(tt);v=model.at(r*mp.cos(theta),r*mp.sin(theta))
                values.append([v['rho']/r,*v['U_over_r'],*v['gradient'],v['R_over_r'],v['R_Nf'],v['R_Nv']])
            rows.append(values)
    with mp.workdps(160):
        for point,a,b in zip(points,rows[0],rows[1]):check('precision_80_110_'+str(point),max(abs(x-y)/(1+abs(y))for x,y in zip(a,b)),'1e-70')
    report['status']='PASS';report['finished_utc']=datetime.now(timezone.utc).isoformat();report['scope']='Manufactured comparisons of complete primitive inverse with separate scalar quadrature, Cartesian differentiation, exact center moments and higher precision. Empirical tests, not interval enclosures.';save()
except BaseException:
    report['status']='FAIL';report['finished_utc']=datetime.now(timezone.utc).isoformat();report['traceback']=traceback.format_exc();save();raise
print(json.dumps(dict(status=report['status'],checks=len(report['checks']),output=str(out))),flush=True)
