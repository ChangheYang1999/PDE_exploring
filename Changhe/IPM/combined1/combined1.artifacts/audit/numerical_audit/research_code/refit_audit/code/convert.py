"""Independent recurrence conversion of exact A2 generator inputs."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from collections import defaultdict
from flint import fmpq,fmpq_poly,ctx,arb
import sys,json,hashlib,time
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/sector_audit/code'))
from sectors_flint import sectors,aq,enc
T=fmpq_poly([0,1]);Z=2*T-1

def legendre(n):
    a,b=fmpq_poly([1]),Z
    if n==0:return a
    for k in range(1,n):a,b=b,((2*k+1)*Z*b-k*a)/(k+1)
    return b

def convert(path):
    raw=path.read_bytes();d=json.loads(raw);A=defaultdict(Q)
    for gen in d['generators']:
        j,m,s,a=gen['j'],gen['m'],gen['spec'],Q(gen['coef'])
        if s[0]=='mono':pol=T**s[1]
        elif s[0]=='leg':pol=T**s[1]*legendre(s[2])
        else:raise ValueError(s)
        for l,b in enumerate(pol):A[j,m,m+l]+=a*Q(str(b))
    order=sorted(k for k,v in A.items() if v)
    serial='\n'.join(','.join(map(str,k))+':'+enc(A[k]) for k in order)+'\n'
    c=Q(d['cl']);g=1/c;strain=Q(0);a0=Q(0)
    for (j,m,k),v in A.items():
        if k>2:continue
        p=(3+g-j*(1-g))/2
        radial=Q(1)
        for z in range(2-k):radial*= (p-k-z)/(z+1)
        # degree four polynomial: radial*(x^2+y^2)^(2-m)*H_m
        if m==0:B,C=2,1
        elif m==1:B,C=0,-1
        elif m==2:B,C=-6,1
        else:continue
        strain+=4*B*radial*v;a0-= (4*B+24*C)*radial*v
    state={'cl':enc(c),'a0':enc(a0),'strain':enc(strain),'order':order,
           'coefficients':[enc(A[k]) for k in order],
           'canonical_serialization_sha256':hashlib.sha256(serial.encode()).hexdigest(),
           'serialization_note':'N4 canonical nonzero triples: j,m,k:num/den newline, sorted triples',
           'source_sha256':hashlib.sha256(raw).hexdigest(),'generator_count':len(d['generators'])}
    return state

if __name__=='__main__':
    ctx.prec=256
    names=sys.argv[1:] or ['d2','Mpen2','b6']
    base=json.loads((ROOT/'research/baseline/data/state131_independent.json').read_text())
    _,BC,BG,BE=sectors(base,qmax=0)
    for name in names:
        start=time.monotonic();src=ROOT/f'research/refit_audit/data/{name}_generators.json';state=convert(src)
        dst=ROOT/f'research/refit_audit/data/{name}_canonical.json';dst.write_text(json.dumps(state,indent=2)+'\n')
        print(name,'canonical',len(state['order']),'strain',str(Q(state['strain'])-(1-Q(state['cl']))),'seconds',time.monotonic()-start,flush=True)
        alpha,C,G,E=sectors(state,qmax=1,hmax=7)
        rows=[]
        for (h,q),P in sorted(E.items(),key=lambda row:alpha(*row[0]),reverse=True):
            # Huge nonleading exact fractions remain reproducible from canonical input.
            ss=sum((v*v for v in P.values()),0);norm=(arb.pi()*aq(ss)).sqrt()
            row={'h':h,'q':q,'exponent':enc(alpha(h,q)),'exponent_arb':aq(alpha(h,q)).str(30),
                 'exact_zero':not P,'max_harmonic':max(P,default=0),'full_circle_norm':norm.str(45)}
            rows.append(row)
            if alpha(h,q)>=-3:print(name,h,q,row['exponent_arb'],row['exact_zero'],row['full_circle_norm'],flush=True)
        out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,
             'source_sha256':state['source_sha256'],'canonical_file_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),
             'strain_exact':state['strain'],'a0_exact':state['a0'],'strain_normalization':Q(state['strain'])==1-Q(state['cl']),
             'c_exact_equal_state131':Q(state['cl'])==Q(base['cl']),'leading_potential_equal_state131':C[0,0]==BC[0,0],
             'leading_density_equal_state131':G[0,0]==BG[0,0],
             'sector_scope':'q<=1, h<=7; q>=2 exponents are below -3.44; h>=8 below -3.02',
             'all_forbidden_exact_zero':all(not E[h,q] for h,q in E if alpha(h,q)>=-2),
             'first_surviving':next(row for row in rows if not row['exact_zero']),
             'sectors':rows,'elapsed_seconds':time.monotonic()-start}
        (ROOT/f'research/refit_audit/verification/{name}_sectors.json').write_text(json.dumps(out,indent=2)+'\n')
