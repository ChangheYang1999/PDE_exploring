"""Controls of packet125 exact coordinates, derivative calculus, and full inverse."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import copy, hashlib, json, time
import numpy as np
import mpmath as mp
from scipy.optimize import least_squares
from third_order_center_tail_chart import (keys, labels, moments, exact_state,
                                  verify_exact_state, BetaCase, ThirdOrderProblem)
from first_ladder_chart import tail_checks as checks
from free_beta_stream import grid, prepare_divided, divided_fields
from cartesian_inverse import CartesianInverse, InverseSettings

start = time.monotonic()
root = Path('research/125_third_order_center_tail_chart/verification')
root.mkdir(exist_ok=True)
out = {'utc': datetime.now(timezone.utc).isoformat(), 'status': 'RUNNING',
       'exact_states': [], 'jacobians': [], 'mp_direct': [], 'inverse': []}
rng = np.random.default_rng(421125)
# The packet115 checker expands in monomial z, independently of this chart's
# angular Chebyshev action. Exact checks include two resolutions and signed a0.
for n,J in [(4,2),(5,4)]:
    for beta,eta,a0 in [(Q(5,2),Q(7,3),Q(1)),(Q(23,10),Q(-11,7),Q(-2)),
                        (Q(29,10),Q(0),Q(3,5))]:
        uc=[Q(int(v),97) for v in rng.integers(-9,10,len(keys(n,J)))]
        ud=[Q(int(v),101) for v in rng.integers(-9,10,len(keys(n,J,False)))]
        data=exact_state(beta,eta,a0,n,J,uc,ud)
        data=json.loads(json.dumps(data));assert verify_exact_state(data)
        from stream_local_jet_certificate import checks as local_checks
        assert not any(local_checks(data)['nonzero'].values())
        ck=checks(data)
        assert not any(ck[k] for k in ['stream_nonzero','temperature_nonzero','first_ladder_stream_nonzero','first_ladder_temperature_nonzero']),ck
        assert Q(ck['constant_vertical'])==eta
        p=root/f'exact_n{n}J{J}_b{str(beta).replace("/","_")}.json'
        p.write_text(json.dumps(data,indent=2)+'\n')
        case=BetaCase(float(beta),n,J,np.array([[0,0],[.1,.3]]),a0=float(a0))
        C,D=case.coefficients(float(eta),np.array(list(map(float,uc+ud))))
        errors=[float(np.max(np.abs(v-np.array(list(map(lambda q:float(Q(q)),data[k]))))))
                for k,v in [('C',C),('D',D)]]
        assert max(errors)<2e-12,errors
        out['exact_states'].append({'path':str(p),'beta':str(beta),'eta':str(eta),
            'a0':str(a0),'free_coordinate_count':len(uc)+len(ud),
            'float_exact_coefficient_errors':errors,'center_moments_exact':True,
            'tail_polynomials_exactly_zero':True,'constant_vertical_exact':str(eta)})
# Reject altered dimensions, field coefficients, and hidden chart inputs.
rejects=[]
for name,mutate in [
    ('coefficient',lambda d:d['C'].__setitem__(0,str(Q(d['C'][0])+Q(1,10**20)))),
    ('labels',lambda d:d['labels'].__setitem__(0,[99,0,0])),
    ('eta',lambda d:d.__setitem__('eta',str(Q(d['eta'])+1))),
    ('freeC_length',lambda d:d['freeC'].pop()),
    ('a0_zero',lambda d:d.__setitem__('a0','0')),
    ('outside_beta',lambda d:d.__setitem__('beta','3'))]:
    bad=copy.deepcopy(data);mutate(bad)
    try:verify_exact_state(bad)
    except (ValueError,AssertionError):rejects.append(name)
    else:raise AssertionError('tampered chart accepted: '+name)
out['rejected_tampering']=rejects
# Compare combined beta/eta/coefficient Jacobian against a five-point stencil.
points=np.array([[0,0],[0,.2],[0,-1.4],[.001,.3],[.1,-.2],[-.1,-.2],[1.1,.8],[3,-2],[10,5]],float)
for beta,eta in [(2.2,-1.1),(2.5,0.),(2.85,2.4)]:
    pr=ThirdOrderProblem(4,3,points)
    case=pr.case(beta);z=np.r_[beta,eta,rng.normal(0,.03,case.size)]
    jac=pr.jacobian(z)
    for mode in ['all','eta','beta']:
        direction=rng.normal(size=len(z)) if mode=='all' else np.zeros(len(z))
        if mode=='eta':direction[1]=1
        if mode=='beta':direction[0]=1
        direction/=np.linalg.norm(direction)
        errors=[]
        for h in [2e-5,1e-5]:
            fd=(pr.residual(z-2*h*direction)-8*pr.residual(z-h*direction)
                +8*pr.residual(z+h*direction)-pr.residual(z+2*h*direction))/(12*h)
            error=float(np.linalg.norm(fd-jac@direction)/max(1.,np.linalg.norm(fd)))
            errors.append(error);assert error<3e-7,(beta,eta,mode,error)
        out['jacobians'].append({'beta':beta,'eta':eta,'direction':mode,
                                'five_point_relative_errors':errors})
# Differentiate the elementary Chebyshev expressions directly at high precision,
# avoiding the own production monomial derivative expansion and center formulas.
beta=Q(5,2);eta=Q(7,3);n=4;J=3
uc=[Q(int(v),107) for v in rng.integers(-4,5,len(keys(n,J)))]
ud=[Q(int(v),109) for v in rng.integers(-4,5,len(keys(n,J,False)))]
data=exact_state(beta,eta,1,n,J,uc,ud)
mp.mp.dps=50
mpq=lambda v:mp.mpf(Q(v).numerator)/Q(v).denominator
bb=mpq(beta);ss=1/bb;cc=list(map(mpq,data['C']));dd=list(map(mpq,data['D']))
gamma=sum(c*mp.chebyt(j,0) for c,(i,j,d) in zip(cc,data['labels']))
def psi(x,y):
    R=mp.sqrt(1+x*x+y*y);u=2*R**(-ss)-1;v=y/R
    return sum(c*x*R**(1-ss-d)*mp.chebyt(i,u)*mp.chebyt(j,v)
               for c,(i,j,d) in zip(cc,data['labels']))-gamma*x
def theta(x,y):
    R=mp.sqrt(1+x*x+y*y);u=2*R**(-ss)-1;v=y/R
    return sum(c*x*x*R**(-1-2*ss-d)*mp.chebyt(i,u)*mp.chebyt(j,v)
               for c,(i,j,d) in zip(dd,data['labels']))
case=BetaCase(float(beta),n,J,points);C,D=case.coefficients(float(eta),np.array(list(map(float,uc+ud))))
center={'gamma':gamma,'strain':mp.diff(psi,(0,0),(1,1)),
        'b0':-mp.diff(psi,(0,0),(3,0))-mp.diff(psi,(0,0),(1,2)),
        'a0':mp.diff(theta,(0,0),(2,0))/2,
        'V1':-mp.diff(psi,(0,0),(0,1)),'V2':mp.diff(psi,(0,0),(1,0))}
target={'gamma':-mpq(eta),'strain':1+bb/2,'b0':4/bb,'a0':mp.mpf(1),'V1':mp.mpf(0),'V2':mp.mpf(0)}
center_errors={k:float(abs(v-target[k])) for k,v in center.items()}
assert max(center_errors.values())<1e-45,center_errors
out['mp_center']={'precision_digits':50,'errors':center_errors,'values':{k:mp.nstr(v,35)for k,v in center.items()}}
# Direct high-precision third-order center PDE identities of the new exact state.
c1=mp.diff(psi,(0,0),(1,2));b1=-mp.diff(psi,(0,0),(3,1))-mp.diff(psi,(0,0),(1,3))
a1=mp.diff(theta,(0,0),(2,1))/2
fc=(1+3*bb/2)*a1-2*c1;gc=(2*bb+1)*b1-c1*4/bb-2*a1
assert max(abs(fc),abs(gc))<mp.mpf('1e-43')
out['mp_transverse_center']={'f1':mp.nstr(fc,12),'g1':mp.nstr(gc,12)}
for yy in [0.,.35,-1.2]:
    y=mp.mpf(yy);A=bb-mp.diff(psi,(0,y),(1,1));B=bb*y+mp.diff(psi,(0,y),(1,0))
    f=mp.diff(theta,(0,y),(2,0))/2;fy=mp.diff(theta,(0,y),(2,1))/2
    g=-mp.diff(psi,(0,y),(3,0))-mp.diff(psi,(0,y),(1,2))
    gy=-mp.diff(psi,(0,y),(3,1))-mp.diff(psi,(0,y),(1,3))
    ref={'A':A,'B':B,'f':f,'fy':fy,'g':g,'gy':gy,
         'RF':(2*A-bb+2)*f+B*fy,'RG':(A+1)*g+B*gy-2*f}
    own=divided_fields(case.basis,prepare_divided(case.basis,np.array([[0,yy]])),C,D)
    errors={k:float(abs(mp.mpf(float(own[k][0]))-v)/max(1,abs(v)))for k,v in ref.items()}
    assert max(errors.values())<2e-11,errors
    out['mp_direct'].append({'y':yy,'relative_to_max_1_errors':errors})
# Recompute this compound field's canonical full-plane velocity without using
# its stream derivative: Cartesian Duffy cells plus all four exterior sectors.
ipoints=np.array([[.1,-.2],[1.,.5],[-.7,1.3],[0.,-2.]])
exact=case.basis.fields(case.basis.prepare(ipoints),C,D)
expected=np.column_stack([exact['U1'],exact['U2']])
for radius,order in [(8.,24),(12.,40),(18.,56)]:
    inv=CartesianInverse(case.basis.omega_callable(C),InverseSettings(radius=radius,
        core_radial_order=12,core_angular_order=order,exterior_radial_order=order,
        exterior_angular_order=order,decay_power=1/float(beta)))
    got=inv.relative(ipoints)
    error=float(np.max(abs(got-expected)))
    out['inverse'].append({'square_radius':radius,'angular_exterior_order':order,
                           'maximum_absolute_error':error,'values':got.tolist()})
assert out['inverse'][-1]['maximum_absolute_error']<2e-7,out['inverse']
# Known-forcing nonlinear fit: checks solver consistency without asserting B2.
pts=grid(np.geomspace(.04,15,9),np.linspace(0,np.pi,10))
p=ThirdOrderProblem(4,2,pts);size=p.case(2.45).size
truth=np.r_[2.45,.8,rng.normal(0,.03,size)];forcing=p.residual(truth)
initial=truth+rng.normal(0,.001,len(truth));initial[0]+=.025;initial[1]-=.01
fit=least_squares(lambda z:p.residual(z)-forcing,initial,jac=p.jacobian,
    bounds=(np.r_[2.02,np.full(1+size,-np.inf)],np.r_[2.98,np.full(1+size,np.inf)]),
    max_nfev=80,ftol=1e-12,xtol=1e-12,gtol=1e-10,x_scale='jac')
error=float(np.max(abs(p.residual(fit.x)-forcing)))
assert error<1e-8,(error,fit.message)
out['manufactured_fit']={'maximum_weighted_residual':error,'nfev':fit.nfev,
 'njev':fit.njev,'beta_target':truth[0],'beta_returned':float(fit.x[0]),
 'eta_target':truth[1],'eta_returned':float(fit.x[1]),'optimality':float(fit.optimality),
 'coefficient_distance':float(np.linalg.norm(fit.x-truth)),
 'meaning':'forced finite-dimensional consistency control; not a B2 profile'}
# Independent symbolic polar differentiation, with r=u^q and a polynomial
# cosine variable w reduced modulo w^2+z^2=1, checks the actual PDE powers.
import sympy as sp
from first_ladder_chart import mono_from_cheb,ladder,inverse_lap
u,z,w=sp.symbols('u z w', real=True)
def angular(e):return sp.expand(w*sp.diff(e,z)-z*sp.diff(e,w))
def reduce_w(e):
    e=sp.expand(e);result=0
    for term in sp.Add.make_args(e):
        j=int(term.as_powers_dict().get(w,0));result+=term/w**j*w**(j%2)*(1-z*z)**(j//2)
    return sp.expand(result)
def expr(a):return sum(sp.Rational(v.numerator,v.denominator)*z**j for j,v in enumerate(a))
polar_rows=[]
for b in [Q(11,5),Q(5,2),Q(29,10)]:
    ss=1/b;den=ss.denominator;rs=lambda p:u**int(p*den)
    dr=lambda e:sp.diff(e,u)/(den*u**(den-1))
    for Jtest in [2,4]:
        pc=[Q(int(v),13)for v in rng.integers(-5,6,Jtest)]
        qc=[Q(int(v),17)for v in rng.integers(-5,6,Jtest)]
        P,Qp=map(mono_from_cheb,[pc,qc]);P10,Q10=ladder(b,P,Qp)
        ps=rs(2-ss)*w*expr(P)+rs(2-2*ss)*w*expr(P10)
        th=rs(1-2*ss)*w*w*expr(Qp)+rs(1-3*ss)*w*w*expr(Q10)
        om=reduce_w(-dr(dr(ps))-rs(-1)*dr(ps)-rs(-2)*angular(angular(ps)))
        vr=-rs(-1)*angular(ps);vt=dr(ps)
        ro=reduce_w((sp.Rational(b.numerator,b.denominator)*rs(1)+vr)*dr(om)+vt*rs(-1)*angular(om)+om-w*dr(th)+z*rs(-1)*angular(th))
        rt=reduce_w((sp.Rational(b.numerator,b.denominator)*rs(1)+vr)*dr(th)+vt*rs(-1)*angular(th)-(sp.Rational(b.numerator,b.denominator)-2)*th)
        for expression,powers in [(ro,[-ss,-2*ss]),(rt,[1-2*ss,1-3*ss])]:
            for power in powers:assert sp.expand(expression).coeff(u,int(power*den))==0,(b,Jtest,power)
        # A second-kind Chebyshev diagonalization, separate from descending monomials.
        rhs=expr(P10);target=expr(P10);k1=sp.Rational((2-2*ss).numerator,(2-2*ss).denominator)
        force=sp.expand(-((k1*k1-1)*target-3*z*sp.diff(target,z)+(1-z*z)*sp.diff(target,z,2)))
        cs=sp.symbols('c:'+str(sp.degree(force,z)+1));basis=sum(c*sp.chebyshevu(j,z)for j,c in enumerate(cs))
        eq=sp.Poly(basis-force,z).all_coeffs();sol=sp.solve(eq,cs,dict=True)[0]
        back=sp.expand(sum(sol[c]/((j+1)**2-k1*k1)*sp.chebyshevu(j,z)for j,c in enumerate(cs)))
        assert sp.expand(back-target)==0
        polar_rows.append({'beta':str(b),'J':Jtest,'actual_PDE_coefficients_zero':True,'second_kind_inverse_agrees':True})
out['symbolic_polar_controls']=polar_rows
# New independent Cartesian differentiation of the six pivots.
x,y,ss=sp.symbols('x y ss', real=True);rr=sp.sqrt(1+x*x+y*y)
pivots=[8*x*rr**(1-3*ss),32*x*rr**(1-4*ss)-48*x*rr**(1-3*ss),
        8*x*y*rr**(-3*ss),32*x*y*rr**(-4*ss)-48*x*y*rr**(-3*ss)]
origin=lambda e:sp.simplify(e.subs({x:0,y:0}))
rows=[]
for pp in pivots:
    oo=-sp.diff(pp,x,2)-sp.diff(pp,y,2)
    rows.append([origin(sp.diff(pp,x)),origin(sp.diff(oo,x)),
        origin(sp.diff(pp,x,y)),origin(sp.diff(oo,x,y)),origin(sp.diff(pp,x,y,2))])
even=sp.Matrix([[rows[j][i]for j in [0,1]]for i in [0,1]])
odd=sp.Matrix([[rows[j][i]for j in [2,3]]for i in [2,3]])
assert even==sp.Matrix([[8,-16],[-32*(1-3*ss),64*(1-ss)]])
assert odd==sp.Matrix([[8,-16],[144*ss,-96*ss]])
assert sp.simplify(even.det()-1024*ss)==0
assert sp.simplify(odd.det()-1536*ss)==0
assert rows[2][4]==rows[3][4]==0
for j,tt in enumerate([8*x*x*rr**(-1-4*ss),8*x*x*y*rr**(-2-4*ss)]):
    assert origin(sp.diff(tt,x,2)/2)==(8 if j==0 else 0)
    assert origin(sp.diff(tt,x,2,y)/2)==(8 if j==1 else 0)
out['cartesian_pivot_matrices']={'even':str(even),'odd':str(odd),
    'determinants':['1024/beta','1536/beta'],'odd_c1_zero':True,'thermal_diagonal':8}
out.update(status='CONFIRMED'  ,elapsed_seconds=time.monotonic()-start,
 code_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
 Path(__file__).with_name('third_order_center_tail_chart.py'),Path(__file__).with_name('first_ladder_chart.py'),Path(__file__).with_name('stream_basis.py'),
 Path(__file__).with_name('free_beta_stream.py'),Path(__file__).with_name('cartesian_inverse.py'),
 Path(__file__).with_name('stream_fractional_tail_certificate.py')]})
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
 'exact_states':len(out['exact_states']),'jacobian_max':max(max(a['five_point_relative_errors'])for a in out['jacobians']),
 'mp_center_max':max(center_errors.values()),'mp_axis_max':max(max(a['relative_to_max_1_errors'].values())for a in out['mp_direct']),
 'inverse':out['inverse'],'manufactured_fit':out['manufactured_fit']},indent=2),flush=True)
