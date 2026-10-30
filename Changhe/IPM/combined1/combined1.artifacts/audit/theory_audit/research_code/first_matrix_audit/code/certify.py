from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from functools import lru_cache
from math import comb
import importlib.util,sys,json,gzip,time,argparse
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,ctx
BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('t4_signed_cover',BASE.parent/'signed_cover_audit/code/certify.py')
shared=importlib.util.module_from_spec(spec);spec.loader.exec_module(shared)
fields,td,ar=shared.fields,shared.td,shared.ar
affine,bernstein,interval,mag,product_range=shared.affine,shared.bernstein,shared.interval,shared.mag,shared.product_range
check_cover,endpoints,tensor,plus=shared.check_cover,shared.endpoints,shared.tensor,shared.plus
LABELS=('a','b','q')
def digest(p):return sha256(Path(p).read_bytes()).hexdigest()
def construct():
    data=json.loads((BASE/'source/d2_canonical.json').read_text());c,delta,_,stream=fields(data)
    modes={}
    for (j,n),S in stream.items():
        d=td(S,(j+1)*delta/2,2)
        for k,C in ((n-1,-(d+n*S)/2),(n+1,(d-n*S)/2)):
            assert k>0 and k%2==1
            modes[j,k]=modes.get((j,k),Poly([]))+C
    z=Poly([0,1]);T=[Poly([1]),z];U=[Poly([1]),2*z]
    for i in range(2,max(n for j,n in modes)//2+2):T.append(2*z*T[-1]-T[-2]);U.append(2*z*U[-1]-U[-2])
    dx={j:{} for j in range(6)};dy={j:{} for j in range(6)}
    for (j,n),C in modes.items():
        d=td(C,(j+1)*delta/2,1)
        tensor(dx[j],(d+n*C)/2,T[(n-1)//2]);tensor(dx[j],(d-n*C)/2,T[(n+1)//2])
        tensor(dy[j],(d-n*C)/2,U[(n+1)//2-1])
        if n>1:tensor(dy[j],-(d+n*C)/2,U[(n-1)//2-1])
    dx={j:{ij:v for ij,v in P.items() if v} for j,P in dx.items()};dy={j:{ij:v for ij,v in P.items() if v} for j,P in dy.items()}
    old=json.loads((BASE/'source/T4_gradient.json').read_text())
    Y={j:{(i,k):Q(v) for i,k,v in old['polynomials'][f'Y_{j}']} for j in range(6)}
    with gzip.open(BASE/'source/N4_polynomials.json.gz','rt') as f:old=json.load(f)
    N4={key:{(i,k):Q(v) for i,k,v in rows} for key,rows in old['polynomials'].items()}
    polys={}
    for j in range(6):
        assert dx[j]=={ij:-v for ij,v in N4[f'chi22_{j}'].items()}
        assert dy[j]=={ij:-v for ij,v in N4[f'chi13_{j}'].items()}
        polys['a',j]=plus(Y[j],dx[j],Q(-1));polys['b',j]=dx[j];polys['q',j]={ij:-v for ij,v in dy[j].items()}
        assert polys['a',j]=={ij:-v for ij,v in N4[f'chi04_{j}'].items()}
    out={'utc':datetime.now(timezone.utc).isoformat(),'all_matrix_coefficients_match':True,
         'canonical_sha256':digest(BASE/'source/d2_canonical.json'),'density_gradient_sha256':digest(BASE/'source/T4_gradient.json'),
         'N4_polynomials_sha256':digest(BASE/'source/N4_polynomials.json.gz'),'code_sha256':digest(__file__),
         'polynomials':{f'{label}_{j}':[[i,k,str(v)] for (i,k),v in sorted(P.items())] for (label,j),P in polys.items()}}
    (BASE/'verification/reconstruction.json').write_text(json.dumps(out,indent=2)+'\n')
    return c,delta,polys

def enclose(P,nt,nz,a,b,c,d,delta):
    local={key:affine(nt,str(a),str(b))*M*(bernstein(nz)*affine(nz,str(c),str(d))).transpose() for key,M in P.items()}
    branch={key:interval(bernstein(nt)*M) for key,M in local.items()};plain={}
    for label in LABELS:
        lo=arb(0);hi=arb(0)
        for j in range(6):
            power=(j+1)*delta/2;wl=(1-ar(b))**ar(power);wh=(1-ar(a))**ar(power)
            ll,hh=product_range(wl,wh,*branch[label,j]);lo+=ll;hi+=hh
        plain[label]=(lo.lower(),hi.upper())
    if b==1:return plain,'independent'
    N=8;v0=1-(a+b)/2;kappa=(b-a)/(2*v0);multipliers={};errors={}
    for j in range(6):
        power=(j+1)*delta/2;pref=ar(v0)**ar(power);kapp=ar(kappa);coeff=[arb(0) for _ in range(N+1)];choose=Q(1)
        for k in range(N+1):
            if k:choose*=(power-k+1)/k
            scale=pref*ar(choose)*kapp**k
            for ell in range(k+1):coeff[ell]+=scale*comb(k,ell)*((-2)**ell)
        choose*=(power-N)/(N+1);errors[j]=pref*ar(abs(choose))*kapp**(N+1)*(1-kapp)**ar(power-N-1)
        M=arb_mat(nt+N+1,nt+1)
        for i in range(nt+1):
            for k in range(N+1):M[i+k,i]=coeff[k]
        multipliers[j]=M
    out={}
    for label in LABELS:
        total=arb_mat(nt+N+1,nz+1);error=arb(0)
        for j in range(6):total+=multipliers[j]*local[label,j];error+=errors[j]*mag(branch[label,j])
        lo,hi=interval(bernstein(nt+N)*total);lo=(lo-error).lower();hi=(hi+error).upper();pl,ph=plain[label]
        out[label]=(lo.max(pl).lower(),hi.min(ph).upper())
    return out,'degree8-correlated-intersection'

def run(seconds,bits):
    ctx.prec=bits;start=time.monotonic();c,delta,polys=construct()
    nt=max(i for P in polys.values() for i,k in P);nz=max(k for P in polys.values() for i,k in P);P={}
    for key,vals in polys.items():
        M=arb_mat(nt+1,nz+1)
        for (i,k),v in vals.items():M[i,k]=ar(v)
        P[key]=M
    source=BASE/'source/N4_M1_cover.json';initial=json.loads(source.read_text());assert not initial['pending']
    paths=[row['path'] for row in initial['accepted']];check_cover(paths)
    dest=BASE/'verification/d2_M1_cover.json'
    if dest.exists():
        old=json.loads(dest.read_text());assert old['code_sha256']==digest(__file__) and old['source_cover_sha256']==digest(source)
        accepted=old['accepted'];queue=old['pending'];refined=old['refined'];elapsed=old['elapsed_seconds']
    else:accepted=[];queue=paths;refined=[];elapsed=0
    print('prepared',nt,nz,'accepted',len(accepted),'pending',len(queue),flush=True)
    while queue and time.monotonic()-start<seconds:
        path=queue.pop(0);a,b,zl,zh=endpoints(path);vals,method=enclose(P,nt,nz,a,b,zl,zh,delta)
        d1=arb(1)/10+vals['a'][0];d2=arb(1)/10+vals['b'][0];zmin=Q(0) if zl<=0<=zh else min(abs(zl),abs(zh))
        det=d1*d2-(1-ar(zmin)**2)*mag(vals['q'])**2;passed=bool(d1>=0 and d2>=0 and det>=0)
        if passed:accepted.append({'path':path,'diag1_lower':d1.str(70),'diag2_lower':d2.str(70),'det_lower':det.str(70),'method':method,'pass':True})
        else:
            assert len(path)<50
            axis='tT' if (b-a)/(1-a)>=(zh-zl)/2 else 'zZ';queue.extend(path+x for x in axis);refined.append(path)
        check_cover([r['path'] for r in accepted]+queue)
        out={'utc':datetime.now(timezone.utc).isoformat(),'target':'M1>=(9/10)I','source_cover_sha256':digest(source),'proof_sha256':digest(BASE/'PROOF.md'),
             'code_sha256':digest(__file__),'helper_sha256':digest(BASE.parent/'signed_cover_audit/code/certify.py'),'reconstruction_sha256':digest(BASE/'verification/reconstruction.json'),
             'accepted':accepted,'pending':queue,'refined':refined,'precision_bits':bits,'complete_partition':True,'all_pass':not queue,
             'elapsed_seconds':elapsed+time.monotonic()-start}
        dest.write_text(json.dumps(out,indent=2)+'\n')
        print('cell',path,passed,'det',det.str(10),'pending',len(queue),'sec',round(time.monotonic()-start,3),flush=True)
    print('stage done',len(accepted),len(queue),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=460);p.add_argument('--bits',type=int,default=768);a=p.parse_args();run(a.seconds,a.bits)
