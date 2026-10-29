#!/usr/bin/env python3
"""Frozen-potential swirl transport on core, matching, far and axis samples."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from scipy.special import roots_legendre
from piecewise_loading import load_piecewise
from piecewise_source_transport import source_transport
from independent_registered_metrics import metric,rms
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent


def points_for_audit(field,aeff):
    sets=[];points=[];weights=[];x,wx=roots_legendre(3);mu,wm=roots_legendre(8)
    intervals=[(f'shell_{k}',aeff*2.**k,aeff*2.**(k+1)) for k in [-4,-1,0,1,3,5]]
    intervals += [(f'interface_{i}',.85*float(a),1.15*float(a)) for i,a in enumerate(field.interfaces)]
    for name,lo,hi in intervals:
        # Split interface windows, avoiding nodes exactly on an interface.
        edges=[lo,*[float(a) for a in field.interfaces if lo<a<hi],hi]
        first=len(points)
        for a,b in zip(edges[:-1],edges[1:]):
            R=(a+b)/2+(b-a)*x/2;wr=(b-a)*wx/2
            for radius,w in zip(R,wr):
                for m,v in zip(mu,wm):
                    points.append([radius*np.sqrt(1-m*m),radius*m]);weights.append(2*np.pi*radius*radius*w*v)
        sets.append(dict(name=name,first=first,last=len(points),measure='Physical volume Gauss quadrature; diagnostic resolution 3 radial by 8 angular per piece.',lower=lo,upper=hi))
    for sign in [-1,1]:
        first=len(points)
        for radius in aeff*np.array([2**-4,2**-2,1.,4.,16.,64.]):
            for sine in [0.,.01]:
                points.append([radius*sine,sign*radius*np.sqrt(1-sine*sine)]);weights.append(1.)
        sets.append(dict(name=f'axis_collar_{sign}',first=first,last=len(points),measure='Equal diagnostic point weights; not a physical volume metric.'))
    return np.asarray(points),np.asarray(weights),sets


def source_point(field):
    z=float(field.metadata.get('z0',0.))*field.dilation
    for _ in range(30):
        p=field.phi.jet(0.,z,1);f=field.c_l*z+2*p[0,0];df=field.c_l+2*p[0,1]
        if abs(df)<1e-10:raise RuntimeError('nonsimple axial source')
        dz=float(f/df);z-=dz
        if abs(dz)<1e-13*max(field.phi.length,1.):break
    p=field.phi.jet(0.,z,1);Wz=float(field.c_l*z+2*p[0,0]);a0=float(1-2*p[0,1])
    eig=[float(field.c_l-p[0,1]),float(field.c_l+2*p[0,1])]
    if abs(Wz)>1e-10 or min(eig)<=0:raise RuntimeError('exported source did not give a numerical hyperbolic source')
    return dict(r=0.,z=z,transport_defect=Wz,a0=a0,meridional_eigenvalues=eig,
                saved_q=float(field.q.evaluate(0.,z)),source_location_certified=False,
                scope='Newton solution near the declared source, not an interval root certificate. Nonzero a0 is retained in the cutoff and compensated diagnostics.')


def compare(field,points,weights,sets,row,source):
    r,z=points.T;d=field.cylindrical(r,z,3);c=field.c_l;U=d['U'];q0=d['q'][0,0];q0r=2*r*d['q'][1,0];q0z=d['q'][0,1]
    eta=d['eta'];er=2*r*d['eta_s'];ez=d['eta_z'];q=np.array(row['q']);grad=np.array(row['gradient_q']);qr,qz=grad.T
    a=1+2*d['ur_over_r'];Wr=c*r+U[:,0];Wz=c*z+U[:,2]
    qres=a*q+Wr*qr+Wz*qz;pred=np.array(row['terminal_a'])*q
    compensation=np.exp(source['a0']*row['cutoff']);qc=compensation*q;gqc=compensation*grad
    def diagnostics(q,qr,qz,sel):
        w=weights[sel];qt=[q,c*r*qr,c*z*qz,U[:,0]*qr,U[:,2]*qz,2*d['ur_over_r']*q]
        et=[(1+c)*eta,c*r*er,c*z*ez,U[:,0]*er,U[:,2]*ez,-2*q*qz]
        return dict(q=metric(sum(qt)[sel],q[sel],sum(qt[3:])[sel],[v[sel] for v in qt],w),
                    eta=metric(sum(et)[sel],et[0][sel],sum(et[3:])[sel],[v[sel] for v in et],w))
    records=[]
    for region in sets:
        sel=slice(region['first'],region['last']);w=weights[sel];saved_norm=rms(q0[sel],w);transport_norm=rms(q[sel],w)
        difference=rms((q-q0)[sel],w);terminal=np.array(row['terminal_points'])[sel]-np.array([0.,source['z']])
        records.append(dict(**region,saved_q_rms=saved_norm,transported_q_rms=transport_norm,q_difference_rms=difference,
                            q_relative_difference=difference/transport_norm if transport_norm else None,
                            q_relative_difference_larger_scale=difference/max(saved_norm,transport_norm) if max(saved_norm,transport_norm)>0 else None,
                            q_compensated_relative_difference=rms((qc-q0)[sel],w)/rms(qc[sel],w) if rms(qc[sel],w)>0 else None,
                            cutoff_identity_max_error=float(np.max(np.abs((qres-pred)[sel]))),
                            terminal_distance_max=float(np.max(np.linalg.norm(terminal,axis=1))),
                            saved=diagnostics(q0,q0r,q0z,sel),transported=diagnostics(q,qr,qz,sel),
                            compensated=diagnostics(qc,gqc[:,0],gqc[:,1],sel)))
    return dict(cutoff=row['cutoff'],compensation_factor=float(compensation),sets=records,
                maximum_cutoff_identity_error=float(np.max(np.abs(qres-pred))),
                compensated_equation_scope='Compensation removes the a0 cutoff factor only. Its limiting q residual is a0*q if a0 is nonzero; it is not a homogeneous transport solution.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--geometry',required=True,type=Path);ap.add_argument('--output',required=True,type=Path)
    ap.add_argument('--K',type=float,default=3.5);args=ap.parse_args();outpath=args.output.resolve()
    if not outpath.is_relative_to(ROOT.parent):raise ValueError('outside lane')
    if outpath.exists():raise FileExistsError('retain previous audit')
    start=time.perf_counter();cpu=time.process_time();working=load_piecewise(args.candidate);field,gauge=working.reporting_gauge()
    geo=json.loads(args.geometry.read_text());aeff=geo['core']['a_eff']
    if abs(gauge['dilation_L']/geo['gauge']['dilation_L']-1)>1e-12:raise ValueError('different geometry gauge')
    points,weights,sets=points_for_audit(field,aeff);source=source_point(field)
    files=[Path(__file__),*sorted((ROOT/'src').glob('piecewise_*.py')),*sorted((ROOT/'src').glob('independent_*.py'))]
    hashes={str(p.relative_to(ROOT)):sha256(p) for p in files}
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),candidate_sha256=sha256(args.candidate),geometry_sha256=sha256(args.geometry),
                source_sha256=hashes,c_l=field.c_l,gauge=gauge,a_eff=aeff,source=source,K=args.K,
                points=points.tolist(),weights=weights.tolist(),sets=sets,levels=[],accepted_as_A=False,
                scope='Independent phi-only finite-cutoff transport. Coarse diagnostic shells, not the registered acceptance grid. Source compatibility, cutoff, quadrature and integration error remain explicit.')
    def save(phase):
        verify_source_identity(ROOT,hashes)
        if sha256(args.candidate)!=result['candidate_sha256'] or sha256(args.geometry)!=result['geometry_sha256']:raise RuntimeError('inputs changed')
        result.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(outpath,result);print(phase,result['elapsed_seconds'],flush=True)
    save('source_and_grid')
    for tol in [2e-8,2e-10]:
        level=dict(rtol=tol,completed_cutoffs=[]);result['levels'].append(level)
        def callback(row,progress):
            level['completed_cutoffs'].append(dict(transport=row,comparison=compare(field,points,weights,sets,row,source),progress=progress))
            save(f'tol_{tol}_cutoff_{row["cutoff"]}')
        transport=source_transport(field,points,args.K,cutoffs=[16.,32.,48.],rtol=tol,atol=tol*.01,max_step=.25,callback=callback)
        level['summary']={k:v for k,v in transport.items() if k not in ['points','rows']};save(f'tol_{tol}_finished')
        if not transport['success']:break
    save('complete')
if __name__=='__main__':main()
