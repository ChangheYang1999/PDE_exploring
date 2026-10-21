"""Independent analytic chain rule checks the eighth-order Cartesian stencil."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
import numpy as np
from numpy.polynomial.chebyshev import chebder,chebval2d
from scipy.fft import dct
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification'
sys.path.insert(0,str(ROOT.parent/'inverse/code'))
from collocation import NodalDensity
base=json.loads((OUT/'actions.json').read_text());assert base['complete']
fd=json.loads((OUT/'gradients_refined.json').read_text());assert fd['complete']
pts=np.array(base['points']);x,y=pts.T;n=len(pts)
obj={'date':datetime.now(timezone.utc).isoformat(),'method':'Independent physical chain rule using polynomial coefficient derivatives; no spatial FD.',
     'states':[],'scope':'Computed differentiation-method discrepancy, not interval error bound.'}
for tag,name in [('n96m40S','dnB_n96m40S.npz'),('n120m48_S','dnSB_n120m48.npz')]:
 d=NodalDensity(ROOT/'data'/name);V=np.load(ROOT/'data'/('directions_'+tag+'.npz'))['V'];K=V.shape[1]
 values=np.zeros((d.N+1,d.M,K));values[1:]=V[:-2].reshape(d.N,d.M,K)
 co=dct(values[::-1],type=1,axis=0)/d.N;co[[0,-1]]*=.5;co=dct(co,type=2,axis=1)/d.M;co[:,0]*=.5
 rr=x*x+y*y;D=d.L**2+rr;ell=np.log1p(rr/d.L**2);q=-np.expm1(-.5*(1-d.k)*ell)
 z=2*q-1;s=d.map_inverse(np.arctan2(y,x));c=np.cos(2*s)
 def ev(coef):return chebval2d(z,c,coef)
 b=ev(d.co);bq=ev(2*chebder(d.co,axis=0));bqq=ev(4*chebder(d.co,m=2,axis=0))
 bc=ev(chebder(d.co,axis=1));bqc=ev(2*chebder(chebder(d.co,axis=0),axis=1))
 db=ev(co);dbq=ev(2*chebder(co,axis=0));dbc=ev(chebder(co,axis=1));dk=(-V[-2]/d.cl**2)[:,None]
 B=b-(1-q)*bq;F=db+dk*ell/2*B
 Fq=dbq+dk*ell/2*(2*bq-(1-q)*bqq);Fc=dbc+dk*ell/2*(bc-(1-q)*bqc);Fl=dk*B/2
 pref=x*x*y*np.exp((d.k-3)*ell/2)
 dctheta=-2*np.sin(2*s)/(1+d.beta*np.cos(2*s))
 bg=[];dg=[]
 for axis,coord in enumerate([x,y]):
  ell_j=2*coord/D;q_j=(1-d.k)*(1-q)*coord/D
  theta_j=(-y if axis==0 else x)/rr;c_j=dctheta*theta_j
  logpref_j=(2/x if axis==0 else 1/y)+(d.k-3)*coord/D
  bg.append(pref*(logpref_j*b+bq*q_j+bc*c_j))
  dg.append(pref*(logpref_j*F+Fq*q_j+Fc*c_j+Fl*ell_j))
 bg=np.stack(bg,axis=-1);dg=np.stack(dg,axis=-1).transpose(1,0,2)
 st=next(st for st in base['states'] if st['tag']==tag);gs=next(st for st in fd['states'] if st['tag']==tag)['gradient_steps'][-1]
 assert st['state_md5']==d.md5
 gfd=np.array(gs['base_gradient']);dgfd=np.array(gs['delta_gradient'])
 rows=st['rows'];rho=np.array([r['rho'] for r in rows]);dr=np.array([r['delta_rho'] for r in rows]);du=np.array([r['delta_U'] for r in rows]);W=d.cl*pts+np.array([r['base_U'] for r in rows]);dc=np.array(st['dcl'])
 nf=abs(rho)+np.sum(abs(W*gfd),axis=1)
 def act(g,dg):return (dc[None,:]*np.sum(pts*g,axis=1)[:,None]+np.einsum('ijk,ik->ij',dg,W)+np.einsum('ijk,ik->ij',du,g)-dr)/nf[:,None]/np.sqrt(n)
 AA=act(bg,dg);FF=act(gfd,dgfd);M=np.vstack([dr/(1+abs(rho[:,None]))/np.sqrt(n),dc])
 entry={'tag':tag,'state_md5':d.md5,'base_gradient':bg.tolist(),'delta_gradient':dg.tolist(),
    'max_base_gradient_difference':float(np.max(abs(bg-gfd))),'max_delta_gradient_difference':float(np.max(abs(dg-dgfd))),
    'max_node_unit_action_difference':float(np.max(abs(AA-FF))*np.sqrt(n)),'spaces':{}}
 for kdim in (4,10,14):
  Q,T=np.linalg.qr(M[:,:kdim],mode='reduced');Delta=np.linalg.solve(T.T,(AA-FF)[:,:kdim].T).T
  BB=np.linalg.solve(T.T,AA[:,:kdim].T).T;BF=np.linalg.solve(T.T,FF[:,:kdim].T).T
  entry['spaces'][str(kdim)]={'whitened_difference_Frobenius':float(np.linalg.norm(Delta)),
    'whitened_difference_spectral':float(np.linalg.norm(Delta,2)),
    'maximum_singular_value_difference':float(max(abs(np.linalg.svd(BB,compute_uv=False)-np.linalg.svd(BF,compute_uv=False))))}
 print(tag,entry['max_node_unit_action_difference'],entry['spaces'],flush=True);obj['states'].append(entry)
obj['complete']=True
(OUT/'gradients_chainrule.json').write_text(json.dumps(obj,indent=2)+'\n')
