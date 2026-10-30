"""Ball-polynomial evaluation with exact endpoint and resonance checks."""
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import sys,json,time,hashlib,argparse
from flint import fmpq,arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import ar
from norms import derivative,endpoint,weight_poly
from pipeline import load,source,digest,DATA,OUT

def norm_ball(D,d,delta,weighted=False,rproxy=False,N=112,harmonic=False):
    start=time.monotonic();groups={};endpoints=[]
    one_minus=arb_poly([1,-1])
    for nx in range(d+1):
        harmonics={}
        for (ell,kind,n),P in D[d,nx].items():
            if not P:continue
            q,Q=endpoint(P)
            exp=d-3+ell*delta+2*q-(fmpq(4,5) if weighted else 0)-(1 if rproxy else 0)
            row={'nx':nx,'ell':ell,'kind':kind,'n':n,'endpoint_order':q,'diagonal_exponent':str(exp)}
            endpoints.append(row)
            assert exp>-1,row
            harmonics.setdefault((kind,n),[]).append((ell,q,arb_poly([ar(v) for v in Q])))
        for (kind,n),rows in harmonics.items():
            for i,(ell,q,P) in enumerate(rows):
                for ell2,q2,Q in rows[i+1:]:assert ((ell-ell2)*delta/2).denominator!=1
                for j in range(i,len(rows)):
                    ell2,q2,Q=rows[j]
                    exp=d-3+(ell+ell2)*delta/2+q+q2-(fmpq(4,5) if weighted else 0)-(1 if rproxy else 0)
                    factor=fmpq(comb(d,nx)*(2 if kind=='c' and n==0 else 1)*(1 if j==i else 2))
                    if harmonic:assert n>0;factor/=n*n
                    poly=P*Q*ar(factor)
                    if d%2==0:poly*=one_minus
                    if rproxy:poly*=one_minus
                    groups[exp]=groups.get(exp,arb_poly([]))+poly
        print('formed component',d,nx,'seconds',time.monotonic()-start,flush=True)
    def integrate(P,b):return sum((a/ar(b+k+1) for k,a in enumerate(P)),arb(0))
    S=sum((integrate(P,b) for b,P in groups.items()),arb(0));assert S>0,S
    eps=fmpq(0);lo=hi=S
    if weighted:
        W,eps=weight_poly(N);W=arb_poly([ar(v) for v in W])
        hi=sum((integrate(P*W,b) for b,P in groups.items()),arb(0));lo=hi-ar(eps)*S
        assert lo>0,lo
    pref=arb.pi()/2*(arb(4)**ar(fmpq(4,5)) if weighted else arb(1))
    lower=(pref*lo).sqrt();upper=(pref*hi).sqrt()
    return {'status':'FINITE','norm_lower_ball':lower.str(80),'norm_upper_ball':upper.str(80),
            'norm_lower':str(lower.lower()),'norm_upper':str(upper.upper()),
            'radial_unweighted_sum':S.str(90),'radial_upper_sum':hi.str(90),'weight_error_rational':str(eps),
            'weight_degree':N if weighted else 0,'endpoint_rows':endpoints,'groups':len(groups),
            'elapsed_seconds':time.monotonic()-start}

def run(args):
    begin=time.monotonic();ctx.prec=args.bits;name=args.candidate;path=source(name)
    delta=1-1/fmpq(json.loads(path.read_text())['cl'])
    params={'G0':(0,False,False,False),'G1':(1,False,False,False),'P2':(2,True,False,False),
            'Q3':(3,True,False,False),'rF_proxy':(0,False,True,False),'angular_Hminus1_proxy':(0,False,True,True)}
    d,w,r,h=params[args.label]
    initial=max(dd for dd in range(d+1) if (DATA/f'{name}_D{dd}.json.gz').exists())
    D=load(name,initial)
    print('loaded',time.monotonic()-begin,flush=True)
    for dd in range(initial,d):
        target={}
        for nx in range(dd+2):target[dd+1,nx]=derivative(D[dd,0],dd,'y',delta) if nx==0 else derivative(D[dd,nx-1],dd,'x',delta)
        for nx in range(1,dd+1):assert target[dd+1,nx]==derivative(D[dd,nx],dd,'y',delta)
        D=target;print('derived',dd+1,time.monotonic()-begin,flush=True)
    out=norm_ball(D,d,delta,w,r,args.degree,h)
    out.update({'candidate':name,'component':args.label,'source_sha256':digest(path),
                'polynomial_sha256':digest(DATA/f'{name}_D0.json.gz'),'code_sha256':digest(Path(__file__)),
                'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
                'total_elapsed_seconds':time.monotonic()-begin,'method':'Ball-polynomial exact power integrals; rational endpoint and nonresonance checks'})
    dest=OUT/f'{name}_{args.label}_ball_{args.bits}.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    print(args.label,out['norm_lower_ball'],out['norm_upper_ball'],'seconds',time.monotonic()-begin,flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('label');p.add_argument('--bits',type=int,default=2048);p.add_argument('--degree',type=int,default=112);run(p.parse_args())
