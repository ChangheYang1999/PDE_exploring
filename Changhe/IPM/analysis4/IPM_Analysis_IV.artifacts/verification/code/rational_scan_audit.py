"""Exact independent Cartesian/Laurent audit of rational resonance scans."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
from math import gcd
import json,argparse,time
from laurent_log_audit import L,parse,Q,Poly


def first(delta):
    n=2*delta.denominator//gcd(delta.numerator,2)
    if n*delta==2:n*=2
    return n,int(n*delta/2)-1


def compute(delta,initial,n0):
    d=Q(str(delta));c=1/(1-d)
    F={};G={};XF={};YF={};XG={};YG={}
    start=time.monotonic()
    for n in range(1,n0+1):
        p=1-n*d
        if n==1: A=parse(p,{str(k):[v] for k,v in initial.items()})
        else:
            non=L(p,0,[])
            for i in range(1,n):
                j=n-i
                non=non+XG[i]*YF[j]-YG[i]*XF[j]
            A=non.scale(1/((n-1)*(c-1)))
        F[n]=A;XF[n]=A.X();YF[n]=A.Y()
        if n<n0:
            H=XF[n];P=p+1
            assert len(H.a)<=1
            bb=[]
            for idx,h in enumerate(H.a[0].coeffs() if H.a else []):
                k=idx-H.M
                divisor=k*k-P*P
                if not divisor:
                    assert not h
                    bb.append(Q(0))
                else:bb.append(h/divisor)
            B=L(P,H.M,[Poly(bb)]);G[n]=B;XG[n]=B.X();YG[n]=B.Y()
            assert (XG[n].X().scale(-1)+YG[n].Y()-XF[n]).zero(),('poisson',n)
    _,j=first(delta);A=F[n0];H=XF[n0]
    kappa=2*A.a[0][A.M+2*j-1]
    forcing=2*H.a[0][H.M+2*j]
    assert forcing==-2*j*kappa
    density={str(k):str(2*A.a[0][A.M+k]) for k in range(1,A.M+1,2) if A.a[0][A.M+k]}
    return dict(delta=str(delta),c=str(c),n0=n0,j0=j,kappa_exact=str(kappa),forcing_exact=str(forcing),
                kappa_nonzero=bool(kappa),density_at_resonance=density,elapsed_s=time.monotonic()-start)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--profile',choices=['sin1','cand007'],default='sin1');ap.add_argument('--seconds',type=float,default=500);args=ap.parse_args()
    target=Path('research/24_rational_scan');src=Path('../a4-num/notes')/('resonance_scan_'+args.profile+'.json')
    snapshot=target/'sources'/src.name
    if not snapshot.exists():snapshot.write_bytes(src.read_bytes())
    raw=snapshot.read_bytes();data=json.loads(raw)
    Nmax=60 if args.profile=='sin1' else 17
    expected={Fraction(a,b) for b in range(2,Nmax+1) for a in range(1,b) if gcd(a,b)==1 and Fraction(2,5)<Fraction(a,b)<Fraction(1,2) and first(Fraction(a,b))[0]<=Nmax}
    assert {Fraction(r['delta']) for r in data}==expected,('enumeration',len(data),len(expected))
    if args.profile=='sin1':initial={1:'1'}
    else:initial={int(k):v for k,v in json.loads(Path('research/02_candidate007/data/leading_exact.json').read_text())['density'].items()}
    start=time.monotonic();completed=[]
    for row in data:
        d=Fraction(row['delta']);n0,j=first(d)
        output=target/'verification'/(args.profile+'_'+str(d).replace('/','_')+'.json')
        if output.exists():
            record=json.loads(output.read_text());assert record['matches_report_exact_kappa'];completed.append(str(d));continue
        if time.monotonic()-start>args.seconds:break
        result=compute(d,initial,n0)
        result.update(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                      code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                      cartesian_engine_sha256=sha256(Path('code/laurent_log_audit.py').read_bytes()).hexdigest(),
                      source_snapshot=str(snapshot),source_sha256=sha256(raw).hexdigest(),profile=args.profile,
                      matches_report_exact_kappa=Q(result['kappa_exact'])==Q(row['kappa_exact']))
        assert result['matches_report_exact_kappa'],str(d)
        output.write_text(json.dumps(result,indent=2)+'\n');completed.append(str(d))
        print(json.dumps(dict(delta=str(d),n0=n0,nonzero=result['kappa_nonzero'],match=True,elapsed_s=result['elapsed_s'])),flush=True)
    summary=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),profile=args.profile,
                 exact_enumeration_count=len(expected),completed_count=len(completed),completed=completed,
                 all_complete=len(completed)==len(expected),actual_elapsed_s=time.monotonic()-start)
    (target/'verification'/(args.profile+'_summary.json')).write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary),flush=True)

if __name__=='__main__':main()
