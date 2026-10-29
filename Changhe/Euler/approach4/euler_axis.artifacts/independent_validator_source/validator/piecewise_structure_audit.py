#!/usr/bin/env python3
"""Source jets, pole signs and finite-part mass from saved coefficients only."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from numpy.polynomial import Legendre
from scipy.special import roots_legendre
from piecewise_loading import load_piecewise
from piecewise_adapter import spherical_jets
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent

def run(candidate,output):
    start=time.perf_counter();cpu=time.process_time()
    files=[Path(candidate).resolve(),Path(__file__).resolve()]
    files += [ROOT/'src'/name for name in ['piecewise_loading.py','piecewise_adapter.py','piecewise_jacobi.py','independent_fields.py']]
    sources={str(p):sha256(p) for p in files}
    working=load_piecewise(candidate);field,gauge=working.reporting_gauge()
    cl=field.c_l;delta=1+cl;alpha=field.alpha
    z0=float(field.metadata.get('z0',0.))*field.dilation
    jets=field.jets(np.array([0.]),np.array([z0]),3)
    ph={f'{j},{k}':float(v[0]) for (j,k),v in jets['phi'].items()}
    qj={f'{j},{k}':float(v[0]) for (j,k),v in jets['q'].items()}
    K=qj['0,0'];a2=ph['0,2'];a3=ph['0,3'];b1=ph['1,0'];d=ph['1,1']
    source=dict(z0=z0,q=K,phi_derivatives=ph,q_derivatives=qj,
        stagnation_defect=cl*z0+2*ph['0,0'],strain_defect=ph['0,1']-.5,
        q_z_defect=qj['0,1']-2*K*a2/delta,
        phi_s_defect=b1+(1/8+K*K/(2*delta**2))*a2,
        q_zz_defect=qj['0,2']-2*K*a2*a2/delta**2-K*a3/delta,
        general_cubic_defect=d+a3*(1+K*K/delta**2)/8+3*K*K*a2*a2/(4*delta**3),
        parity_restricted_cubic_defect=d+a3*(1+K*K/delta**2)/8,
        omitted_quadratic_term=3*K*K*a2*a2/(4*delta**3),
        scope='Necessary exact-source identities evaluated at the exported source coordinate; no parity assumed.')
    e=field.elements[-1];rm=float(e['Rlo']);moments=[]
    for j,p in enumerate(field.radial_keys[2,'phi']):
        coeff=field.matrices[2,'phi'][:,j]*rm**p*field.dilation**(p+1)
        mean=float(coeff[0]-(coeff[2]/5 if len(coeff)>2 else 0))
        moments.append(dict(power=float(p),legendre_coefficients=coeff.tolist(),five_dimensional_mean=mean))
    monopole=sum(row['five_dimensional_mean'] for row in moments if abs(row['power']-3)<1e-12)
    sphere4=8*np.pi*np.pi/3;mu,w=roots_legendre(96);weights=.75*w*(1-mu*mu)
    interfaces=[]
    for i,R in enumerate(field.interfaces):
        inside=spherical_jets(field,np.full_like(mu,R),mu,1,element=i)['phi'][1,0]
        outside=spherical_jets(field,np.full_like(mu,R),mu,1,element=i+1)['phi'][1,0]
        meanjump=float(np.sum(weights*(outside-inside)))
        interfaces.append(dict(radius=float(R),mean_phi_R_jump=meanjump,
            bulk_mass_contribution=float(sphere4*R**4*meanjump)))
    # Work in the native Legendre basis to avoid high-degree monomial cancellation.
    ap=int(np.argmin(np.abs(np.asarray(field.radial_keys[2,'phi'])-alpha)))
    bp=int(np.argmin(np.abs(np.asarray(field.radial_keys[2,'q'])-(alpha+1))))
    assert abs(field.radial_keys[2,'phi'][ap]-alpha)<1e-12
    assert abs(field.radial_keys[2,'q'][bp]-(alpha+1))<1e-12
    A=Legendre(field.matrices[2,'phi'][:,ap]*rm**alpha*field.dilation**(alpha+1))
    B=Legendre(field.matrices[2,'q'][:,bp]*rm**(alpha+1)*field.dilation**(alpha+1))
    grid=np.linspace(-1,1,8193);bg=B(grid)
    imin=int(np.argmin(bg));imax=int(np.argmax(bg))
    E=lambda m:alpha*(3-alpha)*A(m)-(1-m*m)*A.deriv(2)(m)+4*m*A.deriv()(m)
    tail=dict(alpha=alpha,B_sample_min=float(bg[imin]),B_sample_min_mu=float(grid[imin]),
        B_sample_max=float(bg[imax]),B_sample_max_mu=float(grid[imax]),
        B_at_north_pole=float(B(1)),B_at_south_pole=float(B(-1)),
        eta_leading_north_pole=float(E(1)),eta_leading_south_pole=float(E(-1)),
        angular_samples=len(grid),scope='Sampled B extrema, not certified global extrema. Sign restrictions require the asserted T1 global source basin.')
    finitepart=dict(phi_power_moments=moments,phi_Rminus3_monopole=float(monopole),
        distributional_finite_part_mass=float(3*sphere4*monopole),interfaces=interfaces,
        bulk_finite_part_mass=float(3*sphere4*monopole+sum(x['bulk_mass_contribution'] for x in interfaces)),
        normalization='Reporting gauge integral_S2 |F|^2=1. No division by the divergent whole-space absolute eta mass.',
        second_correction_power=3*alpha+2,
        second_correction_distinct_present=any(abs(p-(3*alpha+2))<1e-12 for p in field.radial_keys[2,'phi']),
        scope='Finite-part coefficient readout, with separate interface correction for the piecewise classical Laplacian. Nonzero jumps are regularity defects.')
    verify_source_identity(ROOT,sources)
    record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),source_hashes=sources,
        elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,
        c_l=cl,gauge=gauge,source=source,tail=tail,finite_part=finitepart,
        accepted_as_A=False,scope='Independent structural diagnostics; no full candidate acceptance decision.')
    Path(output).parent.mkdir(parents=True,exist_ok=True)
    atomic_json(output,record)
    print(json.dumps(dict(output=str(output),c_l=cl,source=source,tail=tail,finite_part_mass=finitepart['bulk_finite_part_mass']),indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('candidate',type=Path);parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args();run(args.candidate,args.output)
