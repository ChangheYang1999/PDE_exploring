#!/usr/bin/env python3
"""Independent direct origin moments and targeted origin-collar pressure orders."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from scipy.special import roots_legendre,roots_jacobi
from fast_native_field import FastNativeField
load_piecewise = FastNativeField.load
from piecewise_pressure import InterfaceGreenPoisson
from independent_geometry import shell_quadrature
from independent_registered_metrics import evaluate_set
from independent_artifacts import sha256,atomic_json
ROOT=Path(__file__).resolve().parent

def direct_moments(source,alpha,interfaces=(),nr=64,na=96,scale=1.):
    # This integrates raw values and does not form Green radial/angular modes.
    cutoff=max(64*scale,4*max(interfaces,default=scale))
    edges=np.unique(np.r_[0.,scale*2.**np.arange(-5,int(np.ceil(np.log2(cutoff/scale)))+1),interfaces,cutoff])
    edges=edges[edges<=cutoff]
    x,w=roots_legendre(nr);mu,wm=roots_legendre(na)
    R=((edges[:-1,None]+edges[1:,None])/2+(edges[1:,None]-edges[:-1,None])*x/2).ravel()
    wr=((edges[1:,None]-edges[:-1,None])*w/2).ravel()
    S=source(R[:,None]*np.sqrt(1-mu*mu),R[:,None]*mu)
    innerP=.5*np.sum(wr*R*(S@wm));innerG=.5*np.sum(wr*(S@(wm*mu)))
    tails=[]
    for exponent,power,angular in [(2*alpha-1,3,wm),(2*alpha,2,wm*mu)]:
        xj,wj=roots_jacobi(nr,0,exponent);t=(1+xj)/2;wj=wj/2**(exponent+1)
        radius=cutoff/t;vals=source(radius[:,None]*np.sqrt(1-mu*mu),radius[:,None]*mu)@angular
        tails.append(.5*cutoff**(power-1)*np.sum(wj*vals/t**(power+exponent)))
    return dict(P=float(innerP+tails[0]),gradient_z=float(innerG+tails[1]),inner_P=float(innerP),tail_P=float(tails[0]),inner_gradient_z=float(innerG),tail_gradient_z=float(tails[1]),cutoff=cutoff,nradial=nr,nangle=na)

def self_test(output):
    started=datetime.now(timezone.utc).isoformat();start=time.perf_counter();cpu=time.process_time();rows=[]
    for alpha in [.334,1.,2.]:
        a,b=.7,-.4
        def source(r,z):return (a+b*z/(1+r*r+z*z))*(1+r*r+z*z)**(-1-alpha)
        for nr,na in [(24,32),(48,64)]:
            got=direct_moments(source,alpha,nr=nr,na=na)
            got.update(alpha=alpha,P_error=abs(got['P']-a/(2*alpha)),gradient_error=abs(got['gradient_z']-b/(6*(1+alpha))))
            got['passed']=max(got['P_error'],got['gradient_error'])<2e-10;rows.append(got)
    proof=ROOT.parent/'research/origin_pressure_moment/PROOF.md'
    record=dict(started_utc=started,completed_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,rows=rows,all_passed=all(r['passed'] for r in rows),source_sha256=sha256(__file__),proof_sha256=sha256(proof))
    atomic_json(output,record);print(json.dumps(record,indent=2))
    return 0 if record['all_passed'] else 1

def main():
    ap=argparse.ArgumentParser();ap.add_argument('export',type=Path,nargs='?');ap.add_argument('--geometry',type=Path);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--self-test',action='store_true');args=ap.parse_args()
    if not args.output.resolve().is_relative_to(ROOT.parent) or args.output.exists():raise ValueError('fresh lane output required')
    if args.self_test:return self_test(args.output)
    if args.export is None or args.geometry is None:ap.error('export and geometry required')
    start=time.perf_counter();cpu=time.process_time();f=load_piecewise(args.export/'coeffs.npz');geometry=json.loads(args.geometry.read_text());meta=json.loads((args.export/'candidate.json').read_text())
    paths=[Path(__file__),ROOT/'fast_native_field.py',ROOT.parent/'research/native_derivative_operators/PROOF.md',args.export/'coeffs.npz',args.export/'candidate.json',args.geometry,ROOT.parent/'research/origin_pressure_moment/PROOF.md']
    paths+=list((ROOT/'src').glob('piecewise_*.py'))+list((ROOT/'src').glob('independent_*.py'))
    hashes={str(p.resolve()):sha256(p) for p in paths}
    rec=dict(started_utc=datetime.now(timezone.utc).isoformat(),source_sha256=hashes,moments=[],collar_rows=[],scope='Bulk origin moments and finite origin-collar checks; no global enclosure or complete A7 claim.',coordinates='Original exported working coordinates')
    def save(phase):
        if any(sha256(p)!=h for p,h in hashes.items()):raise RuntimeError('changed input')
        rec.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu);atomic_json(args.output,rec);print(phase,rec['elapsed_seconds'],flush=True)
    save('started')
    radii={'primary_exported':float(meta['a_eff']),'independent_detected':geometry['core']['a_eff']/geometry['gauge']['dilation_L']}
    phi=f.phi.jet(0.,0.,1);Mbare=2*(1-f.c_l)*float(phi[0,0])+4*float(phi[0,0]*phi[0,1]);rec['origin_axial_without_pressure']=Mbare
    for lmax,na,nr in [(32,64,48),(80,128,96),(96,144,128)]:
        direct=direct_moments(f.source,f.alpha,f.interfaces,nr=nr,na=na,scale=f.phi.length)
        pressure=InterfaceGreenPoisson(f.source,interfaces=f.interfaces,decay_power=2*f.alpha,scale=f.phi.length,lmax=lmax,nangle=na,nradial=nr)
        P,G=pressure.evaluate(np.array([0.]),np.array([0.]));direct.update(lmax=lmax,green_P=float(P[0]),green_gradient_z=float(G[0,1]),M_z=Mbare+direct['gradient_z']);rec['moments'].append(direct);save('moments_'+str(lmax))
        for label,aeff in radii.items():
            for collar in [False,True]:
                grid=shell_quadrature(0,aeff/64,nradial=8,nangle=64,collar=collar);P,G=pressure.on_spheres(grid['radii'],grid['mu']);metrics,_=evaluate_set(f,grid['r'],grid['z'],grid['weights'],P,G)
                rec['collar_rows'].append(dict(lmax=lmax,nangle=na,nradial=nr,radius_label=label,a_eff=aeff,set='collar_gauss' if collar else 'shell_gauss',metrics=metrics));save('collar_'+str(lmax)+'_'+label+'_'+str(collar))
    save('complete')
    return 0
if __name__=='__main__':raise SystemExit(main())
