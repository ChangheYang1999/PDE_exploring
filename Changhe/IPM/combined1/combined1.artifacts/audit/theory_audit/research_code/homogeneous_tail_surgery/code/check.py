"""Exact finite potential inverses, with a separately audited q1 comparison."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,time
from flint import fmpq as Q
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def solve(a,target):
    M=(max(target)-1)//2
    def H(m):return -a*a*(a-2) if m==0 else -(a*a-4*m*m)*(a-2-2*m)/2
    def J(m):return (a*a-4*m*m)*(a-2+2*m)/2
    assert a<2 and a!=0 and all(a not in [2*m,-2*m] for m in range(1,M+1))
    out={};nextp=Q(0)
    for m in range(M,-1,-1):
        val=(target.get(2*m+1,Q(0))-J(m+1)*nextp)/H(m)
        out[m]=val;nextp=val
    return out

def direct_density(a,pot):
    out={}
    def add(n,v):
        if n<0:n,v=-n,-v
        if n:out[n]=out.get(n,Q(0))+v
    for m,p in pot.items():
        n=2*m;lap=(a*a-n*n)*p;d=a-2
        add(n+1,-lap*(d-n)/2)
        add(n-1,lap*(d+n)/2)
    return {n:v for n,v in out.items() if v}

def main():
    tick=time.monotonic();c=Q(4076476460239181,2251799813685248);g=1/c;delta=1-g
    q1=-1-4*delta;q2=1-9*delta;q3=-1-5*delta
    assert q1-delta==q3<q2 and 2*q1-1<q2 and q2-delta<q3
    files=[B/'PROOF.md',Path(__file__)];rows=[];previous=None
    for label in ['007','013','014']:
        sp=B/f'source/{label}_sectors.json';rp=B/f'source/{label}_repair.json';files.extend([sp,rp])
        sectors=json.loads(sp.read_text())['sectors'];rep=json.loads(rp.read_text());out=[]
        for key,q in [((4,1),q1),((9,0),q2)]:
            row=next(r for r in sectors if (r['K'],r['L'])==key)
            assert Q(row['exponent_exact'])==q
            target={int(n):Q(v)/(1-c*q) for n,v in row['residual'].items() if Q(v)}
            pot=solve(q+3,target);assert direct_density(q+3,pot)==target
            if key==(4,1):
                expected={v['m']:-Q(v['A1']) for v in rep['moment_checks']}
                assert pot==expected
            else:
                if previous is not None:assert pot==previous
                previous=pot
            out.append({'sector':key,'q':str(q),'potential_homogeneity':str(q+3),'density':{str(n):str(v) for n,v in sorted(target.items())},'potential_cosine_coefficients':{str(m):str(v) for m,v in sorted(pot.items())},'direct_density_equal':True})
        dst=B/f'data/{label}_homogeneous_repairs.json';dst.write_text(json.dumps({'candidate':label,'c_exact':str(c),'repairs':out},indent=2)+'\n')
        rows.append({'candidate':label,'q1_potential_modes':len(out[0]['potential_cosine_coefficients']),'q2_potential_modes':len(out[1]['potential_cosine_coefficients']),'q1_matches_independent_accepted_A1':True,'q2_direct_density_equal':True,'data_sha256':sha(dst)})
    result={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in files},'q1':str(q1),'q2':str(q2),'q3':str(q3),'rows':rows,'elapsed_seconds':time.monotonic()-tick,'verdict':'Own exact checks pass; analytic generalization and q2 design OPEN Opus review'}
    (B/'verification/result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='inputs'},indent=2))
if __name__=='__main__':main()
