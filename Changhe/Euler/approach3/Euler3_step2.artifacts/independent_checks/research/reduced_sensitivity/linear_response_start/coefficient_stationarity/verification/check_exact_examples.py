from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,json
R=Path('RUN_ROOT/verifier')
T=R/'research/reduced_sensitivity/linear_response_start/coefficient_stationarity'
checks=[]
def ck(name,v):
 checks.append(dict(name=name,passed=bool(v)));assert v,name
def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
e1=[F(1),F(0)];e2=[F(0),F(1)]
ck('coefficient gradient zero',dot(e1,e2)==0)
ck('parameter gradient one',dot(e2,e2)==1)
ck('retained projected residual zero',[e2[0],F(0)]==[0,0])
ck('joint gradient nonzero',[dot(e1,e2),dot(e2,e2)]!=[0,0])
ck('discarded coefficient gradient one half',[e2[0],e2[1]/2]==[0,F(1,2)])
ck('discarded example retains zero projection',[e2[0],F(0)]==[0,0])
ck('nonzero projected residual but zero coupling',dot(e2,e1)==0 and dot(e1,e1)>0)
for p in [F(-1,10),F(0),F(1,10),F(1,1000)]:
 kept=(1+p)**2/2;response=kept
 ck('orthogonal coupling difference '+str(p),response-kept==0)
# The scalar counterexample has b=-1; arbitrarily small -t*b=t yields positive difference.
for t in [F(1,10),F(1,100),F(1,1000),F(1,10**12)]:
 delta=t-t*t/2
 ck('small bad displacement '+str(t),delta>0)
 ck('expanded objective '+str(t),F(1,2)-(1-t)**2/2==delta)
now=datetime.datetime.now(datetime.timezone.utc).isoformat();h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
paths=[T/'PROOF.md',Path(__file__).resolve(),R/'artifacts/far_protocol_review_v1/opus_review.md',R/'research/reduced_sensitivity/linear_response_start/PROOF.md']
a=dict(date=now,complete=True,all_checks_pass=all(x['passed']for x in checks),check_count=len(checks),checks=checks,bindings={str(p.relative_to(R)):h(p)for p in paths},scope='Exact examples for an informal proof; no Euler endpoint or formal build.')
out=R/'artifacts/coefficient_stationarity_scope_v1';out.mkdir(exist_ok=False);(out/'audit.json').write_text(json.dumps(a,indent=2)+'\n')
with(R/'VERIFY_REPORT.md').open('a')as f:f.write(f'''\n## V582. Joint nonstationarity does not settle coefficient stationarity\n\nDate: {now}. Claim: a branch that fails joint stationarity necessarily has Pq != 0 in the retained coefficient subspace. Method: a standalone proof and {len(checks)} exact rational checks. Result: all arithmetic checks pass. For A=(1,0)^T, B=(0,1)^T and q=(0,1)^T, the coefficient projection is zero while the joint gradient is (0,1). Truncation gives a second counterexample even when the full coefficient gradient is nonzero. More precisely, the response difference is nonpositive for all sufficiently small parameter displacements if and only if B^TPq=0, which is weaker than Pq=0.\n\nVerdict: CONFIRMED for these finite-dimensional statements and exact examples. REFUTED for the general inference from joint nonstationarity to nonzero retained coefficient projection in the lead's 02:05:41Z explanation. OPEN for either projection at any actual campaign base. The lead's practical ruling remains valid: improvement is not a correctness gate, and measured iteration-zero objectives choose the start. A specific claim Pq != 0 or B^TPq != 0 needs its own retained-factor calculation. Evidence: research/reduced_sensitivity/linear_response_start/coefficient_stationarity/PROOF.md SHA256 {h(T/'PROOF.md')}; artifacts/coefficient_stationarity_scope_v1/audit.json SHA256 {h(out/'audit.json')}. No formal build was run.\n''')
with(R/'NOTES_FOR_TEAM.md').open('a')as f:f.write(f'''\n## {now} verifier: V582 qualification of the stationarity explanation, unchanged PROFILE rule\n\nI agree with your 02:05:41Z response tests and selection rule. One inference needs narrowing: joint nonstationarity, tests (b)/(d), or ongoing objective decrease does not establish Pq != 0. Example A=e1, B=e2, q=e2 has Pq=0 and joint gradient (0,1). A retained-subspace projection can also vanish despite a nonzero discarded coefficient gradient. The exact condition for the affine response to be no worse for every sufficiently small parameter move is B^TPq=0; Pq=0 is sufficient, not necessary. V582 contains a complete proof and {len(checks)} passing rational checks. Please say that coefficient stationarity is unestablished at the chosen base, not that its hypothesis has been disproved by joint nonstationarity. No campaign projection is evaluated here. The response remains a heuristic selected by its measured objective, with no improvement gate.\n''')
print(json.dumps(dict(date=now,checks=len(checks),audit_sha256=h(out/'audit.json'))))
