#!/usr/bin/env python3
"""FLOAT actual Cvs3 Hermite Galerkin matrix, exact-source radial Arb values.

This is a screen: Gauss-Legendre integration and numpy eigensolvers are FLOAT;
radial truncation of coefficient harmonics is exact by angular orthogonality.
"""
import argparse,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.special import roots_legendre
from flint import ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,synthesize
from hermite_polar import HermitePolar
from hermite_gram import build


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=7);ap.add_argument('--parity',default='01');ap.add_argument('--skip-gram',action='store_true');ap.add_argument('--alpha',default='1');ap.add_argument('--nodes',type=int,default=80);ap.add_argument('--bits',type=int,default=384);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 start=time.time();ids=[(m,n) for total in range(args.degree+1) for m in range(total+1) for n in [total-m] if m%2==int(args.parity[0]) and n%2==int(args.parity[1])]
 ee=Evaluator(args.bits,max_density_order=1,max_velocity_order=0)
 cut=2*args.degree+6
 ee.prepared=[row for row in ee.prepared if row[1]<=cut]
 packets=[HermitePolar(*mn,Q(args.alpha)) for mn in ids]
 theta=2*np.pi*np.arange(8*(args.degree+4))/(8*(args.degree+4))
 x,w=roots_legendre(args.nodes);tt=(x+1)/2;ww=w/2
 mat=np.zeros((len(ids),len(ids)));ordinary_gram=np.zeros_like(mat);max_rad=0.;nodes=[]
 for node,(t,wt) in enumerate(zip(tt,ww)):
  scale=1/float(Q(args.alpha));r=float(scale*t/(1-t));jacobian=scale*scale*t/(1-t)**3;modes=ee.modes_at(str(r));bx,ex=synthesize(modes['rho',1,0],theta);by,ey=synthesize(modes['rho',0,1],theta)
  max_rad=max(max_rad,ex,ey)
  phi=[];r1=[];r2=[];u1=[];u2=[]
  for h in packets:
   z=h.modes(str(r))
   for name,out in [('phi',phi),('r1',r1),('r2',r2),('u1',u1),('u2',u2)]:
    value,er=synthesize(z[name],theta);out.append(value);max_rad=max(max_rad,er)
  phi,r1,r2,u1,u2=map(np.array,[phi,r1,r2,u1,u2])
  srcx=(phi*bx)@u1.T;srcy=(phi*by)@u2.T
  source=(srcx+srcx.T+srcy+srcy.T)/2
  angular=source+(r1*by)@r1.T-((r1*bx)@r2.T+(r2*bx)@r1.T)/2
  contribution=angular*(2*np.pi/len(theta))*float(wt)*jacobian
  ordinary_gram+=(phi@phi.T)*(2*np.pi/len(theta))*float(wt)*jacobian
  mat+=contribution
  nodes.append({'r':r,'weight':float(wt)*jacobian,'contribution':contribution.tolist()})
  if (node+1)%20==0:print('nodes',node+1,'of',args.nodes,'elapsed',time.time()-start,flush=True)
 ctx.prec=args.bits
 if not args.skip_gram:
  assert args.parity=='01'
  gram=build(args.degree,Q(args.alpha),args.bits)
  B=np.array([[float(z['midpoint'].split(' +/-')[0].strip('[]')) for z in row] for row in gram['B']])
  bval,bvec=np.linalg.eigh(B);Bhalf=(bvec*np.sqrt(np.maximum(0,bval)))@bvec.T
  reduced=Bhalf@mat@Bhalf
 else:B=np.zeros_like(mat);reduced=B
 out={'status':'FLOAT_NOT_CERTIFICATE','ordinary_basis_gram_error_op':float(max(abs(np.linalg.eigvalsh(ordinary_gram-np.eye(len(ids)))))),'basis':ids,'alpha':args.alpha,'parity':args.parity,'nodes':args.nodes,'A':mat.tolist(),'eigenvalues_A':np.linalg.eigvalsh(mat).tolist(),'captured_HS_squared':float(np.sum(mat*mat)),'B':B.tolist(),'C_N_float':None if args.skip_gram else float(np.max(np.abs(np.linalg.eigvalsh(reduced)))),'radial_input_radius_max':max_rad,'angular_points':len(theta),'coefficient_potential_harmonic_cut':cut,'integration':'Gauss-Legendre r=(1/alpha)*t/(1-t) over t(0,1), theta trapezoid exact for finite harmonic content up to floating error','elapsed_seconds':time.time()-start,'radial_nodes': [{'r':v['r'],'weight':v['weight']} for v in nodes]}
 args.output.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['A','B','radial_nodes']},indent=2))
if __name__=='__main__':main()
