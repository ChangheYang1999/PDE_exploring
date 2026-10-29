#!/usr/bin/env python3
"""Common-grid differences after the unique leading-tail reporting dilation."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from scipy.special import roots_legendre
from fast_native_field import FastNativeField
from cartesian_second_derivatives import velocity_hessian
from independent_identities import vorticity_and_jacobian
from independent_geometry import shell_quadrature
from independent_farfield import angular_data,evaluate_vector
from independent_artifacts import atomic_json,sha256
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
CONFIG={
 'L1':'T1_ladder_L1_20261028T232238Z',
 'L2':'T1_ladder_L2_20261028T235434Z',
 'L3sep':'T1_ladder_L3sep_20261029T013412.291018Z',
 'reflection_L0':'T1_reflection_L0_expanded_20261029T0136Z',
}
PAIRS=[('L1','L2'),('L2','L3sep'),('L1','reflection_L0')]

def norm_points(value):return np.sqrt(np.sum(value.reshape((len(value),-1))**2,axis=1))
def compare(a,b,weights,xyz):
    an,bn,dn=norm_points(a),norm_points(b),norm_points(a-b);total=float(np.sum(weights))
    na=float(np.sqrt(np.dot(weights,an*an)/total));nb=float(np.sqrt(np.dot(weights,bn*bn)/total));nd=float(np.sqrt(np.dot(weights,dn*dn)/total))
    k=int(np.argmax(dn));den=max(na,nb)
    return {'rms_a':na,'rms_b':nb,'difference_rms':nd,'relative_difference_rms':nd/den if den else 0.,
            'sampled_sup_a':float(np.max(an)),'sampled_sup_b':float(np.max(bn)),
            'sampled_sup_difference':float(dn[k]),'difference_sup_location':xyz[k].tolist()}
def values(field,xyz):
    r=xyz[:,0];z=xyz[:,2];j=field.jets(r*r,z,3)
    U,J=field.cartesian(xyz,True);O,JO=vorticity_and_jacobian(field,xyz);H=velocity_hessian(field,xyz)
    p=j['phi'];q=j['q'];eta=-8*p[1,0]-4*r*r*p[2,0]-p[0,2]
    return {'U':U,'DU':J,'D2U':H,'Omega':O,'DOmega':JO,'q':q[0,0],'eta':eta}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True,type=Path);a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT)or out.exists():raise ValueError('fresh output in lane required')
    out.mkdir(parents=True);start=time.perf_counter();cpu=time.process_time()
    paths=[Path(__file__),BASE/'fast_native_field.py',BASE/'cartesian_second_derivatives.py',ROOT/'research/gauge_aligned_comparison/PROOF.md']
    paths += [BASE/'src'/n for n in ['piecewise_adapter.py','piecewise_jacobi.py','piecewise_precision.py','independent_fields.py','independent_identities.py','independent_geometry.py','independent_farfield.py']]
    paths += [BASE/'external_exports'/v/'coeffs.npz'for v in CONFIG.values()]
    geom=BASE/'results/driver_t1_ladder_l1/registered/geometry.json';paths.append(geom)
    hashes={str(p.relative_to(ROOT)):sha256(p)for p in paths}
    aeff=json.loads(geom.read_text())['core']['a_eff'];fields={};gauges={}
    for name,directory in CONFIG.items():fields[name],gauges[name]=FastNativeField.load(BASE/'external_exports'/directory/'coeffs.npz').reporting_gauge()
    record={'created_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashes,'gauges':gauges,'reference_a_eff':aeff,
            'pairs':PAIRS,'rows':[],'tail':[],'scope':'Specified saved states, not controlled fixed-state refinement. Common reporting coordinates; no source translations or independent core rescalings. Piecewise classical derivatives, not distributional derivatives. Supremums are sampled lower bounds.'}
    def checkpoint(phase):
        for name,h in hashes.items():
            if sha256(ROOT/name)!=h:raise RuntimeError('Input changed: '+name)
        record.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(out/'summary.json',record);print(phase,flush=True)
    # The union of all normalized interfaces prevents quadrature from straddling a jump.
    interfaces=sorted(set(float(v)for f in fields.values()for v in f.interfaces))
    bands=[('origin',0.,aeff/64)]+[(f'shell_{k}',aeff*2**k,aeff*2**(k+1))for k in range(-6,12)]
    for level,nr,na in [('medium',24,128),('fine',32,160)]:
        for band,lo,hi in bands:
            edges=[lo]+[v for v in interfaces if lo<v<hi]+[hi];grids=[shell_quadrature(x,y,nradial=nr,nangle=na)for x,y in zip(edges,edges[1:])]
            r=np.concatenate([g['r'].ravel()for g in grids]);z=np.concatenate([g['z'].ravel()for g in grids]);weights=np.concatenate([g['weights'].ravel()for g in grids]);xyz=np.stack((r,np.zeros_like(r),z),axis=-1)
            data={name:values(f,xyz)for name,f in fields.items()}
            for left,right in PAIRS:
                record['rows'].append({'level':level,'band':band,'range': [lo,hi],'points':len(r),'nradial_per_piece':nr,'nangle':na,'interface_splits':edges,'pair':[left,right],'measure':'physical volume','fields':{name:compare(data[left][name],data[right][name],weights,xyz)for name in data[left]}})
            checkpoint(level+'_'+band)
    R=np.r_[0.,aeff*np.geomspace(1/128,4096,96)];z=np.r_[R,-R[1:]];xyz=np.stack((np.zeros_like(z),np.zeros_like(z),z),axis=-1)
    data={name:values(f,xyz)for name,f in fields.items()};weights=np.ones(len(z))
    for left,right in PAIRS:
        record['rows'].append({'level':'axis','band':'axis','points':len(z),'pair':[left,right],'measure':'equal-weight finite point sample, not volume','fields':{name:compare(data[left][name],data[right][name],weights,xyz)for name in data[left]}})
    for na in [64,96]:
        mu,w=roots_legendre(na);w=2*np.pi*w;xyz=np.stack((np.sqrt(1-mu*mu),np.zeros_like(mu),mu),axis=-1);tail={}
        for name,f in fields.items():
            A,B=f.leading_polynomials();tail[name]=evaluate_vector(angular_data(f.alpha,A.coef,B.coef),mu,'F')
        for left,right in PAIRS:
            record['tail'].append({'nangle':na,'pair':[left,right],'comparison':compare(tail[left],tail[right],w,xyz)})
    checkpoint('complete')
if __name__=='__main__':main()
