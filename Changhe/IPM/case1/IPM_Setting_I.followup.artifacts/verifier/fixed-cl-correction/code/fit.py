"""Independent fixed-parameter quadratic residual fit, with a moment constraint."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,copy,time
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import least_squares
from numpy.polynomial.legendre import leggauss
from numpy.polynomial.chebyshev import chebval
ROOT=Path(__file__).resolve().parents[1];P=ROOT.parent/'sampled-physical-actions'
sys.path.insert(0,str(ROOT.parent/'inverse/code'))
from collocation import NodalDensity
from linearized import direction_coefficients
from density import gradient_fd
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'Independent finite fit at fixedcl,C. No continuum residual bound, center regularity or endpoint.','states':[]}
actions=json.loads((P/'refinement4096/actions.json').read_text());grads=json.loads((P/'verification/gradients_chainrule.json').read_text());pts=np.array(actions['points']);n=len(pts)
assert actions['complete'] and grads['complete']

def moments(d,allco,nang,order,panel):
 th=(np.arange(nang)+.5)*np.pi/(2*nang);s=d.map_inverse(th)
 aw=(np.cos(2*np.arange(d.M)[:,None]*s[None,:])@(2/nang*np.cos(th)**2*np.sin(th)*np.sin(3*th)))
 cc=np.einsum('rmk,m->rk',allco,aw)
 edges=np.linspace(np.log(1e-7),np.log(1e30),int(np.ceil(np.log(1e37)/panel))+1);z,w=leggauss(order);t=((edges[:-1,None]+edges[1:,None])/2+np.diff(edges)[:,None]*z/2).ravel();rw=(np.diff(edges)[:,None]*w/2).ravel();r=np.exp(t);lb=np.log1p((r/d.L)**2);q=-np.expm1(-.5*(1-d.k)*lb)
 return chebval(2*q-1,cc)@(rw*r*r*np.exp(.5*(d.k-3)*lb))

for st in actions['states']:
 tag=st['tag'];name='dnB_n96m40S.npz' if tag=='n96m40S' else 'dnSB_n120m48.npz';src=P/'data'/name;d=NodalDensity(src);(ROOT/'data'/name).write_bytes(src.read_bytes())
 V=np.load(P/'data'/('directions_'+tag+'.npz'))['V'];constraints=V[-2:].copy();constraints/=np.linalg.norm(constraints,axis=1)[:,None];H=null_space(constraints);assert H.shape==(14,12) and np.max(abs(V[-2:]@H))<1e-13
 nodal=V[:-2]@H;co=direction_coefficients(d,V)@H
 mc=moments(d,np.concatenate((d.co[:,:,None],co),axis=2),2048,24,.12);mf=moments(d,np.concatenate((d.co[:,:,None],co),axis=2),4096,32,.08)
 rows=st['rows'];gg=next(s for s in grads['states'] if s['tag']==tag);rho=np.array([r['rho'] for r in rows]);g=np.array(gg['base_gradient']);U=np.array([r['base_U'] for r in rows]);W=d.cl*pts+U
 dr=np.array([r['delta_rho'] for r in rows])@H;dg=np.einsum('nik,ia->nak',np.array(gg['delta_gradient']),H);du=np.einsum('nik,ia->nak',np.array([r['delta_U'] for r in rows]),H)
 N=abs(rho)+np.sum(abs(W*g),axis=1);den=N*np.sqrt(n);r0=np.sum(W*g,axis=1)-rho
 linear=np.einsum('nak,nk->na',dg,W)+np.einsum('nak,nk->na',du,g)-dr
 quadratic=np.einsum('nak,nbk->nab',du,dg)
 D=dr/(1+abs(rho[:,None]))/np.sqrt(n);Q,T=np.linalg.qr(D,mode='reduced');sv=np.linalg.svd(D,compute_uv=False);assert sv[-1]>1e-10*sv[0]
 ti=np.linalg.solve(T,np.eye(12));ell=mf[1:]@ti;defect=3*d.cl-1-mf[0];a0=defect*ell/(ell@ell);Z=null_space(ell[None]);C=ti@Z;c0=ti@a0;assert Z.shape==(12,11)
 def calc(b):
  c=c0+C@b;rv=r0+linear@c+np.einsum('nab,a,b->n',quadratic,c,c)
  return rv/den
 def jac(b):
  c=c0+C@b;J=linear+np.einsum('nab,b->na',quadratic+quadratic.transpose(0,2,1),c)
  return (J@C)/den[:,None]
 # Check the polynomial Jacobian with central coefficient differences.
 test=np.linspace(-1,1,11)*1e-4;v=np.cos(np.arange(11));eps=1e-6;je=float(np.max(abs((calc(test+eps*v)-calc(test-eps*v))/(2*eps)-jac(test)@v)));assert je<1e-8
 rr={'tag':tag,'state_md5':d.md5,'parameter_constraints_max':float(np.max(abs(V[-2:]@H))),'moment_base_coarse_fine':mc[:1].tolist()+mf[:1].tolist(),'moment_direction_max_refinement':float(np.max(abs(mc-mf))),'identity_initial_defect':float(defect),'metric_condition':float(sv[0]/sv[-1]),'minimum_particular_shape_norm':float(np.linalg.norm(a0)),'Jacobian_difference':je,'baseline_R_fixedN_RMS':float(np.linalg.norm(r0/den)),'baseline_R_actualN_max':float(max(abs(r0/N))),'fits':[]}
 fits=[]
 for radius in [.005,.02,.05]:
  lim=radius/np.sqrt(11);t=time.monotonic();res=least_squares(calc,np.zeros(11),jac=jac,bounds=(-lim,lim),ftol=1e-13,xtol=1e-13,gtol=1e-13,max_nfev=2000)
  c=c0+C@res.x;newrho=rho+dr@c;newg=g+np.einsum('nak,a->nk',dg,c);newU=U+np.einsum('nak,a->nk',du,c);newW=d.cl*pts+newU;R=np.sum(newW*newg,axis=1)-newrho;newN=abs(newrho)+np.sum(abs(newW*newg),axis=1)
  assert np.max(abs(R/den-calc(res.x)))<1e-12 and abs(mf[1:]@c-defect)<1e-12
  B=d.b.copy();B[1:]+=(nodal@c).reshape(d.N,d.M);assert np.array_equal(B[0],d.b[0])
  filename=tag+'_radius'+str(radius)+'.npz';raw={k:v for k,v in np.load(src).items()};raw['b']=B;np.savez_compressed(ROOT/'data'/filename,**raw)
  # Reconstruction is independent of the saved derivative action formula.
  nd=NodalDensity(ROOT/'data'/filename);errrho=max(abs(float(nd(*pt))-val) for pt,val in zip(pts,newrho));errg=max(float(np.max(abs(gradient_fd(nd,*pt,relative_step=1/32000)-grad))) for pt,grad in zip(pts,newg))
  assert errrho<1e-8 and errg<1e-5
  row={'radius':radius,'success':bool(res.success),'status':int(res.status),'optimality':float(res.optimality),'nfev':res.nfev,'coefficients_in12shape_basis':c.tolist(),'coefficients_in14original':(H@c).tolist(),'whitened_free_coefficients':res.x.tolist(),'shape_norm':float(np.linalg.norm(D@c)),'moment_identity_defect':float(defect-mf[1:]@c),'fit_R_fixedN_RMS':float(np.linalg.norm(R/den)),'fit_R_actualN_max':float(max(abs(R/newN))),'fit_R_actualN_RMS':float(np.linalg.norm(R/newN)/np.sqrt(n)),'sample_density_min':float(newrho.min()),'node_b_range':[float(B.min()),float(B.max())],'reconstruction_density_difference':float(errrho),'reconstruction_gradient_difference':float(errg),'filename':filename,'md5':nd.md5,'seconds':time.monotonic()-t}
  rr['fits'].append(row);fits.append((row, R,newrho,newg,newU));print(tag,radius,row['fit_R_fixedN_RMS'],row['fit_R_actualN_max'],row['shape_norm'],row['node_b_range'],flush=True)
 chosen=min(range(len(fits)),key=lambda i:fits[i][0]['fit_R_fixedN_RMS']);rr['selected']=fits[chosen][0]['filename'];row,R,newrho,newg,newU=fits[chosen]
 np.savez_compressed(ROOT/'verification'/(tag+'_fit_arrays.npz'),H=H,nodal=nodal,co=co,points=pts,rho=rho,gradient=g,U=U,dr=dr,dg=dg,du=du,moments=mf,linear=linear,quadratic=quadratic,denominator=N,D=D,T=T,selected_R=R,selected_rho=newrho,selected_gradient=newg,selected_U=newU,selected_original_coefficients=np.array(row['coefficients_in14original']))
 out['states'].append(rr);(ROOT/'verification/fits.json').write_text(json.dumps(out,indent=2)+'\n')
out['complete']=True;(ROOT/'verification/fits.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',flush=True)
