"""Frozen binary64 geometry, exact finite moments and sensitivity accounting."""
from fractions import Fraction as F
import numpy as np
from node_export_inverse_stage import quadrature_parts
from node_export_mp_chunks import decimal_value
MOMENT_NAMES=['Jx','Jxx','Ix_outer','Ixx_outer','Ix_tail','Ixx_tail']
COMPONENT_NAMES=['V1','V2','Phi','dV2dy','tailV1','tailV2']

def frozen_geometry(jet,x,y,p,rule):
 xx,yy,a,b,t,meta=quadrature_parts(x,y,p,rule)
 arrays=[a,b,t];jj=[jet(xx,z[0])for z in arrays]
 node=np.concatenate([z[0]for z in arrays]);weight=np.concatenate([z[1]for z in arrays]);phase=np.concatenate([np.full(len(z[0]),k,dtype=np.int8)for k,z in enumerate(arrays)])
 derivatives=np.concatenate([z[:,[1,3]]for z in jj]);an,aw=a;bn,bw=b;tn,tw=t;ja,jb,jt=jj
 tx=float(tw@jt[:,1]);txx=float(tw@jt[:,3]);Ix=float(bw@jb[:,1])+tx;Ixx=float(bw@jb[:,3])+txx
 Jx=float((aw*an)@ja[:,1]);Jxx=float((aw*an)@ja[:,3]);sx=-1 if x<0 else 1;sy=-1 if y<0 else 1
 v1=-sx*Ix;v2=sy*(Jxx+yy*Ixx);phi=sx*sy*(Jx+yy*Ix)
 if x==0:v1=0.;phi=0.
 if y==0:v2=0.;phi=0.
 reference=np.array([v1,v2,phi,Ixx,-sx*tx,sy*yy*txx])
 return dict(node=node,weight=weight,phase=phase,derivatives=derivatives,reference=reference,metadata=meta,x=np.array(float(x)),y=np.array(float(y)))

def exact_moments(geometry,rows=None):
 n=geometry['node'];w=geometry['weight'];phase=geometry['phase'];dd=geometry['derivatives']
 if rows is not None and len(rows)!=len(n):raise ValueError('MP row count mismatch')
 out=[F(0)for _ in MOMENT_NAMES]
 for i in range(len(n)):
  if phase[i]not in [0,1,2]:raise ValueError('unknown phase')
  gx,gxx=[F(float(v))for v in dd[i]]if rows is None else[decimal_value(v)for v in rows[i]]
  fac=F(float(w[i]));k=int(phase[i])*2
  if k==0:fac*=F(float(n[i]))
  out[k]+=fac*gx;out[k+1]+=fac*gxx
 return dict(zip(MOMENT_NAMES,out))

def exact_components(m,x,y):
 x,y=F(float(x)),F(float(y));sx=-1 if x<0 else 1;sy=-1 if y<0 else 1;yy=abs(y)
 Ix=m['Ix_outer']+m['Ix_tail'];Ixx=m['Ixx_outer']+m['Ixx_tail']
 z=[-sx*Ix,sy*(m['Jxx']+yy*Ixx),sx*sy*(m['Jx']+yy*Ix),Ixx,-sx*m['Ix_tail'],sy*yy*m['Ixx_tail']]
 if x==0:z[0]=F(0);z[2]=F(0)
 if y==0:z[1]=F(0);z[2]=F(0)
 return dict(zip(COMPONENT_NAMES,z))

def compare_decimal_rows(low,high,double,floor,threshold):
 if len(low)!=len(high)or len(high)!=len(double):raise ValueError('row comparison count')
 floor=F(floor);threshold=F(threshold);width=len(high[0]);maxima=[None]*width;errors=[None]*width;zeros=[0]*width;nearzeros=[0]*width;failed=[]
 for i,(a,b,d)in enumerate(zip(low,high,double)):
  if len(a)!=width or len(b)!=width or len(d)!=width:raise ValueError('row comparison width')
  for j in range(width):
   u,v=decimal_value(a[j]),decimal_value(b[j]);q=F(float(d[j]));delta=abs(u-v);ratio=delta/max(abs(v),floor);error=abs(v-q);den=max(abs(v),abs(q));pure=error/den if den else None
   if maxima[j]is None or ratio>maxima[j][0]:maxima[j]=(ratio,i,delta)
   if errors[j]is None or (pure if pure is not None else F(0))>errors[j][0]:errors[j]=((pure if pure is not None else F(0)),i,error,den==0)
   zeros[j]+=int(v==0);nearzeros[j]+=int(abs(v)<floor)
   if ratio>threshold:failed.append([i,j,str(ratio)])
 return dict(precision_maxima=[dict(component=j,index=i,relative=str(v),absolute=str(a))for j,(v,i,a)in enumerate(maxima)],double_pure_relative_maxima=[dict(component=j,index=i,relative=str(v),absolute=str(a),both_zero=zero)for j,(v,i,a,zero)in enumerate(errors)],zero_counts=zeros,nearzero_counts=nearzeros,precision_failed_entries=failed,precision_diagnostic_passed=not bool(failed),count=len(high),floor=str(floor),threshold=str(threshold),scope='Finite recorded decimal comparisons, not certified errors.')
