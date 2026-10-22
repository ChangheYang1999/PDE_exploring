from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import defaultdict
import json,hashlib,math,sys,time
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_point_jets'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def bounds(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return m-r,m+r
start=time.monotonic();manifest=json.loads((D/'data_exact/manifest.json').read_text());pins=dict(manifest['files'])
for n,h in pins.items():assert sha(B/n)==h
trial=json.loads((B/'data_exact/modal_v2.json').read_text());ar=trial['arrays'];M,nb=ar['S']['shape'];knots=[F.from_float(float.fromhex(x)) for x in ar['knots']['hex']];S=[[F.from_float(float.fromhex(ar['S']['hex'][m*nb+i])) for i in range(nb)] for m in range(M)];assert trial['degree']==7 and len(knots)==nb+8
samples=json.loads((B/'research/residual_samples/evidence/sample_result.json').read_text())['samples'];assert [p['cell'] for p in samples]==manifest['cells']
# Exact angular projection from cos^2(theta)sin(theta)cos(2m theta).
weights=[]
for j in range(262):
 row={}
 for m in range(M):
  z=sum((F(1 if f>0 else -1,8) for f in [1+2*m,1-2*m,3+2*m,3-2*m] if (abs(f)-1)//2==j),F(0))
  if z:row[m]=z
 weights.append(row)
assert not weights[-1]
count=0;records=[]
for point in samples:
 tc=F(point['t_exact']);indices=[i for i in range(len(knots)-1) if knots[i]<tc<knots[i+1]];assert len(indices)==1;span=indices[0];assert 7<=span<nb;a,b=map(F,point['cell_endpoints_exact']);assert knots[span]<=a<tc<b<=knots[span+1] and tc==(a+b)/2
 basis={span:[F(1)]}
 for degree in range(1,8):
  newer={}
  for i in range(span-degree,span+1):
   out=[F(0)]*(degree+1)
   if i in basis:
    den=knots[i+degree]-knots[i];assert den>0
    for power,c in enumerate(basis[i]):out[power]+=(tc-knots[i])*c/den;out[power+1]+=c/den
   if i+1 in basis:
    den=knots[i+degree+1]-knots[i+1];assert den>0
    for power,c in enumerate(basis[i+1]):out[power]+=(knots[i+degree+1]-tc)*c/den;out[power+1]-=c/den
   newer[i]=out
  basis=newer
 assert all(sum((q[a] for q in basis.values()),F(0))==(1 if a==0 else 0) for a in range(8))
 for j,row in enumerate(weights):
  density={i:sum((w*S[m][i] for m,w in row.items()),F(0)) for i in basis}
  for power in range(8):
   exact=sum((basis[i][power]*density[i] for i in basis),F(0));lo,hi=bounds(point['density_polynomial_at_point'][j][power]);assert lo<=exact<=hi,(point['cell'],j,power);count+=1
 records.append({'cell':point['cell'],'t_exact':str(tc),'original_span':span,'span_left_exact':str(knots[span]),'span_right_exact':str(knots[span+1]),'density_coefficients':2096})
assert count==27248
# Closed multinomial differentiation versus iterated free differential algebra.
identities=0
for shift in [0,1]:
 state={(0,shift):1}
 for order in range(6):
  closed=defaultdict(int)
  for l in range(order+1):
   for b in range(l+1):closed[(b,shift+order-l)]+=math.comb(order,l)*math.comb(l,b)*(-2)**(l-b)
  assert dict(closed)==state;identities+=1
  nxt=defaultdict(int)
  for (a,b),v in state.items():nxt[(a,b)]+=-2*v;nxt[(a+1,b)]+=v;nxt[(a,b+1)]+=v
  state=dict(nxt)
expchecks=0
for degree in range(8):
 state={(degree,0):1}
 for order in range(7):
  closed={(degree-b,order-b):math.comb(order,b)*math.factorial(degree)//math.factorial(degree-b) for b in range(min(order,degree)+1)}
  assert state==closed;expchecks+=1
  newer=defaultdict(int)
  for (s,beta),v in state.items():
   newer[(s,beta+1)]+=v
   if s:newer[(s-1,beta)]+=s*v
  state=dict(newer)
# Noncyclic Laurent integer unit test, without using either point checker.
cosine={2:F(1),-2:F(1)};sine={1:F(1),-1:F(-1)};prod=defaultdict(F)
for i,a in cosine.items():
 for j,b in sine.items():prod[i+j]+=a*b
assert dict(prod)=={3:F(1),1:F(-1),-1:F(1),-3:F(-1)}
for p in [D/'data_exact/manifest.json',D/'ADDENDUM.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_INTERIOR_DENSITY_POLYNOMIALS_AND_ORDER_FIVE_ALGEBRA','points':records,'exact_density_coefficients':count,'free_Leibniz_identities':identities,'exponential_polynomial_basis_checks':expchecks,'Laurent_unit_test':True,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Exact middle polynomial input and local order-five algebra; canonical moment validity remains inherited from topic28.'}
with (D/'evidence/preparation.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','exact_density_coefficients','free_Leibniz_identities','exponential_polynomial_basis_checks','seconds']}))
