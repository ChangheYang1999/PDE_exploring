"""Independent Rodrigues-polynomial rank witnesses; no peer code imported."""
from pathlib import Path
from datetime import datetime,timezone
from math import comb,factorial
import hashlib,json,time
from flint import fmpq as Q,fmpq_poly as P
B=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def legendre(n):
    coeff=[Q(0)]*(n+1)
    for k in range((n+1)//2,n+1):
        e=2*k-n
        coeff[e]=Q((-1)**(n-k)*comb(n,k)*factorial(2*k),2**n*factorial(n)*factorial(e))
    return P(coeff)
def main():
    tick=time.monotonic();files=[B/'PROOF.md',Path(__file__),B/'source/N4_result.json',B/'data/old_basis.json']
    old=json.loads((B/'data/old_basis.json').read_text()); peer=json.loads((B/'source/N4_result.json').read_text())
    shape=lambda z:(z['j'],z['m'],tuple(z['spec']))
    assert len(old['generators'])==1922
    c=Q(4076476460239181,2251799813685248);d=1-1/c;p=[(3+1/c-j*d)/2 for j in range(8)]
    assert all(v.q!=1 for v in p)
    diffs=[p[j]-p[k] for j in range(8) for k in range(j+1,8)]
    assert len(diffs)==28 and all(v.q!=1 for v in diffs)
    rows=[]
    for R,label in [(25,'016'),(50,'017')]:
        path=B/f'data/candidate{label}.json';files.append(path);raw=json.loads(path.read_text())
        assert len(raw['generators'])==2174
        assert len(set(map(shape,raw['generators'][:1922])))==1922
        assert set(map(shape,raw['generators'][:1922]))==set(map(shape,old['generators']))
        wanted={(j,m,('legqs',0,n,4,R)) for j in range(1,4) for m in range(9,16) for n in range(12)}
        assert set(map(shape,raw['generators'][1922:]))==wanted
        a=Q(R*R-1);v0=-1/a;t0=1-v0;v=P([0,1]);t=1-v;L=1+a*v;w=2*t-L;out=[]
        for m in range(9,16):
            for n in range(12):
                pol=legendre(n);assert pol(Q(1))==1
                num=Q(R)**8*v**4*t**m*sum((coef*w**i*L**(n-i) for i,coef in enumerate(pol)),P([]))
                val=num(v0)/a**(n+4)
                expected=Q(R)**8*v0**4*comb(2*n,n)*t0**(m+n)/a**(n+4)
                assert val==expected and val!=0
                if R==25:
                    z=next(z for z in peer['pole_witnesses'] if z['m']==m and z['N']==n)
                    assert val==Q(z['laurent_coefficient'])
                out.append({'m':m,'N':n,'pole_order':n+4,'coefficient':str(val)})
        mode17=4*19*18*(p[1]-9-Q(4,R*R));assert mode17!=0
        if R==25:assert mode17==Q(peer['mode17_leading_harmonic_coefficient'])
        rows.append({'candidate':label,'scale':R,'potential_rank':2174,'all_shapes_equal':True,'witnesses':out,'mode17_coefficient':str(mode17)})
    result={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(f):sha(f) for f in files},'p_j':list(map(str,p)),'noninteger_branch_differences':list(map(str,diffs)),'rows':rows,'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED potential ranks and mode17; density extension OPEN Opus review'}
    (B/'verification/result.json').write_text(json.dumps(result,indent=2)+'\n');print(result['utc'],result['elapsed_seconds'],sha(B/'verification/result.json'))
if __name__=='__main__':main()
