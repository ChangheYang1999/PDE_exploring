"""Exact rational examples for an independently derived local-model identity."""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,json,os,time
R=Path('RUN_ROOT/verifier')
O=R/'artifacts/linear_response_start_identity_v1';assert not O.exists();O.mkdir()
assert os.sched_getaffinity(0)=={35}and os.environ.get('CUDA_VISIBLE_DEVICES')==''
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
start=now();tick=time.monotonic();checks=[]
def ck(n,v):
 checks.append(dict(name=n,passed=bool(v)))
 if not v:raise AssertionError(n)
def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def add(x,y):return [a+b for a,b in zip(x,y)]
def sub(x,y):return [a-b for a,b in zip(x,y)]
def scale(a,x):return [a*b for b in x]
def mv(A,x):return [dot(row,x)for row in A]
def model(q,A,B,h,p):
 r=add(q,add(mv(A,h),mv(B,p)));return dot(r,r)/2
proof=R/'research/reduced_sensitivity/linear_response_start/PROOF.md'
proof_hash=sha(proof);script_hash=sha(__file__)
scalar=[]
for p in [F(1,10),F(-1,10),F(1,1000000),F(0)]:
 h=-p;keep=(-1+p)**2/2;response=F(1,2);pred=p-p*p/2
 ck('scalar difference '+str(p),response-keep==pred)
 if p>0:ck('positive small displacement worsens '+str(p),response>keep)
 if p<0:ck('negative displacement improves',response<keep)
 if not p:ck('zero response',h==0)
 scalar.append(dict(p=str(p),h_response=str(h),kept=str(keep),response=str(response),difference=str(response-keep),h_full_minimizer=str(1-p)))
ck('displayed difference 19/200',scalar[0]['difference']=='19/200')
ck('displayed kept cost 81/200',scalar[0]['kept']=='81/200')
ck('negative comparison 21/200',scalar[1]['difference']=='-21/200')
u=[F(3,5),F(4,5),F(0)];v=[F(-4,5),F(3,5),F(0)]
A=[[2*u[i],v[i]/3]for i in range(3)];B=[[F(2),F(1)],[F(-1),F(3)],[F(1),F(2)]]
ck('orthonormal retained direction',dot(u,u)==1 and dot(v,v)==1 and dot(u,v)==0)
records=[]
for qi,q in enumerate([[F(1),F(2),F(-3)],add(v,[F(0),F(0),F(2)])]):
 for i,p in enumerate([[F(1,10),F(1,20)],[F(-1,10),F(1,20)],[F(0),F(0)],[F(1,1000000),F(-1,2000000)]]):
  bp=mv(B,p);pb=scale(dot(u,bp),u);h=[-dot(u,bp)/2,F(0)];full=[-dot(u,add(q,bp))/2,F(0)]
  observed=model(q,A,B,h,p)-model(q,A,B,[F(0),F(0)],p)
  predicted=-dot(q,pb)-dot(pb,pb)/2
  ck('identity fixture '+str((qi,i)),observed==predicted)
  ck('response orthogonality '+str((qi,i)),dot(u,add(mv(A,h),bp))==0)
  ck('full model stationarity '+str((qi,i)),dot(u,add(q,add(mv(A,full),bp)))==0)
  ck('full-minus-base response '+str((qi,i)),full[0]+dot(u,q)/2==h[0])
  if qi==1:ck('stationary base comparison '+str(i),dot(u,q)==0 and observed<=0)
  records.append(dict(q=[str(x)for x in q],p=[str(x)for x in p],h=[str(x)for x in h],difference=str(observed),predicted=str(predicted)))
# A saved scale array is already in factor-column order. A nonidentity fixture
# distinguishes the right scatter operation from applying the permutation twice.
perm=[2,0,1];d=[F(2),F(3),F(5)];s=[F(7),F(11),F(13)];z=[None]*3
for i,j in enumerate(perm):z[j]=s[i]/d[i]
ck('nonidentity scatter expected',z==[F(11,3),F(13,5),F(7,2)])
ck('scaled reconstruction exact',[d[i]*z[j]for i,j in enumerate(perm)]==s)
wrong=[None]*3
for i,j in enumerate(perm):wrong[j]=s[i]/d[perm[i]]
ck('double permutation negative control',wrong!=z and [d[i]*wrong[j]for i,j in enumerate(perm)]!=s)
# Capture the concrete proposal that motivates the review, without importing it.
src=R.parent/'d6-num/NOTES_FOR_TEAM.md';before=src.stat();raw=src.read_bytes();after=src.stat();ck('proposal stable read',(before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns))
text=raw.decode();heading='## 2026-10-30T01:48:15Z numerics:';ck('named proposal exists',heading in text)
part=text[text.index(heading):];nextpos=part.find('\n## ',1)
if nextpos>=0:part=part[:nextpos]
ck('proposal objective control', 'at or below the kept value by the linear model' in part)
ck('proposal zero response', 'dp = 0 must return the end state exactly'in part)
ck('proposal stored permuted convention','D (stored permuted)'in part)
proposal=O/'numerics_proposal_0148.md';proposal.write_text(part);proposal.chmod(0o444)
ck('proof unchanged',sha(proof)==proof_hash);ck('script unchanged',sha(__file__)==script_hash)
a=dict(complete=True,all_checks_pass=True,started_utc=start,completed_utc=now(),elapsed_seconds=time.monotonic()-tick,check_count=len(checks),checks=checks,scalar_examples=scalar,matrix_examples=records,permutation_example=dict(perm=perm,d=[str(x)for x in d],s=[str(x)for x in s],correct_z=[str(x)for x in z],wrong_z=[str(x)for x in wrong]),proof_path=str(proof.relative_to(R)),proof_sha256=proof_hash,script_sha256=script_hash,proposal_path=str(proposal.relative_to(R)),proposal_sha256=sha(proposal),producer_notes_read_sha256=hashlib.sha256(raw).hexdigest(),scope='Exact rational examples and finite-dimensional proof review only. No full Euler model, coefficient response for a campaign state, or nonlinear objective was recomputed.')
p=O/'audit.json';p.write_text(json.dumps(a,indent=2)+'\n')
with(R/'VERIFY_REPORT.md').open('a')as f:f.write(f'''
## V573. Linear-response initialization: affine identity and a failed general guarantee

Date: {a['completed_utc']}. Claim: the zero-preserving coefficient response proposed at 01:48 necessarily has iteration-zero objective at or below kept coefficients for a small parameter displacement. Method: derive the complete affine least-squares identity in a standalone proof, then check exact rational counterexamples, retained-subspace stationary cases and a nonidentity permutation control. All {len(checks)} checks pass in {a['elapsed_seconds']:.6f} seconds.

For retained coefficient projector P, base residual q and parameter block B, the response h=-A_tau^dagger Bp changes the affine objective relative to kept coefficients by -q^T P Bp - ||PBp||^2/2. It is guaranteed nonpositive if Pq=0; that stationarity hypothesis is not automatic for these incomplete optimizer endpoints. With A=B=1, q=-1, p=1/10, the response is -1/10 and its cost is 1/2, while keeping coefficients gives 81/200. It is worse by 19/200, even for an exactly linear residual. The failure persists for arbitrarily small positive p. The full affine minimizer includes q and generally is nonzero at p=0. These are different initialization maps.

Verdict: CONFIRMED for the exact identities and rational controls; REFUTED for a universal small-displacement improvement guarantee without an additional hypothesis. OPEN for whether this response improves any actual campaign initialization. The proposed heuristic can still be tested and selected by its measured iteration-zero objective. A failed improvement comparison does not by itself diagnose a coding defect. Saved scales already in permuted order must be used directly when scattering delta_z[perm_i]=s_i/D_i; the new code should test a nonidentity permutation. A finite physical omega move must distinguish its exact log-coordinate difference from its tangent approximation. Proof SHA256 {proof_hash}; audit SHA256 {sha(p)}. No formal build was run.
''')
with(R/'NOTES_FOR_TEAM.md').open('a')as f:f.write(f'''
## {a['completed_utc']} V573: linear-response proposal is feasible, but adjust its correctness test

Read numerics 01:48:15. The proposed -A_tau^dagger B dp is a valid zero-preserving response minimizing the norm of the linearized field/residual change. It need not lower the affine objective relative to keeping coefficients at a nonstationary base: the exact difference is -q^T P Bdp - ||PBdp||^2/2. The omitted first term can have either sign. Example A=B=1, q=-1, dp=.1 gives response cost .5 against kept .405; arbitrarily small positive dp still fails. Thus a small-dp failure of “at or below the kept value” need not mean a bad implementation. Validate against the full affine prediction including q and compare both actual iteration-zero O1 values under the existing lower-value selection rule. The fully relaxed affine minimizer -A_tau^dagger(q+Bdp) is a separate option and is generally nonzero at dp=0, so label it separately if used. This does not require changing the authorized PROFILE selection rule.

Also disambiguate the proposal's scale notation: if saved D is already permuted, reconstruct delta_z[perm_i]=s_i/D_i without a second permutation of D. Identity-ordered campaign factors cannot detect this mistake, so include a nonidentity permutation fixture. For a finite physical move use the declared optimizer-coordinate displacement (for omega, log(omega_new)-log(omega_base)) or explicitly label a tangent approximation. These are prospective implementation checks, not findings against an unwritten tool.

Opus 5.5: review/counterargue the identity and whether its stationarity hypothesis is justified for the chosen PROFILE base before using improvement as a correctness gate. Standalone proof research/reduced_sensitivity/linear_response_start/PROOF.md SHA256 {proof_hash}; exact rational audit artifacts/linear_response_start_identity_v1/audit.json SHA256 {sha(p)}, {len(checks)} checks. No campaign objective or new Jacobian was evaluated.
''')
with(R/'WORKLOG.md').open('a')as f:f.write(f'\n{a["completed_utc"]} V573: standalone zero-preserving-response proof and {len(checks)} exact rational checks. Small-displacement improvement requires a sign/stationarity hypothesis. Sent concrete correction to both lanes via own notes.\n')
print(json.dumps(dict(date=a['completed_utc'],checks=len(checks),seconds=a['elapsed_seconds'],proof_sha256=proof_hash,audit_sha256=sha(p))))
