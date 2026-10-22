"""All-mode residual samples via independent density moments; no numerics code imports."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,time,hashlib,resource,bisect,itertools
import numpy as np
from pathlib import Path
from fractions import Fraction as F
from types import SimpleNamespace
from datetime import datetime,timezone
from flint import arb,ctx,fmpq,fmpq_mat
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from exact_audit import exact_poly
sys.path.insert(0,str(BASE/'research/exponential_moments/code'))
from moments import aa,phi
E=BASE/'research/residual_samples/evidence'
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import export_ball
def utc():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact(v):return F.from_float(float.fromhex(v))
def fq(v):return fmpq(v.numerator,v.denominator)
def dyad(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def out(x):return {'display':x.str(34),'lower_exact':str(dyad(x.lower())),'upper_exact':str(dyad(x.upper()))}

def setup():
 path=BASE/'data_exact/modal_v2.json';assert sha(path)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 raw=json.loads(path.read_text());ar=raw['arrays'];M,nb=ar['S']['shape'];t=[exact(v) for v in ar['knots']['hex']];sc={k:exact(v) for k,v in raw['scalars_hex'].items()};k,bi,bo=(sc[v] for v in ('k','bi','bo'));cl=1/aa(k)
 assert raw['degree']==7 and t[:8]==[t[0]]*8 and t[-8:]==[t[-1]]*8 and len(t)==nb+8
 assert all(t[i]<t[i+1] for i in range(7,nb)) and 0<k<1 and bi>0
 alpha=[k-3-j*(1-k)-2*l for j,l in raw['outer_jl']]
 def get(name,m,j):return exact(ar[name]['hex'][m*ar[name]['shape'][1]+j])
 weights=[{} for _ in range(M+2)]
 for m in range(M):
  for f in (1+2*m,1-2*m,3+2*m,3-2*m):
   j=(abs(f)-1)//2;weights[j][m]=weights[j].get(m,F(0))+F(1 if f>0 else -1,8)
 weights=[{m:w for m,w in row.items() if w} for row in weights];assert weights[-1]=={}
 sd=[[sum((w*get('S',m,l) for m,w in ws.items()),F(0)) for ws in weights] for l in range(nb)]
 def jets(c,kn,right):
  result=[]
  for p in range(7,0,-1):
   result.append(c[-1] if right else c[0]);c=[p*(c[i+1]-c[i])/(kn[i+p+1]-kn[i+1]) for i in range(len(c)-1)];kn=kn[1:-1]
  return result
 def corr(J,P,b):return [sum(((-b)**(i-l)*(J[l]-P[l])/math.factorial(l)/math.factorial(i-l) for l in range(i+1)),F(0)) for i in range(7)]
 zpath=BASE/'research/modal_repair/evidence/independent_gauss_iv.json';zr=json.loads(zpath.read_text())['values']['A00_correction'];z=aa(F(zr['lower_exact_dyadic'])).union(aa(F(zr['upper_exact_dyadic'])))
 inn=[];outer=[]
 for j,ws in enumerate(weights):
  C=ws.get(0,F(0));D=[sum((w*get('D',m,l) for m,w in ws.items()),F(0)) for l in range(7)];A=[sum((w*get('Aout',m,l) for m,w in ws.items()),F(0)) for l in range(len(alpha))]
  ji=jets([sd[l][j] for l in range(8)],t[:16],False);jo=jets([sd[l][j] for l in range(nb-8,nb)],t[-16:],True)
  pi=[sum((D[l]*(2*l+2)**v for l in range(7)),C if v==0 else F(0)) for v in range(7)];po=[sum((A[l]*alpha[l]**v for l in range(len(alpha))),F(0)) for v in range(7)]
  ei=corr(ji,pi,bi);eo=[aa(v) for v in corr(jo,po,-bo)];A=[aa(v) for v in A];A[0]+=aa(C)*z
  for l in range(7):eo[l]-=aa(C*(alpha[0]+bo)**l/F(math.factorial(l)))*z
  inn.append((C,D,ei));outer.append((A,eo))
 ns=range(1,M+2);iv=[];jv=[]
 for n in ns:
  m=2*n;C,D,ei=inn[n-1];A,eo=outer[n]
  assert all(m-4-v>0 for v in alpha) and m-4+bo>0
  iv.append(aa(C/F(m+4)+sum((D[l]/(m+6+2*l) for l in range(7)),F(0))+sum((ei[l]*(-1)**l*math.factorial(l)/(m+4+bi)**(l+1) for l in range(7)),F(0))))
  jv.append(sum((A[l]/aa(m-4-alpha[l]) for l in range(len(alpha))),arb(0))+sum((eo[l]*math.factorial(l)/aa(m-4+bo)**(l+1) for l in range(7)),arb(0)))
 return dict(t=t,sc=sc,M=M,nb=nb,sd=sd,iv=iv,jv=jv,zpath=zpath)
