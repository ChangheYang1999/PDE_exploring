"""Exact finite checks of the log-independent edge majorant constants."""
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from collections import defaultdict
from math import factorial
import json,time
from edge_sine_audit import parse,source

def norm(x):return sum((abs(v)*factorial(k)*3**k for (k,m),v in x.items()),Q(0))
def main():
 start=time.monotonic();root=Path('research/106_edge_convergence');path=Path('research/102_edge_recurrence_reference/verification/exact_reference.json');raw=path.read_bytes();ref=json.loads(raw)
 full=ref['full_prefix'];H={i:norm(parse(full[i-1]['density'])) for i in (1,2,3)};G={i:norm(parse(full[i-1]['stream'])) for i in (1,2,3)}
 for row in full[:3]:
  assert set(row['density'])=={'0'} and set(row['stream'])=={'0'}
 B={i:(abs(2-Q(2*i,3))+Q(2*i,3))*G[i]+(2*i-1+3*abs(1-Q(2*i,3)))*H[i] for i in H}
 C={i:(abs(2-Q(2*i,3))+Q(4*i,3))*G[i]+5*(2*i-1)*H[i] for i in H}
 assert B=={1:Q(23,10),2:Q(929,2240),3:Q(2537,53760)}
 assert C[1]-B[1]==Q(31,10)
 assert all(C[i]+B[i]*(2*i-3)>=0 for i in H)
 mass=sum((B[i]/Q(5,2)**i for i in B),Q(0));assert mass==Q(831077,840000)<1
 rows=[];pairs=0;checks=0
 for K in (1,3):
  records=ref['variants'][str(K)]['rows'];F={r['n']:parse(r['density']) for r in records};S={r['n']:parse(r['stream']) for r in records};M={n:norm(v) for n,v in F.items()};N={n:norm(v) for n,v in S.items()};A=Q(23,10) if K==1 else Q(5,2);first=4 if K==1 else 7
  for n in M:
   assert M[n]<=A**(n-1) and N[n]<=3*M[n];checks+=2
   if n<first:
    rows.append({'K':K,'n':n,'density_norm':str(M[n]),'geometric_bound':str(A**(n-1)),'base_case':True});continue
   total=defaultdict(Q)
   for i in range(1,K+1):
    j=n-i;part=defaultdict(Q)
    for a,b in ((i,j),(j,i)):
     for key,v in source(S[a],F[b],2-Q(2*a,3),1-Q(2*b,3)).items():part[key]+=v
    actual=norm(part);bound=(2*B[i]*j-C[i])*M[j]
    assert actual<=bound
    assert bound/(2*n-3)<=B[i]*M[j]
    for key,v in part.items():total[key]+=v
    pairs+=2;checks+=2
   forcing=norm(total);assert M[n]<=forcing/(2*n-3)
   majorant=sum((B[i]*M[n-i] for i in range(1,K+1)),Q(0));assert M[n]<=majorant;checks+=2
   rows.append({'K':K,'n':n,'density_norm':str(M[n]),'stream_norm':str(N[n]),'linear_majorant':str(majorant),'base_case':False})
 result={'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'input_path':str(path),'input_sha256':sha256(raw).hexdigest(),'H':{i:str(v) for i,v in H.items()},'Q':{i:str(v) for i,v in G.items()},'B':{i:str(v) for i,v in B.items()},'C':{i:str(v) for i,v in C.items()},'K3_majorant_mass':str(mass),'K3_mass_gap':str(1-mass),'exact_inequalities_checked':checks,'ordered_pair_products':pairs,'rows':rows,'scope':'Exact finite coefficient and majorant checks through18 for K1,K3. Infinite convergence proof is in PROOF.md, pending independent review.','actual_elapsed_s':time.monotonic()-start,'complete':True}
 data=json.dumps(result,indent=2)+'\n';(root/'verification/checks.json').write_text(data)
 hashes={}
 for name in ('edge_convergence_audit.py','edge_sine_audit.py'):
  data=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(data);hashes[name]=sha256(data).hexdigest()
 (root/'verification/MANIFEST.json').write_text(json.dumps({'created_at_utc':result['checked_at_utc'],'source_hashes':hashes,'input_sha256':sha256(raw).hexdigest(),'checks_sha256':sha256((root/'verification/checks.json').read_bytes()).hexdigest()},indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
if __name__=='__main__':main()
