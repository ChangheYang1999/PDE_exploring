"""Independent global identities with explicit tail and search limitations."""
from __future__ import annotations
import numpy as np
from scipy.optimize import minimize
from scipy.special import roots_legendre, beta as beta_function, gamma as gamma_function
from math import fsum
from independent_weighted_identities import power_nodes


def swirl_maximum(field, *, nradial=101, nangle=129, starts=16,
                  minimum_power=-12, maximum_power=14):
    scale=max(field.phi.length,field.q.length)
    logs=np.log(scale)+np.linspace(minimum_power,maximum_power,nradial)*np.log(2.)
    theta=np.linspace(0.,np.pi,nangle)
    r=np.exp(logs[:,None])*np.sin(theta);z=np.exp(logs[:,None])*np.cos(theta)
    values=field.q.evaluate(r*r,z)**2
    seeds=[]
    for i in range(nradial):
        for j in range(nangle):
            if values[i,j]>0 and values[i,j]>=np.max(values[max(0,i-1):min(nradial,i+2),max(0,j-1):min(nangle,j+2)]):
                seeds.append((float(values[i,j]),i,j))
    seeds.sort(reverse=True)
    def objective(x):
        R=np.exp(x[0]);rr=R*np.sin(x[1]);zz=R*np.cos(x[1]);jet=field.q.jet(rr*rr,zz,1)
        q=jet[0,0];dr=2*rr*jet[1,0];dz=jet[0,1]
        return -float(q*q),-2*q*np.array([dr*rr+dz*zz,dr*zz-dz*rr])
    def describe(rr,zz,success):
        d=field.cylindrical(rr,zz,3);red=field.reduced(rr,zz)
        q=float(d['q'][0,0]);qgrad=np.array([2*rr*d['q'][1,0],d['q'][0,1]],dtype=float)
        v=float(d['ur_over_r']);W=np.array([field.c_l*rr+d['U'][0],field.c_l*zz+d['U'][2]])
        return {'r':float(rr),'z':float(zz),'q':q,'abs_q':abs(q),'v':v,'absolute_swirl_maximum_defect':abs(v+.5),
                'gradient_norm':float(np.linalg.norm(qgrad)),'q_residual':float(red['q']),
                'stationarity_correction':float(W@qgrad),
                'pointwise_identity_error':float(red['q']-(1+2*v)*q-W@qgrad),'optimizer_success':bool(success)}
    found=[describe(0.,0.,True)]
    for _,i,j in seeds[:starts]:
        fit=minimize(objective,[logs[i],theta[j]],jac=True,method='L-BFGS-B',
                     bounds=[(logs[0],logs[-1]),(0.,np.pi)],options={'ftol':1e-15,'gtol':1e-13,'maxiter':250})
        R=np.exp(fit.x[0]);found.append(describe(R*np.sin(fit.x[1]),R*np.cos(fit.x[1]),fit.success))
    best=max(found,key=lambda a:a['abs_q'])
    return {'best':best,'local_searches':found,'radial_search_interval':[float(np.exp(logs[0])),float(np.exp(logs[-1]))],
            'boundary_maximum':bool(np.hypot(best['r'],best['z'])>=.999*np.exp(logs[-1])),
            'global_maximum_proved':False,'scope':'Finite scan and analytic-gradient local searches. The defect is necessary at a nonzero true maximum; search completeness is not proved.'}


def bernoulli_balance(field,xyz,pressure,pressure_gradient):
    xyz=np.asarray(xyz,dtype=np.float64);P=np.asarray(pressure,dtype=np.float64);gp=np.asarray(pressure_gradient,dtype=np.float64)
    U,J=field.cartesian(xyz,True);c=field.c_l;a=2*c-1;W=c*xyz+U
    H=np.sum(U*U,axis=-1)/2+P+c*np.sum(xyz*U,axis=-1)+c*a*np.sum(xyz*xyz,axis=-1)/2
    gradH=np.einsum('...ji,...j->...i',J,W)+gp+c*U+c*a*xyz
    lhs=np.sum(W*gradH,axis=-1);rhs=a*np.sum(W*W,axis=-1)
    M=(1-c)*U+np.einsum('...ij,...j->...i',J,W)+gp
    work=np.sum(W*M,axis=-1)
    return {'H':H,'gradient_H':gradH,'W_dot_gradient_H':lhs,'expected_exact_profile':rhs,
            'Euler_defect':lhs-rhs,'residual_work':work,'algebraic_error':lhs-rhs-work}


def _scalar_split(scalar,s,z,target,ds=0,dz=0):
    """Homogeneous leading part and stable remainder for the own power basis.

    Homogeneity classifications allow 2e-11 for exponent roundoff, consistently
    with the exact leading-coefficient extractor. They do not fit tail powers.
    """
    s,z=np.broadcast_arrays(np.asarray(s,dtype=np.float64),np.asarray(z,dtype=np.float64))
    R=np.sqrt(s+z*z)
    if np.any(R<=0):raise ValueError('tail split is used only away from the origin')
    if scalar.kernel=='gaussian':return np.zeros_like(R),scalar.evaluate(s,z,ds,dz)
    mu=z/R;sin2=s/(R*R);lead=np.zeros_like(R);remainder=np.zeros_like(R)
    ttarget=target-2*ds-dz;log_envelope=np.log1p((scalar.length/R)**2)
    for term in scalar.differentiated(ds,dz):
        degree=2*term.i+term.j-2*term.beta
        angular=term.coefficient*sin2**term.i*mu**term.j
        if abs(degree-ttarget)<=2e-11:
            h=angular*R**ttarget;lead+=h;remainder+=h*np.expm1(-term.beta*log_envelope)
        elif degree<ttarget:
            remainder+=angular*R**degree*np.exp(-term.beta*log_envelope)
        else:raise ValueError('basis has a term slower than its declared leading power')
    return lead,remainder


def tail_compatibility(field):
    failures=[]
    for name,scalar,target,required in [('phi',field.phi,-field.alpha,-2*field.alpha-1),('q',field.q,-field.alpha-1,-2*field.alpha-2)]:
        if scalar.kernel=='gaussian':
            if any(t.beta<=0 for t in scalar.terms if t.coefficient):failures.append(name+': nondecaying Gaussian term')
            continue
        for i,t in enumerate(scalar.terms):
            if not t.coefficient:continue
            degree=2*t.i+t.j-2*t.beta
            if abs(degree-target)<=2e-11:continue
            if degree>required+2e-11:failures.append(f'{name} term {i}: intermediate or slower homogeneity {degree}')
    return {'sufficient_basis_test_passed':not failures,'failures':failures,
            'scope':'Conservative termwise test for the own monomial-envelope basis. No cancellation between different terms is assumed.'}


def velocity_tail_split(field,r,z):
    r,z=np.broadcast_arrays(np.asarray(r,dtype=np.float64),np.asarray(z,dtype=np.float64));s=r*r
    pairs={key:_scalar_split(field.phi,s,z,-field.alpha,*key) for key in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]}
    q={key:_scalar_split(field.q,s,z,-field.alpha-1,*key) for key in [(0,0),(1,0),(0,1)]}
    output=[]
    for index in [0,1]:
        p={key:value[index] for key,value in pairs.items()};b={key:value[index] for key,value in q.items()}
        U=np.stack((-r*p[0,1],r*b[0,0],2*p[0,0]+2*s*p[1,0]),axis=-1)
        J=np.zeros(U.shape+(3,),dtype=np.float64)
        J[...,0,0]=-p[0,1]-2*s*p[1,1];J[...,0,1]=-b[0,0];J[...,0,2]=-r*p[0,2]
        J[...,1,0]=b[0,0]+2*s*b[1,0];J[...,1,1]=-p[0,1];J[...,1,2]=r*b[0,1]
        J[...,2,0]=8*r*p[1,0]+4*r*s*p[2,0];J[...,2,2]=2*p[0,1]+2*s*p[1,1]
        omega=np.stack((-r*b[0,1],-r*(8*p[1,0]+4*s*p[2,0]+p[0,2]),2*b[0,0]+2*s*b[1,0]),axis=-1)
        output.append((U,J,omega))
    return output


def radial_integrals(function, *, inner_power, outer_power, scale,nradial=64,nangle=64,map_power=4,dimension=3):
    if not inner_power>-1 or not outer_power<-1:raise ValueError('nonintegrable sufficient endpoint bound')
    mu,wm=roots_legendre(nangle);sin=np.sqrt(1-mu*mu)
    if dimension==3:angular=2*np.pi*wm
    elif dimension==5:angular=2*np.pi**2*(1-mu*mu)*wm
    else:raise ValueError('only dimensions three and five')
    # function returns integrands before the radial volume factor.
    totals={};parts=[]
    for where in ['origin','exterior']:
        if where=='origin':
            x,w=power_nodes(nradial,inner_power);R=scale*x;factor=scale**(inner_power+1);power=inner_power
        else:
            h=int(map_power);u,w=power_nodes(nradial,h*(-outer_power-1)-1);R=scale/u**h
            w=h*w;factor=scale**(outer_power+1);power=outer_power
        vals=function(R[:,None]*sin,R[:,None]*mu,where)
        result={}
        for key,value in vals.items():
            averaged=np.asarray(value,dtype=np.float64)@angular
            answer=float(factor*np.dot(w,averaged*R**(dimension-1-power)))
            totals[key]=totals.get(key,0.)+answer;result[key]=answer
        parts.append(result)
    return {'integrals':totals,'origin':parts[0],'exterior':parts[1],'nradial':nradial,'nangle':nangle,
            'split_radius':float(scale),'exterior_map_power':map_power,'inner_radial_power':inner_power,'outer_radial_power':outer_power}


def energy_remainder_gap(field):
    gaps=[2.]
    for scalar,target in [(field.phi,-field.alpha),(field.q,-field.alpha-1)]:
        if scalar.kernel!='power':continue
        for term in scalar.terms:
            if not term.coefficient:continue
            gap=target-(2*term.i+term.j-2*term.beta)
            if gap>2e-11:gaps.append(gap)
    return min(gaps)


def energy_finite_part(field, *, nradial=64,nangle=64,split_radius=None,map_power=8,residual_check=False):
    if not .5<field.c_l<.6:raise ValueError('this convergent energy subtraction requires 1/2<c_l<3/5')
    compatibility=tail_compatibility(field)
    if not compatibility['sufficient_basis_test_passed']:raise ValueError(compatibility['failures'])
    scale=float(split_radius if split_radius is not None else max(field.phi.length,field.q.length));alpha=field.alpha
    def values(r,z,where):
        (U0,J0,_),(delta,Jdelta,_)=velocity_tail_split(field,r,z)
        U,J=field.cartesian(np.stack((r,np.zeros_like(r),z),axis=-1),True)
        if where=='origin':e=(np.sum(U*U,axis=-1)-np.sum(U0*U0,axis=-1))/2
        else:e=np.sum(delta*(2*U0+delta),axis=-1)/2
        out={'energy_finite_part':e,'absolute_subtracted_energy_integral':np.abs(e)}
        if residual_check:
            xyz=np.stack((r,np.zeros_like(r),z),axis=-1)
            L=np.einsum('...ij,...j->...i',J if where=='origin' else Jdelta,xyz)+alpha*(U if where=='origin' else delta)
            # P=0 is an admissible manufactured pressure for this algebraic
            # test. No claim is made that it is the full-space Euler pressure.
            out['linear_residual_work']=field.c_l*np.sum(U*L,axis=-1)
        return out
    record=radial_integrals(values,inner_power=2-2*alpha,outer_power=2-2*alpha-energy_remainder_gap(field),scale=scale,
                            nradial=nradial,nangle=nangle,map_power=map_power)
    E=record['integrals']['energy_finite_part'];den=record['integrals']['absolute_subtracted_energy_integral']
    record.update(relative_signed_defect=abs(E)/den if den else None,tail_compatibility=compatibility,
                  scope='Convergent renormalized kinetic energy, including infinity. Euler requires zero; quadrature is not an interval proof.')
    if residual_check:
        def nonlinear_values(r,z,where):
            U,J=field.cartesian(np.stack((r,np.zeros_like(r),z),axis=-1),True)
            return {'nonlinear_residual_work':np.einsum('...i,...ij,...j->...',U,J,U)}
        nonlinear=radial_integrals(nonlinear_values,inner_power=2,outer_power=1-3*alpha,scale=scale,
                                  nradial=nradial,nangle=nangle,map_power=map_power)
        record['nonlinear_work_quadrature']=nonlinear
        record['integrals'].update(nonlinear['integrals'])
        work=record['integrals']['linear_residual_work']+record['integrals']['nonlinear_residual_work']
        record['integrals']['zero_pressure_residual_work']=work
        record['residual_identity_error']=(5*field.c_l-2)*E+work
    return record


def helicity_finite_part(field, *, nradial=64,nangle=64,split_radius=None,map_power=4):
    if not .5<field.c_l<.75:raise ValueError('this helicity subtraction requires 1/2<c_l<3/4')
    compatibility=tail_compatibility(field)
    if not compatibility['sufficient_basis_test_passed']:raise ValueError(compatibility['failures'])
    scale=float(split_radius if split_radius is not None else max(field.phi.length,field.q.length));alpha=field.alpha
    def values(r,z,where):
        (U0,_,O0),(dU,_,dO)=velocity_tail_split(field,r,z)
        value=np.sum(U0*dO+dU*O0+dU*dO,axis=-1)
        return {'helicity_finite_part':value,'absolute_subtracted_helicity_integral':np.abs(value)}
    return radial_integrals(values,inner_power=1-2*alpha,outer_power=-3*alpha,scale=scale,
                            nradial=nradial,nangle=nangle,map_power=map_power)


def eta_norm_identity(field, *, nradial=64,nangle=64,split_radius=None,map_power=4):
    if not .5<field.c_l<2/3:raise ValueError('this eta square integral requires 1/2<c_l<2/3')
    scale=float(split_radius if split_radius is not None else max(field.phi.length,field.q.length));alpha=field.alpha
    def values(r,z,where):
        d=field.cylindrical(r,z,3);red=field.reduced(r,z);eta=d['eta']
        return {'eta_squared':eta*eta,'v_eta_squared':d['ur_over_r']*eta*eta,
                'eta_swirl_source':eta*2*d['q'][0,0]*d['q'][0,1],'residual_work':eta*red['eta']}
    record=radial_integrals(values,inner_power=4,outer_power=-2*alpha,scale=scale,nradial=nradial,
                            nangle=nangle,map_power=map_power,dimension=5)
    v=record['integrals'];lhs=(2-3*field.c_l)*v['eta_squared'];rhs=2*(v['v_eta_squared']+v['eta_swirl_source']);work=2*v['residual_work']
    record.update(Euler_defect=lhs-rhs,residual_prediction=work,algebraic_integral_error=lhs-rhs-work,
                  relative_Euler_defect=abs(lhs-rhs)/(abs(lhs)+abs(rhs)) if abs(lhs)+abs(rhs) else None)
    return record


def virial_identity(field, *, nradial=64,nangle=64,split_radius=None,map_power=4):
    compatibility=tail_compatibility(field)
    if not compatibility['sufficient_basis_test_passed']:raise ValueError(compatibility['failures'])
    scale=float(split_radius if split_radius is not None else max(field.phi.length,field.q.length));alpha=field.alpha
    if alpha<=.25:raise ValueError('virial integrability requires alpha>1/4')
    def values(r,z,where):
        xyz=np.stack((r,np.zeros_like(r),z),axis=-1);U,J=field.cartesian(xyz,True)
        if where=='origin':L=np.einsum('...ij,...j->...i',J,xyz)+alpha*U
        else:
            _,(delta,Jdelta,_)=velocity_tail_split(field,r,z)
            L=np.einsum('...ij,...j->...i',Jdelta,xyz)+alpha*delta
        N=np.einsum('...ij,...j->...i',J,U)
        return {'L_squared':np.sum(L*L,axis=-1),'N_dot_L':np.sum(N*L,axis=-1)}
    record=radial_integrals(values,inner_power=2,outer_power=-4*alpha,scale=scale,
                            nradial=nradial,nangle=nangle,map_power=map_power)
    v=record['integrals'];first=field.c_l*v['L_squared'];second=v['N_dot_L']
    record.update(Euler_defect=first+second,relative_Euler_defect=abs(first+second)/(abs(first)+abs(second)) if abs(first)+abs(second) else None,
                  tail_compatibility=compatibility)
    return record


def energy_finite_part_beta(field):
    """Independent closed radial integrals for this specific envelope basis."""
    if not .5<field.c_l<.6:raise ValueError('requires 1/2<c_l<3/5')
    compatibility=tail_compatibility(field)
    if not compatibility['sufficient_basis_test_passed']:raise ValueError(compatibility['failures'])
    components=[]
    p=field.phi;q=field.q
    components.append((p,[( -t.coefficient,2*t.i+1,t.j,t.beta) for t in p.differentiated(0,1)]))
    components.append((q,[(t.coefficient,2*t.i+1,t.j,t.beta) for t in q.terms]))
    components.append((p,[(2*t.coefficient,2*t.i,t.j,t.beta) for t in p.terms]+
                         [(2*t.coefficient,2*t.i+2,t.j,t.beta) for t in p.differentiated(1,0)]))
    values=[]
    for scalar,terms in components:
        for a in terms:
            for b in terms:
                coef=a[0]*b[0]/2;m=a[1]+b[1];n=a[2]+b[2];rate=a[3]+b[3]
                if coef==0 or n%2:continue
                angular=2*np.pi*beta_function((n+1)/2,m/2+1);power=(m+n+3)/2
                if scalar.kernel=='power':
                    gap=rate-power
                    if gap<=-1 or abs(gap)<1e-13:raise ValueError('beta reference outside proved finite-part cases')
                    radial=.5*scalar.length**(2*power-2*rate)*beta_function(power,gap)
                else:
                    if rate<=0:raise ValueError('Gaussian product does not decay')
                    radial=.5*gamma_function(power)/rate**power
                values.append(float(coef*angular*radial))
    total=fsum(values);absolute=fsum(abs(v) for v in values)
    return {'energy_finite_part':total,'absolute_sum_of_terms':absolute,
            'summation_condition_estimate':absolute/abs(total) if total else None,'nonzero_integrated_products':len(values),
            'scope':'Closed beta/gamma radial integrals for the verifier monomial-envelope basis, evaluated in float64 with compensated summation.'}
