from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import comb
import sympy as s
import json,hashlib,time
V=Path('research/320_external_next_resonance_audit/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def ck(n,v,d=None):checks.append(dict(name=n,passed=bool(v),detail=d))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((V/'freeze.json').read_text());ck('proof_precedes_controls',f['utc']<start);ck('proof_hash',sha(V.parent/'PROOF.md')==f['proof_sha256'])
for z in f['inputs']:ck('frozen_'+z['snapshot'],sha(V/z['snapshot'])==z['sha256'])
C,k,H,a=s.symbols('C k H a',real=True)
M=s.Matrix([[416*a+s.Rational(52,25)*C*k,0],[-s.Rational(6,385)*k**8-s.Rational(63,25)*H*k,390*a+s.Rational(21,20)*C*k]])
Mt=M.subs({a:-C*k/260,H:-k**7/231});target=s.Matrix([[s.Rational(12,25)*C*k,0],[-s.Rational(9,1925)*k**8,-s.Rational(9,20)*C*k]])
for i in range(2):
 for j in range(2):ck(f'tuned_matrix_{i}{j}',s.expand(Mt[i,j]-target[i,j])==0)
ck('matrix_determinant',s.expand(Mt.det()+s.Rational(27,125)*C**2*k**2)==0)
conv=[-F(2016,11),F(3472,5),F(-1008),F(690),-F(1520,7),F(24)];ck('stated_convolution',sum(conv)==-F(6,385))
def J(n):return F((-1)**(n-4)*comb(n-2,2),n)if n>=4 else F(0)
# Independent multiplication of (1+z)^4(14+6z), no six-term list used.
p4=[F(comb(4,j))for j in range(5)];prod=[F(0)]*6
for i,c in enumerate(p4):prod[i]+=14*c;prod[i+1]+=6*c
c11=sum(c*J(11-i)for i,c in enumerate(prod));ck('earlier_first_residue',c11==-F(3,770));ck('convolution_quarter_relation',4*c11==sum(conv))
last1=(6*J(5)+4*J(4))/3;last2=F(2,3);ck('third_additive_residue',last1==-F(13,15));ck('fourth_additive_residue',last2==F(2,3));ck('last_two_sum',last1+last2==-F(1,5))
rv=182*a*H-C*H*k/5-s.Rational(3,770)*C*k**8
ck('earlier_vorticity_tuning',s.expand(rv.subs(a,-C*k/260)+s.Rational(9,10)*C*k*(H+k**7/231))==0)
ck('earlier_both_tuned_zero',s.expand(rv.subs({a:-C*k/260,H:-k**7/231}))==0)
ck('thermal_curvature_correction',-F(2,3)*1716+156*10==416);ck('vorticity_curvature_correction',-F(1716,2)+F(156*16,2)==390);ck('previous_vorticity_curvature_correction',-F(1716,6)+F(156*6,2)==182)
convmat=Mt*s.diag(C**2/24,s.Rational(1,6));ct=s.Matrix([[C**3*k/50,0],[-3*C**2*k**8/15400,-3*C*k/40]])
for i in range(2):
 for j in range(2):ck(f'converted_matrix_{i}{j}',s.expand(convmat[i,j]-ct[i,j])==0)
ck('converted_determinant',s.expand(convmat.det()+s.Rational(3,2000)*C**4*k**2)==0)
text=(V/'A171_PROOF.md').read_text();old='-Cku^{-8}P^2\n\\frac{CH}{3}u^{-6}(6+4ku)J_0';new='-Cku^{-8}P^2\n+\\frac{CH}{3}u^{-6}(6+4ku)J_0'
ck('exact_missing_plus_anchor',text.count(old)==1,text.count(old));fixed=text.replace(old,new);ck('one_plus_added',len(fixed)==len(text)+1 and fixed.replace(new,old)==text)
(V/'corrected_A171_PROOF.md').write_text(fixed);(V/'required_A171_replacement.json').write_text(json.dumps(dict(old=old,new=new,scope='Intermediate displayed formula only; all matrix entries and final verdict unchanged.'),indent=2)+'\n')
status=json.loads((V/'A171_opus_status.json').read_text());ck('A171_failed_before_invocation',status['error_type']=='CredentialRetrievalError' and status['requested_model_id']=='us.anthropic.claude-opus-5-5')
for fn,expected in [('P308_fraction_checks.json',256),('P308_symbolic_checks.json',23)]:
 z=json.loads((V/fn).read_text());ck('antecedent_'+fn,z['passed']==z['total']==expected)
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,code_sha256=sha(Path(__file__)),corrected_proof_sha256=sha(V/'corrected_A171_PROOF.md'),scope='Finite adjudication of A171, including an intermediate missing plus sign and normalization conversion. P308 proof remains the independent mathematical dependency.')
(V/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='checks'},indent=2));print('FAILED',[x for x in checks if not x['passed']])
