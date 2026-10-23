"""Numerical shooting for result36's formal angular hierarchy, not the IPM PDE.

Every truncation is reported separately. No missing angular mode is assumed small.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[key]='1'
import argparse, json, time
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def utc():return datetime.now(timezone.utc).isoformat()


def rhs_factory(order):
    js=2*np.arange(order)+3
    def rhs(t,y):
        h,F=y[:2];C=F-1
        out=np.zeros_like(y);H=y[2:]
        out[0]=-h*F;out[1]=h*F/4-(H[0] if order else 0)
        if order:
            out[2]=-(1-h/2)*H[0]+(3*C-3*h/4)*(H[1] if order>1 else 0)+h*F*(.5-F/2-h/16)
        if order>1:
            j=js[1:]
            out[3:]=-(1-h/2)*H[1:]-(j-3)*(C/2+h/(4*(j+1)))*H[:-1]
            out[3:-1]+=(j[:-1]+3)*(C/2-h/(4*(j[:-1]-1)))*H[2:]
        return out
    return rhs


def integrate(alpha,F0,order,T,rtol,atol):
    initial=np.zeros(order+2);initial[:2]=alpha,F0
    def escaped(t,y):return 1e6-np.max(np.abs(y))
    escaped.terminal=True;escaped.direction=-1
    sol=solve_ivp(rhs_factory(order),(0,T),initial,method='DOP853',rtol=rtol,atol=atol,max_step=.5,events=escaped,dense_output=True)
    final=sol.y[:,-1];valid=bool(sol.success and sol.t[-1]>=T and np.isfinite(final).all())
    tail=sol.sol(.8*T) if valid else final
    return {'alpha':alpha,'F0':float(F0),'angular_order':order,'highest_density_mode':2*order+1,
      'sigma_end_requested':T,'sigma_end_reached':float(sol.t[-1]),'rtol':rtol,'atol':atol,
      'success':valid,'message':sol.message,'nfev':int(sol.nfev),'F_end':float(final[1]),
      'h_end':float(final[0]),'H_max_end':float(np.max(abs(final[2:]))) if order else 0.,
      'F_tail_change':float(final[1]-tail[1]),'h_tail_change':float(final[0]-tail[0]),
      'last_mode_end':float(final[-1]) if order else 0.,'final_coefficients':final.tolist(),
      'F_end_minus_one':float(final[1]-1) if valid else None}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--orders',default='0,1,2,4,8,16')
    ap.add_argument('--alphas',default='1,3,5,6,6.5,7,8');ap.add_argument('--final-sigma',type=float,default=30.)
    ap.add_argument('--nodes',type=int,default=21);ap.add_argument('--tag',default='first_scan')
    args=ap.parse_args();dest=Path('evidence/slow_radius')/args.tag;dest.mkdir(parents=True,exist_ok=True)
    log=dest/'rows.jsonl';start=time.time();rows=[];roots=[]
    meta={'started_utc':utc(),'arguments':vars(args),'scope':'Finite truncations of the stated formal D=ell-1 hierarchy only. Forced-core initial conditions and their derivation from full-plane IPM have not been proved. Shooting failures or folds are not PDE nonexistence. All higher coefficients above the chosen order are set to zero.'}
    (dest/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    def record(kind,row):
        row={'utc':utc(),'kind':kind,**row}
        with log.open('a') as f:f.write(json.dumps(row)+'\n')
        if kind!='brent_iteration':print(json.dumps(row),flush=True)
        return row
    grid=np.unique(np.r_[np.geomspace(1e-5,1.,args.nodes),np.linspace(.8,1.3,7)])
    for order in map(int,args.orders.split(',')):
        for alpha in map(float,args.alphas.split(',')):
            cache={}
            def shoot(F0,kind='brent_iteration'):
                key=float(F0)
                if key not in cache:
                    cache[key]=record(kind,integrate(alpha,key,order,args.final_sigma,2e-9,2e-11))
                return cache[key]
            scans=[shoot(float(f),'grid') for f in grid]
            brackets=[]
            for left,right in zip(scans[:-1],scans[1:]):
                if left['success'] and right['success'] and left['F_end_minus_one']*right['F_end_minus_one']<0:
                    brackets.append([left['F0'],right['F0']])
            found=[]
            for bracket in brackets:
                try:
                    def objective(f):
                        row=shoot(f)
                        if not row['success']:raise ValueError('Invalid trajectory inside a sampled sign bracket')
                        return row['F_end_minus_one']
                    root=brentq(objective,*bracket,xtol=2e-10,rtol=2e-10,maxiter=60)
                    base=shoot(root);refined=integrate(alpha,root,order,2*args.final_sigma,2e-11,2e-13)
                    result=record('root',{'bracket':bracket,'root_F0':root,'base':base,'longer_tighter_check':refined})
                    roots.append(result);found.append(root)
                except (ValueError,RuntimeError) as exc:record('root_failure',{'order':order,'alpha':alpha,'bracket':bracket,'error':str(exc)})
            rows.append({'angular_order':order,'alpha':alpha,'sampled_brackets':brackets,'roots_F0':found,
                         'valid_samples':sum(r['success'] for r in scans),'total_samples':len(scans)})
            result={'metadata':meta,'updated_utc':utc(),'elapsed_seconds':time.time()-start,'rows':rows,'roots':roots,
                    'scope':'A finite sampled shooting scan, not a proof of root absence, uniqueness, asymptotic convergence, or existence/nonexistence for full-plane IPM.'}
            (dest/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'finished_utc':utc(),'elapsed_seconds':time.time()-start,'root_count':len(roots)}),flush=True)

if __name__=='__main__':main()
