"""Generate and replay exact Bernstein certificates for frozen far-chart polynomials.

No solver imports. The source binary64 arrays are compared to the exact JSON
inputs. Unexpanded Chebyshev evaluation at degree+1 rational points validates
Q against its own power representation before any interval certification.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import datetime,hashlib,json,sys,argparse
import numpy as np
ap=argparse.ArgumentParser();ap.add_argument('out',nargs='?');ap.add_argument('--root',default='candidate_audits/lead_generating/far_chart');args=ap.parse_args()
ROOT=Path(args.root)
OUT=Path(args.out) if args.out else ROOT/'bernstein_final';OUT.mkdir(parents=True,exist_ok=True)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def horner(a,x):
 out=F(0)
 for v in reversed(a):out=out*x+v
 return out
def cheb_derivatives(z,n):
 out=[[F(1),F(0),F(0)]]
 if n:out.append([z,F(1),F(0)])
 for k in range(2,n+1):
  a,b=out[-1],out[-2]
  out.append([2*z*a[0]-b[0],2*a[0]+2*z*a[1]-b[1],4*a[1]+2*z*a[2]-b[2]])
 return out
def power_to_bernstein(a):
 n=len(a)-1
 return [sum(a[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)) for k in range(n+1)]
def split_midpoint(b):
 row=b[:];left=[row[0]];right=[row[-1]]
 while len(row)>1:
  row=[(x+y)/2 for x,y in zip(row,row[1:])];left.append(row[0]);right.append(row[-1])
 return left,right[::-1]
def affine_power(a,l,r):
 n=len(a)-1;h=r-l
 return [h**k*sum(a[i]*comb(i,k)*l**(i-k) for i in range(k,n+1)) for k in range(n+1)]
report={'start_utc':now(),'script_sha256':digest(__file__),'rows':[],'arithmetic':'exact Python Fraction, binary64 inputs treated as rational; no formal assistant certificate'}
source_audit=json.loads((ROOT/'audit.json').read_text());report['source_audit_sha256']=digest(ROOT/'audit.json')
for row in source_audit['rows']:
 cert_path=Path(row['certificate']);assert digest(cert_path)==row['certificate_sha256']
 old=json.loads(cert_path.read_text());source=Path(row['source']);assert digest(source)==old['source_sha256']
 with np.load(source,allow_pickle=False) as d:
  coeff=np.asarray(d['c']).reshape(int(d['J'])+1,int(d['Kw'])+1)
 assert [[str(F.from_float(float(v))) for v in rr] for rr in coeff]==old['input_coefficients_as_exact_binary64_ratios']
 c0=[F(v) for v in old['P0_cheb_coefficients_exact']];a=[F(v) for v in old['Q_power_coefficients_exact']]
 raw_c0=[sum(F.from_float(float(coeff[j,k]))*((-1)**j) for j in range(coeff.shape[0])) for k in range(coeff.shape[1])]
 assert raw_c0==c0, 'P0 does not match the raw frozen coefficients'
 while len(a)>1 and a[-1]==0:a.pop()
 degree=len(a)-1
 validation_degree=max(degree,len(c0)-1+6)
 for i in range(validation_degree+1):
  w=F(i,validation_degree) if validation_degree else F(0);t=cheb_derivatives(2*w-1,len(c0)-1)
  P=sum(c*tj[0] for c,tj in zip(c0,t));DP=2*sum(c*tj[1] for c,tj in zip(c0,t));DDP=4*sum(c*tj[2] for c,tj in zip(c0,t));u=1-w**3
  direct=(1+2*u/3+2*w**3-8*u*w**3/3)*P+F(4,3)*u*w*(1+2*w**3)*DP-F(4,3)*u*u*w*w*DDP
  assert direct==horner(a,w)
 # Sufficient exact certificate; no result inferred from unresolved nodes.
 stack=[(F(0),F(1),power_to_bernstein(a),0)];leaves=[];unresolved=[];nodes=0
 while stack:
  l,r,b,depth=stack.pop();nodes+=1
  if min(b)>0:
   leaves.append({'l':str(l),'r':str(r),'b':[str(v) for v in b]})
  elif depth>=24 or nodes>=16384:
   unresolved.append({'l':str(l),'r':str(r),'min_b':str(min(b))})
  else:
   bl,br=split_midpoint(b);m=(l+r)/2;stack.extend([(m,r,br,depth+1),(l,m,bl,depth+1)])
 leaves.sort(key=lambda z:F(z['l']))
 certificate={'utc':now(),'source_certificate':str(cert_path),'source_certificate_sha256':digest(cert_path),'source_sha256':old['source_sha256'],'degree':degree,'Q_power_exact':[str(v) for v in a],'leaves':leaves,'unresolved':unresolved}
 cp=OUT/(row['state']+'.json');cp.write_text(json.dumps(certificate,indent=2)+'\n')
 # Replay persisted certificate from exact affine-power conversion, not the
 # subdivision coefficients. Check complete interval coverage separately.
 replay=json.loads(cp.read_text());end=F(0);lower=[];coverage=not unresolved
 for leaf in replay['leaves']:
  l,r=F(leaf['l']),F(leaf['r']);assert l>=0 and r<=1 and l<r
  coverage=coverage and l==end;end=r
  expected=power_to_bernstein(affine_power(a,l,r));claimed=[F(v) for v in leaf['b']]
  assert expected==claimed and min(claimed)>0
  lower.append(min(claimed))
 coverage=coverage and end==1
 item={'state':row['state'],'degree':degree,'validation_points':validation_degree+1,'nodes':nodes,'leaves':len(leaves),'unresolved':len(unresolved),'positive_on_whole_interval':bool(coverage),'source_sha256':old['source_sha256'],'certificate':str(cp),'certificate_sha256':digest(cp),'lower_bound_exact':str(min(lower)) if coverage else None,'lower_bound':float(min(lower)) if coverage else None,'scope':'Q>0 on [0,1] only; finite-radius chart and PDE remain unproved'}
 report['rows'].append(item);print(json.dumps({'utc':now(),**item}),flush=True)
 (OUT/'audit.json').write_text(json.dumps(report,indent=2)+'\n')
report['end_utc']=now();report['all_positive_certified']=all(r['positive_on_whole_interval'] for r in report['rows']);(OUT/'audit.json').write_text(json.dumps(report,indent=2)+'\n')
