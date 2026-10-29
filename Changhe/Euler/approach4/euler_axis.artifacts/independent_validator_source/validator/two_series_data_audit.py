#!/usr/bin/env python3
"""Own rational derivatives and log-coordinate ODEs for frozen two-series data."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from audit_t1_deformation import RationalT1,transport
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parent

class TwoSeries(RationalT1):
    def __init__(self,meta):
        self.meta=meta;self.c_l=float(meta['c']);self.p=1/(2*self.c_l)
        aspect=float(meta['a']);self.terms=[]
        for series,poly in enumerate(meta['polynomials'],1):
            for j,k,C in poly:
                self.terms.append((float(C)*aspect**j,int(j),int(k),series*self.p+j+k,aspect,1.,series-1))
        self.ps=float(self.F(0.,0.,1,0));self.pz=float(self.F(0.,0.,0,1))
        if abs(float(self.F(0.,0.))-.5)>1e-13:raise ValueError('source strain')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('export',type=Path);ap.add_argument('--output',required=True,type=Path);ap.add_argument('--transport',action='store_true');a=ap.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent) or out.exists():raise ValueError('fresh lane output required')
    start=time.perf_counter();cpu=time.process_time();paths=[a.export/'results/ladder'/n for n in ['c068_n08','c068_n16','c068_n24','c074_n08','c074_n16','c074_n24']]+[a.export/'results/best/free']
    sourcefiles=[Path(__file__),ROOT/'audit_t1_deformation.py']+[p/n for p in paths for n in ['metadata.json','grid.npz']]
    hashes={str(p.resolve()):sha256(p) for p in sourcefiles}
    rec=dict(started_utc=datetime.now(timezone.utc).isoformat(),source_sha256=hashes,rows=[],transport_rows=[],scope='Independent canonical-polynomial derivatives and characteristic integration. Saved eta and q are only comparison data; no primary code is executed. No interval enclosure.')
    def checkpoint(phase):
        if any(sha256(Path(p))!=v for p,v in hashes.items()):raise RuntimeError('changed source')
        rec.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(out,rec);print(phase,rec['elapsed_seconds'],flush=True)
    checkpoint('started')
    for path in paths:
        meta=json.loads((path/'metadata.json').read_text());f=TwoSeries(meta)
        with np.load(path/'grid.npz',allow_pickle=False) as g:
            R=np.exp(g['x'])[:,None];mu=g['m'][None,:];r=R*np.sqrt(1-mu*mu);z=R*mu
            jets=f.jets(r,z);phierr=float(np.max(abs(jets['phi']-g['phi'])));etaerr=float(np.max(abs(jets['eta_phi']-g['elliptic_eta'])))
            R=g['shell_R'][:,None];mu=g['shell_mu'][None,:];w=g['shell_weights'][None,:]
            eta=f.jets(R*np.sqrt(1-mu*mu),R*mu)['eta_phi'];ref=g['shell_eta']
            eps=np.sqrt(np.sum(w*(eta-ref)**2,axis=1)/np.sum(w*ref**2,axis=1));E=float(np.sqrt(np.mean(eps**2)))
            row=dict(name=path.name,c_l=f.c_l,p_s=f.ps,p_z=f.pz,phi_max_abs_error=phierr,elliptic_eta_max_abs_error=etaerr,shell_elliptic_eta_max_abs_error=float(np.max(abs(eta-g['shell_elliptic_eta']))),shell_eps_max_abs_error=float(np.max(abs(eps-g['shell_eps']))),E=E,declared_E=meta['E'],E_abs_error=abs(E-meta['E']),max_shell_eps=float(np.max(eps)),shell_R_at_max=float(g['shell_R'][np.argmax(eps)]),K=meta['K'],S=meta['S'],normalization_error=abs(2*meta['K2']*meta['S']-1),comparison_passed=phierr<2e-10 and etaerr<2e-8 and abs(E-meta['E'])<2e-10)
            rec['rows'].append(row);checkpoint('data_'+path.name)
    if a.transport:
        for name in ['c068','c074']:
            path=a.export/'results/best'/name/'independent_points.json';reference=json.loads(path.read_text());hashes[str(path.resolve())]=sha256(path)
            meta_path=a.export/'results/ladder'/('c068_n24' if name=='c068' else 'c074_n24')/'metadata.json'
            field=TwoSeries(json.loads(meta_path.read_text()));points=reference['points']
            R=np.array([p['R'] for p in points]);mu=np.array([p['mu'] for p in points]);r=R*np.sqrt(1-mu*mu);z=R*mu
            href=np.array([p['h'] for p in points]);eref=np.array([p['e'] for p in points]);runs=[]
            for rad,tol in [(1e-4,2e-9),(1e-5,2e-11)]:
                got=transport(field,r,z,source_radius=rad,rtol=tol,atol=tol/100)
                rows=[dict(R=float(R[i]),mu=float(mu[i]),h=float(got['h'][i]),e=float(got['e'][i]),h_reference=float(href[i]),e_reference=float(eref[i])) for i in range(len(points))]
                summary={k:v for k,v in got.items() if k not in ['h','e']}
                summary.update(name=name,count=len(points),points=rows,max_h_relative_error=float(np.max(abs(got['h']-href)/abs(href))),max_e_absolute_error=float(np.max(abs(got['e']-eref))))
                if runs:summary.update(h_refinement_max_abs=float(np.max(abs(got['h']-np.array([p['h'] for p in runs[-1]['points']])))),e_refinement_max_abs=float(np.max(abs(got['e']-np.array([p['e'] for p in runs[-1]['points']])))))
                runs.append(summary);rec['transport_rows'].append(summary);checkpoint(f'transport_{name}_{rad}')
    rec['all_data_comparisons_passed']=all(r['comparison_passed'] for r in rec['rows'])
    checkpoint('complete')
    if not rec['all_data_comparisons_passed']:raise SystemExit(2)
if __name__=='__main__':main()
