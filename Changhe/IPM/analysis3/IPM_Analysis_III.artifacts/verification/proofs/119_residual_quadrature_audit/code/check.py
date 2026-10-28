from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,math,hashlib
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
LEAD=LANE.parent/'s2-lead/work/farres'
def read(name):
 p=LEAD/name;raw=json.loads(p.read_text());ans={}
 for row in raw['results']:
  ans[F(row['t'])]=tuple(row[k] for k in ('axis_energy_density','remainder_energy_density'))
 return ans,hashlib.sha256(p.read_bytes()).hexdigest()
def midpoint(r):return float((F(r['lower_exact'])+F(r['upper_exact']))/2)
def overlap(a,b):return max(F(a['lower_exact']),F(b['lower_exact']))<=min(F(a['upper_exact']),F(b['upper_exact']))
g,h1=read('far_points_160.json');c,h2=read('far_points_192.json')
ind=json.loads((LANE/'proofs/117_far_residual_leading_term/evidence/check.json').read_text())
checks=[]
for row in ind['points']:
 t=F(row['t']);src=g if t in g else c
 assert overlap(row['axis'],src[t][0]) and overlap(row['remainder'],src[t][1])
 checks.append({'t':str(t),'axis_overlap':True,'remainder_overlap':True})
g={float(t):tuple(map(midpoint,r)) for t,r in g.items()};c={float(t):tuple(map(midpoint,r)) for t,r in c.items()}
def seg(t0,f0,t1,f1,lo=None,hi=None):
 lo=t0 if lo is None else lo;hi=t1 if hi is None else hi
 assert f0>0 and f1>0 and lo>=t0 and hi<=t1
 rate=math.log(f1/f0)/(t1-t0)
 return f0*(hi-lo) if abs(rate*(t1-t0))<1e-12 else f0*math.exp(rate*(lo-t0))*math.expm1(rate*(hi-lo))/rate
rates=[math.log(c[60][i]/c[30][i])/30 for i in range(2)]
assert max(rates)<0
tails=[g[20][0]/(-rates[0]),c[30][1]*math.exp(-10*rates[1])/(-rates[1])]
def quadrature(ts,trap=False):
 en=[]
 for i in range(2):
  vals=[]
  for t0,t1 in zip(ts,ts[1:]):
   f0,f1=g[t0][i],g[t1][i]
   vals.append((f0+f1)*(t1-t0)/2 if trap else seg(t0,f0,t1,f1))
  en.append(math.fsum(vals))
 total=math.fsum(en+tails)
 return {'axis_0_20':en[0],'remainder_0_20':en[1],'tail_convention':sum(tails),'total':total,'eta':math.sqrt(total)}
ts=sorted(g);fine=quadrature(ts);coarse=quadrature(ts[::2]);trap=quadrature(ts,True)
lead=json.loads((LEAD/'eta_estimate.json').read_text());assert abs(fine['eta']-lead['eta_Y_estimate'])<1e-8
regions={}
for a,b in [(0,4),(4,8.135),(8.135,12),(12,20)]:
 vals=[]
 for t0,t1 in zip(ts,ts[1:]):
  lo,hi=max(a,t0),min(b,t1)
  if hi>lo:
   for i in range(2):vals.append(seg(t0,g[t0][i],t1,g[t1][i],lo,hi))
 regions[f'[{a},{b}]']={'energy':math.fsum(vals),'share':math.fsum(vals)/fine['total']}
regions['[20,inf)']={'energy':sum(tails),'share':sum(tails)/fine['total']}
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS_NUMERICAL_ARITHMETIC_ONLY','input_hashes':{'far_points_160.json':h1,'far_points_192.json':h2},'independent_point_checks':checks,'fine_loglinear':fine,'coarse_loglinear':coarse,'fine_trapezoid':trap,'fitted_rates':rates,'actual_limiting_rate':float(4*F(1615536043799051,2**53)-F(5,4)),'corrected_regions':regions,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()}
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
