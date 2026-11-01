"""Exact resonance-period majorants; direct total-order verification is separate."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd
import argparse, json, sys, time
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
ROOT = Path('research/171_resonance_block_majorant')


def clean(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,(tuple,list)): return [clean(x) for x in v]
    if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
    return v


class Poly:
    """Short exact ordinary generating polynomial, truncated at a fixed degree."""
    degree = 2
    def __init__(self,v):
        if isinstance(v,Poly): v=v.c
        elif not isinstance(v,(tuple,list)): v=[v]
        self.c=tuple((list(map(F,v))+[F(0)]*(self.degree+1))[:self.degree+1])
    def __add__(self,v):
        v=Poly(v);return Poly([a+b for a,b in zip(self.c,v.c)])
    __radd__=__add__
    def __neg__(self): return Poly([-x for x in self.c])
    def __sub__(self,v): return self+-Poly(v)
    def __rsub__(self,v): return Poly(v)+-self
    def __mul__(self,v):
        v=Poly(v)
        return Poly([sum(self.c[i]*v.c[n-i] for i in range(n+1)) for n in range(self.degree+1)])
    __rmul__=__mul__
    def __truediv__(self,v): return self*F(1,v)
    def __pow__(self,n):
        assert n>=0
        out=Poly(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,v): return self.c==Poly(v).c


class BlockMajorant:
    def __init__(self,h,Q,B,d,s,L,kappa):
        assert h>=2 and Q>2*h and gcd(h,Q)==1
        assert len(d)==Q and all(v>0 for v in d)
        self.h,self.Q,self.B=h,Q,B
        self.d=[F(0)]+list(map(F,d))
        self.s,self.L,self.kappa=map(F,(s,L,kappa))
        self.dimension=2*Q
        zero=[F(0)]*self.dimension
        self.constant=self.phi(F(0),zero)
        self.J=[[F(0)]*self.dimension for _ in zero]
        for j in range(self.dimension):
            e=zero.copy();e[j]=F(1)
            for i,v in enumerate(self.phi(F(0),e)):
                self.J[i][j]=v-self.constant[i]
        assert all(self.J[i][j]==0 for i in range(self.dimension) for j in range(i,self.dimension))
        assert all(v>=0 for row in self.J for v in row)
        self.Y0=self.precondition(self.constant)
        assert all(v>0 for v in self.Y0)
        test=[F(j+2,j+1) for j in range(self.dimension)]
        assert self.phi(F(0),test)==[self.constant[i]+sum(self.J[i][j]*test[j] for j in range(self.dimension)) for i in range(self.dimension)]

    def phi(self,w,Y):
        Q,d,L,kap=self.Q,self.d,self.L,self.kappa
        E=Y[Q-1];X=[0]+list(Y[Q:]);out=[]
        for r in range(1,Q+1):
            D=sum(X[i]*X[r-i] for i in range(1,r))
            C=sum(X[i]*X[Q+r-i] for i in range(r,Q+1))
            a=sum(d[i]*d[Q+r-i] for i in range(r,Q+1))
            cross=sum(d[i]*X[Q+r-i] for i in range(r,Q+1))
            A=a+2*w*cross+w*D+w*w*C
            look=sum(d[j]*Y[r-j-1] for j in range(1,r))
            out.append((L*A+w*E*X[r]+2*L*look)*(kap/(self.s if r==Q else 1)))
        for r in range(1,Q+1):
            D=sum(X[i]*X[r-i] for i in range(1,r))
            C=sum(X[i]*X[Q+r-i] for i in range(r,Q+1))
            b=sum(d[i]*d[Q+r-i] for i in range(r,Q+1))
            cross0=sum(d[i]*X[r-i] for i in range(1,r))
            cross1=sum(d[i]*X[Q+r-i] for i in range(r,Q+1))
            B=b+2*cross0+2*w*cross1+w*D+w*w*C
            out.append(kap*(L*B+E*d[r]+w*E*X[r]))
        return out

    def precondition(self,v):
        out=[]
        for i,x in enumerate(v):out.append(x+sum(self.J[i][j]*out[j] for j in range(i)))
        return out

    def transformed(self,w,Y):
        rem=[a-b for a,b in zip(self.phi(w,Y),self.phi(F(0),Y))]
        assert all(v>=0 for v in rem)
        return [a+b for a,b in zip(self.Y0,self.precondition(rem))]


def direct_scalar(m,degree):
    """No residue projection: ordered sums are taken over original integer orders."""
    Q,L,kap=m.Q,m.L,m.kappa
    x={j:m.d[j] for j in range(1,Q+1)};eta={};u={}
    for n in range(Q,(degree+2)*Q):
        if n%Q==0:
            for r in range(1,Q+1):
                total=n+r
                density=sum(x[i]*x[total-i] for i in range(r,total-r+1))
                harmonic=sum(v*x[total-i] for i,v in eta.items() if total-i>=Q+1)
                look=sum(m.d[j]*u[n,r-j] for j in range(1,r))
                value=kap*(L*density+harmonic+2*L*look)
                if r==Q:eta[n]=value/m.s
                else:u[n,r]=value
        total=n+1
        x[total]=kap*sum((L*x[i]+eta.get(i,F(0)))*x[total-i] for i in range(1,total))
    Y=[[u[(k+1)*Q,r] for k in range(degree+1)] for r in range(1,Q)]
    Y.append([eta[(k+1)*Q] for k in range(degree+1)])
    Y.extend([[x[(k+1)*Q+r] for k in range(degree+1)] for r in range(1,Q+1)])
    assert [v[0] for v in Y]==m.Y0
    Poly.degree=degree
    got=m.phi(Poly([0,1]),[Poly(v) for v in Y])
    assert all(a==Poly(b) for a,b in zip(got,Y))
    return Y


def certificate(m,degree):
    Y=direct_scalar(m,degree)
    box=[2*v for v in m.Y0]
    hi=1
    while any(v>=b for v,b in zip(m.transformed(F(1,2**hi),box),box)):hi*=2
    lo=0
    while hi-lo>1:
        q=(hi+lo)//2
        if all(v<b for v,b in zip(m.transformed(F(1,2**q),box),box)):hi=q
        else:lo=q
    image=m.transformed(F(1,2**hi),box)
    previous=m.transformed(F(1,2**(hi-1)),box)
    assert all(v<b for v,b in zip(image,box))
    assert any(v>=b for v,b in zip(previous,box))
    return dict(h=m.h,Q=m.Q,B=m.B,L=m.L,kappa=m.kappa,initial=m.d[1:],s=m.s,
        scalar_coefficient_checks=2*m.Q*(degree+1),constant=m.constant,J=m.J,Y0=m.Y0,
        scalar_coefficients_sha256=sha256(json.dumps(clean(Y)).encode()).hexdigest(),
        w_dyadic_exponent=hi,radius_exponent=F(hi,2*m.h),box=box,image=image,
        previous_image=previous,maximum_ratio=max(v/b for v,b in zip(image,box)))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--family',choices=['two_mode','candidate','generic'],default='two_mode')
    ap.add_argument('--roots',default='1,2,3,4,5');ap.add_argument('--degree',type=int,default=2)
    ap.add_argument('--constants',choices=['original','improved'],default='improved')
    args=ap.parse_args();started=time.monotonic();rows=[]
    cases=[]
    if args.family=='generic':
        for h,Q in [(2,5),(2,7),(3,7),(3,8),(2,9),(3,13)]:
            cases.append((f'h{h}_Q{Q}',BlockMajorant(h,Q,4,[F(j+2,j+1) for j in range(1,Q+1)],F(3,5),F(Q,2),F(4*(Q-2*h),h)*(3-F(2*h,Q))),None))
    else:
        for index in map(int,args.roots.split(',')):
            path=Path(f'research/168_certified_initial_majorants/verification/{args.family}_root{index}_improved_poisson.json')
            data=json.loads(path.read_text());d=[F(v['rational_upper']) for v in data['initial_bounds']]
            B=data['B'];L=F(data['L']);kap=F(data['kappa'])
            if args.constants=='original':L=F(9,2);kap=F(B*5,2)*(3-F(4,9))
            cases.append((f'{args.family}_root{index}',BlockMajorant(2,9,B,d,F(data['response_lower_bound']),L,kap),path))
    for name,m,path in cases:
        begin=time.monotonic();row=certificate(m,args.degree)
        row.update(name=name,constants=args.constants,checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True)
        if path:
            row.update(seed_source=str(path),seed_source_sha256=sha256(path.read_bytes()).hexdigest())
            if args.family=='candidate':row['restored_amplitude_sufficient_integer_exponent']=(row['w_dyadic_exponent']+38)//4+1
        row['actual_elapsed_s']=time.monotonic()-begin
        (ROOT/'verification'/f'{name}_{args.constants}.json').write_text(json.dumps(clean(row),indent=2)+'\n')
        brief={k:row[k] for k in ['name','w_dyadic_exponent','radius_exponent','actual_elapsed_s']}
        brief['maximum_ratio']=float(row['maximum_ratio']);rows.append(brief);print(json.dumps(clean(brief)),flush=True)
    out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification'/f'{args.family}_{args.constants}_checks.json').write_text(json.dumps(clean(out),indent=2)+'\n')
    (ROOT/'sources/resonance_block_majorant.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(clean(out)),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n')
        print(json.dumps(fail),flush=True);raise SystemExit(1)
