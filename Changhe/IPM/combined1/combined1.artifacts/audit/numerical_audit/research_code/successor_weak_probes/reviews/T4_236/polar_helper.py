"""Independent polar weak pairing; exact coefficients and gamma-free beta moments."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from functools import lru_cache
import importlib.util,json,sys,time,argparse
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
BASE=Path(__file__).resolve().parents[1]
helper=BASE.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('t4_polar_weak',helper)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
T,W,ZERO=m.T,m.U,m.ZERO
fields,td,ar,square_groups=m.fields,m.td,m.ar,m.square_groups
sys.set_int_max_str_digits(0)
def sha(p):return sha256(p.read_bytes()).hexdigest()
@lru_cache(None)
def beta0(b,M):
    b=Q(b);assert b>-1 and M>=0
    v=ar(1/(b+1))
    for j in range(1,M+1):v*=ar(Q(j)/(b+j+1))
    return v

def integral(Pt,b,M):
    Pu=Pt(W);v=beta0(str(b),M);out=arb(0)
    for j,p in enumerate(Pu):
        out+=ar(p)*v
        v*=ar((b+j+1)/(b+j+M+2))
    return out

def supremum(a,b):
    return ar(Q(a,a+b))**a*ar(Q(b,a+b))**b if a else arb(1)

def run(name,ks,bits):
    ctx.prec=bits;start=time.monotonic();src=BASE/f'data/{name}_canonical.json'
    c,delta,rho,stream=fields(json.loads(src.read_text()))
    bg,bpairs=square_groups(stream,delta,2);cg,cpairs=square_groups(rho,delta,1)
    target=BASE/f'source/N4_{name}.json';peer=json.loads(target.read_text());refs={r['k']:r for r in peer['probes']}
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'precision_bits':bits,
         'code_sha256':sha(Path(__file__)),'helper_sha256':sha(helper),'proof_sha256':sha(BASE/'PROOF.md'),
         'canonical_sha256':sha(src),'peer_sha256':sha(target),'method':'polar fields, weak background pairing, gamma-free beta products','rows':[]}
    print('prepared',name,'rho',len(rho),'psi',len(stream),'seconds',time.monotonic()-start,flush=True)
    for k in ks:
        st=time.monotonic();lk=(3*c+1)+2*c*k*W-4*c*T;gk=1+2*k*W+4*T;hk=1+2*k*W-4*T
        linear=-arb.pi()/2*sum((integral(rr*lk,(j+1)*delta/2-1,k+1) for (j,n),rr in rho.items() if n==1),arb(0))
        ng={}
        for (j,mn),ss in stream.items():
            ds=td(ss,(j+1)*delta/2,2)
            for (i,n),rr in rho.items():
                if abs(n-mn)!=1:continue
                sig=1 if n>mn else -1
                ng[j+i]=ng.get(j+i,ZERO)+rr*(sig*mn*ss*hk-ds)
        nonlinear=arb.pi()/4*sum((integral(v,(j+2)*delta/2-1,k+1) for j,v in ng.items()),arb(0))
        pair=linear+nonlinear
        b2=arb.pi()/2*sum((integral(v*gk*gk,1+(j+2)*delta/2,2*k+1) for j,v in bg.items()),arb(0))
        c2=arb.pi()/2*sum((integral(v,1+(j+2)*delta/2,2*k+1) for j,v in cg.items()),arb(0))
        a2=arb.pi()/2*integral(lk*lk,Q(1),2*k+1)
        assert a2>0 and b2>0 and c2>0 and abs(pair)>0
        A,B,C=[x.sqrt() for x in (a2,b2,c2)];D=A+B+C
        H=arb(1) if k==0 else supremum(k,2)+2*k*supremum(k,3)+4*supremum(k+1,2)
        I=abs(pair);radius=2*I/(D+(D*D+4*H*I).sqrt())
        vals={'pairing':pair,'A':A,'B_weighted':B,'C':C,'D':D,'gradient_sup_upper_ball':H,'L2_radius_lower':radius}
        comparison={key:value.overlaps(arb(refs[k][key])) for key,value in vals.items()}
        assert all(comparison.values()),(k,comparison,{key:value.str(10) for key,value in vals.items()})
        row={'k':k,**{key:value.str(95) for key,value in vals.items()},'linear_pairing':linear.str(95),
             'nonlinear_pairing':nonlinear.str(95),'comparisons':comparison,'elapsed_seconds':time.monotonic()-st}
        out['rows'].append(row);out['elapsed_seconds']=time.monotonic()-start
        (BASE/f'verification/{name}_{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
        print('k',k,'radius',radius.str(28),'all7overlap',all(comparison.values()),'seconds',time.monotonic()-st,flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--k',type=int,nargs='+',required=True);p.add_argument('--bits',type=int,default=2048)
    a=p.parse_args();run(a.candidate,a.k,a.bits)
