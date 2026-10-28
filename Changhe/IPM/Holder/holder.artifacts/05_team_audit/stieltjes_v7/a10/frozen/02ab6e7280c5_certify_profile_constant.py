"""One-dimensional Arb certificate for the projection-profile seminorm."""
from pathlib import Path
from datetime import datetime, timezone
from flint import arb,ctx
from certify_far_circles import upper_decimal
import json,hashlib,argparse,time
ctx.prec=192;ROOT=Path(__file__).resolve().parents[1]
def certify(text,n=32768):
    alpha=arb(text);assert 0<alpha<=arb(1)/4
    eps=arb(1)/1000000;k=1/(1-alpha);Rstar=(1-eps)**alpha;c=alpha/(1-eps)**(1-alpha)
    left=(1-eps)**(-alpha)
    right=1+(k-1)*c*c*eps*eps/(8*Rstar)+c*eps**(1-alpha)/2
    best=arb.max(arb(left.upper()),arb(right.upper()));where=-1
    for i in range(n):
        u=(eps+(1-2*eps)*i/n).union(eps+(1-2*eps)*(i+1)/n)
        R=u**alpha;A=(1-u)**(-alpha)
        B=((1+R**k)/2)**(1/k)+(1-R)/(2*(1-u)**alpha)
        value=arb.min(arb(A.upper()),arb(B.upper()))
        if value>best:best=value;where=i
        else:best=arb.max(best,value)
    return dict(alpha=text,cells=n,epsilon='1/1000000',upper_interval=best.str(45,more=True),safe_upper=upper_decimal(best,12),largest_cell=where,left_endpoint_bound=left.str(35,more=True),right_endpoint_bound=right.str(35,more=True))
def main():
    p=argparse.ArgumentParser();p.add_argument('--cells',type=int,default=32768);p.add_argument('--alphas',default='1/20,1/10,1/5,1/4');p.add_argument('--out',default='data/profile_constant_certificate.json');a=p.parse_args();start=time.monotonic()
    rows=[]
    for text in a.alphas.split(','):
        row=certify(text,a.cells);rows.append(row);print(row,flush=True)
    sources=[Path(__file__),ROOT/'07_diagonal_identity_term/refined_profile_constant/PROOF.md']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,rows=rows,elapsed_seconds=time.monotonic()-start,source_hashes={str(s.relative_to(ROOT)):hashlib.sha256(s.read_bytes()).hexdigest() for s in sources})
    (ROOT/a.out).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
