"""Fourier Galerkin in angle, continuous piecewise Chebyshev collocation in log r.
Original variables A=rho/r^sigma, G=psi/r^(1+sigma), U=psi_r/r^sigma.
Matching: all A, G, all U except the first even sine harmonic.
"""
import sys, os, json, time, resource
from pathlib import Path
here=Path(__file__).resolve().parent
old=here.parents[1]/'newton_run'
sys.path[:0]=[str(old/'vendor'),str(old/'validation')]
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import splu
from scipy.interpolate import CubicHermiteSpline
from scipy.linalg import qr,solve_triangular
from numpy.polynomial import chebyshev as T
from threadpoolctl import threadpool_limits
threadpool_limits(1)
from nonlinear_bvp import NonlinearOriginProblem
from origin_manifold import evaluate_origin
from audit import eval_side
threadpool_limits(int(os.environ.get('IPM_BLAS_THREADS','1')))
class Angular:
 def __init__(self,c,a,f,g,li,lo):
  self.c,self.a,self.f,self.g,self.li,self.lo=c,a,f,g,li,lo;self.d=f+2*g
  from polar_origin import PolarOrigin
  self.O=PolarOrigin(g,c,a)
  self.delta=1-1/c; self.l=np.arange(1,2*f,2.);self.k=np.arange(2,2*g+1,2.)
  n=6*max(f,g)+12;t=(np.arange(n)+.5)*np.pi/(2*n); s=lambda v:np.sin(np.outer(t,v));c1=lambda v:np.cos(np.outer(t,v))*v
  self.So,self.Co,self.Se,self.Ce=s(self.l),c1(self.l),s(self.k),c1(self.k)
  self.po=self.So.T*(2/n); self.pe=self.Se.T*(2/n)
  self.S0=self.pe@(np.cos(t)[:,None]*self.So);self.S1=self.pe@(np.sin(t)[:,None]*self.Co)
  ki=np.arange(g)[:,None];lii=np.arange(f)[None,:]
  self.S0=.5*((lii==ki).astype(float)+(lii==ki+1))
  self.S1=.5*self.l[None,:]*((lii==ki).astype(float)-(lii==ki+1))
  I=np.arange(f)[:,None];L=np.arange(f)[None,:];K=np.arange(g)[None,:]+1
  def idx(v,n):return np.where((v>=0)&(v<n),v,n)
  self.diff=idx(abs(I-L)-1,g);self.sum=idx(I+L,g);self.sgn=np.sign(I-L)
  self.fm=idx(np.where(I-K<0,K-I-1,I-K),f);self.fp=idx(I+K,f);self.fs=np.where(I-K<0,-1,1)
  self.eq=np.zeros(self.d);self.eq[[0,f,f+g]]=[a,(1-c)/2,1-c]
  gamma=1/c;q=1+gamma;q2=2*gamma;L=np.arange(1,4*max(f,g)+2,2.);K=np.arange(2,4*max(f,g)+3,2.)
  s0=(2/n)*s(K).T@(np.cos(t)[:,None]*s(L));s1=(2/n)*s(K).T@(np.sin(t)[:,None]*c1(L))
  P1=(gamma*s0-s1)/(K[:,None]**2-q*q);P2=((2*gamma-1)*s0-s1)/(K[:,None]**2-q2*q2)
  self.Far=(self.k+q)[:,None]*P1[:g,:f]
  self.PF=(((K+q2)[:,None]*P2-(K+q)[:,None]*P1)[:g]@(2/n*s(L).T))/(c-1)
  self.farq=[c1(K)@P1[:,:f],s(K)@P1[:,:f],s(self.l),c1(self.l)]
 def origin(self,p):
  f,g=self.f,self.g;v=self.O.origin_value(p);r=np.zeros(f+2*g,dtype=v.dtype);r[:min(f,g)]=v[:min(f,g)];r[f:]=v[g:];return r
 def ojac(self,p):
  f,g=self.f,self.g;v=self.O.origin_jac(p);r=np.zeros((f+2*g,len(p)));r[:min(f,g)]=v[:min(f,g)];r[f:]=v[g:];return r
 def farquad(self,A):
  C,S,F,Ft=self.farq;gamma=1/self.c
  return np.exp(-self.delta*self.lo)*(self.PF@(-gamma*(C@A)*(F@A)+(1+gamma)*(S@A)*(Ft@A)))
 def products(self,G,U):
  # Exact triad sums: K multiplies F by G_theta, L multiplies F_theta by U.
  gv=np.pad(G*self.k,((0,0),(0,1)));uv=np.pad(U,((0,0),(0,1)))
  return .5*(gv[:,self.diff]-gv[:,self.sum]),.5*self.l*(self.sgn*uv[:,self.diff]+uv[:,self.sum])
 def ode(self,t,Y,side,jac=False):
  if len(t)>28:
   acc=[self.ode(t[i:i+28],Y[i:i+28],side,jac) for i in range(0,len(t),28)]
   return (np.concatenate([v[0] for v in acc]),np.concatenate([v[1] for v in acc])) if jac else np.concatenate(acc)
  f,g,d=self.f,self.g,self.d;A=Y[:,:f];G=Y[:,f:f+g];U=Y[:,f+g:]
  z=np.exp(-self.delta*t) if side else np.ones(len(t));s=1/self.c if side else 1.;q=1+s
  K,L=self.products(G,U);mass=self.c*np.eye(f)-z[:,None,None]*K
  if side:r=(z[:,None,None]*(s*K-L))@A[...,None];GG,UU,AA=G,U,A
  else:
   GG=G-self.eq[f:f+g];UU=U-self.eq[f+g:];AA=A-self.eq[:f]
   K1,L1=self.products(GG,UU);K0,L0=self.products(self.eq[None,f:f+g],self.eq[None,f+g:])
   r=(K0-L0+(1-self.c)*np.eye(f))@AA[...,None]+(K1-L1)@A[...,None]
  At=np.linalg.solve(mass,r)[...,0]
  v=np.c_[At,UU-q*GG,-q*UU+self.k**2*GG + AA@(self.S1-s*self.S0).T-At@self.S0.T]
  if not jac:return v
  Ma=z[:,None,None]*(s*K-L)+(1-self.c*s)*np.eye(f)
  w=np.pad(s*A+At,((0,0),(0,1)));ap=np.pad(A*self.l,((0,0),(0,1)))
  Mg=z[:,None,None]*.5*self.k*(self.fs*w[:,self.fm]+w[:,self.fp])
  Mu=-z[:,None,None]*.5*(ap[:,self.fm]-ap[:,self.fp])
  jacf=np.linalg.solve(mass,np.concatenate([Ma,Mg,Mu],axis=2))
  J=np.zeros((len(t),d,d));J[:,:f]=jacf;J[:,f:f+g,f:f+g]=-q*np.eye(g);J[:,f:f+g,f+g:]=np.eye(g)
  J[:,f+g:]=-self.S0@jacf;J[:,f+g:,:f]+=self.S1-s*self.S0;J[:,f+g:,f:f+g]+=np.diag(self.k**2);J[:,f+g:,f+g:]+=-q*np.eye(g)
  return v,J
 def bc(self,A,B,C,D,e,jac=False):
  f,g,d=self.f,self.g,self.d;idx=np.r_[np.arange(f+g),np.arange(f+g+1,d)]
  r=np.r_[A-self.origin(e),(B-C)[idx],D[-g:]+self.k*D[f:f+g]-self.Far@D[:f]-self.farquad(D[:f])]
  if not jac:return r
  J=np.zeros((len(r),4*d+g-1));J[:d,:d]=np.eye(d);J[:d,4*d:]=-self.ojac(e)
  J[d:2*d-1,d:2*d]=np.eye(d)[idx];J[d:2*d-1,2*d:3*d]=-np.eye(d)[idx]
  J[-g:,3*d:3*d+f]=-self.Far-np.column_stack([self.farquad(D[:f]+1e-25j*w).imag/1e-25 for w in np.eye(f)])
  J[-g:,3*d+f:3*d+f+g]=np.diag(self.k);J[-g:,3*d+f+g:4*d]=np.eye(g)
  return r,J
def interpolation(p):
 x=(1-np.cos(np.arange(p+1)*np.pi/p))/2
 V=T.chebvander(2*x-1,p);inv=np.linalg.inv(V)
 D=(2*T.chebvander(2*x-1,p-1))@T.chebder(inv,axis=0)
 return x,inv,D
def evalpoly(edge,v,p,t,order=0):
 """Avoid any RHS call; differentiate saved polynomial itself."""
 _,iv,_=interpolation(p);ix=np.clip(np.searchsorted(edge,t,side='right')-1,0,len(edge)-2);h=np.diff(edge)[ix];u=(t-edge[ix])/h
 mat=T.chebvander(2*u-1,p-order)@T.chebder(iv,m=order,axis=0)
 return np.einsum('ij,ijk->ik',mat,v[ix[:,None]*p+np.arange(p+1)])*(2/h[:,None])**order
class Spectral:
 def __init__(self,c=2,a=6,nf=32,ng=32,p=8,mi=20,mo=40,li=4,lo=40):
  self.A=A=Angular(c,a,nf,ng,li,lo);self.p=p;self.mi=mi;self.mo=mo
  hi=np.linspace(0,1,mi+1);ho=np.linspace(0,1,mo+1);self.edges=[-li*np.sinh(2.8*(1-hi))/np.sinh(2.8), lo*np.expm1(4.25*ho)/np.expm1(4.25)]
  xc,_,_=interpolation(p)
  x=np.r_[0.,(np.polynomial.legendre.leggauss(p)[0]+1)/2]
  iv=np.linalg.inv(T.chebvander(2*x-1,p))
  D=2*T.chebvander(2*x[1:]-1,p-1)@T.chebder(iv,axis=0)
  end=T.chebvander([1.],p)@iv
  self.to_c=T.chebvander(2*xc-1,p)@iv;self.Dstage=D;self.end=end.ravel()
  self.x=[];self.D=[];self.h=[];self.stage=[]
  for ed in self.edges:
   h=np.diff(ed);m=len(h)
   z=np.r_[(ed[:-1,None]+h[:,None]*x).ravel(),ed[-1]];self.x.append(z)
   st=np.arange(m)[:,None]*(p+1)+np.arange(1,p+1);self.stage.append(st.ravel());self.h.append(np.repeat(h,p))
   mat0=np.zeros((p+1,p+2));mat0[:p,:p+1]=D;mat0[p,:p+1]=-end;mat0[p,-1]=1
   ii,jj=np.nonzero(mat0);mat=sp.coo_matrix((np.tile(mat0[ii,jj],m),((np.arange(m)[:,None]*(p+1)+ii).ravel(),(np.arange(m)[:,None]*(p+1)+jj).ravel())),shape=(len(z)-1,len(z))).tocsc()
   self.D.append(mat)
  self.lens=[len(x) for x in self.x];vcols=np.array([0,self.lens[0]-1,self.lens[0],sum(self.lens)-1])*A.d
  self.bc_ind=np.r_[(vcols[:,None]+np.arange(A.d)).ravel(),sum(self.lens)*A.d+np.arange(ng-1)]
  self.block=sp.block_diag([sp.kron(s,sp.eye(A.d),format='csc') for s in self.D],format='csc')
 def unpack(self,y):
  d=self.A.d;f,g=self.A.f,self.A.g;li,lo=self.lens
  return y[:li*d].reshape(-1,d),y[li*d:(li+lo)*d].reshape(-1,d),y[(li+lo)*d:]
 def seed(self,file):
  q=np.load(file) if isinstance(file,(str,Path)) else file;A=self.A;f,g=A.f,A.g
  if 'density_green' in q:
   sys.path.insert(0,str(here.parent/'green'));from green import Model as Green
   m=Green.fromfile(q);F=q['F'];a0,b0,*_=m.moments(F,q['eta']);pp=10
   vals=m.fields(F,a0,b0,float(q['h']),interpolation(pp)[0]);fields=np.concatenate([vals[0],vals[2],vals[3]],axis=2)
   dd=dict(c=m.c,a=m.a,nf=m.n,ng=m.n,p=pp)
   for j,side in enumerate(['i','o']):
    raw=fields[j*m.e:(j+1)*m.e];dd['edge_'+side]=m.breaks[j];dd['v_'+side]=np.r_[raw[:,:-1].reshape(-1,3*m.n),raw[-1,-1:]]
   q=dd
  vs=[]
  for j,(z,side) in enumerate(zip(self.x,['i','o'])):
   if 'v_i' in q:
    of,og=int(q['nf']),int(q['ng']);edge=q['edge_'+side];ts=np.clip(z,edge[0],edge[-1]);v=evalpoly(edge,q['v_'+side],int(q['p']),ts)
   else:
    of=og=int(q['n']);o=int(q['m'])+1;s=slice(j*o,(j+1)*o);zz=q['z'][s];ts=np.clip(z,zz[0],zz[-1]);v=CubicHermiteSpline(zz,q['x'][s],q['xdot'][s],axis=0)(ts)
    if 'ref_format' not in q:
     v[:,2*og:]+=2*v[:,og:2*og]
     if j:v*=np.exp((1-1/float(q['c']))*ts)[:,None]
   if j:v=v*np.exp((1/float(q['c'])-1/A.c)*z)[:,None]
   a,b,c=np.split(v,[of,of+og],axis=1);w=np.zeros((len(z),A.d))
   cut=min(f,of);w[:,:cut]=a[:,:cut]
   cut=min(g,og);w[:,f:f+cut]=b[:,:cut];w[:,f+g:f+g+cut]=c[:,:cut];vs.append(w)
  orig=vs[0][0];dens=np.zeros(g);dens[:min(f,g)]=orig[:min(f,g)];yt=np.r_[dens,orig[f:]];e=A.O.origin_Q.T@(yt-A.O.base_origin)
  if ('eta' in q and 'ng' in q and int(q['ng'])==g and float(q['a'])==A.a and float(q['c'])==A.c and A.li==float(q['li']) and str(q.get('origin_chart',''))=='polar_homogeneous'):e=q['eta']
  return np.r_[vs[0].ravel(),vs[1].ravel(),e]
 def calc(self,y,jac=False):
  vi,vo,e=self.unpack(y);A=self.A;d=A.d;parts=[];Js=[]
  for j,v in enumerate([vi,vo]):
   stage=self.stage[j];out=A.ode(self.x[j][stage],v[stage],j,jac);h=self.h[j]
   if jac:
    val,J=out
    # row-block t couples directly only to stage t, plus scalar differentiation stencil.
    data=-J*h[:,None,None];nb=len(h)
    ptr=np.zeros(len(v),dtype=np.int32);ptr[stage]=1;ptr=np.cumsum(ptr,dtype=np.int32)
    mat=sp.bsr_matrix((data,stage.astype(np.int32),ptr),shape=((len(v)-1)*d,len(v)*d)).tocsc()
    mat.eliminate_zeros();Js.append(mat)
   else:val=out
   row=self.D[j]@(v if j else v-A.eq);row[stage-1]-=h[:,None]*val;parts.append(row.ravel())
  B=A.bc(vi[0],vi[-1],vo[0],vo[-1],e,jac)
  if not jac:return np.r_[parts[0],parts[1],B]
  br,B=B;i,j=np.nonzero(B);bc=sp.coo_matrix((B[i,j],(i,self.bc_ind[j])),shape=(len(br),len(y))).tocsc()
  top=self.block+sp.block_diag(Js,format='csc');J=sp.vstack([sp.hstack([top,sp.csc_matrix((top.shape[0],len(e)))]),bc],format='csc')
  return np.r_[parts[0],parts[1],br],J
 def factor(self,y,one_rhs=None,snapshot=None):
  """Eliminate collocation stages locally, then solve a sparse endpoint BVP.
  Factor.solve(b) accepts ordered ODE, continuity and BC rows as in calc().
  """
  import scipy.linalg as la
  p=self.p;A=self.A;d=A.d
  vi,vo,e=self.unpack(y); ids=np.arange(p*d).reshape(p,d);I=np.eye(d);D=self.Dstage
  blocks=[];nr=0;nc=0;Eblocks=[];elist=[]
  def local(z,v,j,h):
   J=A.ode(z,v,j,True)[1]
   if os.environ.get('IPM_REDUCED_STAGES','0')=='1':
    from stage import Reduced
    lu=Reduced(A,J,D[:,1:],h,j);return lu,lu.solve
   B=np.kron(D[:,1:],I);B[ids[:,:,None],ids[:,None,:]]-=h*J
   lu=la.lu_factor(B,overwrite_a=True,check_finite=False);return lu,lambda b:la.lu_solve(lu,b,check_finite=False)
  lowmem=one_rhs is not None and os.environ.get('IPM_LOWMEM','0')=='1'
  for j,V in enumerate([vi,vo]):
   n=len(self.edges[j])-1;grp=[]
   for i,h in enumerate(np.diff(self.edges[j])):
    v=V[i*(p+1)+1:(i+1)*(p+1)];z=self.x[j][i*(p+1)+1:(i+1)*(p+1)]
    lu,solve_local=local(z,v,j,h)
    H=solve_local(np.kron(-D[:,0,None],I))
    H=H.reshape(p,d,d);E=self.end[0]*I+np.einsum('j,jst->st',self.end[1:],H)
    Eblocks.append(-E);elist.append(nc+i)
    if one_rhs is None:grp.append((lu,H))
    else:
     b0=(nr+i)*(p+1)*d
     q=solve_local(one_rhs[b0:b0+p*d]).reshape(p,d);grp.append((q,None if lowmem else H))
   nr+=n;nc+=n+1;blocks.append(grp)
  B=A.bc(vi[0],vi[-1],vo[0],vo[-1],e,True)[1]
  ix=np.r_[(d*np.array([0,self.mi,self.mi+1,nc-1])[:,None]+np.arange(d)).ravel(),nc*d+np.arange(len(e))]
  if one_rhs is not None and snapshot is None and os.environ.get('IPM_QR_ENDPOINTS','0')=='1':
   from endpoint import endpoint
   bs=[];off=0
   for grp in blocks:
    for q,H in grp:
     rows=one_rhs[off:off+(p+1)*d].reshape(p+1,d);off+=(p+1)*d;bs.append(rows[-1]+self.end[1:]@q)
   bs.append(one_rhs[off:]);W0=endpoint(Eblocks,B,bs,[self.mi,self.mo])
   from types import SimpleNamespace
   glu=SimpleNamespace(solve=lambda b:W0)
  else:
   u,v=np.nonzero(B);bc=sp.coo_matrix((B[u,v],(u,ix[v])),shape=(len(B),nc*d+len(e))).tocsc()
   Edata=np.array(Eblocks);Eblocks.clear();ids0=np.asarray(elist,np.int32)
   top=sp.bsr_matrix((Edata,ids0,np.arange(nr+1,dtype=np.int32)),shape=(nr*d,nc*d)).tocsc();del Edata
   ii=np.arange(nr*d);jj=((ids0+1)[:,None]*d+np.arange(d)).ravel()
   top=top+sp.coo_matrix((np.ones(len(ii)),(ii,jj)),shape=top.shape).tocsc()
   B=sp.vstack([sp.hstack([top,sp.csc_matrix((nr*d,len(e)))]),bc],format='csc');del top
   glu=splu(B)
  if snapshot is not None:
   from scipy.sparse.linalg import LinearOperator,onenormest,norm as spnorm
   name=Path(snapshot);sp.save_npz(name.with_suffix('.npz'),B,compressed=True)
   rng=np.random.get_state();np.random.seed(4012)
   try:inv=onenormest(LinearOperator(B.shape,matvec=glu.solve,rmatvec=lambda v:glu.solve(v,'T'),dtype=float))
   finally:np.random.set_state(rng)
   name.with_suffix('.json').write_text(json.dumps(dict(rows=B.shape[0],nnz=B.nnz,norm1=float(spnorm(B,1)),inverse_norm1_est=float(inv),cond1_est=float(spnorm(B,1)*inv),meaning='endpoint Schur complement after eliminating Gauss stages; not the full operator'),indent=2))
  def solve(b):
   off=0;bs=[];Qs=[];vs=[]
   for grp in blocks:
    qs=[]
    for lu,H in grp:
     rows=b[off:off+(p+1)*d].reshape(p+1,d);off+=(p+1)*d
     q=lu if one_rhs is not None else (lu.solve(rows[:p].ravel()) if hasattr(lu,'solve') else la.lu_solve(lu,rows[:p].ravel(),check_finite=False)).reshape(p,d)
     bs.append(rows[-1]+self.end[1:]@q);qs.append(q)
    Qs.append(qs)
   W=glu.solve(np.r_[np.concatenate(bs),b[off:]])
   ends=W[:nc*d].reshape(nc,d);off=0
   for j,(grp,qs) in enumerate(zip(blocks,Qs)):
    for i,((lu,H),q) in enumerate(zip(grp,qs)):
     L=ends[off+i]
     if H is None:
      ss=slice(i*(p+1)+1,(i+1)*(p+1));h=np.diff(self.edges[j])[i];z=self.x[j][ss];vv=[vi,vo][j][ss]
      lu,sl=local(z,vv,j,h);res=sl((-D[:,0,None]*L).ravel()).reshape(p,d)+q
     else:res=H@L+q
     vs.extend([L,res.ravel()])
    vs.append(ends[off+len(grp)]);off+=len(grp)+1
   return np.r_[np.concatenate(vs),W[nc*d:]]
  from types import SimpleNamespace
  return SimpleNamespace(solve=solve)
 def derivatives(self,field,save_fields=False):
  """Differentiate the complete fixed-(c,grid,chart-basis) nonlinear system twice."""
  A=self.A;O=A.O;f,g,d=A.f,A.g,A.d;O.n=g
  y=self.seed(field);vi,vo,e=self.unpack(y);bsize=2*d+g-1;start=len(y)-bsize
  raw=O.free_transform@e
  def trim(a):
   s=np.zeros(d,dtype=a.dtype);s[:min(f,g)]=a[:min(f,g)];s[f:]=a[g:];return s
  da=trim(O.value_jet(raw,1.,np.zeros_like(raw),1))
  fa=np.zeros_like(y);fa[start:start+d]=-da
  b=self.factor(y,one_rhs=-fa);v=b.solve(-fa);del b;v_in,v_out,de=self.unpack(v)
  hess=np.zeros_like(y);off=0
  for side,(X,V) in enumerate(zip([vi,vo],[v_in,v_out])):
   stage=self.stage[side];t=self.x[side][stage];x=X[stage];dr=V[stage]
   # Compute projected Jacobian and Hessian in modest slugs rather than all-node dense matrices.
   herr=np.zeros_like(X[:-1]); chunks=np.array_split(np.arange(len(t)),max(1,int(np.ceil(len(t)/24))))
   for idx in chunks:
    dt=(A.ode(t[idx],x[idx],side,True)[1]@dr[idx,:,None])[:,:,0];z=np.exp(-A.delta*t[idx]) if side else np.ones(len(idx));sig=1/A.c if side else 1.
    K,L=A.products(dr[idx,f:f+g],dr[idx,f+g:]);Kv,_=A.products(x[idx,f:f+g],x[idx,f+g:])
    mass=A.c*np.eye(f)-z[:,None,None]*Kv
    br=2*z[:,None]*((K@(sig*dr[idx,:f]+dt[:,:f])[...,None]-L@dr[idx,:f,None])[:,:,0])
    hf=np.linalg.solve(mass,br[...,None])[...,0]
    hh=np.c_[hf,np.zeros((len(idx),g)),-hf@A.S0.T];herr[stage[idx]-1]=-self.h[side][idx,None]*hh
   hess[off:off+herr.size]=herr.ravel();off+=herr.size
  jet=O.value_jet(raw,1.,O.free_transform@de,2)
  hess[start:start+d]=-trim(jet);hess[-g:]=-2*A.farquad(v_out[-1,:f]);b=self.factor(y,one_rhs=-hess);w=b.solve(-hess);del b;wi,wo,dde=self.unpack(w)
  def apply(u):
   iu,ou,eu=self.unpack(u);pieces=[]
   for j,(X,V) in enumerate([(vi,iu),(vo,ou)]):
    stage=self.stage[j];t=self.x[j][stage];r=self.D[j]@V
    for ix in np.array_split(np.arange(len(t)),max(1,int(np.ceil(len(t)/24)))):
     rs=stage[ix];D=A.ode(t[ix],X[rs],j,True)[1];r[rs-1]-=self.h[j][ix,None]*(D@V[rs,:,None])[:,:,0]
    pieces.append(r.ravel())
   bb=A.bc(vi[0],vi[-1],vo[0],vo[-1],e,True)[1];return np.r_[*pieces,bb@np.r_[iu[0],iu[-1],ou[0],ou[-1],eu]]
  out=dict(Jp=float(v_out[0,f+g]-v_in[-1,f+g]),Jpp=float(wo[0,f+g]-wi[-1,f+g]),res1=float(max(abs(apply(v)+fa))),res2=float(max(abs(apply(w)+hess))),base_res=float(max(abs(self.calc(y)))))
  if save_fields:
   def storev(v):
    elem=v[:-1].reshape(-1,self.p+1,A.d);return np.vstack([(self.to_c@elem)[:,:-1].reshape(-1,A.d),v[-1]])
   out.update(va_i=storev(v_in),va_o=storev(v_out),vaa_i=storev(wi),vaa_o=storev(wo),eta_a=de,eta_aa=dde)
  return out
 def solve(self,file,tol=8e-12,maxit=8,verbose=True):
  A=self.A;y=self.seed(file);hist=[];tm=time.time()
  for it in range(maxit+1):
   r=self.calc(y);err=max(abs(r));hist.append(err)
   if os.environ.get('IPM_CHECKPOINT'):
    cp=Path(os.environ['IPM_CHECKPOINT']);vi0,vo0,eta0=self.unpack(y)
    def save0(v0):
     E=v0[:-1].reshape(-1,self.p+1,A.d);return np.vstack([(self.to_c@E)[:,:-1].reshape(-1,A.d),v0[-1]])
    b0=A.bc(vi0[0],vi0[-1],vo0[0],vo0[-1],eta0);tmp=cp.with_name(cp.stem+'.tmp.npz')
    np.savez_compressed(tmp,c=A.c,a=A.a,nf=A.f,ng=A.g,li=A.li,lo=A.lo,p=self.p,mi=self.mi,mo=self.mo,edge_i=self.edges[0],edge_o=self.edges[1],v_i=save0(vi0),v_o=save0(vo0),eta=eta0,raw=A.O.free_transform@eta0,origin_chart='polar_homogeneous',J=vo0[0,A.f+A.g]-vi0[-1,A.f+A.g],higher=max(abs(vo0[0,A.f+A.g+1:]-vi0[-1,A.f+A.g+1:])),res=err,bc=max(abs(b0)),ok=err<tol,history=hist,seconds=time.time()-tm,iteration=it);tmp.replace(cp)
   if verbose:print('iteration',it,err,'seconds',round(time.time()-tm,2),flush=True)
   if err<tol or it==maxit:break
   lu=self.factor(y,one_rhs=-r);dy=lu.solve(-r);del lu
   for j in range(14):
    trial=y+2**(-j)*dy
    if np.max(abs(self.calc(trial)))<err:y=trial;break
   else:break
  vi,vo,e=self.unpack(y);f,g=A.f,A.g;bc=A.bc(vi[0],vi[-1],vo[0],vo[-1],e)
  def storev(v):
   elem=v[:-1].reshape(-1,self.p+1,A.d);return np.vstack([(self.to_c@elem)[:,:-1].reshape(-1,A.d),v[-1]])
  return dict(qr_endpoint=os.environ.get('IPM_QR_ENDPOINTS','0'),equil_endpoint=os.environ.get('IPM_EQUIL_ENDPOINTS','0'),peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,c=A.c,a=A.a,products='exact_centered',origin_chart='polar_homogeneous',nf=f,ng=g,p=self.p,mi=self.mi,mo=self.mo,li=A.li,lo=A.lo,edge_i=self.edges[0],edge_o=self.edges[1],v_i=storev(vi),v_o=storev(vo),eta=e,raw=A.O.free_transform@e,J=vo[0,f+g]-vi[-1,f+g],higher=max(abs(vo[0,f+g+1:]-vi[-1,f+g+1:])),bc=max(abs(bc)),res=err,history=hist,ok=err<tol,seconds=time.time()-tm)
def audit(d,ns=11,nang=None):
 c=float(d['c']);f,g,p=int(d['nf']),int(d['ng']),int(d['p']); sides={}
 for j,side in enumerate(['i','o']):
  e=d['edge_'+side];v=d['v_'+side]
  def fun(t):
   y=evalpoly(e,v,p,t);dy=evalpoly(e,v,p,t,1);ddy=evalpoly(e,v,p,t,2)
   return y[:,:f],dy[:,:f],y[:,f:f+g],dy[:,f:f+g],ddy[:,f:f+g],y[:,f+g:],dy[:,f+g:]
  # Include left limits of every element to falsify a bad one-sided derivative.
  zz=np.unique(np.r_[e,np.nextafter(e[1:-1],-np.inf)])
  sides[side]=eval_side(zz,fun,f,g,1/c if j else 1.,c,bool(j),4*(f+g)+128 if nang is None else nang,ns)
 return sides
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser()
 for s,default in [('nf',24),('ng',24),('p',8),('mi',16),('mo',32)]:p.add_argument('--'+s,type=int,default=default)
 for s,default in [('c',2.),('a',6.),('li',4.),('lo',40.)]:p.add_argument('--'+s,type=float,default=default)
 p.add_argument('--tol',type=float,default=8.e-12);p.add_argument('--maxit',type=int,default=8);p.add_argument('--seed',default=str(old/'replay/reference/angular32/a6.npz'));p.add_argument('--out',required=True);arg=vars(p.parse_args());seed=arg.pop('seed');out=Path(arg.pop('out'));tol=arg.pop('tol');maxit=arg.pop('maxit');q=Spectral(**arg);d=q.solve(seed,tol=tol,maxit=maxit);np.savez_compressed(out.with_suffix('.npz'),**d)
 s=audit(d);sm={**arg,**{k:float(d[k]) for k in ['J','higher','bc','res','seconds']},'audit':s}
 out.with_suffix('.json').write_text(json.dumps(sm,indent=2));print(json.dumps({k:[s[j][k] for j in s] for k in ['transport','poisson','transport_high','poisson_high']}),flush=True)
