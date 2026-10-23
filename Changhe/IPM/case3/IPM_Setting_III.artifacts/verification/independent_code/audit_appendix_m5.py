"""Independent rational reconstruction of the Appendix A.3.45 certificates."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
p=Path('evidence/lead_merge_audit/AUD26_m5_inputs.json');data=json.loads(p.read_text())
assert hashlib.sha256(Path(data['source_report']).read_bytes()).hexdigest()==data['source_sha256']
m=F(data['weight_m'])
def b(j):return (m*m+4*j*j)/(4*abs(4*j*j-m*m))
def diag(j,sgn):return F(sgn,4 if j==1 else 2)
rows=[]
for v in data['certificate_A']:
 a=list(map(F,v['vector']));ratio=F(data['tail_ratio']);u=F(v['upper']);l=F(v['lower']);sgn=v['diagonal_sign']
 rs=[]
 for j in range(1,len(a)+1):
  nxt=a[j] if j<len(a) else a[-1]*ratio
  prev=a[j-2] if j>1 else F(0)
  rs.append(diag(j,sgn)+b(j)*nxt/a[j-1]+(b(j-1)*prev/a[j-1] if j>1 else 0))
 # For j>=11 both b(j-1),b(j) decrease, so the first tail row bounds all.
 tail=diag(11,sgn)+b(10)/ratio+b(11)*ratio
 assert all(r<u for r in rs) and tail<u
 norm=sum(z*z for z in a)
 ray=(sum(diag(j,sgn)*a[j-1]**2 for j in range(1,len(a)+1))+sum(2*b(j)*a[j-1]*a[j] for j in range(1,len(a))))/norm
 assert ray>l
 closest=min(range(10),key=lambda j:u-rs[j])
 rows.append(dict(certificate='A',name=v['name'],upper=str(u),lower=str(l),row_ratios=[str(r) for r in rs],minimum_margin=str(u-rs[closest]),closest_row=closest+1,tail_first_ratio=str(tail),rayleigh=str(ray),rayleigh_decimal=float(ray)))
for v in data['certificate_B']:
 N=v['N'];sgn=v['diagonal_sign'];tau=F(v['tau']);u=F(v['upper']);l=F(v['lower'])
 assert tau==diag(N+1,sgn)+2*b(N+1)
 piv=[]
 for j in range(1,N+1):
  q=u-diag(j,sgn)-(b(j-1)**2/piv[-1] if j>1 else 0)
  if j==N:q-=b(N)**2/(u-tau)
  assert q>0
  piv.append(q)
 low=[]
 for j in range(1,8):
  q=l-diag(j,sgn)-(b(j-1)**2/low[-1] if j>1 else 0)
  assert q>0 if j<7 else q<0
  low.append(q)
 rows.append(dict(certificate='B',name=v['name'],upper_pivots=[str(x) for x in piv],lower_pivots=[str(x) for x in low],tau=str(tau)))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),rows=rows,scope='Exact rational finite comparisons and first monotone tail rows. The infinite operator implications are proved in the audited appendix and independent results59/61.')
Path('evidence/lead_merge_audit/AUD26_m5_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(utc=out['utc'],status='PASS',certificate_rows=len(rows),A_margins=[(r['closest_row'],r['minimum_margin']) for r in rows if r['certificate']=='A']),indent=2))
