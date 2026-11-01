"""Independent Cartesian perturbations of fixed-deficit resonant cycles."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import json,time,sys
from laurent_log_audit import L,Q,parse
from maximal_log_cartesian_check import poisson,rational_function
sys.set_int_max_str_digits(0)


def solve_density(non,n):
    lam=2*(n-1);term=non.scale(Q(1,lam));ans=term
    while term.a:
        term=term.dt().scale(Q(3,lam));ans=ans+term
    assert (ans.scale(-lam)+ans.dt().scale(Q(3))+non).zero()
    return ans


def pair(G,F):return G.X()*F.Y()-G.Y()*F.X()

def amplitude(A,q,m):
    if q<0 or q>=len(A.a) or m>A.M:return Q(0)
    return 2*A.a[q][A.M+m]


def main():
    start=time.monotonic();dlt=Q(2,3);F={1:parse(Q(1,3),{1:['1']})};G={1:poisson(F[1])}
    for n in [2,3]:
        non=L(1-dlt*n,0,[])
        for i in range(1,n):non=non+pair(G[i],F[n-i])
        F[n]=solve_density(non,n);G[n]=poisson(F[n])
    rows=[]
    for k in [3,4,5,7,10,15]:
        for deficit in range(min(3,k-1)+1):
            q=k-1-deficit
            hg={0:parse(2-dlt*(3*k),{2*k-2:['0']*q+['1']})};hf={}
            for r in [1,2,3]:
                n=3*k+r;non=L(1-dlt*n,0,[])
                for i in range(r):non=non+pair(hg[i],F[r-i])
                for i in range(1,r):non=non+pair(G[i],hf[r-i])
                hf[r]=solve_density(non,n);hg[r]=poisson(hf[r])
            actual=amplitude(hg[3],q+1,2*k)
            expected=Q(k,k-deficit)*rational_function('',k)
            assert actual==expected,(k,deficit,actual,expected)
            assert actual*factorial(q+1)/factorial(q)==k*rational_function('',k)
            rows.append(dict(k=k,deficit=deficit,input_degree=q,output_degree=q+1,
                actual_transfer=str(actual),expected_transfer=str(expected),
                factorial_transfer=str(actual*(q+1)),matches=True))
    # No degree or frequency truncation occurs in these linearized Cartesian blocks.
    root=Path('research/63_fixed_log_deficit')
    files=['fixed_deficit_transfer.py','maximal_log_cartesian_check.py','laurent_log_audit.py']
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
        delta='2/3',leading_input='sin(theta)',arithmetic='exact rational Cartesian Laurent-log',
        cases=len(rows),checks=rows,all_pass=True,actual_elapsed_s=time.monotonic()-start,
        source_sha256={name:sha256(Path('code',name).read_bytes()).hexdigest() for name in files})
    (root/'verification'/'transfer_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in files:(root/'sources'/f'{name}.txt').write_bytes(Path('code',name).read_bytes())
    print(json.dumps(dict(cases=len(rows),all_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

if __name__=='__main__':main()
