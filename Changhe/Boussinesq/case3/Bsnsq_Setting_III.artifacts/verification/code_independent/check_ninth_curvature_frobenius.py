"""P311 independent rational coefficient matching, no integral-factor or teammate imports."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
N=34
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[];records=[]
def ck(n,b,d=None):checks.append(dict(name=n,passed=bool(b),detail=d))
def p(d=None):return[F((d or {}).get(i,0))for i in range(N+1)]
def add(a,b):return[x+y for x,y in zip(a,b)]
def scale(a,c):return[x*c for x in a]
def mul(a,b):
 out=p()
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:N+1-i]):
    if y:out[i+j]+=x*y
 return out
def der(a):return[(i+1)*a[i+1]if i<N else F(0)for i in range(N+1)]
def solve(B,A,R,m,free):
 """B f' - A f = R except the one explicitly retained resonant defect."""
 assert B[0]==0 and B[1]==1 and A[0]==m
 f=p();defect=None
 for n in range(N+1):
  known=sum((B[i+1]*(n-i)-A[i])*f[n-i]for i in range(1,min(n,N-1)+1))
  # B[N+1] is zero; its multiplier would be zero at n=N.
  if n==m:defect=R[n]-known;f[n]=F(free)
  else:f[n]=(R[n]-known)/F(n-m)
 return f,defect

def evaluate(C,k,H,c,a,freeD=F(0),freeG=F(0),tag=''):
 B=p({1:1,2:k,9:c,13:a});Bd=der(B)
 T,rt=solve(B,add(p({0:8}),scale(Bd,2)),p(),10,C)
 eta,re=solve(B,add(p({0:5}),Bd),scale(T,-1),6,H)
 v=scale(add(der(Bd),eta),F(-1,2))
 rd_rhs=add(scale(mul(der(v),T),8),scale(mul(v,der(T)),-12))
 D,rd=solve(B,add(p({0:16}),scale(Bd,4)),rd_rhs,20,freeD)
 rg_rhs=add(scale(D,-1),add(scale(mul(der(v),eta),2),scale(mul(v,der(eta)),-6)))
 gamma,rg=solve(B,add(p({0:13}),scale(Bd,3)),rg_rhs,16,freeG)
 expected_d=F(48,5)*k+2496*a/C+F(169088,165)*c*k**4/C
 expected_g=-F(6,5)*C*H*k-F(9,385)*C*k**8+1092*a*H+F(517832,1155)*c*H*k**4+162*C*c
 ck(tag+'_first_two_compatibilities',rt==re==0)
 ck(tag+'_fourth_residue',rd==C*C*expected_d,dict(defect=str(rd),expected=str(C*C*expected_d)))
 ck(tag+'_fifth_residue',rg==expected_g,dict(defect=str(rg),expected=str(expected_g)))
 for name,f,A,R,defect,m in [('T',T,add(p({0:8}),scale(Bd,2)),p(),rt,10),('eta',eta,add(p({0:5}),Bd),scale(T,-1),re,6),('D',D,add(p({0:16}),scale(Bd,4)),rd_rhs,rd,20),('gamma',gamma,add(p({0:13}),scale(Bd,3)),rg_rhs,rg,16)]:
  residual=add(add(mul(B,der(f)),scale(mul(A,f),-1)),scale(R,-1))
  ck(tag+'_'+name+'_direct_equation_defect',residual[:N]==p({m:-defect})[:N])
 ck(tag+'_curl',add(add(der(Bd),scale(v,2)),eta)==p())
 ck(tag+'_orders',all(x==0 for x in T[:10])and all(x==0 for x in eta[:6])and all(x==0 for x in D[:9])and all(x==0 for x in gamma[:5]))
 ck(tag+'_leading_D_coefficient',D[9]==-F(120,11)*C*k)
 if k==0 and c==a==0:
  expected=p({15:-F(36,5)*C*H,19:5*C*C,20:freeD})
  ck(tag+'_zero_curvature_exact_D',D==expected)
 records.append(dict(tag=tag,C=str(C),k=str(k),H=str(H),c=str(c),a=str(a),free_D20=str(freeD),free_gamma16=str(freeG),residue_D=str(rd/(C*C)),residue_gamma=str(rg),compatible=(rd==rg==0)))
 return D,gamma,rd,rg

triples=[(F(1),F(-1),F(1)),(F(1),F(1),F(1)),(F(-1),F(1),F(-1)),(F(-2),F(-1,2),F(-3)),(F(2),F(3,2),F(0)),(F(3),F(-2),F(2,7)),(F(1),F(0),F(1)),(F(-1),F(0),F(0))]
for i,(C,k,H)in enumerate(triples):
 tuned_c=k*(231*H+k**7)/6930
 for label,c,a in [('tuned',tuned_c,-C*k/260-F(2642,6435)*tuned_c*k**4),('old_family',F(0),-C*k/260),('arbitrary',F(2,7),F(-3,11)),('retuned_shift',tuned_c+F(1,1000),-C*k/260-F(2642,6435)*(tuned_c+F(1,1000))*k**4)]:
  output=[]
  for j,(fd,fg)in enumerate([(F(0),F(0)),(F(7,3),F(-5,2))]):output.append(evaluate(C,k,H,c,a,fd,fg,f'case{i}_{label}_free{j}'))
  ck(f'case{i}_{label}_free_constants_leave_residues',output[0][2:]==output[1][2:])
  if label=='tuned':ck(f'case{i}_tuned_both_zero',output[0][2]==output[0][3]==0)
  if label=='retuned_shift':ck(f'case{i}_shift_negative_control',output[0][2]==0 and output[0][3]==F(162,1000)*C)
V=Path('research/311_ninth_order_curvature/verification');freeze=json.loads((V/'freeze.json').read_text());ck('proof_precedes_calculation',freeze['utc']<start);ck('proof_hash',hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==freeze['proof_sha256'])
for r in freeze['inputs']:ck('frozen_'+r['snapshot'],hashlib.sha256((V/r['snapshot']).read_bytes()).hexdigest()==r['sha256'])
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,N=N,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,records=records,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact finite parameter controls of the arbitrary-parameter proof; no proof by sampling.')
(V/'fraction_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['checks','records']},indent=2));print('FAILED',[x for x in checks if not x['passed']])
