"""Alternative exact B-spline and exponential-polynomial point audit."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from datetime import datetime,timezone
from math import comb,factorial
import importlib.util,hashlib,json,bisect,time
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
spec=importlib.util.spec_from_file_location('hlower_previous',ROOT/'code/check.py');K=importlib.util.module_from_spec(spec);spec.loader.exec_module(K)
I=K.I;M=K.M;P=K.P;G=K.G;aa=K.aa

def conv(a,b,n=5):
 return [sum((a[j]*b[k-j] for j in range(k+1) if j<len(a) and k-j<len(b)),arb(0)) for k in range(n+1)]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();ctx.prec=1024;ctx.threads=1
 M.SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
 d=M.Data();G.check_hash(d);cache=G.load_cache(d);raw=np.load(M.SOURCE,allow_pickle=False);t=F(8);kn=d.knots;span=bisect.bisect_right(kn,t)-1;ell=1/aa(d.k);D=4*ell-1
 @lru_cache(None)
 def B(i,p,j):
  if j>p:return F(0)
  if j:
   left=F(0) if kn[i+p]==kn[i] else p*B(i,p-1,j-1)/(kn[i+p]-kn[i])
   right=F(0) if kn[i+p+1]==kn[i+1] else p*B(i+1,p-1,j-1)/(kn[i+p+1]-kn[i+1])
   return left-right
  if p==0:return F(int(kn[i]<=t<kn[i+1]))
  left=F(0) if kn[i+p]==kn[i] else (t-kn[i])*B(i,p-1,0)/(kn[i+p]-kn[i])
  right=F(0) if kn[i+p+1]==kn[i+1] else (kn[i+p+1]-t)*B(i+1,p-1,0)/(kn[i+p+1]-kn[i+1])
  return left+right
 controls={i:sum(((-1)**m*F.from_float(float(raw['S'][m,i])) for m in range(260)),F(0)) for i in range(span-7,span+1)}
 exactA=[sum((c*B(i,7,j) for i,c in controls.items()),F(0)) for j in range(7)]
 A=[aa(v)/factorial(j) for j,v in enumerate(exactA)]
 he,pe,qe=I.spline_eps(d,cache,span,t)
 dj=[]
 for j in range(7):
  dj.append(-sum(((-1)**n*ep.atzero() for n,ep in enumerate(pe,1)),arb(0)))
  if j==0:dj[0]+=ell
  pe=[ep.deriv() for ep in pe]
 ds=[v/factorial(j) for j,v in enumerate(dj)]
 Aprime=[(j+1)*A[j+1] for j in range(6)];dprime=[(j+1)*ds[j+1] for j in range(6)]
 da=conv(ds,Aprime);minusda=conv(ds,A);minus2da=conv(dprime,A)
 gam=[da[j]+D*A[j]-minusda[j]-2*minus2da[j] for j in range(6)]
 et=aa(t).exp();z=et/(1+et);m=(-aa(F(9,5)*t)).exp()*((1+et).log()*aa(F(53,10))).exp()
 u=[arb(0)]+[z/factorial(j) for j in range(1,6)];power=[arb(1)]+[arb(0)]*5;bp=F(1);series=[arb(1)]+[arb(0)]*5
 for n in range(1,6):
  power=conv(power,u);bp*= (F(53,10)-n+1)/n
  series=[a+aa(bp)*b for a,b in zip(series,power)]
 e_series=[aa((-F(9,5))**j/F(factorial(j))) for j in range(6)];mj=[m*v for v in conv(e_series,series)]
 weighted=[factorial(j)*v for j,v in enumerate(conv(mj,gam))]
 sig=aa(F(25,4));C0=arb.pi().sqrt()*aa(F(23,4)).gamma()/(2*arb.pi()*sig.gamma());constants=[C0]
 for j in range(5):constants.append(constants[-1]*aa(F(2*j+1,2))/aa(F(25,4)-j-F(3,2)))
 constants=[v.sqrt() for v in constants];bounds=[abs(v)/c for v,c in zip(weighted,constants)]
 old=json.loads((ROOT/'evidence/replay_640.json').read_text());oldrow=next(row for row in old['rows'] if row['t']=='8')
 for j in range(6):
  assert (factorial(j)*gam[j]).overlaps(arb(oldrow['gamma_derivatives'][j]['ball']))
  assert weighted[j].overlaps(arb(oldrow['weighted_derivatives'][j]['ball']))
  assert constants[j].overlaps(arb(old['constants'][j]['ball']))
 assert bounds[5]>1906360017
 pilot=json.loads((ROOT/'evidence/pilot.json').read_text())
 for p in pilot['rows']:
  other=next(v for v in old['rows'] if v['t']==p['t'])
  for a,b in zip(p['weighted_derivatives'],other['weighted_derivatives']):assert arb(a['ball']).overlaps(arb(b['ball']))
 output={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','bits':1024,'t':'8','span':span,'input_sha256':d.sha,'cache_sha256':sha(G.CACHE),'scalar_sha256':sha(M.SCALAR),'original_exact_axis_derivatives':[str(v) for v in exactA],'weighted_derivatives':[G.rec(v) for v in weighted],'sobolev_lower_bounds':[G.rec(v) for v in bounds],'constants':[G.rec(v) for v in constants],'checks':['exact rational Phi control differentiation','explicit exponential-polynomial velocity derivatives','alternative weight binomial series','Sobolev beta recurrence','384/640-bit pilot overlap','640/1024-bit all derivatives overlap'],'code_sha256':sha(Path(__file__)),'seconds':time.monotonic()-start}
 (ROOT/'evidence/independent_1024.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps({'date':output['date'],'verdict':'PASS','strongest_bound':bounds[5].str(30),'seconds':output['seconds']}),flush=True)
if __name__=='__main__':main()
