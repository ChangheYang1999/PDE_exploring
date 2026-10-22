"""Independent physical Cartesian differences of scalar Psi and Theta.

No fitted derivatives or mixed-coordinate jets. The caller supplies scalar
physical values only. Omega is defined as minus the differenced Laplacian, so
this module does not independently test Poisson inversion or its gauge.
"""
from fractions import Fraction as F
from math import factorial
import numpy as np
LD=np.longdouble

def rational_stencils(radius=4):
 nodes=list(range(-radius,radius+1));n=len(nodes);out={}
 for order in range(1,5):
  a=[[F(x**j) for x in nodes]+[F(factorial(order) if j==order else 0)] for j in range(n)]
  for j in range(n):
   pivot=next(k for k in range(j,n) if a[k][j]);a[j],a[pivot]=a[pivot],a[j]
   div=a[j][j];a[j]=[v/div for v in a[j]]
   for k in range(n):
    if k!=j:
     factor=a[k][j];a[k]=[v-factor*w for v,w in zip(a[k],a[j])]
  w=[row[-1] for row in a]
  for j in range(n):assert sum(v*F(x**j) for v,x in zip(w,nodes))==(factorial(order) if j==order else 0)
  out[order]=np.array([LD(v.numerator)/LD(v.denominator) for v in w],dtype=LD)
 return out
WEIGHTS=rational_stencils()

def difference(values,order,axis,radius=4):
 """Symmetric pairs cancel constants and parity zeros before accumulation."""
 if order==0:return np.take(values,radius,axis=axis)
 center=np.take(values,radius,axis=axis);total=np.zeros_like(center,dtype=LD)
 for k in range(1,radius+1):
  plus=np.take(values,radius+k,axis=axis);minus=np.take(values,radius-k,axis=axis)
  part=plus-minus if order%2 else (plus-center)+(minus-center)
  total+=WEIGHTS[order][radius+k]*part
 return total

def ratios(r,n):
 r=abs(np.asarray(r,dtype=LD));n=np.asarray(n,dtype=LD);out=np.full(r.shape,np.inf,dtype=LD)
 np.divide(r,n,out=out,where=n>0);out[(r==0)&(n==0)]=0
 return out,{'floor':None,'zero_over_zero':int(np.sum((r==0)&(n==0))),'nonzero_over_zero':int(np.sum((r!=0)&(n==0))),'nonfinite':int(np.sum(~np.isfinite(r)|~np.isfinite(n))),'positive_normalizers_below_binary64_normal':int(np.sum((n>0)&(n<np.finfo(float).tiny)))}

def assemble(points,beta,d):
 """Assemble the original and parity-continued equations from Cartesian derivatives."""
 x,y=np.asarray(points,dtype=LD).T;b=LD(beta);U1=-d['Psi_y'];U2=d['Psi_x'];W1=b*x+U1;W2=b*y+U2
 om=-d['Psi_xx']-d['Psi_yy'];ox=-d['Psi_xxx']-d['Psi_xyy'];oy=-d['Psi_xxy']-d['Psi_yyy'];gxy=-d['Psi_xxxy']-d['Psi_xyyy']
 tx,ty,th=d['Theta_x'],d['Theta_y'],d['Theta'];wx=b-d['Psi_xy'];wy=b+d['Psi_xy']
 TT=np.stack([W1*tx,W2*ty,-(b-2)*th],axis=-1);OT=np.stack([W1*ox,W2*oy,om,-tx],axis=-1)
 rt=TT.sum(axis=-1);ro=OT.sum(axis=-1);nt=abs(TT).sum(axis=-1);no=abs(OT).sum(axis=-1)
 DT=np.zeros_like(TT);DO=np.zeros_like(OT)
 offy=y!=0;offx=x!=0;off=offx&offy
 DT[offy]=TT[offy]/y[offy,None]
 # Exact continuous y-axis factor cancellation for a temperature odd in y.
 z=~offy;DT[z]=np.stack([W1[z]*d['Theta_xy'][z],wy[z]*ty[z],-(b-2)*ty[z]],axis=-1)
 DO[off]=OT[off]/(x[off]*y[off])[:,None]
 z=offx&(~offy);DO[z]=np.stack([W1[z]*gxy[z]/x[z],wy[z]*oy[z]/x[z],oy[z]/x[z],-d['Theta_xy'][z]/x[z]],axis=-1)
 z=(~offx)&offy;DO[z]=np.stack([wx[z]*ox[z]/y[z],W2[z]*gxy[z]/y[z],ox[z]/y[z],-d['Theta_xx'][z]/y[z]],axis=-1)
 z=(~offx)&(~offy);DO[z]=np.stack([wx[z]*gxy[z],wy[z]*gxy[z],gxy[z],-d['Theta_xxy'][z]],axis=-1)
 out=dict(Theta=th,Psi=d['Psi'],U1=U1,U2=U2,W1=W1,W2=W2,Omega=om,Omega_x=ox,Omega_y=oy,Omega_xy=gxy,
          Theta_x=tx,Theta_y=ty,R_Theta=rt,N_Theta=nt,R_Omega=ro,N_Omega=no,
          D_Theta=DT.sum(axis=-1),ND_Theta=abs(DT).sum(axis=-1),D_Omega=DO.sum(axis=-1),ND_Omega=abs(DO).sum(axis=-1),
          c_from_physical_Psi=d['Psi_xy'],W1_x=wx,W2_y=wy,Theta_xxy=d['Theta_xxy'])
 summary={}
 for key,den in [('R_Theta','N_Theta'),('R_Omega','N_Omega'),('D_Theta','ND_Theta'),('D_Omega','ND_Omega')]:
  rat,meta=ratios(out[key],out[den]);out[key+'_ratio']=rat
  summary[key]={'max_abs':float(np.max(abs(out[key]))),'max_ratio':float(np.max(rat)),'zero_handling':meta}
 return out,summary

def evaluate(scalars,points,beta,hrel,batch=16):
 pts=np.asarray(points,dtype=LD);n=len(pts);h=LD(str(hrel))*np.maximum(LD(1),np.sqrt(np.sum(pts*pts,axis=1)));nodes=np.arange(-4,5,dtype=LD)
 derivatives={};diagnostics=[]
 specs={'Psi':[(0,0,''),(1,0,'_x'),(0,1,'_y'),(2,0,'_xx'),(1,1,'_xy'),(0,2,'_yy'),(3,0,'_xxx'),(2,1,'_xxy'),(1,2,'_xyy'),(0,3,'_yyy'),(3,1,'_xxxy'),(1,3,'_xyyy')],
        'Theta':[(0,0,''),(1,0,'_x'),(0,1,'_y'),(2,0,'_xx'),(1,1,'_xy'),(2,1,'_xxy')]}
 for start in range(0,n,batch):
  p=pts[start:start+batch];hs=h[start:start+batch];xx=p[:,0,None,None]+hs[:,None,None]*nodes[None,:,None];yy=p[:,1,None,None]+hs[:,None,None]*nodes[None,None,:]
  xx,yy=np.broadcast_arrays(xx,yy);values,diag=scalars(xx,yy);diagnostics.append(diag)
  for field,orders in specs.items():
   v=np.asarray(values[field],dtype=LD)
   for dx,dy,suffix in orders:
    key=field+suffix
    if key not in derivatives:derivatives[key]=np.empty(n,dtype=LD)
    z=difference(v,dx,1);z=difference(z,dy,1);z=z/hs**(dx+dy)
    derivatives[key][start:start+len(p)]=z
 out,summary=assemble(pts,beta,derivatives);out.update({'points':pts,'h':h});summary.update({'hrel':float(hrel),'stencil':'9x9 tensor Cartesian, exact rational uniform weights; symmetric paired differences','axis_residuals':'continuous extension of original Cartesian term sums divided by y or xy; fourth physical Psi derivatives on axes','inverse_diagnostics':diagnostics,'elliptic_check':'NOT independent: Omega defined by the same differenced Laplacian; no E or canonical-inverse verdict'})
 return out,summary,derivatives
