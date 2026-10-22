"""Recompute both disk-bound formulas with the opposite interval arithmetic."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,time,math,argparse
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=220
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def aq(x):x=F(x);return arb(x.numerator)/x.denominator
def iq(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def be(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return m-r,m+r

def ie(x):
 z=[]
 for sign,m,e,b in x._mpi_:assert b>=0;z.append((-1 if sign else 1)*F(int(m))*F(2)**int(e))
 return z

def ae(x):
 z=[]
 for v in [x.lower(),x.upper()]:assert v.is_finite() and v.rad()==0;m,e=v.man_exp();z.append(F(int(m))*F(2)**int(e))
 return z

def decode(v,kind):
 a,b=be(v)
 return aq(a).union(aq(b)) if kind=='arb' else iv.mpf([iq(a).a,iq(b).b])
start=time.monotonic();ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,required=True);args=ap.parse_args();manifest=json.loads((D/'data_exact/manifest.json').read_text());record=next(x for x in manifest['cells'] if x['cell']==args.cell);pins=dict(manifest['files'])
for n,hsh in pins.items():assert sha(B/n)==hsh
sample=next(x for x in json.loads((B/'research/residual_samples/evidence/sample_result.json').read_text())['samples'] if x['cell']==args.cell);tc=F(record['center_exact']);h=F(record['h_exact']);trial=json.loads((B/'data_exact/modal_v2.json').read_text());c=1/F.from_float(float.fromhex(trial['scalars_hex']['k']));outputs={};checks=0
for kind in ['arb','iv']:
 qfun=aq if kind=='arb' else iq;efun=(lambda x:x.exp()) if kind=='arb' else iv.exp;en=ae if kind=='arb' else ie;zero=qfun(0);rad=qfun(4*h);H=[[decode(v,kind) for v in p] for p in sample['density_polynomial_at_point']];I=[decode(v,kind) for v in sample['i']];J=[decode(v,kind) for v in sample['j']]
 # Horner evaluations of nonnegative coefficient sums, independently arranged.
 def norm(poly):
  value=zero
  for v in reversed(poly):value=value*rad+abs(v)
  return value
 C=[norm(p) for p in H];Hp=[[3*p[q]+((q+1)*p[q+1] if q<7 else 0) for q in range(8)] for p in H];Cp=[norm(p) for p in Hp]
 density=[efun(qfun(3*tc+12*h))*v for v in C[:261]];derivative=[efun(qfun(3*tc+12*h))*v for v in Cp[:261]];pb=[];qb=[]
 for n in range(1,262):
  m=2*n
  if kind=='arb':
   ib=efun((m+4)*rad)*(abs(I[n-1])+rad*C[n-1]);jb=efun(abs(m-4)*rad)*(abs(J[n-1])+rad*C[n]);fac=efun(qfun(2*tc+8*h));pb.append(qfun(m)*fac*(ib+jb)/2);qb.append(fac*(m*(ib+jb)+C[n-1]+C[n])/2)
  else:
   s=(H[n-1][0]+H[n][0])/2;a=efun(qfun(4*tc))*(s-m*I[n-1]);b=efun(qfun(4*tc))*(m*J[n-1]-s);gp=[((q+1)*(H[n-1][q+1]+H[n][q+1]) if q<7 else zero)/2+2*(H[n-1][q]+H[n][q])+qfun(m)*(H[n][q]-H[n-1][q])/2 for q in range(8)];g=efun(qfun(4*tc+16*h))*norm(gp);ab=efun(m*rad)*(abs(a)+rad*g);bb=efun(m*rad)*(abs(b)+rad*g);v=efun(qfun(-2*tc+8*h))*(ab+bb)/2;pb.append(v);qb.append(v)
 Bs=[]
 for j in range(6):
  total=sum(((2*a+1)**j*(abs(qfun(c))*derivative[a]+density[a]) for a in range(261)),zero)
  for l in range(j+1):
   pu=sum(((2*n)**l*v for n,v in enumerate(pb,1)),zero);qu=sum(((2*n)**l*v for n,v in enumerate(qb,1)),zero);dt=sum(((2*a+1)**(j-l)*v for a,v in enumerate(derivative)),zero);dr=sum(((2*a+1)**(j-l+1)*v for a,v in enumerate(density)),zero);total+=math.comb(j,l)*(pu*dt+qu*dr)
  Bs.append(total)
 original_kind='iv' if kind=='arb' else 'arb';p=D/'evidence'/('%s_preflight_%d.json'%(original_kind,args.cell));original=json.loads(p.read_text());assert original['cell']==args.cell and original['degree']==64 and original['radius_exact']=='4';bound=[]
 for j,v in enumerate(Bs):
  a,b=en(v);u,w=[F(original['B_j'][j][s]) for s in ['lower_exact','upper_exact']];assert 0<a<=b and max(a,u)<=min(b,w),('B_DISJOINT',kind,j);checks+=1;bound.append({'lower_exact':str(a),'upper_exact':str(b)})
 outputs[kind]={'formula':'density' if kind=='arb' else 'physical_Green','B_j':bound};pins[str(p.relative_to(B))]=sha(p)
for p in [D/'data_exact/manifest.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_OPPOSITE_ARITHMETIC_DISK_MAJORANTS','cell':args.cell,'formula_checks':checks,'results':outputs,'arb_bits':512,'iv_dps':220,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Both analytic disk formulas independently recomputed, all uncertain center inputs inherited.'}
with (D/'evidence'/('disk_audit_%d.json'%args.cell)).open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({k:result[k] for k in ['utc','status','cell','formula_checks','seconds']}))
