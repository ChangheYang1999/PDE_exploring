"""Adaptive radial cross-check of a previously published coefficient snapshot."""
import argparse,hashlib,json,time
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.optimize import brentq
from modal_quad import CoefficientModes,at_radius,velocity
from profile_data import CoefficientProfile
from residuals import cartesian,cartesian_from_factors,summary


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--tag',default='published_gauss_N112')
    ap.add_argument('--bracket',nargs=2,type=float,default=[18,20.5])
    args=ap.parse_args();tag=args.tag
    source=Path('data/control_snapshots/'+tag+'.npz')
    p=CoefficientProfile(source);m=CoefficientModes(p)
    reference=json.loads(Path('runs/'+tag+'_audit.json').read_text())
    points=np.asarray(reference['points']);duffy=np.asarray(reference['rows'][-1]['fields']['U'])
    dest=Path('runs/'+tag+'_modal.json');start=time.monotonic()
    report=dict(timestamp_start=datetime.now(timezone.utc).isoformat(),source=str(source),
                source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),metadata=p.metadata(),
                method='Adaptive Gauss-Kronrod radial Green integrals and exact finite sine modes; independent of fitting code',
                warning='Adaptive quadrature error estimates and root brackets are not rigorous certificates; first-root uniqueness unproved',
                bracket=args.bracket,points=points.tolist(),rows=[])
    def save():
        report['last_update']=datetime.now(timezone.utc).isoformat()
        report['elapsed_seconds']=time.monotonic()-start
        dest.write_text(json.dumps(report,indent=2)+'\n')
    save()
    for tol in [1e-7,1e-10,1e-12]:
        history=[]
        def field(x):
            data=at_radius(m,x,p.tail_power,tol)
            w=p.beta*x-data['sigma']
            history.append(dict(x=x,w=w,info=data['info']))
            return w
        root,info=brentq(field,*args.bracket,xtol=1e-11,rtol=1e-14,full_output=True)
        rv=at_radius(m,root,p.tail_power,tol);mu=p.beta-rv['sigma_prime']
        u,uvinfo=velocity(m,points,p.tail_power,tol)
        field_cache=lambda points_requested:u
        # cartesian calls u exactly once at this same fixed point array.
        raw=cartesian(p.theta,p.omega,p.beta,points,u=field_cache,elliptic=False)
        fac=cartesian_from_factors(p.a,p.G,p.beta,points,u=field_cache)
        row=dict(tolerance=tol,root=root,mu=mu,mu_defect=mu-p.beta-2,
                 f_at_root=float(root*root*p.a([[root,0]])[0]),root_quadrature=rv['info'],
                 root_calls=history,root_converged=bool(info.converged),
                 U=u.tolist(),velocity_quadrature=uvinfo,
                 max_velocity_difference_from_duffy=float(np.max(abs(u-duffy))),
                 raw_summary=summary(raw),factored_summary=summary(fac),
                 raw_fields={k:v.tolist() for k,v in raw.items()},
                 factored_fields={k:v.tolist() for k,v in fac.items()})
        report['rows'].append(row);save()
        print(json.dumps({k:row[k] for k in ['tolerance','root','mu','mu_defect','f_at_root','max_velocity_difference_from_duffy']}),flush=True)
    report['timestamp_end']=datetime.now(timezone.utc).isoformat();save()

if __name__=='__main__':main()
