"""Physical Green ODE jets with direct trigonometric scatter, one point per call."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import json,hashlib,sys,time,argparse,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint
from flint import arb,ctx
assert not sys.flags.optimize
ctx.prec=448;ctx.threads=1
assert flint.__version__=='0.9.0'
B=Path(__file__).resolve().parents[3];D=B/'research/residual_point_jets'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def aq(q):q=F(q);return arb(q.numerator)/q.denominator
def fraction(x):
 assert x.is_finite() and x.rad()==0;m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ends(x):return fraction(x.lower()),fraction(x.upper())
def box(x):
 assert x.is_finite();m,e=x.mid().man_exp();r,s=x.rad().man_exp();return {'mid_m':str(m),'mid_e':int(e),'rad_m':str(r),'rad_e':int(s),'schema':'arb-dyadic-mid-radius-v1'}
def decode(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return aq(m-r).union(aq(m+r))
def out(x):
 a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display_only':x.str(20)}
start=time.monotonic();pa=argparse.ArgumentParser();pa.add_argument('--cell',type=int,required=True);args=pa.parse_args();manifest=json.loads((D/'data_exact/manifest.json').read_text());pins=dict(manifest['files'])
for n,h in pins.items():assert sha(B/n)==h
assert args.cell in manifest['cells'];sample=next(r for r in json.loads((B/'research/residual_samples/evidence/sample_result.json').read_text())['samples'] if r['cell']==args.cell)
trial=json.loads((B/'data_exact/modal_v2.json').read_text());k,L=[F.from_float(float.fromhex(trial['scalars_hex'][q])) for q in ['k','L']];knots=sorted(set(F.from_float(float.fromhex(q)) for q in trial['arrays']['knots']['hex']));tc=F(sample['t_exact']);assert any(a<tc<b for a,b in zip(knots,knots[1:]));a,b=map(F,sample['cell_endpoints_exact']);assert tc==(a+b)/2
C=[[decode(v) for v in p] for p in sample['density_polynomial_at_point']];assert len(C)==262 and all(len(p)==8 for p in C) and all(ends(v)==(0,0) for v in C[-1]);I=list(map(decode,sample['i']));J=list(map(decode,sample['j']));assert len(I)==len(J)==261
H=[[math.factorial(a)*p[a] for p in C] for a in range(7)];et=aq(tc).exp();e2,e3,e4=et**2,et**3,et**4
R=[[e3*sum((math.comb(a,b)*3**(a-b)*H[b][j] for b in range(a+1)),arb(0)) for j in range(261)] for a in range(7)]
A=[[e4*((H[0][n-1]+H[0][n])/2-2*n*I[n-1]) for n in range(1,262)]];BB=[[e4*(2*n*J[n-1]-(H[0][n-1]+H[0][n])/2) for n in range(1,262)]]
for a in range(5):
 g=[e4*sum((math.comb(a,b)*4**(a-b)*(H[b+1][n-1]+(4-2*n)*H[b][n-1]+H[b+1][n]+(4+2*n)*H[b][n]) for b in range(a+1)),arb(0))/2 for n in range(1,262)]
 A.append([-2*n*A[-1][n-1]+g[n-1] for n in range(1,262)]);BB.append([2*n*BB[-1][n-1]-g[n-1] for n in range(1,262)])
P=[[-sum((math.comb(a,b)*(-2)**(a-b)*(A[b][n]+BB[b][n]) for b in range(a+1)),arb(0))/(4*e2) for n in range(261)] for a in range(6)]
Q=[[sum((math.comb(a,b)*(-2)**(a-b)*(BB[b][n]-A[b][n]) for b in range(a+1)),arb(0))/(4*e2) for n in range(261)] for a in range(6)]
coef=[];pairs=0
for a in range(6):
 eps=[aq(1/k)*R[a+1][j]-R[a][j] for j in range(261)]+[arb(0) for j in range(261)]
 for n in range(1,262):
  for j in range(261):
   pr=sum((math.comb(a,l)*P[l][n-1]*R[a+1-l][j] for l in range(a+1)),arb(0));pt=sum((math.comb(a,l)*Q[l][n-1]*(2*j+1)*R[a-l][j] for l in range(a+1)),arb(0))
   eps[j+n]+=pr+pt
   if j>=n:eps[j-n]+=pr-pt
   else:eps[n-j-1]-=pr-pt
   pairs+=1
 coef.append(eps)
assert pairs==408726;overlap=0
for actual,saved in zip(coef[0],sample['residual_coefficients']):
 lo,hi=ends(actual);u,v=ends(decode(saved));assert max(lo,u)<=min(hi,v);overlap+=1
saved=json.loads((B/'research/derivative_scalar_aggregation/sources/runs__cert_deriv_middle.json').read_text())['rows'][args.cell];assert saved['ci']==args.cell;V={};comp={};weight=(et/aq(L))**3*((1+(et/aq(L))**2).log()*aq((k-3)/2)).exp()
for a in range(6):
 for j in range(6-a):
  key='W_%d_%d'%(a,j);val=sum(((2*N+1)**j*abs(v) for N,v in enumerate(coef[a])),arb(0));V[key]=out(val)
  if key in saved:
   cap=F.from_float(saved[key]);lo,hi=ends(val);comp[key]={'saved_majorant_exact':str(cap),'comparison':'CONSISTENT_AT_SAMPLE' if hi<=cap else 'EXCEEDS_SAVED_MAJORANT_AT_SAMPLE' if lo>cap else 'OVERLAP_ONLY'}
  else:comp[key]={'comparison':'NO_SAVED_FIELD'}
for p in [D/'data_exact/manifest.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_PHYSICAL_GREEN_POINT_JETS_NEEDS_INDEPENDENT_AUDIT','cell':args.cell,'t_exact':str(tc),'orders':6,'modes':522,'pairs':pairs,'original_order_zero_overlaps':overlap,'coefficient_boxes':[[box(v) for v in row] for row in coef],'wiener_sums':V,'saved_comparisons':comp,'weight_at_point':out(weight),'r':out(et),'bits':ctx.prec,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Thirteen designated point inputs only; no cell supremum, no fresh canonical integration.'}
p=D/'evidence'/('arb_%d.json'%args.cell)
with p.open('x') as f:json.dump(result,f,separators=(',',':'));f.write('\n')
print(json.dumps({k:result[k] for k in ['utc','status','cell','orders','modes','pairs','original_order_zero_overlaps','seconds']}));print(json.dumps(comp))
