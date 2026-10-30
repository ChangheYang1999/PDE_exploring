"""Exact branch-aware matrix construction and bounded full-plane cover stages."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from math import comb,factorial
from hashlib import sha256
import argparse,gzip,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial,pshift,ar
sys.path.insert(0,str(ROOT/'research/global_matrices/code'))
from cover import endpoints,checktree,extrema,maxabs,eigen
BASE=ROOT/'research/candidate_background_cover'
NAME='C1-N1-007-d2w-j7-e2bal'
def digest(p):return sha256(Path(p).read_bytes()).hexdigest()
def source(name):return ROOT/f'research/candidate_audits/data/{name}/canonical.json'
def storage(name):return BASE/f'data/{name}_polynomials.json.gz'
def reconstruct(name,bits):
    ctx.prec=bits;start=time.monotonic();path=source(name);dest=storage(name);assert not dest.exists()
    model=Radial(path);z=Poly([0,1]);T=[Poly([1]),z];U=[Poly([1]),2*z]
    nmax=max(n//2 for field in [model.rx,model.ry] for j,n in field)
    for n in range(2,nmax+1):T.append(2*z*T[-1]-T[-2]);U.append(2*z*U[-1]-U[-2])
    out={};origin={}
    for label,field in [('rx',model.rx),('ry',model.ry)]:
        for (j,n),P in field.items():
            assert n%2==0
            if label=='rx':assert n>0;angular=U[n//2-1]
            else:angular=T[n//2]
            P=pshift(P,2);A=out.setdefault((label,j+1),{})
            for i,a in enumerate(P):
                if not a:continue
                for k,b in enumerate(angular):
                    if b:A[i,k]=A.get((i,k),Q(0))+a*b
        origin[label]={}
        for (lab,j),P in out.items():
            if lab!=label:continue
            for (i,k),v in P.items():
                if i==0:origin[label][k]=origin[label].get(k,Q(0))+v
        origin[label]={k:v for k,v in origin[label].items() if v}
        print('constructed',label,'seconds',time.monotonic()-start,flush=True)
    assert not origin['rx'];assert set(origin['ry'])=={0}
    out={f'{label}_{j}':{key:v for key,v in P.items() if v} for (label,j),P in out.items()}
    # Compare to the independently reproduced direct Cartesian point.
    pf=ROOT/f'research/candidate_audits/verification/{name}_point.json';point=json.loads(pf.read_text())
    x,y=Q(1,10),Q(73,100);r2=x*x+y*y;t=r2/(1+r2);z0=(x*x-y*y)/r2;sin2=2*x*y/r2
    w=(1-ar(t))**ar(model.delta/2);checks={}
    for label in ['rx','ry']:
        value=arb(0)
        for key,P in out.items():
            lab,j=key.split('_');j=int(j)
            if lab==label:value+=w**j*sum((ar(v*t**i*z0**k) for (i,k),v in P.items()),arb(0))
        if label=='rx':value*=ar(sin2)
        field='rho_x' if label=='rx' else 'rho_y';assert value.overlaps(arb(point['fields'][field]))
        checks[field]=value.str(80)
    record={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,
            'canonical_sha256':digest(path),'code_sha256':digest(__file__),'proof_sha256':digest(BASE/'PROOF.md'),
            'radial_code_sha256':digest(ROOT/'research/radial_fourier/code/radial.py'),'cl':str(model.c),'delta':str(model.delta),
            'J':max(j+1 for j in model.p),'origin_rho_y':str(origin['ry'][0]),'point_record_sha256':digest(pf),
            'point_checks':checks,'polynomials':{key:[[i,k,str(v)] for (i,k),v in sorted(P.items())] for key,P in out.items()},
            'elapsed_seconds':time.monotonic()-start}
    with gzip.open(dest,'wt',compresslevel=2) as f:json.dump(record,f,separators=(',',':'))
    summary={k:v for k,v in record.items() if k not in ['polynomials','origin_rho_y']}
    summary.update({'polynomial_sha256':digest(dest),'nonzero_coefficients':sum(len(P) for P in out.values()),'bytes':dest.stat().st_size})
    (BASE/f'verification/{name}_reconstruction.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)

@lru_cache(128)
def transform(degree,low,high):
    a,b=Q(low),Q(high)
    power=arb_mat([[ar(Q(comb(k,l))*a**(k-l)*(b-a)**l) if l<=k else arb(0) for k in range(degree+1)] for l in range(degree+1)])
    bern=arb_mat([[ar(Q(comb(i,k),comb(degree,k))) if k<=i else arb(0) for k in range(degree+1)] for i in range(degree+1)])
    return bern*power

def multipliers(degree,a,b,delta,J,N=6):
    mu=(a+b)/2;H=(b-a)/2;out={};errors={}
    for j in range(J+1):
        q=j*delta/2;fall=Q(1);local=[arb(0)]*(N+1)
        for k in range(N+1):
            if k:fall*=q-k+1
            coefficient=ar((-1)**k*fall/Q(factorial(k)))*(1-ar(mu))**ar(q-k)*ar(H)**k
            for l in range(k+1):local[l]+=coefficient*comb(k,l)*2**l*(-1)**(k-l)
        bern=[sum((local[l]*ar(Q(comb(i,l),comb(N,l))) for l in range(i+1)),arb(0)) for i in range(N+1)]
        factor=ar(abs(fall*(q-N))/Q(factorial(N+1)))*ar(H)**(N+1)
        errors[j]=factor*((1-ar(a))**ar(q-N-1)).max((1-ar(b))**ar(q-N-1))
        M=arb_mat(degree+N+1,degree+1)
        for i in range(degree+1):
            for k in range(N+1):M[i+k,i]=bern[k]*ar(Q(comb(degree,i)*comb(N,k),comb(degree+N,i+k)))
        out[j]=M
    return out,errors

def ranges(P,nt,nz,a,b,c,d,delta,J,tau):
    radial=transform(nt,str(a),str(b));angular=transform(nz,str(c),str(d)).transpose()
    B={key:radial*value*angular for key,value in P.items()}
    wl=(1-ar(b))**ar(delta/2);wh=(1-ar(a))**ar(delta/2)
    W=arb_mat([[sum((ar(Q(comb(n,k)*comb(i,k),comb(J,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(i,n)+1)),arb(0)) for n in range(J+1)] for i in range(J+1)])
    plain={'b':(ar(tau),ar(tau))}
    for label in ['a','q']:plain[label]=extrema((W*arb_mat([B[label,j].entries() for j in range(J+1)])).entries())
    improved=None
    if b<1:
        mult,error=multipliers(nt,a,b,delta,J);improved={'b':(ar(tau),ar(tau))}
        for label in ['a','q']:
            total=arb_mat(nt+7,nz+1);err=arb(0)
            for j in range(J+1):total+=mult[j]*B[label,j];err+=error[j]*maxabs(B[label,j].entries())
            lo,hi=extrema(total.entries());improved[label]=(lo-err).lower(),(hi+err).upper()
    return plain,improved

def run(name,bits,seconds,tau):
    ctx.prec=bits;start=time.monotonic();datafile=storage(name)
    with gzip.open(datafile,'rt') as f:data=json.load(f)
    assert data['canonical_sha256']==digest(source(name))
    fields={key:{(i,k):Q(v) for i,k,v in rows} for key,rows in data['polynomials'].items()}
    J=data['J'];nt=max(i for P in fields.values() for i,k in P);nz=max(k for P in fields.values() for i,k in P)
    P={(label,j):arb_mat(nt+1,nz+1) for label in ['a','q'] for j in range(J+1)};P['a',0][0,0]=ar(tau)
    for key,poly in fields.items():
        label,j=key.split('_');j=int(j);nameout='q' if label=='rx' else 'a';factor=Q(-1,2) if label=='rx' else Q(1)
        for (i,k),v in poly.items():P[nameout,j][i,k]=ar(factor*v)
    target=BASE/f'verification/{name}_theta_{str(tau).replace("/","_")}_{bits}.json'
    codehash=digest(__file__);sourcehash=digest(datafile)
    coverfile=ROOT/'research/signed_matrices/verification/d2_L2_768.json'
    if target.exists():
        old=json.loads(target.read_text());assert old['code_sha256']==codehash and old['source_sha256']==sourcehash
        queue=old['pending'];accepted=old['accepted'];failures=old['inconclusive'];elapsed=old['total_elapsed_seconds']
    else:
        old=json.loads(coverfile.read_text());assert old['all_pass']
        queue=[r['path'] for r in old['accepted']];accepted=[];failures=[];elapsed=0
    checktree(set(queue+[r['path'] for r in accepted]));delta=Q(data['delta'])
    print('prepared',name,'J',J,'degrees',nt,nz,'accepted',len(accepted),'pending',len(queue),'seconds',time.monotonic()-start,flush=True)
    count=0
    while queue and time.monotonic()-start<seconds:
        path=queue.pop(0);a,b,c,d=endpoints(path)
        plain,improved=ranges(P,nt,nz,a,b,c,d,delta,J,tau);bound=eigen(plain,c,d)
        if improved is not None:bound=bound.max(eigen(improved,c,d))
        if bound>=0:accepted.append({'path':path,'bound':bound.str(80),'pass':True})
        else:
            failures.append({'path':path,'bound':bound.str(30)})
            if len(path)>=48:queue.insert(0,path);print('depth limit; no conclusion',path,flush=True);break
            children=('t','T') if (b-a)/(1-a)>=(d-c)/2 else ('z','Z')
            queue.extend([path+x for x in children])
        count+=1;leaves=queue+[r['path'] for r in accepted];assert len(set(leaves))==len(leaves);checktree(set(leaves))
        state={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'tau':str(tau),'precision_bits':bits,
               'source_sha256':sourcehash,'canonical_sha256':data['canonical_sha256'],'code_sha256':codehash,'proof_sha256':digest(BASE/'PROOF.md'),
               'initial_cover_sha256':digest(coverfile),'enclosure_helpers_sha256':digest(ROOT/'research/global_matrices/code/cover.py'),
               'J':J,'degree_t':nt,'degree_z':nz,'accepted':accepted,'pending':queue,'inconclusive':failures,
               'complete_partition':True,'all_pass':not queue,'stage_elapsed_seconds':time.monotonic()-start,'total_elapsed_seconds':elapsed+time.monotonic()-start}
        if not queue:
            kfile=ROOT/f'research/background_sobolev/verification/{name}.json';kd=json.loads(kfile.read_text())
            margin=ar(Q(data['cl']))+1-ar(tau)-arb(kd['gradient_identity_conditional_HS_upper'])
            state.update({'signed_rate_lower':margin.str(80),'signed_rate_at_least_two':bool(margin>=2),'HS_source_sha256':digest(kfile)})
        temp=target.with_suffix('.pending');temp.write_text(json.dumps(state,indent=2)+'\n');temp.replace(target)
        print('cell',count,path,'pass',bool(bound>=0),'bound',bound.str(10),'pending',len(queue),'seconds',time.monotonic()-start,flush=True)
    print('stage done accepted',len(accepted),'pending',len(queue),'seconds',time.monotonic()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('stage',choices=['build','cover']);p.add_argument('--candidate',default=NAME)
    p.add_argument('--bits',type=int,default=768);p.add_argument('--seconds',type=int,default=440);p.add_argument('--tau',default='2/25');a=p.parse_args()
    if a.stage=='build':reconstruct(a.candidate,a.bits)
    else:run(a.candidate,a.bits,a.seconds,Q(a.tau))
