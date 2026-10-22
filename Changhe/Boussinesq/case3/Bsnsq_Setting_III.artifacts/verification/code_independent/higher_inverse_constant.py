"""Exact N-fold inverse-constant certificate, packet111; no numerical quadrature."""
from fractions import Fraction as Q
from pathlib import Path
from math import comb,factorial,prod
from datetime import datetime,timezone
import argparse,json,hashlib,time
import exact_inverse_constant as base
from exact_temperature_certificate import spline_span

def validate(data):
 assert data['source']=='self'
 b=Q(data['basis_beta']);L=Q(data['L']);N=b.numerator//b.denominator
 assert b>2 and N<b<N+1 and L>0 and Q(data['beta'])==b
 knots=[Q(v)for v in data['knots']];d=data['degree'];c=[Q(v)for v in data['coefficients']]
 assert isinstance(d,int)and d>=N and knots[0]==0 and knots[-1]==1
 assert all(x<=y for x,y in zip(knots,knots[1:]))
 assert knots.count(Q(0))==d+1 and knots.count(Q(1))==d+1
 assert all(knots.count(q)<=d-N+1 for q in set(knots)if 0<q<1)
 assert len(c)==len(knots)-d-1
 return b,L,N,knots,d,c

def export(archive,path):
 import numpy as np
 archive=archive.resolve();buf=archive.read_bytes()
 with np.load(archive,allow_pickle=False)as a:
  K=int(a['K']);Nt=int(a['Nt']);d=int(a['deg']);grade=float(a['grade'])
  knots=np.r_[np.zeros(d),np.linspace(0,1,Nt+1)**grade,np.ones(d)]
  raw=a['cG'].reshape(K,Nt+d)
  co=[Q.from_float(float(raw[0,j]))-(Q(0)if j<1 else Q.from_float(float(raw[2,j]))/2)for j in range(Nt+d)]
  data={'schema':'exact-scalar-spline-v2','source':'self','archive_path':str(archive),'archive_sha256':hashlib.sha256(buf).hexdigest(),'source_core_path':str(Path('verification/fixed_velocity_block_20261021T0056/source_snapshots/bq3core.py').resolve()),'source_core_sha256':'79128784b725d66fc429759272ead3c616bf93846952daf187fc7bed96eaa89f','beta':str(Q.from_float(float(a['beta']))),'basis_beta':str(Q.from_float(float(a['beta_basis']))),'L':str(Q.from_float(float(a['L']))),'degree':d,'knots':[str(Q.from_float(float(v)))for v in knots],'coefficients':[str(v)for v in co],'scalar_rule':'exact rational C0 minus masked C2/2; no rounded subtraction'}
 validate(data);base.archive_check(data);path.write_text(json.dumps(data,indent=2)+'\n');return data

def evaluate(data):
 b,L,N,knots,d,c=validate(data);a=N+1-b
 inp={'degree':d,'knots':data['knots'],'coefficients':[data['coefficients']]}
 integral=(Q(0),Q(0));cells=[];endpoint=None;powers={}
 for span in range(d,len(knots)-d-1):
  if knots[span]==knots[span+1]:continue
  A,B,ps=spline_span(inp,span);p=ps[0];width=B-A
  if endpoint is None:endpoint=[p.get((k,0),Q(0))*factorial(k)/width**k for k in range(N)]
  coeff={}
  for(i,j),v in p.items():
   assert j==0
   if i<N:continue
   v=v*factorial(i)/factorial(i-N)/width**i
   for k in range(i-N+1):coeff[k]=coeff.get(k,Q(0))+v*comb(i-N,k)*(1-A)**(i-N-k)*(-1)**k
  lo=1-B;hi=1-A;plo=base.powerbound(lo,a);phi=base.powerbound(hi,a)
  powers[str(lo)]=base.ser(plo);powers[str(hi)]=base.ser(phi)
  value=(Q(0),Q(0))
  for j,cj in coeff.items():value=base.plus(value,base.scale(base.minus(base.scale(phi,hi**j),base.scale(plo,lo**j)),cj/(a+j)))
  value=base.roundout(value);integral=base.plus(integral,value)
  cells.append({'span':span,'z_interval':[str(lo),str(hi)],'integral':base.ser(value)})
 assert endpoint is not None
 denominators=[prod(b-j for j in range(1,k+1))for k in range(N+1)]
 boundary=sum((-1)**(k+1)*endpoint[k]/denominators[k+1]for k in range(N))
 finitepart=base.roundout(base.plus((boundary,boundary),base.scale(integral,(-1)**N/denominators[N])))
 constant=base.roundout(base.scale(finitepart,-b*L*L/2))
 sign='NEGATIVE'if constant[1]<0 else'POSITIVE'if constant[0]>0 else'OPEN'
 return {'N':N,'a':str(a),'parameters':{'bits':base.BITS,'log_terms':base.NLOG,'exp_degree':base.NEXP},'power_bounds':powers,'cells':cells,'origin_derivatives':[str(v)for v in endpoint],'boundary':str(boundary),'integral':base.ser(integral),'finite_part':base.ser(finitepart),'constant_C2':base.ser(constant),'sign':sign}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('certificate',type=Path);ap.add_argument('--archive',type=Path);ap.add_argument('--check',action='store_true');args=ap.parse_args();start=time.monotonic()
 if args.archive:assert not args.check;export(args.archive,args.input)
 data=json.loads(args.input.read_text());validate(data);base.archive_check(data);result=evaluate(data);sha=hashlib.sha256(args.input.read_bytes()).hexdigest()
 if args.check:
  cert=json.loads(args.certificate.read_text());assert cert['input_sha256']==sha and cert['result']==result
 else:
  cert={'created_utc':datetime.now(timezone.utc).isoformat(),'input_sha256':sha,'result':result};args.certificate.write_text(json.dumps(cert,indent=2)+'\n')
 report={'utc':datetime.now(timezone.utc).isoformat(),'verdict':('CONFIRMED_'if args.check else'COMPUTED_')+result['sign'],'N':result['N'],'elapsed_seconds':time.monotonic()-start,'C2_interval':result['constant_C2'],'C2_interval_float':[float(Q(v))for v in result['constant_C2']],'archive_sha256':data['archive_sha256'],'input_sha256':sha,'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 args.certificate.with_suffix('.check.json'if args.check else'.compute.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
