"""Independent exact Laurent check; standard library and no imported fitting code."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, struct, time, zipfile
ZERO=(F(0),F(0));ONE=(F(1),F(0));I=(F(0),F(1))
def cadd(a,b):return (a[0]+b[0],a[1]+b[1])
def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,b):return (a[0]*b,a[1]*b)
def padd(*terms):
 out={}
 for factor,p in terms:
  for n,c in p.items():out[n]=cadd(out.get(n,ZERO),scale(c,factor))
 return {n:v for n,v in out.items() if v!=ZERO}
def pmul(a,b):
 out={}
 for n,c in a.items():
  for m,d in b.items():out[n+m]=cadd(out.get(n+m,ZERO),cmul(c,d))
 return {n:v for n,v in out.items() if v!=ZERO}
def deriv(p):return {n:(-n*v[1],n*v[0]) for n,v in p.items() if n}
def npy(z,name):
 raw=z.read(name+'.npy');assert raw[:6]==b'\x93NUMPY'
 version=raw[6:8];size=2 if version[0]==1 else 4;hlen=int.from_bytes(raw[8:8+size],'little')
 header=ast.literal_eval(raw[8+size:8+size+hlen].decode('latin1'));assert not header['fortran_order']
 assert header['descr'] in ['<f8','=f8'],header
 vals=[F.from_float(x[0]) for x in struct.iter_unpack('<d',raw[8+size+hlen:])]
 return header['shape'],vals

def endpoint(shape,vals,first):
 m,n=shape;out={}
 for ell in range(m):
  value=sum((vals[ell*n+j]*((-1)**j)*(-2*j*j if first else 1) for j in range(n)),F(0))
  if ell==0:out[0]=(value,F(0))
  else:out[2*ell]=out[-2*ell]=(value/2,F(0))
 return out

def decode_certificate(poly):
 out={}
 for n,v in poly.items():
  n=int(n);c=F(int(v['numerator']),int(v['denominator']))
  out[n]=(F(0),-c/2);out[-n]=(F(0),c/2)
 return {n:v for n,v in out.items() if v!=ZERO}

def main():
 start=time.monotonic();certpath=Path('runs/tail_rational_certificate.json');cert=json.loads(certpath.read_text());rows=[]
 x={1:(F(1,2),F(0)),-1:(F(1,2),F(0))};y={1:(F(0),F(-1,2)),-1:(F(0),F(1,2))}
 for row in cert['rows']:
  path=Path('data/control_snapshots')/(row['tag']+'.npz');raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==row['snapshot_sha256']
  with zipfile.ZipFile(path) as z:
   sha,ca=npy(z,'ca');shg,cg=npy(z,'cG');_,betas=npy(z,'beta');_,lengths=npy(z,'L');_,maps=npy(z,'beta_map')
  beta=betas[0];assert beta in [F(2),F(3)] and maps[0]==beta and lengths==[F(1)] and sha==shg
  d=1/beta;q=1-2*d;a=2-d;xy=pmul(x,y);xxy=pmul(x,xy)
  t0=pmul(xxy,endpoint(sha,ca,False));t1=pmul(xxy,endpoint(sha,ca,True))
  o0=pmul(xy,endpoint(shg,cg,False));o1=pmul(xy,endpoint(shg,cg,True))
  p={n:scale(c,1/(n*n-a*a)) for n,c in o0.items()};ur=padd((-1,deriv(p)));up=padd((a,p))
  dt=padd((q,pmul(ur,t0)),(1,pmul(up,deriv(t0))),(-1,t1))
  do=padd((-d,pmul(ur,o0)),(1,pmul(up,deriv(o0))),(-q,pmul(x,t0)),(1,pmul(y,deriv(t0))),(-1,o1))
  checks={}
  for label,poly in [('thermal',dt),('vorticity',do)]:
   c=row['certificates'][label];expected=decode_certificate(c['sine_coefficients']);assert poly==expected,(row['tag'],label)
   assert all(v[0]==0 for v in poly.values()) and 0 not in poly
   n=c['largest_coefficient_frequency'];value=-2*poly[n][1]
   saved=c['largest_coefficient'];assert value==F(int(saved['numerator']),int(saved['denominator']))
   assert abs(value)==max(abs(2*v[1]) for k,v in poly.items())
   bound=c['sup_lower_bound_rational'];assert F(int(bound['numerator']),int(bound['denominator']))==F(3,4)*abs(value)>0
   checks[label]={'all_coefficients_identical':True,'positive_sine_modes':sum(k>0 for k in poly),'largest_mode':n,'bound_exact_match':True}
  rows.append({'tag':row['tag'],'source_sha256':row['snapshot_sha256'],'checks':checks})
 out={'timestamp':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'method':'Independent standard-library NPZ/NPY parser, exact complex-rational Laurent convolution and i*n differentiation','interpretation':cert['interpretation'],'certificate_sha256':hashlib.sha256(certpath.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,'verdict':'PASS'}
 Path('runs/tail_laurent_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
