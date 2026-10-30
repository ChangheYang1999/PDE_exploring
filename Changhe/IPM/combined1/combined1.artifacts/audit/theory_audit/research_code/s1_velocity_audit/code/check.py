from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
start=time.monotonic();root=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[];N=64;tail=Q(1,10**12)
for aq,C in [(Q(6,5),Q(1616466,10**6)),(Q(13,10),Q(1836267,10**6)),(Q(7,5),Q(2142307,10**6)),(Q(3,2),Q(2585263,10**6)),(Q(19,10),Q(13806975,10**6))]:
 def K(n):return (n+aq)/(n-aq)
 def D(i):return Q(2) if i==0 else 3+K(2*i)**2
 def E(i):return 1+K(2*i+2)
 dd=[float(D(i)) for i in range(N)];ee=[float(E(i)) for i in range(N)]
 x=[1.0]*N
 for _ in range(180):
  y=[dd[i]*x[i]+(ee[i-1]*x[i-1] if i else 0)+(ee[i]*x[i+1] if i+1<N else 0) for i in range(N)]
  scale=max(y);x=[z/scale for z in y]
 vv=[Q(round(z*10**14),10**14)+tail for z in x]
 def V(i):return vv[i] if i<N else tail
 ratios=[(D(i)*V(i)+(E(i-1)*V(i-1) if i else 0)+E(i)*V(i+1))/V(i) for i in range(N+2)]
 tailratio=5+K(2*(N+2))**2+K(2*(N+2))+K(2*(N+3))
 rho=max(ratios+[tailratio]);margin=8*C*C-rho
 assert margin>0
 # Independent finite matrix expansion check including both boundary outputs.
 A=[[Q(0)]*5 for _ in range(10)]
 for i in range(5):
  A[2*i][i]=1;A[2*i+1][i]=1
  if i+1<5:A[2*i][i+1]=K(2*i+2);A[2*i+1][i+1]=1
 gram=[[sum(row[i]*row[j] for row in A) for j in range(5)] for i in range(5)]
 for i in range(5):
  for j in range(5):assert gram[i][j]==(D(i) if i==j else E(min(i,j)) if abs(i-j)==1 else 0)
 rows.append({'a':str(aq),'certified_C':str(C),'rho_rational':str(rho),'rho_approx':float(rho),'positive_margin':str(margin),'tail_row_ratio':str(tailratio),'positive_vector':[str(v) for v in vv],'constant_tail':str(tail),'all_rows_verified':True,'finite_gram_exact':True})
 print('a',aq,'C',float(C),'rho',float(rho),'margin',float(margin),flush=True)
record={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':digest(root/'PROOF.md'),'code_sha256':digest(Path(__file__)),'T1_review_sha256':digest(root/'source/T1_REVIEW_v06.md'),'rows':rows,'elapsed_seconds':time.monotonic()-start}
(root/'verification/results.json').write_text(json.dumps(record,indent=2)+'\n')
