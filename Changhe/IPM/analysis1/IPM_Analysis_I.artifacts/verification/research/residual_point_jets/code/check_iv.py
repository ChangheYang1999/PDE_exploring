"""Density moment jets plus exact noncyclic Laurent convolution, one point."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,hashlib,time,math,argparse
import mpmath,flint
from mpmath import iv
from flint import fmpz_poly,ctx
assert not sys.flags.optimize
iv.dps=180;ctx.threads=1
assert mpmath.__version__=='1.3.0' and flint.__version__=='0.9.0'
B=Path(__file__).resolve().parents[3];D=B/'research/residual_point_jets';PREC=640;DEN=1<<(2*PREC)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ie(x):
 result=[]
 for sign,m,e,bc in x._mpi_:
  assert bc>=0;result.append((-1 if sign else 1)*F(int(m))*F(2)**int(e))
 assert result[0]<=result[1];return result

def be(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return m-r,m+r

def decode(x):a,b=be(x);return iv.mpf([iq(a).a,iq(b).b])
def quant(x,p):
 a,b=ie(x);a*=1<<p;b*=1<<p;lo=a.numerator//a.denominator;hi=-((-b.numerator)//b.denominator);m=(lo+hi)//2;return m,max(m-lo,hi-m)
def angular(values,even,sine):
 offset=522 if even else 521;center=[0]*(2*offset+1);radius=[0]*(2*offset+1)
 for n,v in enumerate(values):
  freq=2*(n+1) if even else 2*n+1;vv=v if sine else v/2;m,r=quant(vv,PREC);center[offset+freq]=m;center[offset-freq]=-m if sine else m;radius[offset+freq]=radius[offset-freq]=r
 return fmpz_poly(center),fmpz_poly(radius),fmpz_poly([abs(m) for m in center])
def conv(x,y):
 a,r,aa=x;b,s,bb=y;return a*b,aa*s+r*bb+r*s

def out(v):return {'lower_exact':str(v[0]),'upper_exact':str(v[1])}
start=time.monotonic();ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,required=True);args=ap.parse_args();firstpath=D/'evidence'/('arb_%d.json'%args.cell);first=json.loads(firstpath.read_text());assert first['status']=='COMPUTED_PHYSICAL_GREEN_POINT_JETS_NEEDS_INDEPENDENT_AUDIT' and first['cell']==args.cell;pins=dict(first['files'])
prep=json.loads((D/'evidence/preparation.json').read_text());assert prep['status']=='PASS_EXACT_INTERIOR_DENSITY_POLYNOMIALS_AND_ORDER_FIVE_ALGEBRA' and prep['exact_density_coefficients']==27248
for n,h in prep['files'].items():assert n not in pins or pins[n]==h;pins[n]=h
for n,h in pins.items():assert sha(B/n)==h
sample=next(p for p in json.loads((B/'research/residual_samples/evidence/sample_result.json').read_text())['samples'] if p['cell']==args.cell);assert sample['t_exact']==first['t_exact'];tc=F(sample['t_exact']);et=iv.exp(iq(tc));trial=json.loads((B/'data_exact/modal_v2.json').read_text());k,L=[F.from_float(float.fromhex(trial['scalars_hex'][q])) for q in ['k','L']]
polys=[[decode(v) for v in p] for p in sample['density_polynomial_at_point']];assert len(polys)==262 and all(len(p)==8 for p in polys)
# Different polynomial recurrence: differentiate the coefficient vector, extracting its value each time.
hjets=[];work=polys
for order in range(7):
 hjets.append([p[0] if p else iv.mpf(0) for p in work]);work=[[(j+1)*p[j+1] for j in range(len(p)-1)] for p in work]
I=[list(map(decode,sample['i']))];J=[list(map(decode,sample['j']))]
for order in range(5):
 I.append([-(2*n+4)*I[-1][n-1]+hjets[order][n-1] for n in range(1,262)]);J.append([(2*n-4)*J[-1][n-1]-hjets[order][n] for n in range(1,262)])
# Apply (D+3) to whole coefficient vectors before extracting R^(i).
R=[];work=polys[:261]
for order in range(7):
 R.append([et**3*p[0] for p in work]);work=[[3*p[j]+((j+1)*p[j+1] if j+1<len(p) else 0) for j in range(len(p))] for p in work]
pjets=[];qjets=[]
for a in range(6):
 pjets.append([-n*et**2*sum((math.comb(a,l)*2**(a-l)*(J[l][n-1]-I[l][n-1]) for l in range(a+1)),iv.mpf(0)) for n in range(1,262)])
 qjets.append([et**2*sum((math.comb(a,l)*2**(a-l)*(2*n*(J[l][n-1]+I[l][n-1])-hjets[l][n-1]-hjets[l][n]) for l in range(a+1)),iv.mpf(0))/2 for n in range(1,262)])
pe=[angular(v,True,False) for v in pjets];qe=[angular(v,True,True) for v in qjets];re=[angular(v,False,True) for v in R];te=[angular([(2*j+1)*x for j,x in enumerate(v)],False,False) for v in R]
coefficients=[];intersection=[];checks=0;convs=0;old_overlap=0;wiener={};iv_wiener={};comparison={}
saved=json.loads((B/'research/derivative_scalar_aggregation/sources/runs__cert_deriv_middle.json').read_text())['rows'][args.cell]
for a in range(6):
 mc=fmpz_poly([0]);rc=fmpz_poly([0])
 for l in range(a+1):
  m1,r1=conv(pe[l],re[a+1-l]);m2,r2=conv(qe[l],te[a-l]);weight=math.comb(a,l);mc+=(m1+m2)*weight;rc+=(r1+r2)*weight;convs+=8
 assert mc.degree()<=2086 and rc.degree()<=2086
 row=[];joint=[]
 for N in range(522):
  idx=1043+2*N+1;m,r=int(mc[idx]),int(rc[idx]);assert r>=0
  if N<261:
   lm,lr=quant(iq(1/k)*R[a+1][N]-R[a][N],2*PREC);m+=lm;r+=lr
  lo,hi=F(m-r,DEN),F(m+r,DEN);u,v=be(first['coefficient_boxes'][a][N]);assert max(lo,u)<=min(hi,v),('DISJOINT',args.cell,a,N);checks+=1;row.append((lo,hi));joint.append((max(lo,u),min(hi,v)))
  if a==0:
   u,v=be(sample['residual_coefficients'][N]);assert max(lo,u)<=min(hi,v),('old',N);old_overlap+=1
 encoded=[]
 for lo,hi in row:
  cm=(lo+hi)*DEN/2;cr=(hi-lo)*DEN/2;assert cm.denominator==cr.denominator==1 and cr>=0
  encoded.append({'schema':'arb-dyadic-mid-radius-v1','mid_m':str(cm.numerator),'mid_e':-2*PREC,'rad_m':str(cr.numerator),'rad_e':-2*PREC})
 coefficients.append(encoded);intersection.append(joint)
 for j in range(6-a):
  key='W_%d_%d'%(a,j);sums=[]
  for source in [row,joint]:
   lower=F(0);upper=F(0)
   for N,(lo,hi) in enumerate(source):
    low=0 if lo<=0<=hi else min(abs(lo),abs(hi));high=max(abs(lo),abs(hi));lower+=(2*N+1)**j*low;upper+=(2*N+1)**j*high
   sums.append((lower,upper))
  iv_wiener[key]=out(sums[0]);wiener[key]=out(sums[1]);ar=first['wiener_sums'][key];assert max(F(ar['lower_exact']),sums[0][0])<=min(F(ar['upper_exact']),sums[0][1])
  if key in saved:
   cap=F.from_float(saved[key]);comparison[key]={'saved_majorant_exact':str(cap),'comparison':'CONSISTENT_AT_SAMPLE' if sums[1][1]<=cap else 'EXCEEDS_SAVED_MAJORANT_AT_SAMPLE' if sums[1][0]>cap else 'OVERLAP_ONLY'}
  else:comparison[key]={'comparison':'NO_SAVED_FIELD'}
assert checks==3132 and old_overlap==522 and convs==168
weight=ie((et/iq(L))**3*iv.exp(iq((k-3)/2)*iv.log(1+(et/iq(L))**2)));assert weight[0]>0
for p in [firstpath,D/'evidence/preparation.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():assert sha(B/n)==h
outcome={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_RECURRENCES_AND_POINT_JET_COEFFICIENTS','cell':args.cell,'t_exact':str(tc),'orders':6,'modes':522,'coefficient_comparisons':checks,'order_zero_prior_comparisons':old_overlap,'integer_polynomial_products':convs,'coefficient_boxes':coefficients,'wiener_sums':wiener,'iv_wiener_sums':iv_wiener,'saved_comparisons':comparison,'weight_at_point':out(weight),'iv_dps':iv.dps,'quantization_bits':PREC,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Finite derivative coefficients at inherited canonical point inputs; no new integration, cell supremum, forcing norm or endpoint.'}
with (D/'evidence'/('iv_%d.json'%args.cell)).open('x') as f:json.dump(outcome,f,separators=(',',':'));f.write('\n')
print(json.dumps({k:outcome[k] for k in ['utc','status','cell','coefficient_comparisons','order_zero_prior_comparisons','integer_polynomial_products','seconds']}));print(json.dumps(comparison))
