"""Independent finite-basis far coefficients and original PDE compatibility.

Decoder math is documented in research/asymptotics/coefficient_audit/PROOF.md.
No fitting routines are read or imported. Endpoint sums use long double.
"""
import argparse,json,hashlib,time
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from profile_data import CoefficientProfile,snapshot


def radial_endpoints(obj,c,sigma):
    d=1/obj.beta
    c=np.asarray(c,dtype=np.longdouble)
    n=np.arange(c.shape[1],dtype=np.longdouble)
    if obj.mapname=='xi':
        z=((np.longdouble(2)*obj.length**2)**sigma)*np.sum(c,axis=1)
        return np.array(z,float),np.zeros(c.shape[0])
    if obj.beta_map != obj.beta:
        raise ValueError('Different beta_map requires a different asymptotic expansion')
    signs=(-np.ones(len(n),dtype=np.longdouble))**np.arange(len(n))
    scale=np.longdouble(obj.length)**(2*sigma)
    z=scale*(c@signs)
    f=2*scale*np.longdouble(obj.length)**d*(c@(-signs*n*n))
    return np.array(z,float),np.array(f,float)


def angular(c,phi,temperature=False):
    phi=np.asarray(phi); l=np.arange(len(c)); k=2*l
    z=np.cos(phi[:,None]*k)@c
    dz=-np.sin(phi[:,None]*k)@(k*c)
    co,si=np.cos(phi),np.sin(phi)
    if temperature:
        p=co*co*si; dp=co*(co*co-2*si*si)
    else:p=co*si;dp=co*co-si*si
    return p*z,dp*z+p*dz


def stream_modes(b):
    """Exact finite trigonometric product, including negative frequency sign."""
    m=np.zeros(len(b)+1)
    for l,v in enumerate(b):
        m[l+1]+=v/4
        if 1-l>0:m[1-l]+=v/4
        elif 1-l<0:m[l-1]-=v/4
    return m[1:]


def evaluate(obj,phi):
    d=1/obj.beta;q=1-2*d;alpha=2-d
    if obj.beta<2:raise ValueError('This coefficient audit is scoped to beta>=2')
    if abs(obj.sigma_a-1-d)>1e-12 or abs(obj.sigma_g-1-d/2)>1e-12:
        raise ValueError('Nonstandard envelope powers need separately derived matching')
    a0,a1=radial_endpoints(obj,obj.ca,obj.sigma_a)
    b0,b1=radial_endpoints(obj,obj.cg,obj.sigma_g)
    T0,T0p=angular(a0,phi,True);T1,_=angular(a1,phi,True)
    O0,O0p=angular(b0,phi);O1,_=angular(b1,phi)
    m=2*np.arange(1,len(b0)+1);om=stream_modes(b0);sm=om/(m*m-alpha*alpha)
    S=np.sin(phi[:,None]*m)@sm;Sp=np.cos(phi[:,None]*m)@(m*sm)
    Vr=-Sp;Vp=alpha*S
    predicted_T1=q*Vr*T0+Vp*T0p
    predicted_O1=-d*Vr*O0+Vp*O0p-q*np.cos(phi)*T0+np.sin(phi)*T0p
    return dict(A0=a0,A1=a1,B0=b0,B1=b1,omega_sine_modes=om,stream_sine_modes=sm,
                T0=T0,T1=T1,O0=O0,O1=O1,T0prime=T0p,O0prime=O0p,
                Vr=Vr,Vphi=Vp,predicted_T1=predicted_T1,predicted_O1=predicted_O1,
                D_T=predicted_T1-T1,D_O=predicted_O1-O1)


def audit(source,tag):
    obj=CoefficientProfile(source);phi=np.linspace(0,np.pi/2,4097)
    vals=evaluate(obj,phi)
    summaries={}
    for k in ['T0','T1','O0','O1','D_T','D_O','predicted_T1','predicted_O1']:
        v=vals[k];i=int(np.argmax(np.abs(v)))
        summaries[k]=dict(max_abs=float(abs(v[i])),argmax_phi=float(phi[i]),value=float(v[i]))
    # Compare only a few actual values at very large radii to their leading
    # and next-order expansion. No numerical inverse is used in this check.
    pp=np.array([.19,.53,.97,1.33]);v=evaluate(obj,pp);d=1/obj.beta
    # These decoder spot checks use the literal stored envelope powers.
    # A tiny power mismatch eventually dominates a first-correction limit.
    q_stored=3-2*obj.sigma_a
    omega_power_stored=2-2*obj.sigma_g
    rows=[]
    for r in [1e4,1e8,1e12,1e16,1e20]:
        p=r*np.column_stack([np.cos(pp),np.sin(pp)])
        th=obj.theta(p)/r**q_stored;om=obj.omega(p)/r**omega_power_stored
        tscaled=(th-v['T0'])*r**d;oscaled=(om-v['O0'])*r**d
        rows.append(dict(radius=r,temperature_next=tscaled.tolist(),omega_next=oscaled.tolist(),
                         max_T1_disagreement=float(np.max(np.abs(tscaled-v['T1']))),
                         max_O1_disagreement=float(np.max(np.abs(oscaled-v['O1'])))))
    data=dict(timestamp=datetime.now(timezone.utc).isoformat(),source=str(source),
              source_sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),metadata=obj.metadata(),
              phi=phi.tolist(),summary=summaries,arrays={k:v.tolist() for k,v in vals.items()},
              asymptotic_spot_angles=pp.tolist(),asymptotic_spots=rows,
              asymptotic_spot_powers=dict(theta=q_stored,omega=omega_power_stored),
              residual_powers=dict(theta=1-3/obj.beta,omega=-2/obj.beta),
              stored_power_roundoff=dict(theta_linear_coefficient=obj.beta*(3-2*obj.sigma_a)-(obj.beta-2),
                                         omega_linear_coefficient=obj.beta*(2-2*obj.sigma_g)+1),
              asymptotic_interpretation=(
                  'The t-map parameter must equal beta exactly as stored. Decoder spot checks use '
                  'literal stored envelope powers. The displayed PDE correction matching and residual '
                  'powers assume the intended exact envelopes sigma_a=1+1/beta, sigma_G=1+1/(2beta). '
                  'Endpoint amplitudes are evaluated using stored powers; their rounding and the '
                  'recorded leading linear mismatch prevent an exact-certificate interpretation.'),
              warning='Sampled angular maxima and floating-point coefficient sums, not interval bounds')
    Path('runs/'+tag+'_far_coefficients.json').write_text(json.dumps(data,indent=2)+'\n')
    return dict(tag=tag,metadata=obj.metadata(),summary=summaries,
                coefficient_check_at_largest_radius=rows[-1])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('--tag',required=True);args=ap.parse_args()
    print(json.dumps(audit(args.source,args.tag),indent=2))

if __name__=='__main__':main()
