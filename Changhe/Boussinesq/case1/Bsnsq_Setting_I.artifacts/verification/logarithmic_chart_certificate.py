"""Exact rational interval/Bernstein global-chart certificate for beta3 G.
Soundness statement: research/logarithmic_chart_certificate/PROOF.md.
Only complete finite trees prove positivity. No PDE or inverse conclusion.
"""
from fractions import Fraction as F
from math import comb,lcm
from pathlib import Path
from functools import lru_cache
import argparse,datetime,hashlib,json,time
import numpy as np
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
class I:
 def __init__(self,a,b=None):
  if isinstance(a,I):self.a,self.b=a.a,a.b
  else:self.a,self.b=F(a),F(a if b is None else b)
  if self.a>self.b:raise ValueError('reversed interval')
 def __add__(self,o):
  o=I(o);return I(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,o):return self+-I(o)
 def __rsub__(self,o):return I(o)+-self
 def __mul__(self,o):
  o=I(o);v=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b];return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=I(o)
  if o.a<=0<=o.b:raise ValueError('interval division across zero')
  return self*I(1/o.b,1/o.a)
 def __rtruediv__(self,o):return I(o)/self
 def __pow__(self,n):
  if not isinstance(n,int) or n<0:raise ValueError('nonnegative integer power only')
  if n==0:return I(1)
  if n%2:return I(self.a**n,self.b**n)
  return I(0 if self.a<=0<=self.b else min(self.a**n,self.b**n),max(self.a**n,self.b**n))
 def text(self):return [str(self.a),str(self.b)]
def dyadic_enclosure(a,bits=160):
 # Directed exact rounding, using integer floor and ceiling.
 a=I(a);d=2**bits
 return I(F((a.a*d).__floor__(),d),F((a.b*d).__ceil__(),d))
@lru_cache(maxsize=32768)
def exp_enclosure(u,N=80):
 u=F(u)
 if u<0:return 1/exp_enclosure(-u,N)
 if u>=N+2:raise ValueError('Taylor geometric bound condition')
 a=F(1);s=a
 for j in range(1,N+1):a*=u/j;s+=a
 tail=a*u/(N+1)/(1-u/F(N+2))
 return dyadic_enclosure(I(s,s+tail))
def transcendental(alpha,tl,th,N=80):
 ea=exp_enclosure(alpha,N);den=1-1/ea
 if den.a<=0:raise ValueError('Increase exponential order to separate denominator from zero')
 b=I(exp_enclosure(alpha*tl,N).a,exp_enclosure(alpha*th,N).b)
 T=(1-1/b)/den;T=I(max(F(0),T.a),min(F(1),T.b))
 ell=-(b-1)/(6*alpha);ell2=b*(b-1)/(36*alpha)
 return tuple(dyadic_enclosure(a) for a in (T,ell,ell2))

def cheb_power(n):
 c=[[1]]
 if n:c.append([-1,2])
 for j in range(1,n):
  r=[0]*(j+2)
  for i,v in enumerate(c[-1]):r[i]-=2*v;r[i+1]+=4*v
  for i,v in enumerate(c[-2]):r[i]-=v
  c.append(r)
 return c

def cheb_to_bernstein_matrix(n):
 polys=cheb_power(n);b=[]
 for i in range(n+1):
  b.append([sum(F(a*comb(i,r),comb(n,r)) for r,a in enumerate(polys[j]) if r<=i) for j in range(n+1)])
 d=1
 for row in b:
  for v in row:d=lcm(d,v.denominator)
 return [[int(v*d) for v in row] for row in b],d

def root_bernstein(c):
 n,m=len(c)-1,len(c[0])-1;u,du=cheb_to_bernstein_matrix(n);v,dv=cheb_to_bernstein_matrix(m);dc=1
 for row in c:
  for q in row:dc=lcm(dc,q.denominator)
 a=[[int(q*dc) for q in row] for row in c]
 mid=[[sum(u[i][j]*a[j][k] for j in range(n+1)) for k in range(m+1)] for i in range(n+1)]
 b=[[sum(mid[i][k]*v[l][k] for k in range(m+1)) for l in range(m+1)] for i in range(n+1)]
 return b,du*dv*dc

def split_curve(b):
 # Binomial midpoint identities, common denominator multiplied by2^n.
 n=len(b)-1
 left=[sum(comb(i,j)*b[j] for j in range(i+1))*2**(n-i) for i in range(n+1)]
 right=[sum(comb(n-i,j)*b[i+j] for j in range(n-i+1))*2**i for i in range(n+1)]
 return left,right

def split(b,d,axis):
 n,m=len(b)-1,len(b[0])-1
 if axis==0:
  cc=[split_curve([b[i][j] for i in range(n+1)]) for j in range(m+1)]
  return [[cc[j][0][i] for j in range(m+1)] for i in range(n+1)],[[cc[j][1][i] for j in range(m+1)] for i in range(n+1)],d*2**n
 rr=[split_curve(row) for row in b]
 return [r[0] for r in rr],[r[1] for r in rr],d*2**m

def derivative_arrays(b):
 n,m=len(b)-1,len(b[0])-1
 p={(0,0):b}
 p[1,0]=[[n*(b[i+1][j]-b[i][j]) for j in range(m+1)] for i in range(n)] if n else [[0]]
 p[0,1]=[[m*(b[i][j+1]-b[i][j]) for j in range(m)] for i in range(n+1)] if m else [[0]]
 p[2,0]=[[n*(n-1)*(b[i+2][j]-2*b[i+1][j]+b[i][j]) for j in range(m+1)] for i in range(n-1)] if n>=2 else [[0]]
 p[0,2]=[[m*(m-1)*(b[i][j+2]-2*b[i][j+1]+b[i][j]) for j in range(m-1)] for i in range(n+1)] if m>=2 else [[0]]
 p[1,1]=[[n*m*(b[i+1][j+1]-b[i+1][j]-b[i][j+1]+b[i][j]) for j in range(m)] for i in range(n)] if n and m else [[0]]
 return p

def polynomial_bounds(b,d,ht,hw):
 out={}
 for (i,j),a in derivative_arrays(b).items():
  den=d*ht**i*hw**j;out[i,j]=I(F(min(min(r) for r in a))/den,F(max(max(r) for r in a))/den)
 return out

def q_bound(p,T,l,l2,wl,wh):
 w=I(wl,wh);v=w**3;z0=1-T**6-v
 if z0.b<0:raise ValueError('Outside cell must be discarded before Q bound')
 z=I(max(F(0),z0.a),min(F(1),z0.b))
 C0=1+(2*z+6*v)/3-F(8,3)*z*v
 Cw=w*(2-2*z/3-2*v+F(8,3)*z*v)
 Cww=-F(4,3)*z*(1-v)*w*w
 Ct=(2*z+6*v-4*z*v)*l+12*z*v*l2
 Ctw=4*z*w*l*(1-2*v);Ctt=12*z*v*l*l
 return C0*p[0,0]+Cw*p[0,1]+Cww*p[0,2]+Ct*p[1,0]+Ctw*p[1,1]+Ctt*p[2,0]

def direct_cheb(c,t,w):
 def rec(x,n):
  a=[F(1)]
  if n:a.append(2*x-1)
  for _ in range(2,n+1):a.append(2*(2*x-1)*a[-1]-a[-2])
  return a
 a=rec(t,len(c)-1);b=rec(w,len(c[0])-1)
 return sum(c[i][j]*a[i]*b[j] for i in range(len(c)) for j in range(len(c[0])))
def bernstein_value(b,d,t,w):
 n,m=len(b)-1,len(b[0])-1
 tt=[comb(n,i)*t**i*(1-t)**(n-i) for i in range(n+1)];ww=[comb(m,j)*w**j*(1-w)**(m-j) for j in range(m+1)]
 return sum(b[i][j]*tt[i]*ww[j] for i in range(n+1) for j in range(m+1))/d

def validate_root(c,b,d):
 points=[(F(0),F(0)),(F(1),F(0)),(F(1,3),F(2,5)),(F(1),F(1))]
 for t,w in points:assert direct_cheb(c,t,w)==bernstein_value(b,d,t,w)
 return {'exact_rational_point_checks':len(points),'scope':'Finite input/transformation check; root identity follows from the algebraic construction, with an independent replay required.'}

def certify(c,alpha,out,max_seconds=240,max_nodes=32768,N=80):
 start=time.monotonic();out=Path(out);out.mkdir(parents=True,exist_ok=True)
 b,d=root_bernstein(c);rootcheck=validate_root(c,b,d)
 h=direct_cheb(c,F(1),F(0));root={'utc':now(),'coefficients':[[str(q) for q in row] for row in c],'alpha':str(alpha),'bernstein_numerators':[[str(q) for q in row] for row in b],'denominator':str(d),'source_code_sha256':sha(__file__),'center':str(h),'self_check':rootcheck,'N':N}
 (out/'input.json').write_text(json.dumps(root,indent=2)+'\n')
 stack=[('',F(0),F(1),F(0),F(1),b,d)];leaves=[];visited=0;lo=None;depth=0
 report={'start_utc':now(),'input_sha256':sha(out/'input.json'),'verdict':'OPEN','scope':'Complete exact rational tree proves positive global chart only. No PDE or canonical inverse conclusion.'}
 def store(final=False):
  report.update(utc=now(),visited=visited,remaining=len(stack),leaves=leaves,seconds=time.monotonic()-start,max_depth=depth,lower_bound=str(lo) if not stack and h>0 else None,verdict='CONFIRMED_CHART' if not stack and h>0 else ('REFUTED_POSITIVE_CHART' if h<=0 else 'OPEN'))
  tmp=out/'certificate.tmp';tmp.write_text(json.dumps(report,indent=2)+'\n');tmp.replace(out/'certificate.json')
 if h<=0:store(True);return report
 while stack and visited<max_nodes and time.monotonic()-start<max_seconds:
  path,tl,th,wl,wh,b,d=stack.pop();visited+=1;depth=max(depth,len(path));T,l,l2=transcendental(alpha,tl,th,N)
  if T.a**6+wl**3>1:
   leaves.append({'path':path,'kind':'outside'});continue
  q=q_bound(polynomial_bounds(b,d,th-tl,wh-wl),T,l,l2,wl,wh)
  if q.a>0:
   lo=q.a if lo is None else min(lo,q.a);leaves.append({'path':path,'kind':'positive','lower':str(q.a)});continue
  axis=len(path)%2;left,right,dd=split(b,d,axis)
  if axis==0:
   mid=(tl+th)/2;stack.extend([(path+'1',mid,th,wl,wh,right,dd),(path+'0',tl,mid,wl,wh,left,dd)])
  else:
   mid=(wl+wh)/2;stack.extend([(path+'3',tl,th,mid,wh,right,dd),(path+'2',tl,th,wl,mid,left,dd)])
  if visited%64==0:
   store();print(json.dumps({'utc':now(),'visited':visited,'remaining':len(stack),'leaves':len(leaves),'max_depth':depth,'seconds':time.monotonic()-start}),flush=True)
 store(True)
 # Sufficient restart data, without replaying completed subtrees. Replay is separate.
 checkpoint={'utc':now(),'input_sha256':sha(out/'input.json'),'pending':[{'path':p,'bounds':list(map(str,[tl,th,wl,wh])),'b':[[str(v) for v in row] for row in b],'d':str(d)} for p,tl,th,wl,wh,b,d in stack]}
 (out/'pending.json').write_text(json.dumps(checkpoint,separators=(',',':'))+'\n')
 return report

def main():
 ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('--out',required=True);ap.add_argument('--max-seconds',type=float,default=240);ap.add_argument('--max-nodes',type=int,default=32768);args=ap.parse_args()
 source=Path(args.source)
 with np.load(source,allow_pickle=False) as a:
  if int(a['m'])!=3 or float(a['beta'])!=3:raise ValueError('beta3 only')
  raw=np.asarray(a['c']);c=raw.reshape(int(a['J'])+1,int(a['Kw'])+1);alpha=F.from_float(float(a['alpha']))
  if alpha<=0:raise ValueError('This positive-alpha certificate does not cover the limiting alpha0 case')
  coeff=[[F.from_float(float(v)) for v in row] for row in c]
  se=str(F.from_float(float(a['se']))) if 'se' in a.files else '1'
  if F(se)<=0:raise ValueError('Positive se required')
 result=certify(coeff,alpha,args.out,args.max_seconds,args.max_nodes)
 out=Path(args.out);(out/'source.json').write_text(json.dumps({'utc':now(),'source':str(source),'source_sha256':sha(source),'input_sha256':sha(out/'input.json'),'se_exact_binary64':se,'source_dtype':str(raw.dtype),'conversion':'Source numeric values converted to binary64 then interpreted as exact dyadic rationals. Stored se does not enter the positivity formula.'},indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='leaves'}),flush=True)
if __name__=='__main__':main()
