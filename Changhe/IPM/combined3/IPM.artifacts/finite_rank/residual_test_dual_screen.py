#!/usr/bin/env python3
"""FLOAT full-M inverse norm of a smooth R J^-0.1 polar Laguerre test."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from full_remainder_screen import mesh
from fractional_riesz_gaussian import laguerre_radial_modes
HERE=Path(__file__).resolve().parent


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--width',type=float,default=.015);ap.add_argument('--m',type=int,default=1);ap.add_argument('--k',type=int,default=1);ap.add_argument('--radial',type=int,default=512);ap.add_argument('--angular',type=int,default=512);ap.add_argument('--heat',type=int,default=512);ap.add_argument('--radius',type=float,default=32.);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 start=time.time();x,w=roots_legendre(args.radial);T=args.radius/(args.radius+args.width);t=(x+1)*T/2;wt=w*T/2;r=args.width*t/(1-t);wr=wt*args.width/(1-t)**2*r
 theta=np.arange(args.angular)*2*np.pi/args.angular;xx=r[:,None]*np.cos(theta);yy=r[:,None]*np.sin(theta)
 cache=json.loads((HERE/'radial_mesh_cache.float.json').read_text());b=mesh(cache,xx,yy)
 c=4076476460239181/2251799813685248;q=2.1;r2=xx*xx+yy*yy
 Vx=c*xx+b['u1',0,0];Vy=c*yy+b['u2',0,0];aw=(Vx*xx+Vy*yy)/(.25+r2)
 M11=c+1+aw-q*(c+b['u1',1,0])+b['rho',0,1]
 M22=c+1+aw-q*(c+b['u2',0,1]);M12=-q*(b['u1',0,1]+b['u2',1,0])/2-b['rho',1,0]/2
 vv=laguerre_radial_modes(r,args.width,args.m,args.k,nodes=args.heat);Phi=[np.zeros_like(xx),np.zeros_like(xx)]
 for (component,kind,n),a in vv.items():Phi[0 if component=='r1' else 1]+=a[:,None]*(np.sin(n*theta) if kind=='s' else np.cos(n*theta))
 A,B=Phi;out={}
 for beta in [.0,.5,.7,.704955805507]:
  det=(M11-beta)*(M22-beta)-M12*M12
  form=((M22-beta)*A*A-2*M12*A*B+(M11-beta)*B*B)/det
  value=np.sum(wr*np.mean(form,axis=1))*2*np.pi
  out[str(beta)]={'Gamma_float':float(value),'min_determinant_mesh':float(np.min(det))}
 z={'status':'FLOAT_NOT_CERTIFICATE','test':{'width':args.width,'m':args.m,'k':args.k},'radial_nodes':args.radial,'angular_nodes':args.angular,'heat_nodes':args.heat,'truncation_radius':args.radius,'Gamma':out,'L2_Phi_mesh':float(np.sum(wr*np.mean(A*A+B*B,axis=1))*2*np.pi),'elapsed_seconds':time.time()-start,'warning':'Background spline, heat and polar quadrature, finite radius and floating errors are not enclosed.'}
 args.output.write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z,indent=2))
if __name__=='__main__':main()
