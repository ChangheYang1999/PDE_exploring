from pathlib import Path
from fractions import Fraction as F
from flint import fmpq
import json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[3];D=R/'research/resolution_aggregate_audit';E=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def decimal_q(t):
 t=t.strip().lower();sg=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,sep,e=t.partition('e');a,dot,b=m.partition('.');return fmpq(sg*int(a+b))*fmpq(10)**((int(e) if sep else 0)-len(b))
A=json.loads((E/'check.json').read_text());rows={}
for line in (D/'source/NUM_REPORT.md').read_text().splitlines():
 if line.startswith('| '):
  v=[x.strip() for x in line.strip('|').split('|')]
  if len(v)==5 and v[0] in ['x_*','mu~ - 1','g = rho~_y(P)',"w'(P)"]:rows[v[0]]=v[1:]
ans=[]
for i,tag in enumerate(['','v3_h0.004','v4_M230','v5_R0knot2']):
 for name,key in [('x_star','x_*'),('mu_minus_1','mu~ - 1'),('g','g = rho~_y(P)'),('w_prime_P',"w'(P)")]:
  text=rows[key][i]
  if '+/-' in text:
   tokens=text.split('+/-');m,r=map(F,tokens);l,u=m-r,m+r;mm,rr=map(decimal_q,tokens);ll,uu=mm-rr,mm+rr
  else:
   tokens=text.strip('[]').split(',');l,u=map(F,tokens);ll,uu=map(decimal_q,tokens)
  raw=A['scalars'][tag][name];lo,hi=F(raw['lo']),F(raw['hi']);assert l<lo<=hi<u
  assert ll<fmpq(raw['lo'])<=fmpq(raw['hi'])<uu and str(ll)==str(l) and str(uu)==str(u)
  ans.append({'tag':tag,'scalar':name,'display':text,'display_lo':str(l),'display_hi':str(u),'raw_lo':str(lo),'raw_hi':str(hi),'strict_outward':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ALL_16_PRINTED_SCALAR_INTERVALS_STRICTLY_OUTWARD_TWO_EXACT_METHODS','code_sha256':sha(Path(__file__)),'source_sha256':sha(D/'source/NUM_REPORT.md'),'primary_sha256':sha(E/'check.json'),'checks':ans,'scope':'Supplementary Fraction/decimal-token fmpq comparison. Physical scalar enclosures remain conditional on producer certificates.'}
with (E/'scalar_displays_checked.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(out['status'])
