"""Scalar and coefficient-level checks of the h>=2 rational majorant."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from hashlib import sha256
from math import comb, gcd
import json, time, sys
sys.dont_write_bytecode = True
from general_component_radius import polynomial_product, shifted_tail_value, stringify

class RationalMajorant:
    """Ordering V1,...,V(Q-1),E,W.  No leading harmonic is omitted."""
    def __init__(self,h,Q,B,a,s):
        assert h>=2 and Q>2*h and gcd(h,Q)==1 and B>=2 and B%2==0
        self.h,self.Q,self.B,self.a,self.s=h,Q,B,F(a),F(s)
        self.L=F(Q,2);self.kappa=F(B*(Q-2*h),h)*(3-F(2*h,Q))
        self.x=[F(0)]+[F(comb(2*j-2,j-1),j)*(self.kappa*self.L)**(j-1)*self.a**j for j in range(1,Q+1)]
        self.square=polynomial_product(self.x,self.x)
        self.squares={r:polynomial_product([F(0)]*r+self.x[r:],[F(0)]*r+self.x[r:]) for r in range(1,Q+1)}
        d=Q+1;zero=[F(0)]*d
        self.constant=self.phi(F(0),zero)
        self.J=[[F(0)]*d for _ in range(d)]
        for j in range(d):
            e=zero.copy();e[j]=F(1)
            col=self.phi(F(0),e)
            for i in range(d):self.J[i][j]=col[i]-self.constant[i]
        assert all(self.J[i][j]==0 for i in range(d) for j in range(i,d))
        assert all(v>=0 for row in self.J for v in row)
        self.Y0=self.precondition(self.constant)
        assert all(v>0 for v in self.Y0)
        for test in [[F(j+2,j+1) for j in range(d)], [F((j+1)**2) for j in range(d)]]:
            assert self.phi(F(0),test)==[self.constant[i]+sum(self.J[i][j]*test[j] for j in range(d)) for i in range(d)]
    def phi(self,z,Y):
        Q,L,c,x=self.Q,self.L,self.kappa,self.x
        E,W=Y[-2:]
        P=sum(x[j]*z**j for j in range(1,Q+1))
        out=[]
        for r in range(1,Q+1):
            A=shifted_tail_value(self.squares[r],Q+r,z)
            A+=2*z*sum(x[j]*z**(j-r) for j in range(r,Q+1))*W+z**(Q+2-r)*W**2
            term=L*A+z**(Q+1-r)*E*W+2*L*sum(x[j]*Y[r-j-1] for j in range(1,r))
            out.append(c*term/(self.s if r==Q else 1))
        out.append(c*L*shifted_tail_value(self.square,Q+1,z)+2*c*L*P*W+c*L*z**(Q+1)*W**2
                   +c*E*(sum(x[j]*z**(j-1) for j in range(1,Q+1))+z**Q*W))
        return out
    def precondition(self,v):
        out=[]
        for i,x in enumerate(v):out.append(x+sum(self.J[i][j]*out[j] for j in range(i)))
        return out
    def transformed(self,z,Y):
        rem=[a-b for a,b in zip(self.phi(z,Y),self.phi(F(0),Y))]
        assert all(v>=0 for v in rem)
        return [a+b for a,b in zip(self.Y0,self.precondition(rem))]

def scalar_prefix(m,M):
    """Direct ordered sums, indexed by total order, independent of generating shifts."""
    Q,L,c=m.Q,m.L,m.kappa
    x={j:v for j,v in enumerate(m.x) if j};eta={};u={}
    for n in range(Q,Q+M+1):
        for r in range(1,Q+1):
            total=n+r
            density=sum(x[i]*x[total-i] for i in range(r,total-r+1))
            harmonic=sum(v*x[total-i] for i,v in eta.items() if total-i>=Q+1)
            look=sum(x[j]*u[n,r-j] for j in range(1,r))
            value=c*(L*density+harmonic+2*L*look)
            if r==Q:eta[n]=value/m.s
            else:u[n,r]=value
        total=n+1
        x[total]=c*sum((L*x[i]+eta.get(i,F(0)))*x[total-i] for i in range(1,total))
    y=[[u[Q+d,r] for d in range(M+1)] for r in range(1,Q)]
    y+=[[eta[Q+d] for d in range(M+1)],[x[Q+1+d] for d in range(M+1)]]
    assert [v[0] for v in y]==m.Y0
    return y

def polynomial_rhs(m,Y,M):
    """Build equation (5) as truncated polynomials, without scalar-prefix indices."""
    Q,L,c=m.Q,m.L,m.kappa
    def trim(p):return (p+[F(0)]*(M+1))[:M+1]
    def add(*ps):return [sum(p[j] if j<len(p) else F(0) for p in ps) for j in range(M+1)]
    def scale(p,a):return trim([a*x for x in p])
    def mul(p,q):return trim(polynomial_product(p,q))
    def shift(p,n):return trim([F(0)]*n+p)
    P=m.x;E,W=Y[-2:];EW=mul(E,W);W2=mul(W,W);out=[]
    for r in range(1,Q+1):
        A=add(m.squares[r][Q+r:],scale(shift(mul(P[r:],W),1),2),shift(W2,Q+2-r))
        look=add(*[scale(Y[r-j-1],2*L*P[j]) for j in range(1,r)])
        rhs=add(scale(A,L),shift(EW,Q+1-r),look)
        out.append(scale(rhs,c/(m.s if r==Q else 1)))
    out.append(add(scale(m.square[Q+1:],c*L),scale(mul(P,W),2*c*L),scale(shift(W2,Q+1),c*L),
                   scale(mul(E,add(P[1:],shift(W,Q))),c)))
    return out

def main():
    start=time.monotonic();root=Path('research/145_general_rational_convergence');rows=[]
    for h,Q in [(2,5),(2,7),(3,7),(3,8),(2,9),(3,13)]:
        m=RationalMajorant(h,Q,4,F(2,3),F(3,5));M=5
        Y=scalar_prefix(m,M);rhs=polynomial_rhs(m,Y,M);assert Y==rhs
        box=[2*v for v in m.Y0]
        hi=1
        while any(v>b for v,b in zip(m.transformed(F(1,2**hi),box),box)):hi*=2
        lo=hi//2 if hi>1 else 0
        while hi-lo>1:
            q=(hi+lo)//2
            if all(v<=b for v,b in zip(m.transformed(F(1,2**q),box),box)):hi=q
            else:lo=q
        z=F(1,2**hi);values=m.transformed(z,box)
        assert all(v<b for v,b in zip(values,box))
        row=dict(h=h,Q=Q,B=4,a=m.a,s=m.s,kappa=m.kappa,L=m.L,
                 coefficients_per_component=M+1,components=Q+1,all_coefficient_identities_equal=True,
                 constant=m.constant,J=m.J,Y0=m.Y0,z0=z,z_power=hi,box=box,map_on_box=values,
                 maximum_ratio=max(v/b for v,b in zip(values,box)),
                 scalar_coefficients_sha256=sha256(json.dumps(stringify(Y)).encode()).hexdigest())
        rows.append(row);print(json.dumps(dict(h=h,Q=Q,checks=(Q+1)*(M+1),z_power=hi,ratio=float(row['maximum_ratio']))),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start,
                scope='Finite verification of polynomial shifts and exact boxes. The response bound is an assumed input; no new profile is certified here.')
    (root/'verification/generating_shift_checks.json').write_text(json.dumps(stringify(result),indent=2)+'\n')
    for name in ['general_rational_majorant.py','general_component_radius.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
    print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        import traceback
        fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/145_general_rational_convergence/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n')
        print(json.dumps(fail),flush=True);raise SystemExit(1)
