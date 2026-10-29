#!/usr/bin/env python3
"""Independent interface and exported-value audit; no solver code is imported."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time
import numpy as np
from piecewise_loading import load_piecewise
from scipy.special import roots_legendre
from piecewise_adapter import PiecewiseField,spherical_jets

def audit(field,nangle=129):
    # Endpoints plus a shifted dense angular grid, independently of collocation.
    mu=np.unique(np.r_[-1.,1.,roots_legendre(nangle)[0],np.cos(np.linspace(0,np.pi,nangle))])
    rows=[];physical=[]
    for i,R in enumerate(field.interfaces):
        left=spherical_jets(field,R,mu,3,element=i)
        right=spherical_jets(field,R,mu,3,element=i+1)
        for key in ['phi','q']:
            for (dR,dm),a in left[key].items():
                if dR+dm>(3 if key=='phi' else 2):continue
                b=right[key][dR,dm];scale=float(max(np.max(abs(a)),np.max(abs(b))))
                jump=float(np.max(abs(b-a)));relative=jump/scale if scale>0 else 0.
                j=int(np.argmax(abs(b-a)))
                rows.append(dict(interface=float(R),field=key,d_R=dR,d_mu=dm,max_abs_jump=jump,local_derivative_scale=scale,
                                 relative_jump=relative,mu_at_worst=float(mu[j]),A8_pass=relative<=1e-6,B4_pass=relative<=1e-3))
        r=R*np.sqrt(1-mu*mu);z=R*mu;traces=[]
        for side in [i,i+1]:
            j=field.jets(r*r,z,3,element=side);p=j['phi'];q=j['q']
            U=np.stack([-r*p[0,1],r*q[0,0],2*p[0,0]+2*r*r*p[1,0]],axis=-1)
            Un=U[:,0]*np.sqrt(1-mu*mu)+U[:,2]*mu
            traces.append((U,Un))
        du=traces[1][0]-traces[0][0];dn=traces[1][1]-traces[0][1]
        scale=float(max(np.max(np.linalg.norm(t[0],axis=-1)) for t in traces))
        physical.append(dict(interface=float(R),max_velocity_jump=float(np.max(np.linalg.norm(du,axis=-1))),
                             relative_velocity_jump=float(np.max(np.linalg.norm(du,axis=-1))/scale),
                             max_normal_velocity_jump=float(np.max(abs(dn))),velocity_scale=scale))
    return dict(angular_count=len(mu),derivative_jumps=rows,physical_jumps=physical,
                maximum_relative_derivative_jump=max(x['relative_jump'] for x in rows),
                all_A8_interface_checks_pass=all(x['A8_pass'] for x in rows),all_B4_interface_checks_pass=all(x['B4_pass'] for x in rows),
                pressure_caveat='A volume-only reconstruction of tr(DU^2) omits distributional interface terms when velocity jumps. Such a reconstruction is diagnostic only until interface regularity is established.')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('coefficients');ap.add_argument('--output',required=True);args=ap.parse_args()
    started=time.monotonic();path=Path(args.coefficients);field=load_piecewise(path);out=audit(field)
    _,out['gauge']=field.reporting_gauge()
    sample=path.parent/'samples.npz'
    if sample.exists():
        with np.load(sample,allow_pickle=False) as a:
            d=field.cylindrical(a['r'],a['z']);out['sample_count']=a['r'].size
            out['sample_comparison']={k:dict(max_abs_error=float(np.max(abs(v-a[k]))),max_abs_reference=float(np.max(abs(a[k]))))
              for k,v in [('phi',d['phi'][0,0]),('q',d['q'][0,0]),('Ur',d['U'][:,0]),('Utheta',d['U'][:,1]),('Uz',d['U'][:,2]),('eta',d['eta'])]}
    out.update(recorded_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started,
               coefficient_path=str(path.resolve()),coefficient_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
               source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).parent/'src/piecewise_adapter.py',Path(__file__).parent/'src/piecewise_jacobi.py',Path(__file__).parent/'src/piecewise_loading.py']},
               candidate_status='Export explicitly labels this an unsuccessful pilot, not a candidate solution.')
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:out[k] for k in ['recorded_utc','elapsed_seconds','maximum_relative_derivative_jump','all_A8_interface_checks_pass','all_B4_interface_checks_pass','physical_jumps']}))
if __name__=='__main__':main()
