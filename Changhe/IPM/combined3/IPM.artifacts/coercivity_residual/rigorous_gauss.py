"""Self-contained containing Gauss-Legendre nodes and weights.

Floating roots supply initial guesses only.  Each root is refined at high
precision and admitted only after an exact-polynomial sign bracket.  N
disjoint brackets for a degree-N polynomial prove completeness.  Derivative
variation uses |P_N''|<=N^4 on [-1,1], following |P_l|<=1 and
P_N'=sum_{l<N,N-l odd}(2l+1)P_l.  Weights use the exact Legendre formula.
"""
import argparse,json,time
from hashlib import sha256
from pathlib import Path
from flint import arb,arb_poly,fmpq_poly,ctx
from scipy.special import roots_legendre

def build(n):
    old=ctx.prec;ctx.prec=2*n+512
    p=fmpq_poly.legendre_p(n);P=arb_poly(p);D=arb_poly(p.derivative())
    guesses,_=roots_legendre(n);positive=[];h=arb(2)**(-192);start=time.monotonic()
    for guess in guesses[guesses>0]:
        m=arb(float(guess))
        for j in range(4):m=(m-P(m)/D(m)).mid()
        lo,hi=m-h,m+h
        assert lo>-1 and hi<1
        pl,ph=P(lo),P(hi);assert pl*ph<0
        node=arb(m,h)
        derivative=D(m)+arb(0,(n**4*h).abs_upper())
        assert not derivative.contains(0)
        weight=2/((1-node*node)*derivative**2)
        assert weight>0
        positive.append((node,weight))
        if len(positive)%128==0:print('positive roots',len(positive),'/',n//2,'seconds',time.monotonic()-start,flush=True)
    values=[(-x,w)for x,w in reversed(positive)]
    if n%2:
        m=arb(0);assert P(m)==0;values.append((m,2/D(m)**2))
    values+=positive
    assert len(values)==n
    assert all(values[i][0].upper()<values[i+1][0].lower()for i in range(n-1))
    total=sum((w for x,w in values),arb(0));assert total.contains(2)
    out={'status':'CONTAINING_GAUSS_LEGENDRE_RULE','n':n,'root_precision_bits':ctx.prec,'root_halfwidth':'2^-192','root_admission':'N disjoint opposite-sign brackets for exact degree-N Legendre polynomial','derivative_bound':'|P_N_second_derivative| <= N^4 on [-1,1]','code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'nodes_weights':[[x.str(100),w.str(100)]for x,w in values],'weight_sum':total.str(100),'elapsed_seconds':time.monotonic()-start}
    ctx.prec=old
    return out

def load_rule(path,n):
    path=Path(path)
    if path.exists():
        out=json.loads(path.read_text());assert out['n']==n and out['status']=='CONTAINING_GAUSS_LEGENDRE_RULE'
        assert out['code_sha256']==sha256(Path(__file__).read_bytes()).hexdigest()
    else:
        out=build(n);path.write_text(json.dumps(out,indent=2)+'\n')
    return [(arb(x),arb(w))for x,w in out['nodes_weights']]

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--nodes',type=int,default=1024);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    r=load_rule(args.out,args.nodes);print('nodes',len(r),'sum',sum((w for x,w in r),arb(0)),flush=True)
