"""New exact compact Fourier derivative norms, integrated as powers of u."""
from pathlib import Path
from datetime import datetime,timezone
from math import comb
from flint import fmpq,fmpq_poly,arb,ctx
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial,ar,T,U,ZERO,pshift
ONE=fmpq_poly([1])

def put(A,ell,kind,n,P):
    if n<0:n,P=-n,(-P if kind=='s' else P)
    if n==0 and kind=='s':return
    if P:A[ell,kind,n]=A.get((ell,kind,n),ZERO)+P

def derivative(A,d,axis,delta):
    out={}
    for (ell,kind,n),Q in A.items():
        P=Q*T**(d//2)
        R=(1-d-ell*delta*T)*P+2*T*U*P.derivative()
        minus=pshift((R+n*P)/2,(d+1)//2)
        plus=pshift((R-n*P)/2,(d+1)//2)
        target=kind
        if axis=='y':
            target='s' if kind=='c' else 'c'
            minus*=1 if kind=='s' else -1
            plus*=-1 if kind=='s' else 1
        put(out,ell,target,n-1,minus);put(out,ell,target,n+1,plus)
    return {k:P for k,P in out.items() if P}

def construct(model,maxd=3):
    start=time.monotonic()
    D={(0,0):{(h+1,'s',n):P for (h,n),P in model.residual_sine().items()}}
    for d in range(maxd):
        for nx in range(d+2):
            D[d+1,nx]=derivative(D[d,0],d,'y',model.delta) if nx==0 else derivative(D[d,nx-1],d,'x',model.delta)
        for nx in range(1,d+1):assert D[d+1,nx]==derivative(D[d,nx],d,'y',model.delta)
    print('constructed derivative polynomials',maxd,'seconds',time.monotonic()-start,flush=True)
    return D

def endpoint(P):
    Q=P(U);q=0
    while q<len(Q) and Q[q]==0:q+=1
    assert q<len(Q)
    return q,fmpq_poly(list(Q)[q:])

def weight_poly(N):
    c=fmpq(1);a=[c]
    for k in range(1,N+1):
        c*= (fmpq(4,5)-(k-1))/k*fmpq(-3,4);a.append(c)
    nxt=c*(fmpq(4,5)-N)/(N+1)*fmpq(-3,4)
    return fmpq_poly(a),4*abs(nxt)

def integral(P,b):
    return sum((a/(b+k+1) for k,a in enumerate(P)),fmpq(0))

def norm(D,d,delta,weighted=False,rproxy=False,N=112,harmonic_proxy=False,multiplicities=None):
    start=time.monotonic();bad=[];groups={};endpoint_rows=[]
    for nx in range(d+1):
        multiplicity=comb(d,nx) if multiplicities is None else multiplicities.get(nx,0)
        if not multiplicity:continue
        harmonics={}
        for (ell,kind,n),P in D[d,nx].items():
            if not P:continue
            q,Q=endpoint(P)
            exp=d-3+ell*delta+2*q-(fmpq(4,5) if weighted else 0)-(1 if rproxy else 0)
            row={'nx':nx,'ell':ell,'kind':kind,'n':n,'endpoint_order':q,'diagonal_exponent':str(exp)}
            endpoint_rows.append(row)
            if exp<=-1:bad.append(row)
            harmonics.setdefault((kind,n),[]).append((ell,q,Q))
        for (kind,n),rows in harmonics.items():
            for i,(ell,q,P) in enumerate(rows):
                for ell2,q2,Q in rows[i+1:]:assert ((ell-ell2)*delta/2).denominator!=1
            if bad:continue
            for i,(ell,q,P) in enumerate(rows):
                for j in range(i,len(rows)):
                    ell2,q2,Q=rows[j]
                    exp=d-3+(ell+ell2)*delta/2+q+q2-(fmpq(4,5) if weighted else 0)-(1 if rproxy else 0)
                    factor=fmpq(multiplicity*(2 if kind=='c' and n==0 else 1)*(1 if j==i else 2))
                    if harmonic_proxy:
                        assert n>0
                        factor/=n*n
                    poly=P*Q*factor
                    if d%2==0:poly*=U
                    if rproxy:poly*=U
                    groups[exp]=groups.get(exp,ZERO)+poly
    if bad:return {'status':'INFINITE','bad_sectors':bad,'endpoint_rows':endpoint_rows}
    S=sum((integral(P,b) for b,P in groups.items()),fmpq(0))
    assert S>=0,S
    eps=fmpq(0);lo=hi=S
    if weighted:
        W,eps=weight_poly(N)
        hi=sum((integral(P*W,b) for b,P in groups.items()),fmpq(0));lo=hi-eps*S
        assert lo>0
    pref=arb.pi()/2*((arb(4)**ar(fmpq(4,5))) if weighted else arb(1))
    lower=(pref*ar(lo)).sqrt();upper=(pref*ar(hi)).sqrt()
    return {'status':'FINITE','norm_lower_ball':lower.str(60),'norm_upper_ball':upper.str(60),
            'norm_lower':str(lower.lower()),'norm_upper':str(upper.upper()),
            'unweighted_rational_sum':str(S),'upper_rational_sum':str(hi),'weight_error_rational':str(eps),
            'weight_degree':N if weighted else 0,'endpoint_rows':endpoint_rows,'groups':len(groups),
            'elapsed_seconds':time.monotonic()-start}

def evaluate_derivative(A,d,model,x,y):
    from flint import acb
    from radial import q
    x,y=ar(q(x)),ar(q(y));r2=x*x+y*y;r=r2.sqrt();u=1/(1+r2);t=r2*u
    z=acb(x/r,y/r);power={0:acb(1)}
    for n in range(1,1+max(n for ell,kind,n in A)):power[n]=power[n-1]*z
    value=arb(0)
    for (ell,kind,n),P in A.items():
        trig=power[n].real if kind=='c' else power[n].imag
        value+=r**(1-d%2)*u**ar(d//2+ell*model.delta/2)*model.poly_arb(P,t,u)*trig
    return value

def run(name,path,N=112):
    start=time.monotonic();ctx.prec=768;model=Radial(path);D=construct(model)
    # A genuinely separate direct-field path verifies the nonlinear residual identity.
    fieldchecks=[]
    for x,y in [('1/2','1/2'),('0','1'),('3','4'),('6','8')]:
        a=evaluate_derivative(D[0,0],0,model,x,y);b=model.evaluate(x,y)['residual']
        assert a.overlaps(b),(x,y,a,b)
        fieldchecks.append({'x':x,'y':y,'residual':a.str(40),'direct_field_overlap':True})
    out={'candidate':name,'utc_start':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'precision_bits':ctx.prec,
         'method':'Exact independent radial Fourier derivatives, exact u-monomial integrals, one-sided binomial radial-weight bound',
         'tensor_convention':'ordered Cartesian tensor, binomial multiplicities','angular_convention':'full circle',
         'fieldchecks':fieldchecks,'norms':{}}
    dest=ROOT/f'research/whole_plane_norms/verification/{name}_norms.json'
    for label,d,weighted,rproxy,hproxy in [('G0',0,False,False,False),('G1',1,False,False,False),
                   ('P2',2,True,False,False),('Q3',3,True,False,False),('rF_proxy',0,False,True,False),
                   ('angular_Hminus1_proxy',0,False,True,True)]:
        out['norms'][label]=norm(D,d,model.delta,weighted,rproxy,N,hproxy)
        out['utc_updated']=datetime.now(timezone.utc).isoformat(timespec='seconds')
        dest.write_text(json.dumps(out,indent=2)+'\n')
        row=out['norms'][label];print(name,label,row['status'],row.get('norm_lower_ball',''),row.get('norm_upper_ball',''),flush=True)
    out['elapsed_seconds']=time.monotonic()-start;dest.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    for name in sys.argv[1:] or ['d2','Mpen2','b6']:
        path=ROOT/f'research/refit_audit/data/{name}_canonical.json'
        if name.startswith('state'):path=ROOT/f'research/baseline/data/{name}_independent.json'
        run(name,path)
