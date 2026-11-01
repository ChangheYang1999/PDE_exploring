"""Independent exact Cartesian audit with rational Laurent polynomial products."""
from dataclasses import dataclass
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import argparse
import json
import time
import sys
sys.set_int_max_str_digits(0)
from flint import fmpq as Q, fmpq_poly as Poly


def poly_shift(p,k):
    assert k>=0
    return Poly([Q(0)]*k+p.coeffs()) if p else Poly([])


def trim(a):
    a=list(a)
    while a and not a[-1]: a.pop()
    return a


@dataclass
class L:
    q: object
    M: int
    a: list

    def __post_init__(self):
        self.q=Q(self.q)
        self.a=trim(self.a)

    def __add__(self,o):
        assert self.q==o.q
        M=max(self.M,o.M)
        a=[poly_shift(p,M-self.M) for p in self.a]
        b=[poly_shift(p,M-o.M) for p in o.a]
        d=max(len(a),len(b))
        return L(self.q,M,[(a[k] if k<len(a) else Poly([]))+(b[k] if k<len(b) else Poly([])) for k in range(d)])

    def scale(self,s): return L(self.q,self.M,[p*Q(s) for p in self.a])
    def __sub__(self,o):return self+o.scale(-1)
    def dt(self):return L(self.q,self.M,[self.a[k]*k for k in range(1,len(self.a))])

    def __mul__(self,o):
        if not self.a or not o.a:return L(self.q+o.q,self.M+o.M,[])
        a=[Poly([]) for _ in range(len(self.a)+len(o.a)-1)]
        for j,p in enumerate(self.a):
            for k,v in enumerate(o.a):a[j+k]+=p*v
        return L(self.q+o.q,self.M+o.M,a)

    def diff(self,which):
        a=[]
        for j,p in enumerate(self.a):
            kp=Poly([Q(k-self.M)*v for k,v in enumerate(p.coeffs())])
            tp=self.a[j+1]*(j+1) if j+1<len(self.a) else Poly([])
            lower=self.q*p+kp+tp
            higher=self.q*p-kp+tp
            if which=='Y':higher=-higher
            a.append((poly_shift(higher,2)+lower)*Q(1,2))
        return L(self.q-1,self.M+1,a)

    def X(self):return self.diff('X')
    def Y(self):return self.diff('Y')
    def zero(self):return not self.a


def parse(q,sine):
    sine={int(m):[Q(v) for v in p] for m,p in sine.items()}
    M=max(sine,default=0)
    degree=max((len(p) for p in sine.values()),default=0)
    columns=[[Q(0) for _ in range(2*M+1)] for _ in range(degree)]
    for m,p in sine.items():
        for t,v in enumerate(p):
            columns[t][M+m]+=v/2
            columns[t][M-m]-=v/2
    return L(q,M,[Poly(p) for p in columns])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',default='../a4-lead/astra/rational_logs/rational_log_series/verification/run_4_9.json')
    ap.add_argument('--N',type=int,default=73)
    ap.add_argument('--output',default='research/21_logarithmic_data_audit/verification/cartesian_check.json')
    args=ap.parse_args()
    start=time.monotonic()
    path=Path(args.input); blob=path.read_bytes(); data=json.loads(blob)
    delta=Q(data['delta']); c=Q(data['c'])
    N=min(args.N,data['completed_order'])
    assert delta==Q(4,9) and c==Q(9,5)
    assert data['density']['1']=={'1':['1']}
    F={int(n):parse(1-int(n)*delta,v) for n,v in data['density'].items() if int(n)<=N}
    G={int(n):parse(2-int(n)*delta,v) for n,v in data['stream'].items() if int(n)<=N}
    XF={n:v.X() for n,v in F.items()}; YF={n:v.Y() for n,v in F.items()}
    XG={n:v.X() for n,v in G.items()}; YG={n:v.Y() for n,v in G.items()}
    results=[]
    out=Path(args.output)
    source=out.parent.parent/'sources'/'lead_exact_log_data.json'
    source.write_bytes(blob)
    for n in range(1,N+1):
        poisson=XG[n].X().scale(-1)+YG[n].Y()-XF[n]
        assert poisson.zero(), ('poisson',n)
        nonlinear=L(F[n].q,0,[])
        for i in range(1,n):
            j=n-i
            nonlinear=nonlinear+XG[i]*YF[j]-YG[i]*XF[j]
        residual=F[n].scale(c*F[n].q-1)+F[n].dt().scale(c)+nonlinear
        assert residual.zero(), ('stationary',n)
        P=G[n].q
        if P<0 and P.q==1 and int(P)%2==0:
            amp=data['stream'][str(n)].get(str(-int(P)),[])
            assert not amp or Q(amp[0])==0, ('constant',n)
        row=dict(n=n,density_log_degree=len(F[n].a)-1,stream_log_degree=len(G[n].a)-1,
                 poisson_exact_zero=True,stationary_exact_zero=True,elapsed_s=time.monotonic()-start)
        results.append(row)
        report=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                    code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),input=str(path),
                    input_sha256=sha256(blob).hexdigest(),input_snapshot=str(source),
                    requested_order=N,verified_through=n,delta=str(delta),c=str(c),
                    method='Independent exact Cartesian derivatives with rational Laurent polynomial products',
                    results=results)
        out.write_text(json.dumps(report,indent=2)+'\n')
        if n%5==0 or n==N:print(json.dumps(row),flush=True)
    print('All requested exact Cartesian identities pass.',flush=True)

if __name__=='__main__': main()
