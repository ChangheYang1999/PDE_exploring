"""Independent reversed interval sums and de Casteljau subdivision; no subject imports."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,argparse,time
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction
from math import comb
from datetime import datetime,timezone
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
iv.dps=160
BASE=Path(__file__).resolve().parents[3];OUT=BASE/'research/flow_composition/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def ration(x):return Fraction(float(x))
def point(q):
 q=Fraction(q);return iv.mpf(q.numerator)/q.denominator
def interval(m,r):
 m,r=ration(m),ration(r);assert r>=0
 lo,hi=point(m-r),point(m+r)
 return iv.mpf([lo.a,hi.b])
def magnitude(x):return abs(x).b
def exact_bounds(x):
 values=[]
 for sign,m,e,bits in x._mpi_:
  assert bits>=0
  values.append(Fraction(-int(m) if sign else int(m))*Fraction(2)**int(e))
 assert values[0]<=values[1];return values

def casteljau_range(poly,ell):
 length=2*ell
 global_b=[]
 for k in range(13):
  acc=iv.mpf(0)
  for j in range(k,-1,-1):acc+=poly[j]*length**j*comb(k,j)/comb(12,j)
  global_b.append(acc)
 row=global_b;left=[row[0]];right=[row[-1]]
 for depth in range(12):
  row=[(row[j]+row[j+1])/2 for j in range(len(row)-1)]
  left.append(row[0]);right.append(row[-1])
 ranges=left+right
 return iv.mpf([min(x.a for x in ranges),max(x.b for x in ranges)])
def final_range(q,error,d,ell):
 polys=[[q[0][j]-q[1][j]*d+q[2][j]*d**2 for j in range(13)],
        [q[0][j]-q[2][j]*d**2 for j in range(13)],
        [q[0][j]+q[1][j]*d+q[2][j]*d**2 for j in range(13)]]
 ranges=[casteljau_range(p,ell) for p in polys]
 hull=iv.mpf([min(x.a for x in ranges),max(x.b for x in ranges)])
 return hull+iv.mpf([-error.b,error.b])

def compute(data,angular_index):
 scalar=data['scalar'];h=ration(scalar[0]);width=ration(data['ell'][0]);assert h>0 and width*2>=h
 ell=point(width);d=point(ration(data['d'][angular_index]));powers=[point(ration(x)) for x in scalar[9:22]]
 for j,x in enumerate(scalar[9:22]):assert ration(x)>=h**j
 cl=interval(*data['cl']);mu=interval(*scalar[7:9]);alpha=iv.mpf(129)/20;beta=iv.mpf(307)/100
 rad={};error={};magnitudes={}
 for letter in ('P','R'):
  rad[letter]=[[interval(data[letter+'_mid'][n,j],data[letter+'_rad'][n,j]) for j in range(13)] for n in range(261)]
  error[letter]=[point(ration(x)) for x in data[letter+'_rem']];assert all(ration(x)>=0 for x in data[letter+'_rem'])
  magnitudes[letter]=[]
  for n in range(261):
   v=iv.mpf(0)
   for j in range(12,-1,-1):v+=magnitude(rad[letter][n][j])*powers[j]
   magnitudes[letter].append(v)
 products=[];errors=[]
 for fam,letter in enumerate(('P','R','R')):
  factors=[[interval(data['angular_mid'][angular_index,fam,k,n],data['angular_rad'][angular_index,fam,k,n]) for n in range(261)] for k in range(3)]
  rest=[point(ration(x)) for x in data['angular_rem'][angular_index,fam]];assert all(ration(x)>=0 for x in data['angular_rem'][angular_index,fam])
  sums=[]
  for k in range(3):
   coeffs=[]
   for j in range(13):
    v=iv.mpf(0)
    for n in range(260,-1,-1):v+=factors[k][n]*rad[letter][n][j]
    coeffs.append(v)
   sums.append(coeffs)
  products.append(sums)
  err=iv.mpf(0)
  for n in range(260,-1,-1):
   bound=magnitude(factors[2][n])*d*d+magnitude(factors[1][n])*d+magnitude(factors[0][n])
   err+=rest[n]*magnitudes[letter][n]+error[letter][n]*(rest[n]+bound)
  errors.append(err)
 sp,sc,ss=products;ep,ec,es=errors
 sq=[[-x for x in row] for row in sp];sq[0][0]+=cl
 v1=[[sq[k][j]-ss[k][j] for j in range(13)] for k in range(3)]
 v2=[[sq[k][j]+sc[k][j] for j in range(13)] for k in range(3)]
 tq=[[-alpha*ss[k][j]+beta*sc[k][j]+mu*sq[k][j] for j in range(13)] for k in range(3)];tq[0][0]-=1+cl
 output=[]
 for name,poly,error in [('s',sq,ep),('v1x',v1,ep+es),('v2y',v2,ep+ec),('T0',tq,alpha*es+beta*ec+magnitude(mu)*ep)]:
  value=final_range(poly,error,d,ell);ref=exact_bounds(value);target=[ration(data['target_'+name+'_'+end][angular_index]) for end in ('lo','hi')];assert target[0]<=target[1]
  output.append({'name':name,'reference':[str(x) for x in ref],'target':[str(x) for x in target],'analytic_error_interval':[str(x) for x in exact_bounds(error)],'contained':target[0]<=ref[0] and ref[1]<=target[1],'margins':[str(ref[0]-target[0]),str(target[1]-ref[1])]})
 return {'angular_index':angular_index,'node':data['nodes'][angular_index].tolist(),'ranges':output,'modal_products':3*3*13*261,'degree':12,'radial_subintervals':2}

parser=argparse.ArgumentParser();parser.add_argument('--ci',required=True,type=int,choices=[0,4102,7808]);args=parser.parse_args();start=utc();start_tick=time.monotonic()
path=OUT/f'packet_{args.ci:04d}.npz';prep=json.loads((OUT/'preparation.json').read_text());entry=next(x for x in prep['packets'] if x['ci']==args.ci);assert sha(path)==entry['sha256']
with np.load(path,allow_pickle=False) as z:data={k:z[k] for k in z.files}
for name,a in data.items():assert np.isfinite(a).all(),name
rows=[compute(data,i) for i in range(3)];passed=all(x['contained'] for row in rows for x in row['ranges'])
result={'start_utc':start,'end_utc':utc(),'elapsed_seconds':time.monotonic()-start_tick,'method':'mpmath.iv160 reversed product sums, global radial Bernstein and midpoint de Casteljau subdivision','ci':args.ci,'status':'PASS' if passed else 'OPEN_SUFFICIENT_COMPARISON_FAILED','rows':rows,'packet_sha256':sha(path),'code_sha256':sha(__file__),'preparation_sha256':sha(OUT/'preparation.json')}
dest=OUT/f'iv_{args.ci:04d}.json';assert not dest.exists();dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('end_utc','elapsed_seconds','ci','status')}),flush=True)
