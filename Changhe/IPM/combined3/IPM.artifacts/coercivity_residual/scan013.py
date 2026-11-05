"""FLOAT whole-plane logarithmic radial screens using enclosed exact-source modes.

No quadrature/discretization/tail certificate is claimed by this screen.  Arb
radius arithmetic is retained in the output to distinguish point roundoff from
the open whole-domain enclosure.
"""
import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.integrate import simpson
from fields013 import Evaluator,synthesize,C,SOURCE_HASHES

E=None
def setup(precision):
    global E
    E=Evaluator(precision,max_density_order=2,max_velocity_order=1)

def row(task):
    i,s,nt=task;r=math.exp(s);m=E.modes_at(str(r));theta=np.linspace(0,math.pi/2,nt)
    def field(name,a,b):return synthesize(m[name,a,b],theta)
    rx,ex=field('rho',1,0);ry,ey=field('rho',0,1)
    thetaf=(np.hypot(rx,ry)-ry)/2;idx=int(thetaf.argmax())
    def norm2(modes):
        return sum((2 if n==0 else 1)*float(v.mid())**2 for (kind,n),v in modes.items())*math.pi
    xx=norm2(m['rho',2,0]);xy=norm2(m['rho',1,1]);yy=norm2(m['rho',0,2])
    u1,_=field('u1',0,0);u2,_=field('u2',0,0);rho,_=field('rho',0,0)
    f=(float(C)*r*np.cos(theta)+u1)*rx+(float(C)*r*np.sin(theta)+u2)*ry-rho
    sx,_=field('u1',1,0);sy,_=field('u2',0,1);s12a,_=field('u1',0,1);s12b,_=field('u2',1,0)
    d=float(C)+1+(float(C)*r*r+r*(u1*np.cos(theta)+u2*np.sin(theta)))/(.25+r*r)
    a=d-2.1*(float(C)+sx)+ry;dd=d-2.1*(float(C)+sy);b=-1.05*(s12a+s12b)-rx/2
    mineig=(a+dd)/2-np.hypot((a-dd)/2,b)
    return {'i':i,'s':s,'r':r,'theta':float(thetaf[idx]),'theta_max':float(theta[idx]),'rho_y_min':float(ry.min()),'gradient_max':float(np.hypot(rx,ry).max()),
            'r2Hxx2':r*r*xx,'r2Hxy2':r*r*xy,'r2Hyy2':r*r*yy,'radial_error_gradient':ex+ey,
            'matrix_mineig':float(mineig.min()),'matrix_mineig_theta':float(theta[mineig.argmin()]),
            'residual_point_max':float(np.abs(f).max())}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--nr',type=int,default=401);ap.add_argument('--nt',type=int,default=481);ap.add_argument('--lo',type=float,default=-9.21);ap.add_argument('--hi',type=float,default=13.82);ap.add_argument('--workers',type=int,default=8);ap.add_argument('--precision',type=int,default=384);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    start=time.monotonic();ss=np.linspace(args.lo,args.hi,args.nr);rows=[]
    with ProcessPoolExecutor(args.workers,initializer=setup,initargs=(args.precision,))as pool:
        for rr in pool.map(row,[(i,float(s),args.nt) for i,s in enumerate(ss)],chunksize=1):
            rows.append(rr)
            if len(rows)%20==0:print('rows',len(rows),'seconds',time.monotonic()-start,flush=True)
    hx=float(simpson([r['r2Hxx2']+r['r2Hxy2'] for r in rows],x=ss));hy=float(simpson([r['r2Hyy2']+r['r2Hxy2'] for r in rows],x=ss))
    kap=math.sqrt(((math.log(2)-.5)*hx+(3*math.log(2)-2)*hy)/(16*math.pi));th=max(rows,key=lambda r:r['theta'])
    out={'status':'FLOAT_SCREEN_ONLY','source_hashes':SOURCE_HASHES,'precision':args.precision,'s_range':[args.lo,args.hi],'nr':args.nr,'nt':args.nt,'Hessian_x_L2sq_screen':hx,'Hessian_y_L2sq_screen':hy,
         'kappa_screen':kap,'theta_screen':th,'beta_screen':float(C)+1-kap-th['theta'],'matrix_mineig_screen':min(rows,key=lambda r:r['matrix_mineig']),
         'started_or_finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'rows':rows,
         'open_errors':['radial quadrature','angular maximum discretization','near-origin and far-field tails','full error certificates']}
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2),flush=True)
if __name__=='__main__':main()
