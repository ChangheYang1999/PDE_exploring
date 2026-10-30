"""Independently verify positive-vector infinite Schur certificates."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json,time
BASE=Path(__file__).resolve().parents[1]
def digest(p):return sha256(p.read_bytes()).hexdigest()
start=time.monotonic()
p=BASE/'source/T4_results.json';peer=json.loads(p.read_text())
assert peer['proof_sha256']==digest(BASE/'source/T4_S1_PROOF.md')
assert peer['code_sha256']==digest(BASE/'source/T4_check.py')
assert peer['T1_review_sha256']==digest(BASE/'source/T1_REVIEW_v06.md')
rows=[]
for row in peer['rows']:
    a=Q(row['a']);C=Q(row['certified_C']);v=list(map(Q,row['positive_vector']))
    tail=Q(row['constant_tail']);N=len(v)
    assert 0<a<2 and tail>0 and all(x>0 for x in v)
    def K(n):return (n+a)/(n-a)
    def V(i):return v[i] if i<N else tail
    def diagonal(i):return Q(2) if not i else 3+K(2*i)**2
    def edge(i):return 1+K(2*i+2)
    ratios=[]
    for i in range(N+2):
        s=diagonal(i)*V(i)+edge(i)*V(i+1)
        if i:s+=edge(i-1)*V(i-1)
        ratios.append(s/V(i))
    i=N+2;tr=5+K(2*i)**2+K(2*i)+K(2*i+2)
    rho=max(ratios+[tr]);margin=8*C*C-rho
    assert rho==Q(row['rho_rational'])
    assert tr==Q(row['tail_row_ratio'])
    assert margin==Q(row['positive_margin']) and margin>0
    size=9;gram=[[Q(0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for first,second in [(Q(1),K(2*i+2)),(Q(1),Q(1))]:
            co={i:first}
            if i+1<size:co[i+1]=second
            for j,x in co.items():
                for k,y in co.items():gram[j][k]+=x*y
    for i in range(size):
        for j in range(size):
            expected=diagonal(i) if i==j else edge(min(i,j)) if abs(i-j)==1 else Q(0)
            assert gram[i][j]==expected
    rows.append({'a':str(a),'C':str(C),'rho':str(rho),'margin':str(margin),
                 'checked_individual_rows':N+2,'tail_first_index':N+2,
                 'tail_ratio':str(tr),'positive_vector_verified':True,
                 'finite_gram_size':size,'all_checks_pass':True})
    print(a,'C',C,'positive margin',float(margin),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
     'code_sha256':digest(Path(__file__)),'proof_sha256':digest(BASE/'PROOF.md'),
     'source_hashes':{q.name:digest(q) for q in (BASE/'source').iterdir() if q.is_file()},
     'rows':rows,'elapsed_seconds':time.monotonic()-start}
dest=BASE/'verification/results.json';assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
