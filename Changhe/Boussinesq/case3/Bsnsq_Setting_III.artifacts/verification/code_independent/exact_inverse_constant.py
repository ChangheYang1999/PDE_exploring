"""Exact rational weighted-spline integral certificate, packet104.

Only rational arithmetic establishes bounds. NumPy is used solely to read and
reconstruct the binary archive schema. No numerical quadrature is used.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import comb
from functools import lru_cache
from datetime import datetime,timezone
import json,hashlib,time,argparse,resource,io
from exact_temperature_certificate import spline_span
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
BITS=120; NLOG=48; NEXP=32

def down(q,bits=BITS):
 d=1<<bits;return Q(q.numerator*d//q.denominator,d)
def up(q,bits=BITS):return -down(-q,bits)
def roundout(pair):return down(pair[0]),up(pair[1])
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def recip(a):
 assert 0<a[0]<=a[1];return 1/a[1],1/a[0]
def ser(a):return [str(v) for v in a]

def log_series(h):
 assert 0<=h<=Q(1,3)
 h2=h*h;power=h;total=Q(0)
 for n in range(NLOG):total+=2*power/(2*n+1);power*=h2
 return roundout((total,total+2*power/((2*NLOG+1)*(1-h2))))
LOG2=log_series(Q(1,3))

def logbound(v):
 assert 0<v<=1
 if v==1:return Q(0),Q(0)
 w=v;k=0
 while w<1:w*=2;k+=1
 assert 1<=w<2
 return roundout(minus(log_series((w-1)/(w+1)),scale(LOG2,Q(k))))

def exp_positive(x):
 assert x>=0
 y=x;m=0
 while y>Q(1,2):y/=2;m+=1
 term=Q(1);total=Q(1)
 for j in range(1,NEXP+1):term=term*y/j;total+=term
 first=term*y/(NEXP+1)
 ans=roundout((total,total+first/(1-y/(NEXP+2))))
 for _ in range(m):ans=roundout((ans[0]**2,ans[1]**2))
 return ans

@lru_cache(maxsize=10000)
def powerbound(v,a):
 assert 0<=v<=1 and 0<a<1
 if v in[0,1]:return v,v
 x=scale(logbound(v),-a)
 # Roundoff enclosure can straddle zero arbitrarily close to v=1.
 x=(max(Q(0),x[0]),max(Q(0),x[1]))
 lower_exp=exp_positive(x[0]);upper_exp=exp_positive(x[1])
 return roundout((1/upper_exp[1],1/lower_exp[0]))

def validate(data):
 assert data['source']=='self'
 b=Q(data['basis_beta']);L=Q(data['L']);assert 2<b<3 and L>0
 assert Q(data['beta'])==b
 knots=[Q(v) for v in data['knots']];d=data['degree'];c=[Q(v) for v in data['coefficients']]
 assert isinstance(d,int) and d>=2 and knots[0]==0 and knots[-1]==1
 assert all(a<=b for a,b in zip(knots,knots[1:]))
 assert knots.count(Q(0))==d+1 and knots.count(Q(1))==d+1
 assert all(knots.count(q)<=d-1 for q in set(knots) if 0<q<1)
 assert len(c)==len(knots)-d-1
 return b,L,knots,d,c

def archive_check(data):
 import numpy as np
 path=Path(data['archive_path']);buf=path.read_bytes();assert hashlib.sha256(buf).hexdigest()==data['archive_sha256']
 with np.load(io.BytesIO(buf),allow_pickle=False) as a:
  K=int(a['K']);Nt=int(a['Nt']);degree=int(a['deg']);grade=float(a['grade'])
  assert K>=3 and str(a['rmap'].item())=='r2' and str(a['scheme'].item())=='mask'
  assert int(a['mreg'])==2 and Nt>=1 and grade>0
  for name in ['cG','beta','beta_basis','L','grade']:assert a[name].dtype==np.dtype('float64')
  assert a['cG'].shape in[(K*(Nt+degree),),(K,Nt+degree)] and a['cG'].flags.c_contiguous
  declared={item.split(':',1)[0]:item.split(':',1)[1] for item in a['code_sha256'].tolist()}
  assert declared['bq3core.py']==data['source_core_sha256']
  assert hashlib.sha256(Path(data['source_core_path']).read_bytes()).hexdigest()==data['source_core_sha256']
  assert Q.from_float(float(a['beta_basis']))==Q(data['basis_beta'])
  assert Q.from_float(float(a['beta']))==Q(data['beta'])
  assert Q.from_float(float(a['L']))==Q(data['L']) and degree==data['degree']
  knots=np.concatenate((np.zeros(degree),np.linspace(0,1,Nt+1)**grade,np.ones(degree)))
  assert [Q.from_float(float(x)) for x in knots]==[Q(x) for x in data['knots']]
  raw=a['cG'].reshape(K,Nt+degree)
  assert raw[2,0]==0  # All four target archives also store this masked slot as zero.
  expected=[Q.from_float(float(raw[0,j]))-(Q(0) if j<1 else Q.from_float(float(raw[2,j]))/2) for j in range(Nt+degree)]
  assert expected==[Q(x) for x in data['coefficients']]
 return data['archive_sha256']

def export(archive,path):
 import numpy as np
 archive=archive.resolve();buf=archive.read_bytes()
 with np.load(io.BytesIO(buf),allow_pickle=False) as a:
  K=int(a['K']);Nt=int(a['Nt']);d=int(a['deg']);grade=float(a['grade'])
  knots=np.concatenate((np.zeros(d),np.linspace(0,1,Nt+1)**grade,np.ones(d)))
  raw=a['cG'].reshape(K,Nt+d)
  co=[Q.from_float(float(raw[0,j]))-(Q(0) if j<1 else Q.from_float(float(raw[2,j]))/2) for j in range(Nt+d)]
  data={'schema':'exact-scalar-spline-v1','source':'self','archive_path':str(archive),'archive_sha256':hashlib.sha256(buf).hexdigest(),'source_core_path':str(Path('verification/fixed_velocity_block_20261021T0056/source_snapshots/bq3core.py').resolve()),'source_core_sha256':'79128784b725d66fc429759272ead3c616bf93846952daf187fc7bed96eaa89f','beta':str(Q.from_float(float(a['beta']))),'basis_beta':str(Q.from_float(float(a['beta_basis']))),'L':str(Q.from_float(float(a['L']))),'degree':d,'knots':[str(Q.from_float(float(x))) for x in knots],'coefficients':[str(x) for x in co],'scalar_rule':'exact rational C0 minus masked C2/2; not a rounded floating subtraction'}
 validate(data);archive_check(data);path.write_text(json.dumps(data,indent=2)+'\n')
 return data

def evaluate(data):
 b,L,knots,d,c=validate(data);a=3-b
 inp={'degree':d,'knots':data['knots'],'coefficients':[data['coefficients']]}
 integral=(Q(0),Q(0));cells=[];endpoint=None;power_records={}
 for span in range(d,len(knots)-d-1):
  if knots[span]==knots[span+1]:continue
  A,B,ps=spline_span(inp,span);p=ps[0];width=B-A
  if endpoint is None:endpoint=(p.get((0,0),Q(0)),p.get((1,0),Q(0))/width)
  # Substitute u=(1-A-z)/width in S_tt. All global z powers exact.
  coeff={}
  for (i,j),v in p.items():
   assert j==0
   if i<2:continue
   v=v*i*(i-1)/width**i
   for k in range(i-1):coeff[k]=coeff.get(k,Q(0))+v*comb(i-2,k)*(1-A)**(i-2-k)*(-1)**k
  lo=1-B;hi=1-A;plo=powerbound(lo,a);phi=powerbound(hi,a)
  power_records[str(lo)]=ser(plo);power_records[str(hi)]=ser(phi)
  val=(Q(0),Q(0))
  for j,cj in coeff.items():val=plus(val,scale(minus(scale(phi,hi**j),scale(plo,lo**j)),cj/(a+j)))
  val=roundout(val);integral=plus(integral,val)
  cells.append({'span':span,'z_interval':[str(lo),str(hi)],'integral':ser(val)})
 assert endpoint is not None
 boundary=endpoint[1]-(b-2)*endpoint[0]
 bracket=roundout(plus(integral,(boundary,boundary)))
 constant=roundout(scale(bracket,-b*L*L/(2*(b-1)*(b-2))))
 verdict='NEGATIVE' if constant[1]<0 else 'POSITIVE' if constant[0]>0 else 'OPEN'
 return {'parameters':{'bits':BITS,'log_terms':NLOG,'exp_degree':NEXP},'power_bounds':power_records,'cells':cells,'S0':str(endpoint[0]),'Sprime0':str(endpoint[1]),'integral':ser(integral),'bracket':ser(bracket),'constant_C2':ser(constant),'sign':verdict}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('certificate',type=Path);ap.add_argument('--archive',type=Path);ap.add_argument('--check',action='store_true');args=ap.parse_args();start=time.monotonic()
 if args.archive:assert not args.check;export(args.archive,args.input)
 data=json.loads(args.input.read_text());validate(data);archive_check(data)
 result=evaluate(data);sha=hashlib.sha256(args.input.read_bytes()).hexdigest()
 if args.check:
  cert=json.loads(args.certificate.read_text());assert cert['input_sha256']==sha and cert['result']==result
 else:
  cert={'created_utc':datetime.now(timezone.utc).isoformat(),'input_sha256':sha,'result':result}
  args.certificate.write_text(json.dumps(cert,indent=2)+'\n')
 elapsed=time.monotonic()-start
 summary={'utc':datetime.now(timezone.utc).isoformat(),'verdict':('CONFIRMED_' if args.check else 'COMPUTED_')+result['sign'],'elapsed_seconds':elapsed,'C2_interval':result['constant_C2'],'C2_interval_float':[float(Q(x)) for x in result['constant_C2']],'archive_sha256':data['archive_sha256'],'input_sha256':sha,'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'spline_code_sha256':hashlib.sha256(Path(__file__).with_name('exact_temperature_certificate.py').read_bytes()).hexdigest()}
 args.certificate.with_suffix('.check.json' if args.check else '.compute.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
