#!/usr/bin/env python3
"""FLOAT whole compact energy remainder in an S1 Hermite Galerkin space.

Computes Krest = T_IS+T_II+C_tr+C_aw+C_vs1+C_vs2+C_vs3 by the
original conjugated energy minus the exact principal and negative A sandwich.
Fourier collocation, radial spline, finite box and roundoff are uncertified.
"""
import argparse,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import eval_hermite
from scipy.fft import fft2,ifft2,fftfreq
from flint import ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,synthesize,C
from hermite_gram import build


def radial_cache(path,rmax,number,bits):
 if path.exists():
  z=json.loads(path.read_text())
  if z['rmax']>=rmax and z['number']>=number:return z
 start=time.time();e=Evaluator(bits,max_density_order=1,max_velocity_order=1)
 rr=np.exp(np.linspace(np.log(1e-5),np.log(rmax),number));rows=[]
 for k,r in enumerate(rr):
  mm=e.modes_at(str(r));rows.append({','.join(map(str,key)):{f'{j},{n}':float(v.mid()) for (j,n),v in vals.items()} for key,vals in mm.items()})
  if (k+1)%100==0:print('radial',k+1,'elapsed',time.time()-start,flush=True)
 ans={'status':'FLOAT_RADIAL_INTERPOLATION_CACHE','r':rr.tolist(),'rmax':rmax,'number':number,'rows':rows,'bits_at_input':bits,'elapsed_seconds':time.time()-start}
 path.write_text(json.dumps(ans)+'\n');return ans


def mesh(z,xx,yy):
 r=np.sqrt(xx*xx+yy*yy);tt=np.arctan2(yy,xx);lr=np.log(np.maximum(r,z['r'][0]));ln=np.log(z['r']);out={}
 for key in z['rows'][0]:
  kk=tuple([key.split(',')[0]]+[int(k) for k in key.split(',')[1:]])
  value=np.zeros_like(xx)
  for mode in z['rows'][0][key]:
   kind,n=mode.split(',');n=int(n)
   radial=np.array([row[key].get(mode,0.) for row in z['rows']]);fn=CubicSpline(ln,radial)
   value+=fn(lr)*(np.sin(n*tt) if kind=='s' else np.cos(n*tt))
  out[kk]=value
 return out


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=7);ap.add_argument('--skip-gram',action='store_true');ap.add_argument('--norm-order',choices=['N','Q'],default='N');ap.add_argument('--alpha',type=float,default=1.);ap.add_argument('--grid',type=int,default=512);ap.add_argument('--radius',type=float,default=24.);ap.add_argument('--radial',type=int,default=512);ap.add_argument('--bits',type=int,default=384);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--cache',type=Path,default=HERE/'radial_mesh_cache.float.json');args=ap.parse_args()
 if args.norm_order=='Q':args.skip_gram=True
 start=time.time();ids=[(m,n) for total in range(args.degree+1) for m in range(total+1) for n in [total-m] if m%2==0 and n%2==1]
 z=radial_cache(args.cache,args.radius*2,args.radial,args.bits)
 n=args.grid;R=args.radius;dx=2*R/n;x=np.arange(n)*dx-R;xx,yy=np.meshgrid(x,x,indexing='xy');r2=xx*xx+yy*yy;W=np.sqrt(1+4*r2)
 fields=mesh(z,xx,yy);c=float(C);q=2.1
 print('mesh ready',time.time()-start,flush=True)
 Vx=c*xx+fields['u1',0,0];Vy=c*yy+fields['u2',0,0]
 aw=(Vx*xx+Vy*yy)/(.25+r2)
 A11=c+fields['u1',1,0];A22=c+fields['u2',0,1];A12=(fields['u1',0,1]+fields['u2',1,0])/2
 bx=fields['rho',1,0];by=fields['rho',0,1]
 M11=c+1+aw-q*A11+by;M22=c+1+aw-q*A22;M12=-q*A12-bx/2
 k=2*np.pi*fftfreq(n,d=dx);kx,ky=np.meshgrid(k,k,indexing='xy');k2=kx*kx+ky*ky;J=np.sqrt(1+k2);kinv=np.zeros_like(k2);kinv[k2>0]=1/np.sqrt(k2[k2>0]);R1=1j*kx*kinv;R2=1j*ky*kinv
 U1=np.zeros_like(k2);U2=np.zeros_like(k2);U1[k2>0]=kx[k2>0]*ky[k2>0]/k2[k2>0];U2[k2>0]=-kx[k2>0]**2/k2[k2>0]
 pp=[];Jqp=[];Lp=[];R1p=[];R2p=[];pR1p=[];pR2p=[];norm=[]
 for m,nj in ids:
  import math
  phi=args.alpha/math.sqrt(math.pi*2**(m+nj)*math.factorial(m)*math.factorial(nj))*eval_hermite(m,args.alpha*xx)*eval_hermite(nj,args.alpha*yy)*np.exp(-args.alpha**2*r2/2)
  ph=fft2(phi)
  if args.norm_order=='N':
   uq=ifft2(J**(-q)*ph).real;h=uq/W;hh=fft2(h)
   LW=Vx*ifft2(1j*kx*J**(-q)*ph).real+Vy*ifft2(1j*ky*J**(-q)*ph).real-(1+aw)*uq+W*(bx*ifft2(U1*hh).real+by*ifft2(U2*hh).real)
   left=ifft2(J**q*ph).real
  else:
   hh=J**(-q)*fft2(phi/W);h=ifft2(hh).real
   LW=Vx*ifft2(1j*kx*hh).real+Vy*ifft2(1j*ky*hh).real-h+bx*ifft2(U1*hh).real+by*ifft2(U2*hh).real
   left=ifft2(J**q*fft2(W*phi)).real
  Jqp.append(left.ravel());Lp.append(LW.ravel());pp.append(phi.ravel())
  R1p.append(ifft2(R1*ph).real.ravel());R2p.append(ifft2(R2*ph).real.ravel());pR1p.append(ifft2(R1/J*ph).real.ravel());pR2p.append(ifft2(R2/J*ph).real.ravel());norm.append(float(np.sum(phi*phi)*dx*dx))
 Jqp,Lp,R1p,R2p,pR1p,pR2p,pp=map(np.asarray,[Jqp,Lp,R1p,R2p,pR1p,pR2p,pp])
 E=(Jqp@Lp.T)*dx*dx;E=(E+E.T)/2
 pphi=np.array([ifft2(fft2(row.reshape(args.grid,args.grid))/J).real.ravel() for row in pp])
 free_gain= q*c*(pphi@pphi.T)*dx*dx
 def quad(xx,yy,a,b,d):return ((xx*a.ravel())@xx.T+(xx*b.ravel())@yy.T+(yy*b.ravel())@xx.T+(yy*d.ravel())@yy.T)*dx*dx
 principal_M=quad(R1p,R2p,M11,M12,M22)
 if args.norm_order=='N':
  negative_sandwich=q*quad(pR1p,pR2p,A11,A12,A22)
 else:
  Td=np.array([ifft2(fft2(row.reshape(args.grid,args.grid)/W)/(J*J)).real.ravel() for row in pp])
  negative_sandwich=q*c*((pp*W.ravel())@Td.T)*dx*dx
  negative_sandwich=(negative_sandwich+negative_sandwich.T)/2
 K=E+principal_M+negative_sandwich;K=(K+K.T)/2
 Kc=E+principal_M+free_gain;Kc=(Kc+Kc.T)/2
 if args.norm_order=='Q':Kc=K.copy()
 # Full pointwise-matrix finite-core absorption, beta0 fixed rational screens.
 full_matrix_dual={}
 for beta0 in [.3,.4,.5]:
  det=(M11-beta0)*(M22-beta0)-M12*M12
  dual=quad(R1p,R2p,(M22-beta0)/det,-M12/det,(M11-beta0)/det)
  dd,QQ=np.linalg.eigh(dual);Dh=(QQ*np.sqrt(np.maximum(0,dd)))@QQ.T
  full_matrix_dual[str(beta0)]={'D':dual.tolist(),'lambda_max_Dhalf_Kc_Dhalf':float(max(np.linalg.eigvalsh(Dh@Kc@Dh))),'minimum_margin_I_Dhalf_Kc_Dhalf':float(1-max(np.linalg.eigvalsh(Dh@Kc@Dh))),'min_dual_eigenvalue':float(min(dd))}
 # Diagnostic unweighted transport commutator Ctr and its Hminus1 metric.
 ctr_left=[];ctr_right=[];b1=[];b2=[]
 for row in pp:
  agrid=row.reshape(args.grid,args.grid);ah=fft2(agrid)
  ctr_left.append(ifft2(J**q*ah).real.ravel())
  ctr_right.append((fields['u1',0,0]*ifft2(1j*kx*J**(-q)*ah).real+fields['u2',0,0]*ifft2(1j*ky*J**(-q)*ah).real).ravel())
  b1.append(ifft2(1j*kx/J*ah).real.ravel());b2.append(ifft2(1j*ky/J*ah).real.ravel())
 ctr_left,ctr_right,b1,b2=map(np.asarray,[ctr_left,ctr_right,b1,b2])
 Ctr=ctr_left@ctr_right.T*dx*dx;Ctr=(Ctr+Ctr.T)/2-q*quad(b1,b2,A11-c,A12,A22-c)
 Hmetric=((pphi/W.ravel())@(pphi/W.ravel()).T)*dx*dx
 ee,QQ=np.linalg.eigh(Hmetric);Hi=(QQ/np.sqrt(ee))@QQ.T
 Ctr_Hminus1_estimate=float(max(abs(np.linalg.eigvalsh(Hi@Ctr@Hi))))
 # Cvs3 for consistency with exact polar screen.
 source=[]
 for row in pp:
  hh=fft2(row.reshape(args.grid,args.grid));source.append((bx*ifft2(U1*hh).real+by*ifft2(U2*hh).real).ravel())
 Cvs=np.asarray(source)@pp.T*dx*dx;Cvs=(Cvs+Cvs.T)/2
 Cvs+=quad(R1p,R2p,by,-bx/2,np.zeros_like(by))
 ctx.prec=args.bits
 if not args.skip_gram:
  gram=build(args.degree,Q(str(args.alpha)),args.bits)
  B=np.array([[float(v['midpoint'].split(' +/-')[0].strip('[]')) for v in row] for row in gram['B']]);bv,bw=np.linalg.eigh(B);Bh=(bw*np.sqrt(np.maximum(0,bv)))@bw.T
 else:Bh=np.zeros_like(K)
 out={'status':'FLOAT_NOT_CERTIFICATE','norm_order':args.norm_order,'basis':ids,'alpha':args.alpha,'grid':args.grid,'radius':R,'dx':dx,'A':K.tolist(),'A_Kc':Kc.tolist(),'eigenvalues_Kc':np.linalg.eigvalsh(Kc).tolist(),'C_N_Kc_float':None if args.skip_gram else float(np.max(np.abs(np.linalg.eigvalsh(Bh@Kc@Bh)))),'energy_E':E.tolist(),'principal_M':principal_M.tolist(),'negative_sandwich':negative_sandwich.tolist(),'Cvs3':Cvs.tolist(),'eigenvalues_A':np.linalg.eigvalsh(K).tolist(),'Ctr':Ctr.tolist(),'Ctr_Hminus1_metric':Hmetric.tolist(),'Ctr_Hminus1_estimate':Ctr_Hminus1_estimate,'full_matrix_dual':full_matrix_dual,'eigenvalues_Cvs3':np.linalg.eigvalsh(Cvs).tolist(),'captured_HS_squared_A':float(np.sum(K*K)),'captured_HS_squared_Cvs3':float(np.sum(Cvs*Cvs)),'C_N_float':None if args.skip_gram else float(np.max(np.abs(np.linalg.eigvalsh(Bh@K@Bh)))),'C_N_Cvs3_float':None if args.skip_gram else float(np.max(np.abs(np.linalg.eigvalsh(Bh@Cvs@Bh)))),'basis_L2_diagonal_range':[min(norm),max(norm)],'elapsed_seconds':time.time()-start,'warnings':['FFT on finite periodic box, radial interpolation, finite mesh, and floating arithmetic are not rigorously enclosed.','No finite-rank tail bound has been verified.','For norm N: retained negative A sandwich; for Q: retained negative qc*Sym(Wp²W^-1). Matrix Kc duplicates KQ for Q mode.']}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['A','A_Kc','Ctr','Ctr_Hminus1_metric','full_matrix_dual','energy_E','principal_M','negative_sandwich','Cvs3']},indent=2))
if __name__=='__main__':main()
