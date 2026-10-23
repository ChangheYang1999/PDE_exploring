"""Two independent canonical DF evaluators on literal spectral directions."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as Fr
import argparse,json,time,hashlib
import numpy as np
import mpmath as mp
from q_local_checkpoint import QLocalCheckpoint
from q_mp_primitives import MPQPrimitives,mf,guard_digits
from independent_dynamic_spectrum import CanonicalCompression,utc,sha


def pack(x,digits=60):
 if isinstance(x,np.ndarray):return pack(x.tolist(),digits)
 if isinstance(x,dict):return {k:pack(v,digits)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [pack(v,digits)for v in x]
 if isinstance(x,(mp.mpf,mp.mpc)):
  if isinstance(x,mp.mpc):return [mp.nstr(x.real,digits),mp.nstr(x.imag,digits)]
  return mp.nstr(x,digits)
 if isinstance(x,(complex,np.complexfloating)):return [float(x.real),float(x.imag)]
 if isinstance(x,np.floating):return float(x)
 return x


def make_q(root,name,u,N,M,t,C=3.,L=1.,P=None):
 p=root/(name+'.npz');np.savez_compressed(p,u=u,N=N,M=M,tk=t,basis='local',cl=C,L=L,p=1/(1-1/C)if P is None else P)
 return QLocalCheckpoint(p)


def prepare(root,tag):
 if tag.startswith('producer_'):
  name=tag.removeprefix('producer_');base=Path('../numerics/artifacts/data/dr_spectra_export');meta=json.loads((base/'META.json').read_text())[name]
  source=base/(name+'.npz');frozen=root/'export.npz';frozen.write_bytes(source.read_bytes());(root/'META.json').write_text(json.dumps(meta,indent=2)+'\n')
  with np.load(frozen,allow_pickle=False)as f:
   N,M,C=meta['N'],meta['M'],meta['C'];t=f['tk'].copy();u=f['u'].copy();v=f['eigvec_coef'].copy();jv=f['Jv_coef'].copy();ee=f['lambda_lead'].ravel();ev=complex(ee[0])if len(ee)==1 else complex(*ee); theta=f['theta_fine'].copy()
   mode=f['eigvec_modevalues'];r=f['rR'];weight=r[:,None]*(1-t[:,None])/2*np.sin(theta)[None,:]
   dens=weight*(mode@np.cos(2*np.arange(M)[:,None]*theta[None,:]));ix=np.unravel_index(np.argmax(abs(dens)),dens.shape);peak=[float(r[ix[0]]*np.cos(theta[ix[1]])),float(r[ix[0]]*np.sin(theta[ix[1]]))]
  q=make_q(root,'background',u,N,M,t,C);qs=[make_q(root,'direction_'+part,getattr(v,part),N,M,t,C)for part in ['real','imag']]
  jqs=[make_q(root,'producer_Jv_'+part,getattr(jv,part),N,M,t,C)for part in ['real','imag']]
  info=dict(kind='producer',source=str(source.resolve()),source_sha256=sha(source),metadata=meta,lambda_value=pack(ev),peak_point=peak,producer_sample_density_sup=float(np.max(abs(dens))))
 else:
  name=tag.removeprefix('own_');base=Path('research/independent_dynamic_spectrum/verification')/name;meta=json.loads((base/'AUDIT.json').read_text());source=base/'order20_feedbackTrue.npz'
  N,M,C=meta['N'],meta['M'],3.
  with np.load(source,allow_pickle=False)as f:
   t=f['t'].copy();theta=f['theta'].copy();ev=complex(f['eigenvalues'][0]);r=np.sqrt((1+t)/2)/(1-t)**(1/(1-1/C))
   if 'leading_full_vectors' in f.files:v=f['leading_full_vectors'][:,0].copy()
   else:
    z=f['eigenvectors'][:,0];parts=[];lo=0
    for k in range(M):V=f[f'V{k}'];hi=lo+V.shape[1];parts.append(V@z[lo:hi]);lo=hi
    v=np.concatenate(parts)
  if name.startswith('constant'):
   u=np.zeros(len(v));u[0]=1.;q=make_q(root,'background',u,N,M,t,C)
  else:
   sourceq=QLocalCheckpoint(base/'literal_background.npz');sourceq.save_snapshot(root/'background.npz');q=QLocalCheckpoint(root/'background.npz')
  qs=[make_q(root,'direction_'+part,getattr(v,part),N,M,t,C)for part in ['real','imag']];jqs=None
  rr,tt=np.meshgrid(r[1:],theta,indexing='ij');xx=rr*np.cos(tt);yy=rr*np.sin(tt);dens=qs[0].rho(xx,yy)+1j*qs[1].rho(xx,yy);ix=np.unravel_index(np.argmax(abs(dens)),dens.shape);peak=[float(xx[ix]),float(yy[ix])]
  info=dict(kind='verifier',source=str(source.resolve()),source_sha256=sha(source),lambda_value=pack(ev),peak_point=peak,own_sample_density_sup=float(np.max(abs(dens))))
 return q,qs,jqs,ev,info


def double_fields(q,points,order):
 # SVD-free shell: only the independently defined scalar evaluator is used here.
 m=CanonicalCompression.__new__(CanonicalCompression);m.N=q.N;m.M=q.M;m.C=q.cl;m.L=q.L;m.kappa=q.kappa;m.delta=1/q.kappa;m.log_core=np.log(q.L)-q.kappa*np.log(2.);m.t=q.tk
 p=np.array(points);x,y=p.T;r=np.hypot(x,y);theta=np.arctan2(y,x);lr=np.log(r);t,s,w=m.stable_coordinates(lr);B=np.zeros(len(r));Bt=B.copy();Ba=B.copy();ur=B.copy();ut=B.copy();c=0.
 for k,cc in enumerate(q.coeff):
  if not np.any(cc):continue
  if q.basis=='cheb':
   from q_local_checkpoint import exact_affine_chebyshev
   tk=Fr(float(m.t[k]));cc=np.array(list(map(float,exact_affine_chebyshev(cc,(1-tk)/2,(1+tk)/2))))
  co=cc[:,None];H,Ht=m.mode_fields(k,t,co);B+=H[:,0]*np.cos(2*k*theta);Bt+=Ht[:,0]*np.cos(2*k*theta);Ba+=-2*k*H[:,0]*np.sin(2*k*theta)
  u,v=m.polar_inverse(k,co,lr,theta,order);ur+=u[np.arange(len(r)),np.arange(len(r)),0];ut+=v[np.arange(len(r)),np.arange(len(r)),0];c+=float(m.strain(k,co)[0])
 Q=w+2*m.kappa*s;Z=1-2*s/Q;T=4*s*w/Q;dr=w*np.sin(theta)*(Z*B+T*Bt);da=w*(np.cos(theta)*B+np.sin(theta)*Ba)
 gx=np.cos(theta)*dr-np.sin(theta)*da;gy=np.sin(theta)*dr+np.cos(theta)*da;ux=r*(ur*np.cos(theta)-ut*np.sin(theta));uy=r*(ur*np.sin(theta)+ut*np.cos(theta));rho=y*w*B
 gx[x==0]=0.;ux[x==0]=0.;rho[y==0]=0.;gx[y==0]=0.;uy[y==0]=0.
 return dict(rho=rho,gradient=np.array([gx,gy]).T,U=np.array([ux,uy]).T,c=c)


def df(point,B,H,cB,cH,C):
 x,y=point;cw=-cB/(C-1);cx=C*cw;gx,gy=H['gradient'];bx,by=B['gradient'];ux,uy=B['U'];vx,vy=H['U']
 return cw*H['rho']-(cx*x+ux)*gx-(cx*y+uy)*gy-vx*bx-vy*by-cH/(C-1)*(B['rho']-C*(x*bx+y*by))


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tags',default='producer_const64,producer_const96,producer_stall64');ap.add_argument('--digits',default='65,95');args=ap.parse_args();top=Path('research/eigenvector_canonical_audit/verification');top.mkdir(parents=True,exist_ok=True)
 for tag in args.tags.split(','):
  root=top/tag;root.mkdir(exist_ok=True);start=time.monotonic();q,qs,jqs,ev,info=prepare(root,tag)
  points=[(.5,.5),(3.,0.),(0.,3.),(6.,8.),(30.,40.),tuple(info['peak_point']),(.137,.219),(.025,.034)]
  out=dict(started_utc=utc(),status='RUNNING',code_sha256=sha(__file__),proof_sha256=sha(top.parent/'PROOF.md'),tag=tag,info=info,points=points,quadrature=[],multiprecision=[],scope='Selected pointwise canonical DF evaluations; no continuum spectral theorem.')
  def save():(root/'AUDIT.json').write_text(json.dumps(pack(out),indent=2)+'\n')
  save();allq=[q]+qs
  for order in [12,20]:
   fields=[double_fields(qq,points,order)for qq in allq];rows=[]
   for i,pt in enumerate(points):
    b={k:(v if k=='c' else v[i])for k,v in fields[0].items()};hr={k:(v if k=='c'else v[i])for k,v in fields[1].items()};hi={k:(v if k=='c'else v[i])for k,v in fields[2].items()};h={k:hr[k]+1j*hi[k]for k in hr}
    val=df(pt,b,h,b['c'],h['c'],q.cl);rows.append(dict(point=pt,background=b,direction=h,DF=val,canonical_eigen_residual=val-ev*h['rho']))
   out['quadrature'].append(dict(order=order,rows=rows));save()
  exact=[qq.exact_coefficients()for qq in allq+(jqs or [])]
  for digits in map(int,args.digits.split(',')):
   work=digits+max(guard_digits(qq.N,qq.M,qq.kappa)for qq in allq+(jqs or []))
   with mp.workdps(work):
    models=[MPQPrimitives(co,Fr(qq.L),Fr(qq.kappa),Fr(qq.cl))for qq,co in zip(allq+(jqs or []),exact)];rows=[];lam=mp.mpc(mf(ev.real),mf(ev.imag))
    for i,pt in enumerate(points):
     xy=list(map(mf,pt));vals=[mm.at(*xy)for mm in models];b=vals[0];hr,hi=vals[1:3];h={k:hr[k]+1j*hi[k]for k in ['rho']};h.update({k:[u+1j*v for u,v in zip(hr[k],hi[k])]for k in ['gradient','U']});ch=models[1].c+1j*models[2].c
     val=df(xy,b,h,models[0].c,ch,mf(q.cl));double=out['quadrature'][-1]['rows'][i];ref=complex(double['DF']);err=abs(val-mp.mpc(mf(ref.real),mf(ref.imag)))
     row=dict(point=pt,background={k:b[k]for k in ['rho','gradient','U']},direction=h,c_background=models[0].c,c_direction=ch,DF=val,canonical_eigen_residual=val-lam*h['rho'],double_DF_absolute_error=err)
     if jqs:
      pj=vals[3]['rho']+1j*vals[4]['rho'];row.update(producer_projected_Jv=pj,canonical_minus_producer_projected_Jv=val-pj,producer_projected_eigen_residual=pj-lam*h['rho'])
     rows.append(pack(row,digits))
    out['multiprecision'].append(dict(digits=digits,work_digits=work,rows=rows));save()
   print(json.dumps(dict(utc=utc(),tag=tag,digits=digits,elapsed=time.monotonic()-start)),flush=True)
  out.update(status='COMPUTED',finished_utc=utc(),elapsed_seconds=time.monotonic()-start);save()
if __name__=='__main__':main()
