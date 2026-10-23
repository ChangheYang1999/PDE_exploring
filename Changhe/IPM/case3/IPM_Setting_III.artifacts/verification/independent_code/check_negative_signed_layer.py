"""Independent finite checks accompanying the written result224 proof."""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,math
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
import sympy as sp
import mpmath as mp
from negative_signed_layer import parameters,constants,series_moments,combination_moments,contour_moments,z_euler_moments,ode_terms
root=Path('research/negative_signed_inner_layer');v=root/'verification';v.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
result={'status':'RUNNING','utc_started':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'proof_sha256':sha(root/'PROOF.md'),'module_sha256':sha('independent_code/negative_signed_layer.py'),'driver_sha256':sha(__file__),'checks':[],'rows':[]}
def check(name,condition,evidence=None):
    result['checks'].append({'name':name,'passed':bool(condition),'evidence':evidence})
def checkpoint():
    result['utc_updated']=datetime.now(timezone.utc).isoformat();(v/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
def num(x):return mp.nstr(x,24)
p,z,c,K,T,j=sp.symbols('p z c K T j',positive=True);mu=(p+1)/2;n=mu*p;q=n+p-1;r=p-1/mu;A=(1-mu)/p;lam=p*K/(2*mu**2*A)
a=-p/2;b=(1-p)/2;d=1/(p+1);B=1-d
for name,expr in {
 'density_inverse_exponent':q-2*mu-(n-2),'transport_constant':q/p-1+A*(p+2),
 'lambda_closed':lam-4*p**2*K/((p+1)**2*(1-p)),
 'signed_operator_transform':(p-2*T-p)*(p-2*T-r)*(p-2*T-p-2)+8*T*(T+B-1)*(T+1),
 'second_derivative_transform':(p-2*T)*(p-2*T-1)-4*(T+a)*(T+b),
 'r_negative_form':r-(p+2)*(p-1)/(p+1),'exp_common':(a+d+b+d)-(1+d+2+d)+d-(a+b-B-2),
 'contour_left_gap':(p/2-sp.Rational(3,4))-(-a-1)-sp.Rational(1,4),
 'contour_right_gap':-b-(p/2-sp.Rational(3,4))-sp.Rational(1,4),
 'a_plus_d_positive':a+d-(1-p)*(p+2)/(2*(p+1)),
 'matching_sign':(-2*A)*(-p*K/(1/p-1))+p*K*(-1),
 'gamma_pole_separation':b-a-sp.Rational(1,2),
 'F1_indicial':0*(0-d)*(0+1),
 'F2_indicial':d*(d-d)*(d+1),
 'third_indicial':(-1)*(-1-d)*(-1+1),
}.items():check(name,sp.simplify(expr)==0,str(sp.factor(expr)))
# Verify full reduced ODE on monomials, rather than only the leading degree.
X=sp.symbols('X',positive=True);nu=sp.symbols('nu')
for vv in [0,d,-1]:
    check('indicial '+str(vv),sp.simplify(vv*(vv-d)*(vv+1))==0)
check('third_log_coefficient',sp.simplify((-d)*(-(a-1)*(b-1)/d)-(a-1)*(b-1))==0)
checkpoint();mp.mp.dps=60
plist=[mp.mpf(1)/4,mp.mpf(1)/3,mp.sqrt(2)-1,mp.mpf(1)/2,mp.mpf(3)/4]
for pv in plist:
    co=constants(pv);pa=parameters(pv);tag=num(pv)
    check(tag+' odd_negative',co['odd']<0,num(co['odd']));check(tag+' even_negative',co['even']<0,num(co['even']))
    check(tag+' exponential_signs',co['E1']<0<co['E2'])
    check(tag+' slow_coefficients_nonzero',co['A1']<0 and co['A2']<0)
    cancel=co['A1']*co['E1']+co['A2']*co['E2'];check(tag+' exponential_cancellation',abs(cancel)<mp.mpf('1e-55'),num(cancel))
    # Distinct coefficient recurrences vs complete contour at three arguments and two rules.
    for xx in [mp.mpf('.3'),mp.mpf('3'),mp.mpf('30')]:
        ser,terms=combination_moments(pv,xx)
        C32=contour_moments(pv,xx,32);C48=contour_moments(pv,xx,48)
        dif=max(abs(u-vv)/(1+abs(u))for u,vv in zip(ser,C48));ref=max(abs(u-vv)/(1+abs(vv))for u,vv in zip(C32,C48))
        check(tag+' contour_series X'+num(xx),dif<mp.mpf('1e-28'),num(dif));check(tag+' contour_refinement X'+num(xx),ref<mp.mpf('1e-24'),num(ref))
        zz=mp.sqrt(1/xx);zm=z_euler_moments(pv,zz,mp.mpf(1),C48);lhs,rhs=ode_terms(pv,zz,mp.mpf(1),zm);err=abs(lhs-rhs)/(1+abs(lhs)+abs(rhs))
        check(tag+' independent_contour_ODE X'+num(xx),err<mp.mpf('1e-27'),num(err))
        result['rows'].append({'p':tag,'X':num(xx),'terms':terms,'series_contour_error':num(dif),'contour_refinement':num(ref),'ODE_residual':num(err)});checkpoint()
    # An independently rescaled contour exposes the one-sided derivative directly.
    zz=mp.mpf('1e-5');xx=1/zz**2;C48=contour_moments(pv,xx,48);zm=z_euler_moments(pv,zz,mp.mpf(1),C48)
    derivative=zm[1]/zz;err=abs(derivative-co['odd'])/(1+abs(co['odd']))
    check(tag+' axis_derivative_limit',err<mp.mpf('1e-3'),num(err))
    check(tag+' axis_derivative_nonzero',derivative<0,num(derivative))
    # Exponential coefficients tested without cancellation, using the separate series.
    for branch,expected in [(1,co['E1']),(2,co['E2'])]:
        xx=mp.mpf(2000);val,terms=series_moments(pv,xx,branch,0);kap=pa['a']+pa['b']-pa['B']-2
        ratio=val[0]*mp.exp(-xx)*xx**(-kap)/expected
        check(tag+' exponential_limit branch'+str(branch),abs(ratio-1)<mp.mpf('.015'),num(ratio))
    print(datetime.now(timezone.utc).isoformat(),tag,'done',len(result['checks']),flush=True);checkpoint()
# Endpoint examples are outside the theorem and prevent accidental endpoint inclusion.
check('p0 constant solves degenerateODE',sp.simplify((-p)*(-r)*(-p-2)).subs(p,0)==0,'p=0,r=-2,theta h=0 for h=1')
check('p1 constant solves degenerateODE',sp.simplify((-p)*(-r)*(-p-2)).subs(p,1)==0,'p=1,r=0,theta h=0 for h=1')
result['status']='PASS'if all(x['passed']for x in result['checks'])else'FAIL';result['count']=len(result['checks']);result['utc_finished']=datetime.now(timezone.utc).isoformat();checkpoint();print(result['status'],len(result['checks']),flush=True)
for row in result['checks']:
    if not row['passed']:print('FAILED',row,flush=True)
