"""Exact finite-field compatibility certificates by Cartesian Laurent products."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
from math import gcd
import argparse,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import nmod_poly,fmpz
ROOT=Path('research/225_modular_cartesian_scan')
PRIMES=[33554393,33554383,33554371]
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def red(value,p):
    q=F(value);assert q.denominator%p
    return q.numerator%p*pow(q.denominator%p,-1,p)%p

def derivatives(coeff,M,q,p):
    a=[0]*(len(coeff)+2);b=[0]*(len(coeff)+2);half=pow(2,-1,p)
    for j,v in enumerate(coeff):
        if not v:continue
        m=j-M;lo=v*(q+m)*half%p;hi=v*(q-m)*half%p
        a[j]=(a[j]+lo)%p;a[j+2]=(a[j+2]+hi)%p
        b[j]=(b[j]+lo)%p;b[j+2]=(b[j+2]-hi)%p
    return nmod_poly(a,p),nmod_poly(b,p)

def compute(profile,Q,h,p):
    start=time.monotonic();assert fmpz(p).is_prime()
    assert gcd(h,Q)==1 and h>=2 and 2*h<Q and Q%p
    B=max(profile)+1;delta=red(F(2*h,Q),p);cm1=F(2*h,Q-2*h)
    XF={};YF={};XG={};YG={};count=0;divisions=0;ordered=0
    for n in range(1,Q+1):
        M=B*n-1;q=(1-n*delta)%p
        if n==1:
            vals=[0]*(2*M+1)
            for m,v in profile.items():
                v=red(v/2,p);vals[M+m]=v;vals[M-m]=-v%p
        else:
            acc=nmod_poly([],p)
            for i in range(1,n):
                j=n-i;acc+=XG[i]*YF[j]-YG[i]*XF[j];ordered+=1
            acc*=red(1/((n-1)*cm1),p);divisions+=1
            raw=[int(v) for v in acc.coeffs()];rawM=M+2;vals=[0]*(2*M+1)
            for j,v in enumerate(raw):
                m=j-rawM
                if m==0 or abs(m)>M or not m%2:assert v==0,('density support',n,m);count+=1
                else:vals[M+m]=v
        for m in range(1,M+1):
            assert (vals[M+m]+vals[M-m])%p==0,('antisymmetry',n,m);count+=1
            if not m%2:assert vals[M+m]==0;count+=1
        XF[n],YF[n]=derivatives(vals,M,q,p)
        if n<Q:
            GM=B*n;P=(2-n*delta)%p;rhs=[int(v) for v in XF[n].coeffs()];g=[0]*(2*GM+1)
            for j,v in enumerate(rhs):
                m=j-GM
                if m==0 or m%2:assert not v,('stream support',n,m);count+=1;continue
                denom=(m*m-P*P)%p;assert denom,('modular divisor',n,m,p)
                g[j]=v*pow(denom,-1,p)%p;divisions+=1
            for m in range(1,GM+1):assert (g[GM+m]+g[GM-m])%p==0;count+=1
            XG[n],YG[n]=derivatives(g,GM,P,p)
    m=2*h-2;kappa=2*vals[M+m-1]%p;forcing=2*int(XF[Q][B*Q+m])%p
    assert (forcing+m*kappa)%p==0
    return kappa,vals,dict(prime=p,kappa=kappa,forcing=forcing,ordered_pairs=ordered,
        support_and_symmetry_checks=count,checked_divisions=divisions,
        final_density_sha256=sha256(json.dumps(vals,separators=(',',':')).encode()).hexdigest(),
        actual_elapsed_s=time.monotonic()-start)

def references(profile,Q,h,p,vals):
    f=Path('research/24_rational_scan/verification')/f'{profile}_{2*h}_{Q}.json'
    if not f.exists() and not f.with_suffix(f.suffix+'.gz').exists():return None
    from read_evidence_bytes import read_bytes
    raw=read_bytes(f);r=json.loads(raw);B=(20 if profile=='cand007' else 2);M=B*Q-1
    expected={int(k):red(v,p) for k,v in r['density_at_resonance'].items()}
    for m in range(1,M+1,2):assert 2*vals[M+m]%p==expected.get(m,0),('exact reference',profile,Q,h,m)
    return dict(path=str(f),sha256=sha256(raw).hexdigest(),full_final_density_match=True,coordinates=(M+1)//2)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--profile',choices=['sin1','cand007'],default='cand007');ap.add_argument('--Qmax',type=int,default=120);ap.add_argument('--pairs');ap.add_argument('--seconds',type=float,default=18000);a=ap.parse_args()
    started=time.monotonic();out=ROOT/'verification'/a.profile;out.mkdir(exist_ok=True)
    if a.profile=='sin1':profile={1:F(1)};lo=F(0);hi=F(1);source=None
    else:
        p=Path('research/02_candidate007/data/leading_exact.json');raw=p.read_bytes();profile={int(k):F(v) for k,v in json.loads(raw)['density'].items() if F(v)};lo=F(2,5);hi=F(1,2);source=dict(path=str(p),sha256=sha256(raw).hexdigest())
    grid=[(Q,h) for Q in range(5,a.Qmax+1) for h in range(2,Q//2+1) if gcd(h,Q)==1 and 2*h<Q and lo<F(2*h,Q)<hi]
    if a.pairs:grid=[tuple(map(int,p.split(':'))) for p in a.pairs.split(',')]
    completed=[]
    for Q,h in grid:
        path=out/f'Q{Q}_h{h}.json'
        if path.exists():
            row=json.loads(path.read_text());assert row['Q']==Q and row['h']==h and row['all_checks_pass'];completed.append(row);continue
        if time.monotonic()-started>a.seconds:break
        attempts=[];refs=[]
        for prime in PRIMES:
            kap,vals,result=compute(profile,Q,h,prime);attempts.append(result)
            ref=references(a.profile,Q,h,prime,vals)
            if ref:refs.append(ref)
            if kap:break
        row=dict(checked_at_utc=stamp(),all_checks_pass=True,profile=a.profile,source=source,delta=str(F(2*h,Q)),Q=Q,h=h,first_resonance=Q,mode=2*h-3,attempts=attempts,certified_nonzero=bool(kap),exact_references=refs)
        path.write_text(json.dumps(row,indent=2)+'\n');completed.append(row)
        print(json.dumps(dict(profile=a.profile,Q=Q,h=h,kappa=kap,prime=prime,seconds=sum(r['actual_elapsed_s'] for r in attempts),utc=stamp())),flush=True)
        manifest=dict(checked_at_utc=stamp(),profile=a.profile,Qmax=a.Qmax,requested_pairs=grid,completed_pairs=[[r['Q'],r['h']] for r in completed],complete=len(completed)==len(grid),all_nonzero=all(r['certified_nonzero'] for r in completed),actual_elapsed_s=time.monotonic()-started)
        (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    for name in ['modular_cartesian_scan.py','read_evidence_bytes.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(dict(utc=stamp(),profile=a.profile,completed=len(completed),requested=len(grid),seconds=time.monotonic()-started)),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        r=dict(checked_at_utc=stamp(),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True);raise SystemExit(1)
