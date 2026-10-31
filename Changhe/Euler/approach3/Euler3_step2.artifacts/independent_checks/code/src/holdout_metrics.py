"""Registered finite-quadrature momentum diagnostics, with explicit domains."""
import math
import numpy as np

def jvec(a):
    return np.stack((-a[...,1],a[...,0],np.zeros_like(a[...,0])),axis=-1)

def shell_family(core_radius,offset,n_rad):
    if core_radius<=0 or n_rad<2:raise ValueError('positive reference radius and at least two radial nodes required')
    logc=math.log2(core_radius);jlo=math.floor(logc-offset)-5;jhi=math.ceil(logc-offset)+12
    edges=2.**(np.arange(jlo,jhi+1)+offset)
    intervals=[(0.,float(edges[0]))]+[(float(a),float(b)) for a,b in zip(edges[:-1],edges[1:])]
    return [volume_shell(a,b,n_rad,'core_ball' if a==0 else 'dyadic_shell') for a,b in intervals]

def volume_shell(a,b,n_rad,kind):
    if not 0<=a<b:raise ValueError('invalid positive-volume shell')
    t,w=np.polynomial.legendre.leggauss(n_rad);t=(t+1)/2;w=w/2
    # Stable even on very thin far shells. The normalized Jacobian cancels.
    rr=(b*np.cbrt(t) if a==0 else a*np.cbrt(1+t*np.expm1(3*np.log1p((b-a)/a))))
    return {'kind':kind,'inner_radius':a,'outer_radius':b,'reference_radius':math.sqrt(a*b) if a else 0.,'radii':rr,'radial_weights':w}

def rms(values,weights):
    return float(np.sqrt(np.sum(weights*np.sum(np.asarray(values)**2,axis=-1))))

def ratio(numerator,denominator):
    return float(numerator/denominator) if denominator>0 else None

def shell_metrics(shell,directions,angular_weights,U,DU,linear,P,gradP,c,omega):
    radii=np.asarray(shell['radii']);points=radii[:,None,None]*directions[None,:,:]
    weights=np.asarray(shell['radial_weights'])[:,None]*angular_weights[None,:]
    if not np.isclose(weights.sum(),1.,rtol=0,atol=2e-14):raise ValueError('weights must be normalized volume weights')
    terms=[(1-c)*U,c*np.einsum('raij,raj->rai',DU,points),omega*(jvec(U)-np.einsum('raij,raj->rai',DU,jvec(points))),np.einsum('raij,raj->rai',DU,U),gradP]
    nonlinear=terms[3]+terms[4];residual=linear+nonlinear
    tnorm=[rms(t,weights) for t in terms];six_tnorm=tnorm[:2]+[rms(omega*jvec(U),weights),rms(-omega*np.einsum('raij,raj->rai',DU,jvec(points)),weights)]+tnorm[3:];rn=rms(residual,weights);un=rms(U,weights);ln=rms(linear,weights);nn=rms(nonlinear,weights)
    peak=float(np.linalg.norm(residual,axis=-1).max());a=sum(tnorm[:3]);b=sum(tnorm[3:]);total=a+b
    dot=float(np.sum(weights*np.sum(linear*nonlinear,axis=-1)));gram=ln*ln+nn*nn+2*dot
    curl=np.stack((DU[...,2,1]-DU[...,1,2],DU[...,0,2]-DU[...,2,0],DU[...,1,0]-DU[...,0,1]),axis=-1)
    div=np.trace(DU,axis1=-2,axis2=-1);dun=float(np.sqrt(np.sum(weights*np.sum(DU**2,axis=(-2,-1)))));divn=float(np.sqrt(np.sum(weights*div**2)))
    rk=shell['reference_radius'];alpha=(1-c)/c
    return {k:v for k,v in shell.items() if k not in ('radii','radial_weights')} | {
        'radial_nodes':len(radii),'angular_nodes':len(directions),'term_rms':tnorm,'six_term_rms':six_tnorm,'rho_u_six_term':ratio(rn,sum(six_tnorm)),'residual_rms':rn,'U_rms':un,'linear_rms':ln,'nonlinear_rms':nn,'rho_u':ratio(rn,total),'rho_nl':ratio(rn,b),'rho_lin':ratio(rn,a),'rho_sp':max(ratio(rn,a),ratio(rn,b)) if a>0 and b>0 else None,'pi_u':ratio(peak,total),'pi_nl':ratio(peak,b),'peak_factor':ratio(peak,rn),'sigma_u':ratio(rn,tnorm[0]),'weighted_absolute_residual':float((1+rk)**(2*alpha+1)*rn),'weighted_linear_denominator':float((1+rk)**alpha*a),'weighted_nonlinear_denominator':float((1+rk)**(2*alpha+1)*b),'weighted_single_term_denominator':float((1+rk)**alpha*tnorm[0]),'absolute_r_alpha_residual':float(rk**alpha*rn),'absolute_r_2alpha_plus1_residual':float(rk**(2*alpha+1)*rn),'gram_nonlinear_to_linear_ratio':ratio(nn,ln),'gram_inner_product':dot,'gram_cosine':ratio(dot,ln*nn),'gram_identity_absolute_defect':abs(rn*rn-gram),'nonlinear_cancellation_ratio':ratio(nn,b),'U_max':float(np.linalg.norm(U,axis=-1).max()),'Omega_max':float(np.linalg.norm(curl,axis=-1).max()),'divergence_rms':divn,'rho_div':ratio(divn,dun),'pressure_rms':float(np.sqrt(np.sum(weights*P**2))),'pressure_gradient_rms':tnorm[4],'direct_vs_stable_linear_rms':rms(sum(terms[:3])-linear,weights)}

def family_summary(rows):
    fields=['rho_u','rho_nl','rho_lin','rho_sp','sigma_u','pi_u','pi_nl','weighted_absolute_residual','rho_div','rho_u_six_term','absolute_r_alpha_residual','absolute_r_2alpha_plus1_residual']
    denominators=['weighted_linear_denominator','weighted_nonlinear_denominator','weighted_single_term_denominator']
    totalmax=max(sum(r['term_rms']) for r in rows)
    for i,row in enumerate(rows):
        flags=[]
        if sum(row['term_rms'])<1e-14*totalmax:flags.append('total_term_sum_small')
        if 0<i<len(rows)-1 and sum(row['term_rms'])<1e-3*min(sum(rows[i-1]['term_rms']),sum(rows[i+1]['term_rms'])):flags.append('total_term_sum_small_both_neighbors')
        for key in denominators:
            value=row[key]
            if value<1e-14*max(r[key] for r in rows):flags.append(key+'_small_global')
            if 0<i<len(rows)-1 and value<1e-3*min(rows[i-1][key],rows[i+1][key]):flags.append(key+'_small_both_neighbors')
        row['denominator_flags']=flags
        row['peak_factor_exceeds_30']=row['peak_factor'] is not None and row['peak_factor']>30
    summary={k+'_max':max((r[k] for r in rows if r[k] is not None),default=None) for k in fields}
    summary['rho_u_equal_shell_rms']=float(np.sqrt(np.mean([r['rho_u']**2 for r in rows]))) if all(r['rho_u'] is not None for r in rows) else None
    summary['flagged_shells']=[i for i,r in enumerate(rows) if r['denominator_flags']]
    summary['all_denominators_positive']=all(r[k] is not None for r in rows for k in ['rho_u','rho_nl','rho_lin','sigma_u'])
    return summary
