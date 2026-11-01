"""Independent Arb Laurent-Cartesian coefficients and full-circle residual bounds."""
from dataclasses import dataclass
from datetime import datetime,timezone
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,arb_poly,acb,acb_poly,ctx,fmpz

DELTA=None

def shift(poly,n):
    return arb_poly([0]*n+poly.coeffs()) if n else poly

@dataclass
class Field:
    a:int
    n:int
    M:int
    poly:object
    def q(self):return arb(self.a)-self.n*DELTA
    def __add__(self,o):
        assert (self.a,self.n)==(o.a,o.n)
        m=max(self.M,o.M)
        return Field(self.a,self.n,m,shift(self.poly,m-self.M)+shift(o.poly,m-o.M))
    def scale(self,s):return Field(self.a,self.n,self.M,self.poly*s)
    def __sub__(self,o):return self+o.scale(-1)
    def __mul__(self,o):return Field(self.a+o.a,self.n+o.n,self.M+o.M,self.poly*o.poly)
    def deriv(self,y=False):
        p=self.poly.coeffs();q=self.q()
        low=arb_poly([v*(q+(i-self.M))/2 for i,v in enumerate(p)])
        high=arb_poly([v*(q-(i-self.M))/2 for i,v in enumerate(p)])
        if y:high=-high
        return Field(self.a-1,self.n,self.M+1,low+shift(high,2))
    def X(self):return self.deriv()
    def Y(self):return self.deriv(True)
    def zero_contains(self):return all(v.contains(0) for v in self.poly.coeffs())


def sine(a,n,amps):
    M=max(amps,default=0);arr=[arb(0) for _ in range(2*M+1)]
    for m,v in amps.items():arr[M+m]=v/2;arr[M-m]=-v/2
    return Field(a,n,M,arb_poly(arr))


def sine_project(A,cap,parity):
    out={}
    for m in range(-A.M,len(A.poly)-A.M):
        v=A.poly[A.M+m]
        if abs(m)>cap or abs(m)%2!=parity or m==0:assert v.contains(0),('forbidden',A.a,A.n,m)
        elif m>0:
            assert (v+A.poly[A.M-m]).contains(0)
            out[m]=2*v
    return sine(A.a,A.n,out)


def poisson(F):
    H=F.X();q=arb(2)-F.n*DELTA;arr=[]
    for i,h in enumerate(H.poly.coeffs()):
        m=i-H.M;den=m*m-q*q
        assert not den.contains(0),('divisor',F.n,m)
        arr.append(h/den)
    G=sine_project(Field(2,F.n,H.M,arb_poly(arr)),2*F.n,0)
    assert (G.X().X().scale(-1)+G.Y().Y()-H).zero_contains(),('poisson',F.n)
    return G


def encode(x):
    m,e=x.mid().man_exp();r,re=x.rad().man_exp()
    return [str(m),int(e),str(r),int(re)]


def record(A):
    return dict(a=A.a,n=A.n,M=A.M,positive_coefficients={str(m):encode(A.poly[A.M+m]) for m in range(A.M+1)})


def sum_at_radius(fields,R,variant):
    z=(-DELTA*arb(R).log()).exp();degree=max(A.M+1 for A in fields.values());a=[arb(0) for _ in range(degree+1)]
    kind='sin'
    for n,A in fields.items():
        B=A
        if variant=='dx':B=A.X()
        if variant=='dy':B=A.Y();kind='cos'
        factor=z**(n-1)
        for m in range(B.M+1):
            amp=B.poly[B.M+m]*(1 if m==0 else 2)
            if variant=='theta':amp*=m;kind='cos'
            if variant=='theta2':amp*=-m*m
            a[m]+=factor*amp
    while a and a[-1].is_zero():a.pop()
    return a,kind


def supremum(amps,kind,grid):
    coeff=[acb(amps[0] if kind=='cos' else 0)]
    coeff += [acb(a/2) if kind=='cos' else acb(0,-a/2) for a in amps[1:]]
    poly=acb_poly(coeff);lower=arb(0);upper=arb(0)
    for j in range(grid):
        theta=2*arb.pi()*j/grid;z=acb(theta.cos(),theta.sin())
        v=2*poly(z).real-coeff[0].real
        lower=lower.max(v.abs_lower());upper=upper.max(v.abs_upper())
    deriv=sum((m*abs(a) for m,a in enumerate(amps)),arb(0));upper+=arb.pi()*deriv/grid
    assert lower>0 and upper>lower
    return dict(kind=kind,degree=len(amps)-1,grid=grid,sup_lower=lower.str(30),sup_upper=upper.str(30),derivative_l1=deriv.str(30),ratio=(upper/lower).str(20),lower_ball=encode(lower),upper_ball=encode(upper))


def main():
    global DELTA
    ap=argparse.ArgumentParser();ap.add_argument('--N',type=int,default=161);ap.add_argument('--truncations',default='80,160');ap.add_argument('--radii',default='0.25,1,4');ap.add_argument('--grid',type=int,default=2048);ap.add_argument('--bits',type=int,default=1024);args=ap.parse_args()
    ctx.prec=args.bits;DELTA=1/arb(5).sqrt();c=1/(1-DELTA)
    root=Path('research/56_sqrt5_residuals');start=time.monotonic();F={};G={};XF={};YF={};XG={};YG={};checks=[]
    proof=root/'PROOF.md';snap=root/'sources/sqrt5_cartesian_residuals.py.txt';snap.write_bytes(Path(__file__).read_bytes())
    meta=dict(started_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),parameter='delta=1/sqrt(5), c=(5+sqrt(5))/4',input='sin(theta)',bits=args.bits,source_sha256=sha256(snap.read_bytes()).hexdigest(),proof_sha256=sha256(proof.read_bytes()).hexdigest())
    def checkpoint():
        data=dict(meta,completed_order=len(F),density={str(n):record(v) for n,v in F.items()},stream={str(n):record(v) for n,v in G.items()},actual_elapsed_s=time.monotonic()-start)
        (root/'verification/coefficients.json').write_text(json.dumps(data)+'\n')
        (root/'verification/checks.json').write_text(json.dumps(dict(meta,checks=checks,rows=[],completed_order=len(F),actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
    for n in range(1,args.N+1):
        if n==1:F[n]=sine(1,n,{1:arb(1)})
        else:
            S=Field(1,n,0,arb_poly([]))
            for i in range(1,n):S=S+XG[i]*YF[n-i]-YG[i]*XF[n-i]
            F[n]=sine_project(S.scale(1/((n-1)*(c-1))),2*n-1,1)
            assert (F[n].scale((n-1)*(c-1))-S).zero_contains(),('stationary',n)
        G[n]=poisson(F[n]);XF[n],YF[n]=F[n].X(),F[n].Y();XG[n],YG[n]=G[n].X(),G[n].Y()
        norm=sum((2*abs(F[n].poly[F[n].M+m]) for m in range(1,F[n].M+1,2)),arb(0));rads=sum((2*F[n].poly[F[n].M+m].rad() for m in range(1,F[n].M+1,2)),arb(0))
        assert rads/norm<arb('1e-150'),('precision',n)
        checks.append(dict(n=n,poisson_enclosure=True,stationarity_enclosure=True,density_norm=norm.str(20),relative_radius=(rads/norm).str(10)))
        if n%20==0 or n==args.N:
            checkpoint();print(json.dumps(dict(n=n,elapsed_s=time.monotonic()-start)),flush=True)
    rows=[];saved={}
    for N in map(int,args.truncations.split(',')):
        assert N+1<=args.N;E={}
        for i in range(1,N+1):
            for j in range(max(1,N+1-i),N+1):
                n=i+j;term=XG[i]*YF[j]-YG[i]*XF[j]
                E[n]=E.get(n,Field(1,n,0,arb_poly([])))+term
        E={n:sine_project(A,2*n-1,1) for n,A in E.items()}
        assert (E[N+1]-F[N+1].scale(N*(c-1))).zero_contains()
        for R in args.radii.split(','):
            row=dict(N=N,R=R,bounds={});packed={}
            for variant in ['residual','theta','theta2','dx','dy','increment']:
                if variant=='increment':a,kind=sum_at_radius({N+1:F[N+1]},R,'residual')
                else:a,kind=sum_at_radius(E,R,variant)
                result=supremum(a,kind,args.grid);row['bounds'][variant]=result;packed[variant]=dict(kind=kind,amplitudes=[encode(v) for v in a])
            rows.append(row);saved[f'{N}:{R}']=packed
            (root/'verification/evaluated_coefficients.json').write_text(json.dumps(dict(meta,rows=saved))+'\n')
            (root/'verification/checks.json').write_text(json.dumps(dict(meta,checks=checks,completed_order=len(F),rows=rows,actual_elapsed_s=time.monotonic()-start,checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')),indent=2)+'\n')
            print(json.dumps(dict(N=N,R=R,residual=row['bounds']['residual'],elapsed_s=time.monotonic()-start)),flush=True)
    print('All interval coefficient and full-circle checks completed.',flush=True)

if __name__=='__main__':main()
