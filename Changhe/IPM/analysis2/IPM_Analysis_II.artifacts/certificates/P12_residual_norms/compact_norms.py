"""Exact compactified residual polynomials and whole-plane beta integrals.
No archived or sibling code is imported. The only shared module is this lane's
previously audited exact polar derivative rule.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import json,sys,time,hashlib
from flint import fmpq,fmpq_poly,arb,ctx
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'02_energy/verification'))
from compact_matrix import derivative
Z=fmpq_poly([0,1]); ONE=fmpq_poly([1]); OM=ONE-Z

def fq(x):
    if isinstance(x,fmpq):return x
    q=Q(x);return fmpq(q.numerator,q.denominator)
def aq(x):
    q=Q(str(x));return arb(q.numerator)/q.denominator

def add(D,ell,kind,n,p):
    if n<0:
        n=-n
        if kind=='s':p=-p
    if not p or (kind=='s' and n==0):return
    key=(ell,kind,n)
    D[key]=D.get(key,fmpq_poly([]))+p
    if not D[key]:del D[key]

def source(name):
    if name.startswith('state'):
        path=BASE/'source_audit'/f'{name}_exact.json'
        raw=path.read_bytes();d=json.loads(raw)
        c=Q(d['exact_parameters']['cl'])
        sh=d['canonical_serialization_sha256']
    elif name.startswith('algebraic_'):
        path=BASE/'13_algebraic_repair/verification'/f'{name}.json'
        raw=path.read_bytes();d=json.loads(raw);c=Q(d['cl']);sh=d['canonical_sha256']
    else:
        path=BASE/'08_refits/verification'/f'{name}_audit.json'
        raw=path.read_bytes();d=json.loads(raw);c=Q(d['cl']);sh=d['canonical_sha256']
    A={tuple(k):Q(v) for k,v in zip(d['canonical_order'],d['canonical_coefficients'])}
    return c,A,sh,hashlib.sha256(raw).hexdigest()

def chi_compact(A,c,d,nx):
    gamma=1/c;delta=1-gamma;out={}
    for (j,m,k),a in A.items():
        p=(3+gamma-j*delta)/2
        T={('c',2*m,0):a}
        for di,axis in enumerate('x'*nx+'y'*(d-nx)):
            T=derivative(T,p,k,di,axis)
        for (kind,n,l),v in T.items():
            key=j+1,kind,n
            P=out.setdefault(key,{})
            power=k-2+l
            P[power]=P.get(power,Q(0))+v
    ans={}
    for (ell,kind,n),P in out.items():
        P={i:v for i,v in P.items() if v}
        assert all(i>=0 for i in P),(d,nx,ell,kind,n,P)
        if P:
            p=fmpq_poly([fq(P.get(i,0)) for i in range(max(P)+1)])
            add(ans,ell,kind,n,p)
    return ans

def plus(*terms):
    out={}
    for scale,D in terms:
        for (ell,kind,n),p in D.items():add(out,ell,kind,n,p*fq(scale))
    return out

def trigprod(k,n,l,m):
    if k=='c' and l=='c':return [('c',n+m,Q(1,2)),('c',n-m,Q(1,2))]
    if k=='s' and l=='s':return [('c',n-m,Q(1,2)),('c',n+m,-Q(1,2))]
    if k=='s':return [('s',n+m,Q(1,2)),('s',n-m,Q(1,2))]
    return [('s',n+m,Q(1,2)),('s',n-m,-Q(1,2))]

def mul(D,E):
    out={}
    for (ell,k,n),p in D.items():
        for (ell2,l,m),q in E.items():
            v=p*q
            for kind,mode,factor in trigprod(k,n,l,m):
                add(out,ell+ell2,kind,mode,v*fq(factor))
    return out

def diff(D,d,axis,delta):
    out={}
    for (ell,kind,n),p in D.items():
        if d%2==0:
            rad=(ONE-Z*fq(d+ell*delta))*p+2*Z*OM*p.derivative()
            ang=p
        else:
            rad=-fq(d-1+ell*delta)*p+2*OM*p.derivative()
            if n:
                ang,rem=divmod(p,Z)
                assert not rem,('origin pole',d,ell,kind,n,p)
            else:ang=fmpq_poly([])
        # cos theta * radial - sin theta * angular derivative (x)
        # sin theta * radial + cos theta * angular derivative (y)
        rk='c' if axis=='x' else 's'
        for kk,nn,factor in trigprod(rk,1,kind,n):add(out,ell,kk,nn,rad*fq(factor))
        if n:
            ak='s' if axis=='x' else 'c'
            dk='s' if kind=='c' else 'c'
            sign=(-1 if kind=='c' else 1)*(-1 if axis=='x' else 1)
            for kk,nn,factor in trigprod(ak,1,dk,n):add(out,ell,kk,nn,ang*fq(sign*n*factor))
    return out

def enc(D):
    return [{'ell':ell,'kind':kind,'mode':n,'coeff':[str(v) for v in p.coeffs()]}
            for (ell,kind,n),p in sorted(D.items())]
def dec(rows):
    return {(r['ell'],r['kind'],r['mode']):fmpq_poly([fmpq(v) for v in r['coeff']]) for r in rows}

def construct(name,write=True,max_order=3,encode=True):
    c,A,sha,rawsha=source(name);delta=1-1/c
    start=time.monotonic();j3={};j4={}
    for d,nxs,save in [(3,range(3),j3),(4,range(4),j4)]:
        for nx in nxs:
            save[nx]=chi_compact(A,c,d,nx)
            print(name,'chi derivative',d,nx,'sec',time.monotonic()-start,flush=True)
    rho=plus((-1,j3[0]),(-1,j3[2]));u1=plus((-1,j3[1]));u2=j3[2]
    rx=plus((-1,j4[1]),(-1,j4[3]));ry=plus((-1,j4[0]),(-1,j4[2]))
    cx={(0,'c',1):ONE};sy={(0,'s',1):ONE}
    F=plus((c,mul(cx,rx)),(c,mul(sy,ry)),(-1,rho),(1,mul(u1,rx)),(1,mul(u2,ry)))
    D={(0,0):F}
    for d in range(max_order):
        for nx in range(d+2):
            if nx==0:D[d+1,nx]=diff(D[d,0],d,'y',delta)
            else:D[d+1,nx]=diff(D[d,nx-1],d,'x',delta)
        # All mixed paths must give the same exact rational polynomials.
        for nx in range(1,d+1):
            assert D[d+1,nx]==diff(D[d,nx],d,'y',delta)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,
         'c':str(c),'delta':str(delta),'canonical_sha256':sha,'source_record_sha256':rawsha,
         'polynomials':{f'{d},{nx}':enc(v) for (d,nx),v in D.items()} if encode else None}
    p=HERE/f'{name}_polynomials.json'
    if write:p.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(name,'polynomials complete','sec',time.monotonic()-start,flush=True)
    return out,D

def endpoint(p):
    q=0
    while p and p(1)==0:
        p,rem=divmod(p,OM);assert not rem;q+=1
    assert p and p(1)!=0
    return q,p

def weight_poly(N):
    z=(6*Z-3)/5;p=ONE;term=ONE;coef=fmpq(1)
    for n in range(1,N+1):
        coef*=fq(Q(4,5)-n+1)/n;term*=z;p+=coef*term
    nextcoef=coef*fq(Q(4,5)-N)/(N+1)
    eps=abs(nextcoef)*fq(Q(3,5)**(N+1))/fq(Q(2,5))
    return p,eps

def integral(p,b,cache):
    need=p.degree()+1
    if b not in cache:cache[b]=[fq(1/(b+1))]
    bet=cache[b]
    while len(bet)<need:
        n=len(bet);bet.append(bet[-1]*n/fq(b+n+1))
    return sum((coef*bet[n] for n,coef in enumerate(p.coeffs())),fmpq(0))

def norm(D,d,delta,weight=False,rproxy=False,N=56):
    start=time.monotonic();groups={};bad=[];facts=[]
    for nx in range(d+1):
        modes={}
        for (ell,kind,n),p in D[d,nx].items():
            q,p2=endpoint(p)
            modes.setdefault((kind,n),[]).append((ell,q,p2))
            b=Q(d-3)+ell*delta+2*q-(Q(4,5) if weight else 0)-(1 if rproxy else 0)
            facts.append({'nx':nx,'ell':ell,'kind':kind,'mode':n,'order':q,'diagonal_exponent':str(b)})
            if b<=-1:bad.append(facts[-1])
        # Distinct branches cannot cancel noninteger endpoint powers.
        ells={ell for rows in modes.values() for ell,q,p in rows}
        for l in ells:
            for m in ells:
                if l!=m:assert ((l-m)*delta/2).denominator!=1
        if bad:continue
        for (kind,n),rows in modes.items():
            for i,(ell,q,p) in enumerate(rows):
                for j in range(i,len(rows)):
                    ell2,q2,p2=rows[j]
                    b=Q(d-3)+(ell+ell2)*delta/2+q+q2-(Q(4,5) if weight else 0)-(1 if rproxy else 0)
                    factor=comb(d,nx)*(2 if n==0 and kind=='c' else 1)*(1 if i==j else 2)
                    v=p*p2*factor
                    if d%2==0:v*=Z
                    if rproxy:v*=Z
                    groups[b]=groups.get(b,fmpq_poly([]))+v
    if bad:
        return {'status':'INFINITE','bad_sectors':bad,'endpoint_factors':facts,'scope':'Exact nonzero asymptotic sectors and nonresonance.'}
    cache={};S=fmpq(0);T=fmpq(0);wp,eps=weight_poly(N)
    for i,(b,p) in enumerate(sorted(groups.items())):
        assert b>-1
        S+=integral(p,b,cache)
        if weight:T+=integral(p*wp,b,cache)
        if i%10==0:print('integral',d,'weight',weight,'group',i,'of',len(groups),'sec',time.monotonic()-start,flush=True)
    assert S>=0,('negative exact square integral',d)
    if weight:
        lo=T-eps*S;hi=T+eps*S;assert lo>=0
        pref=aq(Q(5,2))**aq(Q(4,5));sqlo=arb.pi()/2*pref*aq(lo);sqhi=arb.pi()/2*pref*aq(hi)
    else:
        T=S;lo=hi=S;pref=arb(1);sqlo=sqhi=arb.pi()/2*aq(S)
    assert sqlo.is_finite() and sqhi.is_finite() and sqlo>=0
    return {'status':'FINITE','norm_lower':str(sqlo.sqrt().lower()),'norm_upper':str(sqhi.sqrt().upper()),
            'norm_lower_ball':sqlo.sqrt().str(65),'norm_upper_ball':sqhi.sqrt().str(65),
            'base_beta_sum':str(S),'weighted_beta_sum':str(T),'weight_N':N if weight else 0,
            'weight_error_rational':str(eps if weight else 0),'endpoint_factors':facts,
            'elapsed_seconds':time.monotonic()-start}

def run(name,degree=56):
    ctx.prec=512;start=time.monotonic();p=HERE/f'{name}_polynomials.json'
    if p.exists():
        raw=json.loads(p.read_text());c,A,sha,rawsha=source(name)
        assert raw['canonical_sha256']==sha and raw['source_record_sha256']==rawsha
        D={tuple(map(int,key.split(','))):dec(v) for key,v in raw['polynomials'].items()}
    else:raw,D=construct(name)
    delta=Q(raw['delta']);out={'utc_start':datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'name':name,'polynomial_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'norms':{}}
    dest=HERE/f'{name}_norms.json'
    for label,d,weight,rproxy in [('rF',0,False,True),('F',0,False,False),('DF',1,False,False),('omega_D2F',2,True,False),('omega_D3F',3,True,False)]:
        out['norms'][label]=norm(D,d,delta,weight,rproxy,degree)
        out['utc_updated']=datetime.now(timezone.utc).isoformat(timespec='seconds')
        dest.write_text(json.dumps(out,separators=(',',':'))+'\n')
        row=out['norms'][label];print(name,label,row['status'],row.get('norm_lower_ball',''),row.get('norm_upper_ball',''),flush=True)
    out['elapsed_seconds']=time.monotonic()-start;out['status']='PENDING_INDEPENDENT_AUDIT'
    dest.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('DONE',name,'sec',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
    run(sys.argv[1] if len(sys.argv)>1 else 'state131',int(sys.argv[2]) if len(sys.argv)>2 else 56)
