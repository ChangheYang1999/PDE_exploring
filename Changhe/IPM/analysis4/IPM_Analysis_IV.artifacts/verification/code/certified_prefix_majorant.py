"""Finite-prefix continuation majorant, with a separately indexed scalar audit."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from resonance_block_majorant import BlockMajorant,Poly,clean
ROOT=Path('research/172_certified_prefix_majorant')


def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[i+j]+=x*y
    return out


class PrefixMajorant(BlockMajorant):
    def __init__(self,h,Q,B,d,e,s,L,kappa):
        self.h,self.Q,self.B=h,Q,B
        self.N=len(d);assert self.N%Q==0
        self.M=self.N//Q;assert len(e)==self.M-1
        self.d=[F(0)]+list(map(F,d));self.e=list(map(F,e))
        self.s,self.L,self.kappa=map(F,(s,L,kappa))
        assert all(x>0 for x in self.d[1:]) and all(x>=0 for x in self.e)
        self.dimension=2*Q
        H=[F(0)]*(self.N-Q+1)
        for a,x in enumerate(self.e,1):H[a*Q]=x
        P=self.d
        P2=mul(P,P);HP=mul(H,P)
        Phigh=[F(0)]*(Q+1)+P[Q+1:]
        HPhi=mul(H,Phigh)
        self.fixed={};self.cross={};self.known_residue={}
        for r in range(1,Q+1):
            Pr=[F(0)]*r+P[r:]
            project=lambda pol:pol[self.N+r::Q]
            self.fixed[r]=[project(pol) for pol in [mul(Pr,Pr),P2,HPhi,HP]]
            for low in [1,r]:
                self.cross[r,low]=[(i,t,(i+t-r)//Q) for i in range(low,self.N+1) for t in range(1,Q+1) if i+t>=r and (i+t-r)%Q==0]
            for low in [1,Q+1]:
                self.known_residue[r,low]=[(a,P[a*Q+r]) for a in range(self.M) if low<=a*Q+r<=self.N]
        zero=[F(0)]*self.dimension
        self.constant=self.phi(F(0),zero)
        self.J=[[F(0)]*self.dimension for _ in zero]
        for j in range(self.dimension):
            unit=zero.copy();unit[j]=F(1)
            for i,x in enumerate(self.phi(F(0),unit)):self.J[i][j]=x-self.constant[i]
        assert all(self.J[i][j]==0 for i in range(self.dimension) for j in range(i,self.dimension))
        assert all(v>=0 for row in self.J for v in row)
        self.Y0=self.precondition(self.constant)
        assert all(v>0 for v in self.Y0)
        test=[F(i+2,i+1) for i in range(self.dimension)]
        assert self.phi(F(0),test)==[self.constant[i]+sum(self.J[i][j]*test[j] for j in range(self.dimension)) for i in range(self.dimension)]

    def phi(self,w,Y):
        Q,N,M,d,L,kap=self.Q,self.N,self.M,self.d,self.L,self.kappa
        powers=[w**j for j in range(M+2)]
        evaluate=lambda coeff:sum(c*powers[j] for j,c in enumerate(coeff))
        E=Y[Q-1];X=[0]+list(Y[Q:]);lookrows=[];densityrows=[]
        Hstar=sum(e*powers[a] for a,e in enumerate(self.e,1))
        for r in range(1,Q+1):
            A0,B0,Zhigh0,Zlow0=map(evaluate,self.fixed[r])
            D=sum(X[i]*X[r-i] for i in range(1,r))
            C=sum(X[i]*X[Q+r-i] for i in range(r,Q+1))
            tails=powers[M]*D+powers[M+1]*C
            cross=lambda low:sum(d[i]*X[t]*powers[a] for i,t,a in self.cross[r,low])
            known=lambda low:sum(value*powers[a] for a,value in self.known_residue[r,low])
            A=A0+2*cross(r)+tails
            B=B0+2*cross(1)+tails
            Ztail=Hstar*X[r]+powers[M]*E*X[r]
            Zh=Zhigh0+Ztail+E*known(Q+1)
            Zl=Zlow0+Ztail+E*known(1)
            look=sum(d[j]*Y[r-j-1] for j in range(1,r))
            lookrows.append((L*A+Zh+2*L*look)*(kap/(self.s if r==Q else 1)))
            densityrows.append(kap*(L*B+Zl))
        return lookrows+densityrows


def direct_scalar(m,degree):
    Q,N,L,kap=m.Q,m.N,m.L,m.kappa
    x={j:m.d[j] for j in range(1,N+1)}
    eta={a*Q:e for a,e in enumerate(m.e,1)};u={}
    for n in range(N,N+(degree+1)*Q):
        if n%Q==0:
            for r in range(1,Q+1):
                total=n+r
                density=sum(x[i]*x[total-i] for i in range(r,total-r+1))
                harmonic=sum(e*x[total-i] for i,e in eta.items() if total-i>=Q+1)
                look=sum(m.d[j]*u[n,r-j] for j in range(1,r))
                value=kap*(L*density+harmonic+2*L*look)
                if r==Q:eta[n]=value/m.s
                else:u[n,r]=value
        total=n+1
        x[total]=kap*sum((L*x[i]+eta.get(i,F(0)))*x[total-i] for i in range(1,total))
    Y=[[u[N+k*Q,r] for k in range(degree+1)] for r in range(1,Q)]
    Y.append([eta[N+k*Q] for k in range(degree+1)])
    Y.extend([[x[N+k*Q+r] for k in range(degree+1)] for r in range(1,Q+1)])
    assert [row[0] for row in Y]==m.Y0
    Poly.degree=degree
    actual=m.phi(Poly([0,1]),[Poly(row) for row in Y])
    assert all(a==Poly(b) for a,b in zip(actual,Y))
    return Y


def certificate(m,degree):
    Y=direct_scalar(m,degree)
    box=[2*x for x in m.Y0];hi=1
    while any(v>=b for v,b in zip(m.transformed(F(1,2**hi),box),box)):hi*=2
    lo=0
    while hi-lo>1:
        mid=(lo+hi)//2
        if all(v<b for v,b in zip(m.transformed(F(1,2**mid),box),box)):hi=mid
        else:lo=mid
    image=m.transformed(F(1,2**hi),box)
    previous=m.transformed(F(1,2**(hi-1)),box)
    assert all(v<b for v,b in zip(image,box))
    assert any(v>=b for v,b in zip(previous,box))
    return dict(h=m.h,Q=m.Q,B=m.B,N=m.N,L=m.L,kappa=m.kappa,s=m.s,
        initial_density=m.d[1:],initial_harmonics=m.e,constant=m.constant,J=m.J,Y0=m.Y0,
        box=box,image=image,previous_image=previous,w_dyadic_exponent=hi,
        radius_exponent=F(hi,2*m.h),maximum_ratio=max(v/b for v,b in zip(image,box)),
        scalar_coefficient_checks=2*m.Q*(degree+1),scalar_coefficients_sha256=sha256(json.dumps(clean(Y)).encode()).hexdigest())


def upper(x):
    a,b=x.mid().man_exp();c,d=x.rad().man_exp()
    return F(int(a))*F(2)**int(b)+F(int(c))*F(2)**int(d)


def roundup(v):
    assert v>0
    scale=F(1)
    while v*scale<1000:scale*=10
    while v*scale>=10000:scale/=10
    result=F((v*scale).__floor__()+1)/scale
    assert result>v
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--family',choices=['generic','two_mode5'],default='generic')
    ap.add_argument('--prefixes',default='9,18,27,45,90');ap.add_argument('--degree',type=int,default=2)
    args=ap.parse_args();started=time.monotonic();ctx.prec=768;cases=[];rows=[]
    source=None;seedrows=None
    if args.family=='generic':
        for h,Q in [(2,5),(3,7),(2,9)]:
            for M in [1,2,3]:
                d=[F(j+2,j+1) for j in range(1,M*Q+1)];e=[F(a+1,a+2) for a in range(1,M)]
                kap=F(4*(Q-2*h),h)*(3-F(2*h,Q));L=F(Q,2);s=F(3,5)
                m=PrefixMajorant(h,Q,4,d,e,s,L,kap)
                if M==1:
                    old=BlockMajorant(h,Q,4,d,s,L,kap)
                    assert (old.J,old.constant,old.Y0)==(m.J,m.constant,m.Y0)
                    assert old.phi(F(3,17),[F(i+1,i+2) for i in range(2*Q)])==m.phi(F(3,17),[F(i+1,i+2) for i in range(2*Q)])
                cases.append((f'h{h}_Q{Q}_M{M}',m))
    else:
        matches=[]
        for path in Path('research/167_four_ninths_finite_audit/verification').glob('root5_*/checks.json'):
            value=json.loads(path.read_text())
            if value['all_checks_pass'] and value['arithmetic_bits']>=3072 and value['maximum_order']>=90:matches.append((path,value))
        assert matches,'No successful 3072-bit finite-prefix certificate available'
        source,data=max(matches,key=lambda item:item[1]['checked_at_utc'])
        source_record=dict(path=str(source),sha256=sha256(source.read_bytes()).hexdigest(),arithmetic_bits=data['arithmetic_bits'])
        density={row['n']:roundup(upper(arb(row['density_norm'])*row['n'])) for row in data['norms']}
        harmonics={row['n']:roundup(upper(abs(arb(row['H']))*row['n'])) for row in data['harmonics']}
        seedrows=dict(source=source_record,density=density,harmonics=harmonics)
        (ROOT/'verification/two_mode5_prefix_bounds.json').write_text(json.dumps(clean(seedrows),indent=2)+'\n')
        for N in map(int,args.prefixes.split(',')):
            assert N%9==0 and N<=90
            kap=4*(F(14,9)+F(5,9))*F(5,4)*F(N+1,N)
            m=PrefixMajorant(2,9,4,[density[j] for j in range(1,N+1)],
                [harmonics[n] for n in range(9,N,9)],F(1),F(243,104),kap)
            cases.append((f'two_mode5_N{N}',m))
    for name,m in cases:
        begin=time.monotonic();row=certificate(m,args.degree)
        row.update(name=name,checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True)
        if source:row['source']=seedrows['source']
        row['actual_elapsed_s']=time.monotonic()-begin
        (ROOT/'verification'/f'{name}.json').write_text(json.dumps(clean(row),indent=2)+'\n')
        brief={k:row[k] for k in ['name','N','w_dyadic_exponent','radius_exponent','actual_elapsed_s']}
        brief['maximum_ratio']=float(row['maximum_ratio']);rows.append(brief);print(json.dumps(clean(brief)),flush=True)
    result=dict(all_checks_pass=True,checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows,actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification'/f'{args.family}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    for name in ['certified_prefix_majorant.py','resonance_block_majorant.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(clean(result)),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
