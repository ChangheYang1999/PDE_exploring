"""Independent reconstruction and midpoint-Taylor Bernstein matrix cover audit."""
from pathlib import Path
from math import comb,factorial
from functools import lru_cache
from fractions import Fraction
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,gzip,time,argparse
from flint import fmpq,fmpq_poly,arb,arb_mat,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial,pshift,ar
BASE=ROOT/'research/global_matrices'

def digest(p):return sha256(Path(p).read_bytes()).hexdigest()
def add(A,B,factor=1,shift=0):
    for (i,k),v in B.items():A[i+shift,k]=A.get((i+shift,k),fmpq(0))+factor*v
    return {k:v for k,v in A.items() if v}

def reconstruct():
    start=time.monotonic();path=ROOT/'research/refit_audit/data/d2_canonical.json';model=Radial(path)
    z=fmpq_poly([0,1]);T=[fmpq_poly([1]),z];U=[fmpq_poly([1]),2*z]
    for n in range(2,64):T.append(2*z*T[-1]-T[-2]);U.append(2*z*U[-1]-U[-2])
    out={}
    for label,dx,dy in [('chi22',2,2),('chi04',0,4),('chi31',3,1),('chi13',1,3),('e',1,1)]:
        for (j,n),P in model.deriv(dx,dy).items():
            assert n%2==0
            if label=='e':P=-n*P;angular=T[n//2]
            elif dy%2:
                assert n>0;angular=U[n//2-1]
            else:angular=T[n//2]
            P=pshift(P,2);A=out.setdefault(f'{label}_{j}',{})
            for i,a in enumerate(P):
                if not a:continue
                for k,b in enumerate(angular):
                    if b:A[i,k]=A.get((i,k),fmpq(0))+a*b
        print('reconstructed',label,time.monotonic()-start,flush=True)
    out={key:{ij:v for ij,v in P.items() if v} for key,P in out.items()}
    prior=BASE/'data/prior_d2_polynomials.json';old=json.loads(prior.read_text())
    oldP={key:{(i,k):fmpq(v) for i,k,v in rows} for key,rows in old['polynomials'].items()}
    assert set(out)==set(oldP)
    for key in out:assert out[key]==oldP[key],key
    result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':digest(path),
            'prior_sha256':digest(prior),'cl':str(model.c),'delta':str(model.delta),'exact_match_all_fields':True,
            'polynomials':{key:[[i,k,str(v)] for (i,k),v in sorted(P.items())] for key,P in out.items()},
            'elapsed_seconds':time.monotonic()-start}
    dest=BASE/'data/independent_d2_polynomials.json.gz'
    with gzip.open(dest,'wt',compresslevel=2) as f:json.dump(result,f,separators=(',',':'))
    (BASE/'verification/reconstruction.json').write_text(json.dumps({k:v for k,v in result.items() if k!='polynomials'},indent=2)+'\n')
    print('all exact matches; saved',dest.stat().st_size,flush=True)

def matrices(data,kind):
    P={key:{(i,k):fmpq(v) for i,k,v in rows} for key,rows in data['polynomials'].items()};c=fmpq(data['cl'])
    A={(label,j):{} for label in ['a','b','q'] for j in range(7)}
    constants={'M':(2*c+1-fmpq(19,5),0),'M1':(fmpq(1,2),-c/5),
               'M2':(fmpq(1,2)-c,fmpq(3,2)+c/5)}
    constant,slope=constants[kind]
    for label in ['a','b']:A[label,0]={(0,0):constant,(1,0):slope}
    terms={'M':[('a','chi22',-2),('a','chi04',-1),('b','chi22',1),('q','chi31',1)],
           'M1':[('a','chi04',-1),('b','chi22',-1),('q','chi13',1)],
           'M2':[('a','chi22',1),('a','chi04',-1),('b','chi22',-2),('q','chi13',fmpq(3,2)),('q','chi31',-fmpq(1,2))]}
    for j in range(6):
        for label,field,factor in terms[kind]:
            A[label,j+1]=add(A[label,j+1],P[f'{field}_{j}'],factor)
            if kind=='M2':A[label,j+1]=add(A[label,j+1],P[f'{field}_{j}'],3*factor,1)
        if kind!='M':
            for label in ['a','b']:A[label,j+1]=add(A[label,j+1],P[f'e_{j}'],-fmpq(1,5) if kind=='M1' else fmpq(16,5),1)
    return {key:{ij:v for ij,v in B.items() if v} for key,B in A.items()}

@lru_cache(None)
def transform(degree,low,high):
    a,b=fmpq(low),fmpq(high)
    power=arb_mat([[ar(fmpq(comb(k,l))*a**(k-l)*(b-a)**l) if l<=k else arb(0) for k in range(degree+1)] for l in range(degree+1)])
    bern=arb_mat([[ar(fmpq(comb(i,k),comb(degree,k))) if k<=i else arb(0) for k in range(degree+1)] for i in range(degree+1)])
    return bern*power

def extrema(values):
    low=high=values[0]
    for v in values[1:]:low=low.min(v);high=high.max(v)
    return low.lower(),high.upper()
def maxabs(values):
    v=arb(0)
    for x in values:v=v.max(abs(x))
    return v.upper()

def midpoint_multipliers(degree,a,b,delta,N=6):
    mu=(a+b)/2;H=(b-a)/2;out={};errors={}
    for j in range(7):
        q=j*delta/2;fall=fmpq(1);local=[arb(0)]*(N+1)
        for k in range(N+1):
            if k:fall*=q-k+1
            C=ar((-1)**k*fall/fmpq(factorial(k)))*(1-ar(mu))**ar(q-k)*ar(H)**k
            for l in range(k+1):local[l]+=C*comb(k,l)*2**l*(-1)**(k-l)
        bern=[sum((local[l]*ar(fmpq(comb(i,l),comb(N,l))) for l in range(i+1)),arb(0)) for i in range(N+1)]
        factor=ar(abs(fall*(q-N))/fmpq(factorial(N+1)))*ar(H)**(N+1)
        errors[j]=factor*((1-ar(a))**ar(q-N-1)).max((1-ar(b))**ar(q-N-1))
        M=arb_mat(degree+N+1,degree+1)
        for i in range(degree+1):
            for k in range(N+1):M[i+k,i]=bern[k]*ar(fmpq(comb(degree,i)*comb(N,k),comb(degree+N,i+k)))
        out[j]=M
    return out,errors

def ranges(P,nt,nz,a,b,c,d,delta):
    radial=transform(nt,str(a),str(b));angular=transform(nz,str(c),str(d)).transpose()
    B={key:radial*value*angular for key,value in P.items()}
    wl=(1-ar(b))**ar(delta/2);wh=(1-ar(a))**ar(delta/2)
    W=arb_mat([[sum((ar(fmpq(comb(n,k)*comb(i,k),comb(6,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(i,n)+1)),arb(0)) for n in range(7)] for i in range(7)])
    plain={}
    for label in ['a','b','q']:plain[label]=extrema((W*arb_mat([B[label,j].entries() for j in range(7)])).entries())
    improved=None
    if b<1:
        multipliers,errors=midpoint_multipliers(nt,a,b,delta);improved={}
        for label in ['a','b','q']:
            total=arb_mat(nt+7,nz+1);error=arb(0)
            for j in range(7):
                total+=multipliers[j]*B[label,j];error+=errors[j]*maxabs(B[label,j].entries())
            lo,hi=extrema(total.entries());improved[label]=(lo-error).lower(),(hi+error).upper()
    return plain,improved

def eigen(R,zl,zh):
    a,b=R['a'][0],R['b'][0];ql,qh=R['q']
    z=fmpq(0) if zl<=0<=zh else min(abs(zl),abs(zh))
    C=abs(ql).max(abs(qh))*(1-ar(z)**2).sqrt()
    return ((a+b-((a-b)**2+4*C*C).sqrt())/2).max(a.min(b)-C)

def endpoints(path):
    a,b,c,d=map(fmpq,[0,1,-1,1])
    for letter in path:
        if letter=='t':b=(a+b)/2
        elif letter=='T':a=(a+b)/2
        elif letter=='z':d=(c+d)/2
        elif letter=='Z':c=(c+d)/2
        else:raise ValueError(letter)
    return a,b,c,d

def checktree(paths,prefix=''):
    if prefix in paths:
        assert not any(p!=prefix and p.startswith(prefix) for p in paths);return
    children={p[len(prefix)] for p in paths if p.startswith(prefix)}
    assert children in [{'t','T'},{'z','Z'}],(prefix,children)
    for child in children:checktree(paths,prefix+child)

def audit(kind,bits=768):
    ctx.prec=bits;start=time.monotonic();datafile=BASE/'data/independent_d2_polynomials.json.gz'
    with gzip.open(datafile,'rt') as f:data=json.load(f)
    S=matrices(data,kind);nt=max(i for A in S.values() for i,k in A);nz=max(k for A in S.values() for i,k in A)
    P={}
    for key,A in S.items():
        M=arb_mat(nt+1,nz+1)
        for (i,k),v in A.items():M[i,k]=ar(v)
        P[key]=M
    cover=BASE/f'data/nb_d2_exact.{kind}.correlated.json';old=json.loads(cover.read_text())
    paths={row['path'] for row in old['accepted']};assert len(paths)==len(old['accepted']);checktree(paths)
    dest=BASE/f'verification/d2_{kind}_{bits}.json';rows=[];worst=arb(100);delta=fmpq(data['delta'])
    print('prepared',kind,nt,nz,'leaves',len(paths),'seconds',time.monotonic()-start,flush=True)
    if dest.exists():
        prev=json.loads(dest.read_text());assert prev['polynomial_sha256']==digest(datafile) and prev['cover_sha256']==digest(cover)
        rows=prev['rows']
        for row in rows:worst=worst.min(arb(row['lower']))
    done={row['path'] for row in rows}
    for cell in old['accepted']:
        if cell['path'] in done:continue
        a,b,c,d=endpoints(cell['path']);assert [str(a),str(b)]==cell['t'] and [str(c),str(d)]==cell['z']
        plain,improved=ranges(P,nt,nz,a,b,c,d,delta);low=eigen(plain,c,d)
        if improved is not None:low=low.max(eigen(improved,c,d))
        row={'path':cell['path'],'lower':low.str(70),'pass':bool(low>=0)};rows.append(row);worst=worst.min(low)
        result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'kind':kind,'precision_bits':bits,
                'method':'Independent exact polynomial reconstruction and midpoint degree-six Taylor Bernstein bounds',
                'polynomial_sha256':digest(datafile),'cover_sha256':digest(cover),'complete_cover_tree':True,
                'rows':rows,'total_leaves':len(paths),'all_pass':len(rows)==len(paths) and all(v['pass'] for v in rows),
                'worst':worst.str(70),'stage_elapsed_seconds':time.monotonic()-start}
        dest.write_text(json.dumps(result,indent=2)+'\n')
        print('cell',len(rows),cell['path'],row['pass'],low.str(12),'seconds',time.monotonic()-start,flush=True)
        if time.monotonic()-start>480:break

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('stage',choices=['reconstruct','M','M1','M2']);p.add_argument('--bits',type=int,default=768);a=p.parse_args()
    if a.stage=='reconstruct':reconstruct()
    else:audit(a.stage,a.bits)
