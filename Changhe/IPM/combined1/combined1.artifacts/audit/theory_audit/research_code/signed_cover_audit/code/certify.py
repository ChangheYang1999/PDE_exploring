from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from math import comb
from hashlib import sha256
from datetime import datetime, timezone
import argparse,gzip,json,sys,time
from flint import fmpq as Q, fmpq_poly as Poly, arb, arb_mat, ctx
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE.parent/'weak_probe_audit/code'))
from reproduce import fields,td,ar

def digest(path):return sha256(Path(path).read_bytes()).hexdigest()
def plus(A,B,scale=Q(1)):
    out=dict(A)
    for k,v in B.items():out[k]=out.get(k,Q(0))+scale*v
    return {k:v for k,v in out.items() if v}
def tensor(A,p,z):
    for i,x in enumerate(p):
        if x:
            for k,y in enumerate(z):
                if y:A[i,k]=A.get((i,k),Q(0))+x*y

def construct():
    data=json.loads((BASE/'data/d2_canonical.json').read_text())
    c,delta,rho,_=fields(data)
    Z=Poly([0,1]);T=[Poly([1]),Z];U=[Poly([1]),2*Z]
    for i in range(2,max(n for j,n in rho)//2+2):T.append(2*Z*T[-1]-T[-2]);U.append(2*Z*U[-1]-U[-2])
    out={(label,j):{} for label in ('X','Y') for j in range(6)}
    for (j,n),p in rho.items():
        d=td(p,(j+1)*delta/2,1)
        tensor(out['X',j],(d-n*p)/2,U[(n+1)//2-1])
        if n>1:tensor(out['X',j],(d+n*p)/2,U[(n-1)//2-1])
        tensor(out['Y',j],(d+n*p)/2,T[(n-1)//2])
        tensor(out['Y',j],(-d+n*p)/2,T[(n+1)//2])
    out={key:{ij:v for ij,v in vals.items() if v} for key,vals in out.items()}
    with gzip.open(BASE/'source/N4_polynomials.json.gz','rt') as f:old=json.load(f)
    oldp={key:{(i,j):Q(v) for i,j,v in vals} for key,vals in old['polynomials'].items()}
    for j in range(6):
        wantX=plus({},plus(oldp[f'chi31_{j}'],oldp[f'chi13_{j}']),Q(-1))
        wantY=plus({},plus(oldp[f'chi22_{j}'],oldp[f'chi04_{j}']),Q(-1))
        assert out['X',j]==wantX,('X',j)
        assert out['Y',j]==wantY,('Y',j)
    record={'utc':datetime.now(timezone.utc).isoformat(),'cl':str(c),'delta':str(delta),
            'all_gradient_coefficients_match':True,
            'canonical_sha256':digest(BASE/'data/d2_canonical.json'),
            'N4_polynomial_sha256':digest(BASE/'source/N4_polynomials.json.gz'),
            'code_sha256':digest(__file__),
            'polynomials':{f'{label}_{j}':[[i,k,str(v)] for (i,k),v in sorted(vals.items())]
                           for (label,j),vals in out.items()}}
    (BASE/'verification/gradient_reconstruction.json').write_text(json.dumps(record,indent=2)+'\n')
    return c,delta,out

def endpoints(path):
    a,b,c,d=map(Q,(0,1,-1,1))
    for k in path:
        if k=='t':b=(a+b)/2
        elif k=='T':a=(a+b)/2
        elif k=='z':d=(c+d)/2
        elif k=='Z':c=(c+d)/2
        else:raise ValueError(k)
    return a,b,c,d

def check_cover(paths):
    leaves=set(paths)
    assert len(leaves)==len(paths)
    while leaves!={''}:
        p=max(leaves,key=len)
        assert p
        sibling=p[:-1]+{'t':'T','T':'t','z':'Z','Z':'z'}[p[-1]]
        assert sibling in leaves,(p,sibling)
        parent=p[:-1]
        assert parent not in leaves
        leaves.remove(p);leaves.remove(sibling);leaves.add(parent)

@lru_cache(None)
def affine(n,a,b):
    a,b=Q(a),Q(b)
    return arb_mat([[ar(Q(comb(k,l))*a**(k-l)*(b-a)**l) if l<=k else arb(0)
                      for k in range(n+1)] for l in range(n+1)])
@lru_cache(None)
def bernstein(n):
    return arb_mat([[ar(Q(comb(i,k),comb(n,k))) if k<=i else arb(0)
                    for k in range(n+1)] for i in range(n+1)])
def interval(M):
    it=iter(M.entries());v=next(it);lo=v;hi=v
    for v in it:lo=lo.min(v);hi=hi.max(v)
    return lo.lower(),hi.upper()
def mag(bounds):return abs(bounds[0]).max(abs(bounds[1])).upper()
def product_range(a,b,c,d):
    vals=[a*c,a*d,b*c,b*d];lo=vals[0];hi=vals[0]
    for v in vals[1:]:lo=lo.min(v);hi=hi.max(v)
    return lo.lower(),hi.upper()

def enclose(P,nt,nz,a,b,c,d,delta):
    local={key:affine(nt,str(a),str(b))*M*(bernstein(nz)*affine(nz,str(c),str(d))).transpose()
           for key,M in P.items()}
    branch={key:interval(bernstein(nt)*M) for key,M in local.items()}
    plain={}
    for label in ('X','Y'):
        lo=arb(0);hi=arb(0)
        for j in range(6):
            power=(j+1)*delta/2
            wl=(1-ar(b))**ar(power);wh=(1-ar(a))**ar(power)
            ll,hh=product_range(wl,wh,*branch[label,j]);lo+=ll;hi+=hh
        plain[label]=(lo.lower(),hi.upper())
    if b==1:return plain,'independent'
    N=8;u0=1-(a+b)/2;kappa=(b-a)/(2*u0)
    correlated={};multipliers={};errors={}
    for j in range(6):
        power=(j+1)*delta/2
        pref=ar(u0)**ar(power);kapp=ar(kappa)
        coeff=[arb(0) for _ in range(N+1)];choose=Q(1)
        for k in range(N+1):
            if k:choose*=(power-k+1)/k
            scale=pref*ar(choose)*kapp**k
            for ell in range(k+1):coeff[ell]+=scale*comb(k,ell)*((-2)**ell)
        choose*=(power-N)/(N+1)
        errors[j]=pref*ar(abs(choose))*kapp**(N+1)*(1-kapp)**ar(power-N-1)
        M=arb_mat(nt+N+1,nt+1)
        for i in range(nt+1):
            for k in range(N+1):M[i+k,i]=coeff[k]
        multipliers[j]=M
    for label in ('X','Y'):
        total=arb_mat(nt+N+1,nz+1);error=arb(0)
        for j in range(6):
            total+=multipliers[j]*local[label,j]
            error+=errors[j]*mag(branch[label,j])
        lo,hi=interval(bernstein(nt+N)*total)
        lo=(lo-error).lower();hi=(hi+error).upper()
        plo,phi=plain[label]
        correlated[label]=(lo.max(plo).lower(),hi.min(phi).upper())
    return correlated,'degree8-correlated-intersection'

def run(seconds,bits):
    ctx.prec=bits;start=time.monotonic()
    c,delta,polys=construct()
    nt=max(i for vals in polys.values() for i,k in vals)
    nz=max(k for vals in polys.values() for i,k in vals)
    P={}
    for key,vals in polys.items():
        M=arb_mat(nt+1,nz+1)
        for (i,k),v in vals.items():M[i,k]=ar(v)
        P[key]=M
    src=BASE/'source/N4_L2_cover.json';initial=json.loads(src.read_text())
    paths=[row['path'] for row in initial['accepted']];assert not initial['pending'];check_cover(paths)
    output=BASE/'verification/d2_signed_cover.json'
    if output.exists():
        prior=json.loads(output.read_text());assert prior['code_sha256']==digest(__file__)
        queue=prior['pending'];accepted=prior['accepted'];elapsed=prior['elapsed_seconds'];refined=prior['refined']
    else:queue=paths;accepted=[];elapsed=0;refined=[]
    print('prepared',nt,nz,'accepted',len(accepted),'pending',len(queue),flush=True)
    while queue and time.monotonic()-start<seconds:
        path=queue.pop(0);a,b,zl,zh=endpoints(path)
        vals,method=enclose(P,nt,nz,a,b,zl,zh,delta)
        tau=arb(2)/25;zmin=Q(0) if zl<=0<=zh else min(abs(zl),abs(zh))
        lower=tau*(tau+vals['Y'][0])-(1-ar(zmin)**2)*mag(vals['X'])**2/4
        if lower>=0:
            accepted.append({'path':path,'schur_lower':lower.str(70),'method':method,'pass':True})
        else:
            assert len(path)<45,('depth',path)
            axes='tT' if (b-a)/(1-a)>=(zh-zl)/2 else 'zZ'
            queue.extend(path+x for x in axes);refined.append(path)
        check_cover([r['path'] for r in accepted]+queue)
        state={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'d2','target':'theta<=2/25',
            'code_sha256':digest(__file__),'proof_sha256':digest(BASE/'PROOF.md'),
            'source_sha256':digest(BASE/'data/d2_canonical.json'),'N4_cover_sha256':digest(src),
            'reconstruction_sha256':digest(BASE/'verification/gradient_reconstruction.json'),
            'precision_bits':bits,'accepted':accepted,'pending':queue,'refined':refined,
            'complete_partition':True,'all_pass':not queue,
            'elapsed_seconds':elapsed+time.monotonic()-start}
        output.write_text(json.dumps(state,indent=2)+'\n')
        print('cell',path,bool(lower>=0),'margin',lower.str(10),'pending',len(queue),
              'sec',round(time.monotonic()-start,3),flush=True)
    print('stage done',len(accepted),len(queue),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=460);p.add_argument('--bits',type=int,default=768)
    a=p.parse_args();run(a.seconds,a.bits)
