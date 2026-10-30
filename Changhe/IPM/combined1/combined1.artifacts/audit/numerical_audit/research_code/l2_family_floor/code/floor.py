"""Finite-family L2 lower bound; no sampling or coefficient optimization."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq,arb,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import ar
BASE=ROOT/'research/l2_family_floor'

def distance(B,K,delta,direct=False):
    a0=(B+1)*delta/2-fmpq(3,2);assert a0>-fmpq(1,2)
    step=delta/2;assert step.denominator>2*B
    D=1/ar(2*a0+1).sqrt();count=0;removed=False
    for ell in range(1,2*B+1):
        lam=ell*step;x=1-lam;lo=max(0,int(x.numerator//x.denominator)+1);hi=2*K+4
        assert lam+lo>1
        count+=max(0,hi-lo+1)
        a=(ell-B-1)*step;b=(ell+B+1)*step-2
        while lo<=hi and lo+a<=0:
            if lo+a==0:assert ell==B+1 and lo==0;removed=True
            else:D*=ar(abs(lo+a))/ar(lo+b)
            lo+=1
        if lo>hi:continue
        if direct:
            for k in range(lo,hi+1):D*=ar(k+a)/ar(k+b)
        else:
            D*=ar(hi+a+1).gamma()*ar(lo+b).gamma()/(ar(lo+a).gamma()*ar(hi+b+1).gamma())
    assert removed
    return D,count

def run():
    ctx.prec=512;start=time.monotonic();source=ROOT/'research/sector_audit/verification/stationary_principal.json'
    data=json.loads(source.read_text());c=fmpq(data['cl']);delta=1-1/c;s=fmpq(1,131072);eta=fmpq(1,163840)
    rows=[]
    for B in range(4,9):
        rec=data['branches'][B-1];assert rec['index']==B
        E2=sum((fmpq(v)**2 for v in rec['forcing_sin'].values()),fmpq(0));E=(arb.pi()*ar(E2)).sqrt()
        minK=max([max(map(int,data['leading_potential']))//2]+[max(map(int,r['potential_cos']))//2 for r in data['branches'][:B-1]])
        for K in [75,150,300,750,1500,3675,10000,100000]:
            if K<minK:continue
            D,count=distance(B,K,delta);G0=E*D/arb(2).sqrt();X=(1-ar(34*s))*512*G0
            check=None
            if K==150:
                other,_=distance(B,K,delta,True);assert D.overlaps(other);check=True
            row={'branches':B,'K':K,'minimum_K_for_nonempty_family':minK,'power_count':count,
                 'fixed_exponent':str(1-(B+1)*delta),'fixed_sector_norm':E.str(60),'power_distance':D.str(60),
                 'L2_lower':G0.str(60),'X_lower_at_s2m17':X.str(60),'ratio_to_eta':(X/ar(eta)).str(30),
                 'excludes_T4_019_threshold':bool(X>ar(eta)),'direct_product_overlap':check}
            rows.append(row);print('B',B,'K',K,'G0>=',G0.str(16),'X/eta',row['ratio_to_eta'],flush=True)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
         'source_sha256':sha256(source.read_bytes()).hexdigest(),'proof_sha256':sha256((BASE/'PROOF.md').read_bytes()).hexdigest(),
         'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Validated N4-origin finite-family lower bounds; independent theory and arithmetic reviews pending.',
         'rows':rows,'elapsed_seconds':time.monotonic()-start}
    (BASE/'verification/floors.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
