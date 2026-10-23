"""Read-only analytic far-field coefficient audit of an exact saved candidate.

No coefficients are fitted to samples.  Finite Fourier algebra differentiates
the implemented potential term by term.  The formal inverse-even expansion is
specified for every order; only the explicitly requested finite number of its
coefficients is evaluated.  Fresh full-field samples are independent checks,
not a continuous supremum or a rigorous asymptotic remainder certificate.
"""
import argparse
import math
from pathlib import Path
import sys
import time

PROJECT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(PROJECT))
from absolute_common import ROOT,A_REF,np,read,atomic,npz,digest,array_hash,provenance
from absolute_fields_v2 import prepare_candidate,fields,residual,CORE_ORDER
from absolute_chart import hp_report
from stage13_model_v3 import original_namespace_identity_record
from far_asymptotic import leading_residual_coefficient
from scipy.special import gammaln
from threadpoolctl import threadpool_limits


def add(*terms):
    out={}
    for term in terms:
        for k,c in term.items():out[k]=out.get(k,0j)+c
    return out


def scale(a,c):return {k:v*c for k,v in a.items()}


def product(a,b):
    out={}
    for k,c in a.items():
        for l,d in b.items():out[k+l]=out.get(k+l,0j)+c*d
    return out


def angular(a):return {k:1j*k*c for k,c in a.items()}


def derivative(a,p,axis):
    """Cartesian derivative of r**p sum a_k exp(ik theta)."""
    out={}
    for k,c in a.items():
        if axis=='x':upper,lower=(p-k)*c/2,(p+k)*c/2
        elif axis=='y':upper,lower=(p-k)*c/(2j),-(p+k)*c/(2j)
        else:raise ValueError('Unknown Cartesian derivative')
        out[k+1]=out.get(k+1,0j)+upper
        out[k-1]=out.get(k-1,0j)+lower
    return out


def laplace(a,p):return {k:(p*p-k*k)*c for k,c in a.items()}


def cosine(m,c):return {0:complex(c)} if m==0 else {2*m:complex(c/2),-2*m:complex(c/2)}


def choose(a,n):
    result=1.
    for k in range(n):result*=(a-k)/(k+1)
    return result


def evaluate(a,theta):
    value=np.zeros_like(theta,dtype=complex)
    for k,c in a.items():value+=c*np.exp(1j*k*theta)
    return value.real


def sine_coefficients(a):
    maximum=max((abs(k) for k in a),default=0)
    coeff=np.zeros(maximum+1)
    for k in range(1,maximum+1):coeff[k]=-2*a.get(k,0j).imag
    leakage=max([abs(a.get(0,0j))]+[abs(a.get(k,0j).real) for k in a]+[
        abs(a.get(k,0j)) for k in a if k%2==0])
    return coeff,float(leakage)


def quotient_cosines(a):
    """Exact finite identity sin((2l+1)t)/sin(t)=1+2 sum cos(2kt)."""
    s,leakage=sine_coefficients(a);c=np.zeros(len(s))
    for n in range(1,len(s),2):
        c[0]+=s[n]
        for k in range(2,n+1,2):c[k]+=2*s[n]
    return c,leakage


def evaluate_cosines(c,theta):
    out=np.zeros_like(theta)
    for k,v in enumerate(c):out+=v*np.cos(k*theta)
    return out


def norm2(a):
    s,_=sine_coefficients(a)
    return float(math.sqrt(math.pi/4*float(s@s)))


def quotient_norm2(a):
    c,_=quotient_cosines(a)
    return float(math.sqrt(math.pi/2*c[0]**2+math.pi/4*float(c[1:]@c[1:])))


def density_moment(a,b):
    keys=set(a)|set(b)
    return float(max((abs(a.get(k,0j)-b.get(k,0j)) for k in keys),default=0))


def layer_report(a,theta,reference_norm=None,power=None):
    coeff,leakage=sine_coefficients(a);qc,qleakage=quotient_cosines(a)
    values=evaluate(a,theta);qvalues=evaluate_cosines(qc,theta)
    loc=int(np.argmax(abs(values)));qloc=int(np.argmax(abs(qvalues)))
    l2=norm2(a);ql2=quotient_norm2(a)
    energy=float(coeff@coeff)
    row={'sine_coefficients':[{'harmonic':k,'coefficient':float(v)} for k,v in enumerate(coeff) if k%2==1],
        'quotient_cosine_coefficients':[{'harmonic':k,'coefficient':float(v)} for k,v in enumerate(qc) if k%2==0],
        'angular_L2':l2,'angular_RMS':l2/math.sqrt(math.pi/2),
        'quotient_angular_L2':ql2,'quotient_angular_RMS':ql2/math.sqrt(math.pi/2),
        'dense_sampled_max_abs':float(abs(values[loc])),'sampled_theta':float(theta[loc]),
        'quotient_dense_sampled_max_abs':float(abs(qvalues[qloc])),
        'quotient_sampled_theta':float(theta[qloc]),'angular_nodes':len(theta),
        'quotient_axis_y0':float(sum(qc)),
        'quotient_axis_x0':float(sum(v*math.cos(k*math.pi/2) for k,v in enumerate(qc))),
        'density_E_axis_y0':0.,
        'density_E_prime_axis_y0':float(sum(qc)),
        'density_E_axis_x0':float(sum(v*math.cos(k*math.pi/2) for k,v in enumerate(qc))),
        'continuous_supremum_certified':False,'forbidden_parity_coefficient_max_abs':max(leakage,qleakage),
        'L2_energy_fraction_harmonics_above_current_tail_F_cutoff7':float(coeff[8:]@coeff[8:]/energy) if energy else 0.,
        'L2_energy_fraction_harmonics_above_proposed_tail_F_cutoff19':float(coeff[20:]@coeff[20:]/energy) if energy else 0.}
    if reference_norm is not None:
        row['fixed_reference_amplitude_normalized_L2']=l2/A_REF
        row['scale_invariant_density_L2_ratio']=float(A_REF**(power-1)*l2/reference_norm**power)
        row['scale_invariant_density_ratio_definition']='a_ref**N ||E_N||_L2 / ||F_0||_L2**(N+1), N=power-1; physical f(X/lambda) dilation'
    return row


def potential_layers(prepared,qmax):
    cl=float(prepared['parameters'][0]);gamma=1/cl;lam=1-gamma;A=(3+gamma)/2
    layers={(j,q):{} for j in range(4) for q in range(qmax+1)}
    details=[]
    for c,(m,k) in zip(prepared['coefficients'],CORE_ORDER):
        if k<=2:j,shift=0,k;sigma=float(k)
        else:j,shift=k-2,0;sigma=j*lam/2
        beta=A-m-sigma
        values=[]
        for q in range(shift,qmax+1):
            v=float(c)*choose(beta,q-shift)
            layers[j,q]=add(layers[j,q],cosine(m,v));values.append(v)
        details.append({'family':'core','m':m,'k':k,'j':j,'initial_inverse_even_order':shift,
            'radial_binomial_exponent':beta,'coefficient':float(c),'evaluated_coefficients':values})
    for c,mode in zip(prepared['extra'],prepared['modes']):
        if mode['family']!='global' or float(mode.get('sigma',0))!=0 or float(mode.get('alpha',0))!=0 or float(mode.get('beta',0))!=0:
            raise ValueError('This exact analytic audit requires the actual Global-only normalized Legendre sigma0 basis')
        m,n=int(mode['m']),int(mode['n']);vanish=max(5-m,0)
        # Match the actual binary64 log-Gamma expression in spectral_basis,
        # rather than replacing its algebraically equal value by sqrt(2n+1).
        lognorm=(gammaln(1.)+gammaln(1.)-gammaln(2.)) if n==0 else (
            gammaln(n+1.)+gammaln(n+1.)-math.log(2*n+1)-gammaln(n+1)-gammaln(n+1.))
        normal=math.exp(-.5*lognorm) if mode.get('normalize',True) else 1.
        normal*=float(mode.get('scale',1.))
        values=[]
        for q in range(qmax+1):
            v=float(c)*normal*math.fsum(((-1)**h*math.comb(n,h)*math.comb(n+h,h)*
                choose(A-m-vanish-h,q-h) for h in range(min(n,q)+1)))
            layers[0,q]=add(layers[0,q],cosine(m,v));values.append(v)
        details.append({'family':'global','m':m,'n':n,'initial_inverse_even_order':0,
            'normalization':normal,'origin_t_power':vanish,'coefficient':float(c),'evaluated_coefficients':values})
    return layers,details


def physical_layers(potentials,gamma,lam,qmax):
    F={};Phi={};checks=[]
    for (j,q),C in potentials.items():
        alpha=gamma-j*lam-2*q;b=alpha+3
        Phi[j,q]=derivative(derivative(C,b,'y'),b-1,'x')
        F[j,q]=scale(derivative(laplace(C,b),b-2,'y'),-1)
        lhs=scale(laplace(Phi[j,q],alpha+1),-1)
        rhs=derivative(F[j,q],alpha,'x')
        error=density_moment(lhs,rhs);normal=max([1.]+[abs(c) for c in lhs.values()]+[abs(c) for c in rhs.values()])
        checks.append({'j':j,'inverse_even_order':q,'minus_laplacian_psi_equals_rho_x_coefficient_max_error':error,
            'coefficient_scale':float(normal),'scaled_error':float(error/normal),
            'sanity_tolerance':1e-10,'passed':bool(error<=1e-10*normal)})
    return F,Phi,checks


def residual_layers(F,Phi,cl,gamma,lam,qmax):
    E={};cartesian_checks=[];term_sums={}
    for k in range(8):
        for q in range(qmax+1):
            linear=scale(F.get((k,q),{}),-k*(cl-1)-2*cl*q)
            terms=[linear];alternative=[linear]
            for a in range(4):
                b=k-1-a
                if b<0 or b>3:continue
                for u in range(q+1):
                    v=q-u;aa=gamma-a*lam-2*u;ab=gamma-b*lam-2*v
                    pa,fb=Phi[a,u],F[b,v]
                    terms.extend([scale(product(pa,angular(fb)),aa+1),scale(product(angular(pa),fb),-ab)])
                    alternative.extend([scale(product(derivative(pa,aa+1,'y'),derivative(fb,ab,'x')),-1),
                        product(derivative(pa,aa+1,'x'),derivative(fb,ab,'y'))])
            E[k,q]=add(*terms)
            term_sums[k,q]=sum(norm2(z) for z in terms)
            alternative_sum=add(*alternative)
            error=density_moment(E[k,q],alternative_sum)
            normal=max([1.]+[abs(c) for term in terms+alternative for c in term.values()])
            cartesian_checks.append({'k':k,'inverse_even_order':q,
                'polar_vs_cartesian_nonlinear_coefficient_max_abs_error':error,
                'coefficient_scale':float(normal),'scaled_error':float(error/normal),
                'sanity_tolerance':1e-10,'passed':bool(error<=1e-10*normal)})
    return E,cartesian_checks,term_sums


def homogeneous_inverse(F,alpha):
    """Unique nonresonant homogeneous particular inverse, no free multipole."""
    G=derivative(F,alpha,'x');out={}
    for k,c in G.items():
        divisor=(alpha+1)**2-k*k
        if divisor==0 and c!=0:raise ValueError('A homogeneous Poisson resonance requires separate treatment')
        out[k]=-c/divisor if divisor else 0j
    return out


def nonlinear_pair(Phi,F,alpha_a,alpha_b):
    return add(scale(product(Phi,angular(F)),alpha_a+1),scale(product(angular(Phi),F),-alpha_b))


def required_tail_layers(F,Phi,E,cl,gamma,lam,theta):
    conditional={};recursive_F={0:F[0,0]};recursive_Phi={0:Phi[0,0]};recursive={}
    for j in range(1,4):
        target=scale(add(E[j,0],scale(F[j,0],j*(cl-1))),1/(j*(cl-1)))
        conditional[str(j)]={'meaning':'Required F_j with lower layers held at the actual saved mismatched values',
            'required_F':layer_report(target,theta),'difference_from_actual_F':layer_report(add(target,scale(F[j,0],-1)),theta)}
        rhs=add(*(nonlinear_pair(recursive_Phi[a],recursive_F[j-1-a],
            gamma-a*lam,gamma-(j-1-a)*lam) for a in range(j)))
        recursive_F[j]=scale(rhs,1/(j*(cl-1)))
        recursive_Phi[j]=homogeneous_inverse(recursive_F[j],gamma-j*lam)
        recursive[str(j)]={'meaning':'Recursive leading-ladder PDE match after replacing every earlier F_j and its nonresonant homogeneous Poisson inverse',
            'required_F':layer_report(recursive_F[j],theta),
            'maximum_F_angular_harmonic':max((abs(k) for k,c in recursive_F[j].items() if c!=0),default=0),
            'maximum_Phi_angular_harmonic':max((abs(k) for k,c in recursive_Phi[j].items() if c!=0),default=0),
            'free_harmonic_multipoles_included':False}
    return conditional,recursive,recursive_F,recursive_Phi


def fourier_arrays(prefix,table,out,maxharmonic=80):
    for (j,q),a in table.items():
        value=np.zeros(2*maxharmonic+1,dtype=complex)
        for k,c in a.items():
            if abs(k)>maxharmonic:raise ValueError('Fourier storage cutoff is too small')
            value[k+maxharmonic]=c
        out[prefix+'_j'+str(j)+'_q'+str(q)]=value


def exact_field_checks(prepared,F,Phi,E,gamma,lam,qmax,radii,angles):
    records=[];arrays={};cl=float(prepared['parameters'][0])
    for radius in radii:
        x=radius*np.cos(angles);y=radius*np.sin(angles);x[-1]=0.;y[0]=0.
        ff=fields(prepared,x,y);rf=residual(prepared,x,y)
        rho=y*ff['f'];rrho=y*rf
        physical_rho=(cl*x-ff['psiy'])*(y*ff['fx'])+(cl*y+ff['psix'])*(ff['f']+y*ff['fy'])-rho
        predicted={};predicted_q={}
        for name,kmax,qq in [('leading_E1',1,0),('through_E3',3,0),('all_fractional_leading_layers',7,0),('finite_inverse_even_expansion',7,qmax)]:
            value=np.zeros_like(angles);quot=np.zeros_like(angles)
            for k in range(kmax+1):
                for q in range(qq+1):
                    exponent=gamma-k*lam-2*q
                    value+=radius**exponent*evaluate(E[k,q],angles)
                    qc,_=quotient_cosines(E[k,q]);quot+=radius**(exponent-1)*evaluate_cosines(qc,angles)
            predicted[name]=value;predicted_q[name]=quot
        rho_prediction=np.zeros_like(angles);psi_prediction=np.zeros_like(angles)
        for j in range(4):
            for q in range(qmax+1):
                exponent=gamma-j*lam-2*q
                rho_prediction+=radius**exponent*evaluate(F[j,q],angles)
                psi_prediction+=radius**(exponent+1)*evaluate(Phi[j,q],angles)
        rn=max(float(np.linalg.norm(rrho)),1e-300);rfn=max(float(np.linalg.norm(rf)),1e-300)
        leading=radius**(2*gamma-1)*evaluate(E[1,0],angles)
        row={'radius':float(radius),'angular_nodes':len(angles),
            'exact_full_Rrho_max_abs':float(np.max(abs(rrho))),
            'exact_full_Rf_max_abs':float(np.max(abs(rf))),
            'leading_Rrho_power':2*gamma-1,'leading_Rf_power':2*gamma-2,
            'Rrho_divided_by_r_power_minus_E1_relative':float(np.linalg.norm(rrho/radius**(2*gamma-1)-evaluate(E[1,0],angles))/max(np.linalg.norm(evaluate(E[1,0],angles)),1e-300)),
            'full_direct_density_minus_y_Rf_max_abs':float(np.max(abs(physical_rho-rrho))),
            'finite_series_rho_relative_error':float(np.linalg.norm(rho_prediction-rho)/max(np.linalg.norm(rho),1e-300)),
            'finite_series_psi_relative_error':float(np.linalg.norm(psi_prediction-ff['psi'])/max(np.linalg.norm(ff['psi']),1e-300)),
            'approximations':{name:{'density_relative_error':float(np.linalg.norm(z-rrho)/rn),
                'density_max_abs_error':float(np.max(abs(z-rrho))),
                'quotient_relative_error':float(np.linalg.norm(predicted_q[name]-rf)/rfn),
                'quotient_max_abs_error':float(np.max(abs(predicted_q[name]-rf)))} for name,z in predicted.items()},
            'whole_field_rho_max_abs':float(np.max(abs(rho))),
            'asymptotic_remainder_rigorously_bounded':False}
        records.append(row)
        tag='r_'+format(float(radius),'.12g').replace('.','p').replace('+','')
        arrays.update({tag+'_Rf_full':rf,tag+'_Rrho_full':rrho,tag+'_Rrho_direct':physical_rho,
            tag+'_rho_full':rho,tag+'_psi_full':ff['psi'],tag+'_Rrho_leading_E1':leading})
        for name,z in predicted.items():arrays[tag+'_Rrho_'+name]=z;arrays[tag+'_Rf_'+name]=predicted_q[name]
    return records,arrays


def run(args):
    began=time.time();candidate=args.candidate.resolve();case=read(candidate)
    if args.output.exists():raise ValueError('A fresh audit output directory is required')
    args.output.mkdir(parents=True)
    if digest(candidate)!=args.candidate_sha256:raise ValueError('The explicitly frozen candidate changed')
    commit=read(args.commit)
    if commit['post_state']['candidate_sha256']!=args.candidate_sha256:
        raise ValueError('The actual immutable commit does not bind the frozen saved candidate')
    p=np.asarray(case['core_parameters'],float);extra=np.asarray(case['extra_coefficients'],float)
    if p.shape!=(24,) or extra.shape!=(162,):raise ValueError('The complete original24 and Global-only162 parameters are required')
    prepared=prepare_candidate(case,'center_chart',parameters=p,extra=extra)
    cl=float(p[0]);gamma=1/cl;lam=1-gamma;qmax=args.inverse_even_order
    source_names=['absolute_fields.py','absolute_fields_v2.py','absolute_common.py','base/spectral_basis.py',
        'highprecision_origin.py','stage13_model_v3.py','stage13_stable_exp.py','far_asymptotic.py']
    sources={name:digest(ROOT/name) for name in source_names}
    report={'schema':'stage13_analytic_full_farfield_coefficients_v1','candidate_path':str(candidate),
        'candidate_sha256':args.candidate_sha256,'commit_path':str(args.commit.resolve()),'commit_sha256':digest(args.commit),
        'source_sha256':sources,'worker_source_sha256':digest(Path(__file__)),
        'environment':provenance(),'cl':cl,'gamma':gamma,'lambda':lam,'a_ref':A_REF,
        'center_convention':'unchanged analytic center_chart','C5':hp_report(p),
        'optimization_performed':False,'physical_coefficients_or_modes_modified':False,
        'coefficient_extraction':'Exact finite Fourier differentiation of homogeneous potential powers; analytic binomial/Legendre endpoint coefficients. No large-radius fitting.',
        'inverse_even_orders_evaluated':list(range(qmax+1)),
        'formal_all_orders_global_coefficient':'sqrt(2n+1)*sum_{h=0}^{min(n,q)} (-1)^h binom(n,h)binom(n+h,h)binom(A-m-max(5-m,0)-h,q-h), with saved scale/normalization and coefficient',
        'normalization_arithmetic':'Algebraic sqrt(2n+1); evaluation repeats the actual scipy.special.gammaln and math.exp binary64 expression in spectral_basis._radial, including saved scale/normalize.',
        'formal_all_orders_core_coefficient':'binom(A-m-sigma,q-q_shift), q_shift=0,1,2 for sigma=0,1,2; q_shift=0 and j=1,2,3 for sigma=j*(1-gamma)/2',
        'density_exponent':'alpha_jq=gamma-j*(1-gamma)-2q','psi_exponent':'alpha_jq+1',
        'residual_coefficient_formula':'E_kq=-(k*(cl-1)+2cl*q)F_kq+sum_{a+b=k-1,u+v=q}[(alpha_au+1)Phi_au*F_bv_prime-alpha_bv*Phi_au_prime*F_bv]',
        'inverse_even_first_linear_exponent':gamma-2,
        'first_even_correction_fractional_layer_location':2/lam,
        'first_three_fractional_layers_precede_first_inverse_even_correction':bool(3*lam<2),
        'canonical_harmonic_multipoles':'This implemented algebraic potential contains only the stated fractional-plus-inverse-even exponents. No independent r**(-2n) stream-function multipole is present unless an exponent happens to coincide; absence is an ansatz fact, not a statement about all canonical inverse solutions.',
        'namespace_before':original_namespace_identity_record(),'completed':False,'passed':False}
    atomic(args.output/'coefficients.json',report)
    theta=np.linspace(0,np.pi/2,args.angular_nodes);physical_theta=np.linspace(0,np.pi/2,args.physical_angular_nodes)
    with threadpool_limits(limits=1,user_api='blas'):
        potentials,mode_details=potential_layers(prepared,qmax)
        F,Phi,poisson_checks=physical_layers(potentials,gamma,lam,qmax)
        E,cartesian_checks,term_sums=residual_layers(F,Phi,cl,gamma,lam,qmax)
        old_leading=leading_residual_coefficient(prepared,theta)
        new_leading=evaluate_cosines(quotient_cosines(E[1,0])[0],theta)
        leading_error=float(np.linalg.norm(old_leading['coefficient']-new_leading)/max(np.linalg.norm(old_leading['coefficient']),1e-300))
        leading_control={'old_source':'far_asymptotic.leading_residual_coefficient unchanged _assemble/_harmonics evaluation',
            'relative_error':leading_error,'maximum_absolute_error':float(np.max(abs(old_leading['coefficient']-new_leading))),
            'tolerance':1e-8,'passed':bool(leading_error<=1e-8)}
        conditional,recursive,recursive_F,recursive_Phi=required_tail_layers(F,Phi,E,cl,gamma,lam,theta)
        f0norm=norm2(F[0,0]);qf0norm=quotient_norm2(F[0,0])
        if f0norm==0 or qf0norm==0:raise ValueError('A nonzero leading angular profile is required')
        layers={};e_reports={}
        for j in range(4):
            for q in range(qmax+1):
                key='j'+str(j)+'_q'+str(q)
                frow=layer_report(F[j,q],theta)
                # Phi has even rather than odd sine harmonics, so report its
                # Fourier coefficients directly; the quotient routine is for rho only.
                phicoeff=[{'harmonic':k,'coefficient':float(-2*Phi[j,q].get(k,0j).imag)}
                    for k in range(2,max((abs(n) for n in Phi[j,q]),default=0)+1,2)]
                layers[key]={'alpha':gamma-j*lam-2*q,'F':frow,'Phi_sine_coefficients':phicoeff,
                    'Phi_angular_L2':float(math.sqrt(math.pi/4*sum(z['coefficient']**2 for z in phicoeff)))}
        for k in range(8):
            for q in range(qmax+1):
                key='k'+str(k)+'_q'+str(q)
                erow=layer_report(E[k,q],theta,f0norm,k+1) if q==0 and 1<=k<=3 else layer_report(E[k,q],theta)
                erow.update(density_radial_power=gamma-k*lam-2*q,
                    quotient_radial_power=gamma-k*lam-2*q-1,
                    term_sum_angular_L2=term_sums[k,q],
                    relative_term_sum_L2_diagnostic=norm2(E[k,q])/max(term_sums[k,q],1e-300))
                if q==0 and 1<=k<=3:
                    erow['scale_invariant_quotient_L2_ratio']=float(A_REF**k*quotient_norm2(E[k,q])/qf0norm**(k+1))
                e_reports[key]=erow
        physical_records,physical_arrays=exact_field_checks(prepared,F,Phi,E,gamma,lam,qmax,args.radii,physical_theta)
    saved={'dense_angular_theta':theta,'physical_angular_theta':physical_theta,
        'harmonic_integer_indices':np.arange(-80,81),'p':p,'extra':extra,
        'analytic_center_coefficients':prepared['coefficients']}
    fourier_arrays('potential',potentials,saved);fourier_arrays('rho_F',F,saved)
    fourier_arrays('psi_Phi',Phi,saved);fourier_arrays('residual_E',E,saved);saved.update(physical_arrays)
    fourier_arrays('recursive_required_F',{(j,0):a for j,a in recursive_F.items()},saved)
    fourier_arrays('recursive_required_Phi',{(j,0):a for j,a in recursive_Phi.items()},saved)
    npz(args.output/'arrays.npz',**saved)
    report.update(layers=layers,residual_layers=e_reports,mode_radial_expansions=mode_details,
        poisson_coefficient_checks=poisson_checks,polar_vs_cartesian_checks=cartesian_checks,
        exact_full_field_checks=physical_records,leading_density_L2=f0norm,leading_quotient_L2=qf0norm,
        conditional_required_tail_layers=conditional,recursive_PDE_matched_required_tail_layers=recursive,
        current_tail_density_harmonic_cutoff=7,proposed_tail_density_harmonic_cutoff=19,
        leading_density_harmonic_cutoff=19,leading_psi_harmonic_cutoff=20,
        arrays_path=str((args.output/'arrays.npz').resolve()),arrays_sha256=digest(args.output/'arrays.npz'),
        namespace_after=original_namespace_identity_record(),seconds=time.time()-began,
        finite_inverse_even_expansion_rigorous_error_bound=False,
        full_physical_field_vs_analytic_series_used_as_independent_diagnostic=True,
        continuous_supremum_certified=False,completed=True)
    physical_controls={'leading_E1_at_largest_radius':bool(physical_records[-1]['Rrho_divided_by_r_power_minus_E1_relative']<1e-2),
        'finite_series_rho_at_largest_radius':bool(physical_records[-1]['finite_series_rho_relative_error']<1e-9),
        'finite_series_psi_at_largest_radius':bool(physical_records[-1]['finite_series_psi_relative_error']<1e-9),
        'finite_series_density_residual_at_radii_at_least256':bool(all(z['approximations']['finite_inverse_even_expansion']['density_relative_error']<1e-6 for z in physical_records if z['radius']>=256))}
    report.update(old_independent_leading_coefficient_check=leading_control,
        physical_series_sanity_controls=physical_controls,
        physical_series_sanity_thresholds={'leading_largest_radius_relative':1e-2,
            'rho_and_psi_largest_radius_relative':1e-9,'density_residual_radii_at_least256_relative':1e-6})
    report['passed']=bool(report['namespace_before']['passed'] and report['namespace_after']['passed'] and
        hp_report(p)['max_abs']<1e-10 and all(digest(ROOT/name)==sha for name,sha in sources.items()) and
        digest(candidate)==args.candidate_sha256 and all(z['passed'] for z in poisson_checks+cartesian_checks) and
        leading_control['passed'] and all(physical_controls.values()))
    atomic(args.output/'coefficients.json',report)
    if not report['passed']:raise SystemExit(2)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--candidate-sha256',required=True)
    parser.add_argument('--commit',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--inverse-even-order',type=int,default=6)
    parser.add_argument('--angular-nodes',type=int,default=4097)
    parser.add_argument('--physical-angular-nodes',type=int,default=801)
    parser.add_argument('--radii',type=float,nargs='+',default=[16.,256.,4096.,65536.,1e6,1e8])
    args=parser.parse_args()
    if not 0<=args.inverse_even_order<=12 or min(args.angular_nodes,args.physical_angular_nodes)<33 or min(args.radii)<=1:
        parser.error('Require inverse-even order0..12, at least33angles, and radii>1')
    run(args)
