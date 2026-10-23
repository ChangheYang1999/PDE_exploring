"""Independent exact arithmetic for finite arrays. No producer or candidate imports."""
from fractions import Fraction as F
from pathlib import Path
import math,json,gzip,hashlib,re
import numpy as np
COMPONENTS=['V1','V2','Phi','dV2dy','tailV1','tailV2']
MOMENTS=['Jx','Jxx','Ix_outer','Ixx_outer','Ix_tail','Ixx_tail']
f=lambda z:F.from_float(float(z))
def residual(x,y,j,v):
 g,gx,gy=j[:3];a=(2*x+v[0])*gx;b=(2*y+v[1])*gy
 rr=a+b-g;nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(v[0]*gx+v[1]*gy)
 return [rr,nf,nv,abs(rr)/nf if nf else None,abs(rr)/nv if nv else None]
def same_round(a,b):return (a is None and math.isnan(float(b)))or(a is not None and float(a)==float(b))
def summarize(xy,rr):
 radius=np.hypot(xy[:,0],xy[:,1]);out=[]
 for name,lo,hi in [('r<.1',0,.1),('.1<=r<1',.1,1),('1<=r<100',1,100),('r>=100',100,float('inf'))]:
  ids=[i for i,r in enumerate(radius)if lo<=r<hi];metrics={}
  for name2,k in [('absR',0),('Rf',3),('Rv',4)]:
   valid=[i for i in ids if math.isfinite(float(rr[i,k]))];idx=max(valid,key=lambda i:abs(float(rr[i,k])))if valid else None
   d=dict(index=idx,value=abs(float(rr[idx,k]))if idx is not None else None,defined_count=len(valid),undefined_count=len(ids)-len(valid))
   if idx is not None:d.update(x=float(xy[idx,0]),y=float(xy[idx,1]),fields=[float(z)if math.isfinite(z)else None for z in rr[idx]])
   metrics[name2]=d
  out.append(dict(region=name,count=len(ids),metrics=metrics))
 return out

def discrepancy(a,b):
 d=abs(a-b);den=max(abs(a),abs(b));return dict(absolute=str(d),pure_relative=str(d/den)if den else None,both_zero=not bool(den))
def compare(low,high,double,floor,threshold):
 if not len(low)==len(high)==len(double)>0:raise ValueError('comparison row counts')
 width=len(high[0]);zeros=[0]*width;near=[0]*width;failed=[];pm=[];dm=[]
 for k in range(width):
  p=d=None
  for i in range(len(low)):
   if not len(low[i])==len(high[i])==len(double[i])==width:raise ValueError('comparison widths')
   lo,hi,dd=low[i][k],high[i][k],double[i][k];ab=abs(hi-lo);scaled=ab/max(abs(hi),floor);delta=abs(hi-dd);den=max(abs(hi),abs(dd));rel=delta/den if den else F(0)
   zeros[k]+=int(hi==0);near[k]+=int(abs(hi)<floor)
   if scaled>threshold:failed.append([i,k,str(scaled)])
   if p is None or scaled>F(p['relative']):p=dict(component=k,index=i,relative=str(scaled),absolute=str(ab))
   if d is None or rel>F(d['relative']):d=dict(component=k,index=i,relative=str(rel),absolute=str(delta),both_zero=not bool(den))
  pm.append(p);dm.append(d)
 return dict(precision_maxima=pm,double_pure_relative_maxima=dm,zero_counts=zeros,nearzero_counts=near,precision_failed_entries=sorted(failed,key=lambda z:(z[0],z[1])),precision_diagnostic_passed=not failed,count=len(high),floor=str(floor),threshold=str(threshold))

def decimal(s):
 if not isinstance(s,str)or len(s)>2048 or not re.fullmatch(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?',s):raise ValueError('finite decimal syntax')
 if 'e'in s.lower()and abs(int(s.lower().split('e')[1]))>1000:raise ValueError('finite decimal exponent')
 return F(s)
def read_chunks(directory,total,width,digits,bindings,bind):
 allrows=[];paths=sorted(Path(directory).glob('chunk_*.json.gz'));expected=[f'chunk_{i:07d}.json.gz'for i in range(0,total,64)]
 if [p.name for p in paths]!=expected:raise ValueError('chunk filename coverage')
 for p in paths:
  bind(p);d=json.loads(gzip.decompress(p.read_bytes()));start=len(allrows);stop=min(total,start+64)
  signature=dict(schema='FINITE_MP_DECIMALS_V1',total=total,digits=digits,width=width,chunk_size=64,bindings=bindings,start=start,stop=stop)
  if set(d)!=set(signature)|{'rows','rows_sha256'}or any(d[k]!=v for k,v in signature.items()):raise ValueError('chunk exact signature')
  if type(d['start'])is not int or type(d['stop'])is not int or len(d['rows'])!=stop-start:raise ValueError('chunk interval')
  if hashlib.sha256(json.dumps(d['rows'],separators=(',',':'),ensure_ascii=True).encode()).hexdigest()!=d['rows_sha256']:raise ValueError('chunk digest')
  for row in d['rows']:
   if not isinstance(row,list)or len(row)!=width:raise ValueError('chunk width')
   allrows.append(list(map(decimal,row)))
 if len(allrows)!=total:raise ValueError('incomplete chunks')
 return allrows

def moments(rows,nodes,weights,phases):
 if not(len(rows)==len(nodes)==len(weights)==len(phases)):raise ValueError('moment dimensions')
 positive=[F(0)]*6;negative=positive.copy()
 for row,t,w,phase in zip(rows,nodes,weights,phases):
  if phase not in [0,1,2]or len(row)!=2:raise ValueError('moment phase/width')
  for k,v in enumerate(row):
   z=w*v*(t if phase==0 else 1);i=2*phase+k
   if z>=0:positive[i]+=z
   else:negative[i]+=z
 return [a+b for a,b in zip(positive,negative)],positive,negative

def components(m,y):return [-m[2]-m[4],m[1]+y*(m[3]+m[5]),m[0]+y*(m[2]+m[4]),m[3]+m[5],-m[4],y*m[5]]
def signed_item(p,n):
 if not(p>=0 and n<=0):raise ValueError('signed ledger signs')
 return dict(positive=str(p),negative=str(n),total=str(p+n),sum_absolute=str(p-n),cancellation_ratio=str((p-n)/abs(p+n))if p+n else None)
def ledgers(m,p,n,y):
 if not y>0:raise ValueError('positive target y required')
 formulas=[[(2,-1),(4,-1)],[(1,1),(3,y),(5,y)],[(0,1),(2,y),(4,y)],[(3,1),(5,1)],[(4,-1)],[(5,y)]];cc=[]
 for terms in formulas:
  pp=nn=F(0)
  for i,a in terms:
   if a>=0:pp+=a*p[i];nn+=a*n[i]
   else:pp+=a*n[i];nn+=a*p[i]
  cc.append(signed_item(pp,nn))
 if [F(v['total'])for v in cc]!=components(m,y):raise ArithmeticError('ledger component totals')
 return dict(moments=dict(zip(MOMENTS,[signed_item(a,b)for a,b in zip(p,n)])),components=dict(zip(COMPONENTS,cc)))
def four(x,y,j,jp,v,vp):
 rr00=residual(x,y,j,v)[0];rr10=residual(x,y,jp,v)[0];rr01=residual(x,y,j,vp)[0];rr11=residual(x,y,jp,vp)[0];cross=sum((jp[k+1]-j[k+1])*(vp[k]-v[k])for k in range(2))
 if rr11-rr00!=(rr10-rr00)+(rr01-rr00)+cross:raise ArithmeticError('four-combination cross identity')
 return dict(R00=str(rr00),R10=str(rr10),R01=str(rr01),R11=str(rr11),cross=str(cross))
