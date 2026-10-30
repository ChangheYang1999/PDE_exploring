from pathlib import Path
from datetime import datetime,timezone
import json,sys,hashlib,time,importlib.util,argparse
from flint import fmpq as Q, fmpq_poly as P, arb, ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('weighted_lap_polar',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(name,weights,bits):
    start=time.monotonic();ctx.prec=bits;src=ROOT/f'data/{name}.json'
    c,delta,rho,stream=m.fields(json.loads(src.read_text()));F={};Z=P([]);U=P([1,-1]);t=P([0,1])
    def add(ell,n,V):
        if not n or not V:return
        if n<0:n,V=-n,-V
        F[ell,n]=F.get((ell,n),Z)+V
        if not F[ell,n]:del F[ell,n]
    for (j,n),R in rho.items():add(j+1,n,c*m.td(R,(j+1)*delta/2,1)-R)
    for (j,k),S in stream.items():
        DS=m.td(S,(j+1)*delta/2,2)
        for (i,n),R in rho.items():
            DR=m.td(R,(i+1)*delta/2,1)
            add(i+j+2,n+k,(n*R*DS-k*S*DR)/2)
            add(i+j+2,n-k,(-n*R*DS-k*S*DR)/2)
    print('built residual',name,len(F),'elapsed',time.monotonic()-start,flush=True)
    bymode={};components=[]
    for (ell,n),V in F.items():
        d=ell*delta/2;K=m.td(m.td(V,d,1),d,1)-n*n*V
        L,rem=divmod(K,t);assert not rem
        L=L(U)
        if not L:continue
        v=next(k for k,x in enumerate(L) if x)
        components.append((ell,n,v));bymode.setdefault(n,[]).append((ell,L))
    groups={}
    for terms in bymode.values():
        for j,(ell,V) in enumerate(terms):
            for k in range(j,len(terms)):
                ell2,W=terms[k];e=(ell+ell2)*delta/2-3
                groups[e]=groups.get(e,Z)+(1 if j==k else 2)*U*V*W
    monomials=[(e+k+1,x) for e,V in groups.items() for k,x in enumerate(V) if x]
    print('square groups',len(groups),'nonzero monomials',len(monomials),'elapsed',time.monotonic()-start,flush=True)
    A=m.ar;terms=[(e,A(x)) for e,x in monomials]
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'c':str(c),'source_sha256':sha(src),'code_sha256':sha(__file__),'helper_sha256':sha(helper),'proof_sha256':sha(ROOT/'PROOF.md'),'precision_bits':bits,'residual_components':len(F),'square_power_groups':len(groups),'nonzero_monomials':len(monomials),'weights':[]}
    for aa in weights:
        a=Q(aa);tick=time.monotonic();assert all(a+ell*delta+2*v-2>0 for ell,n,v in components)
        assert all(a+e>0 for e,x in monomials)
        E=sum((x/A(a+e) for e,x in terms),arb(0));assert E>0
        norm=(arb.pi()*E/2).sqrt();lower=arb(5)**A((a-2)/2)*norm
        beta=1+c-c*a;ceiling=(8*arb.pi()).sqrt()*A(beta*beta/(1+a)) if beta>0 else arb(0)
        row={'a':str(a),'weighted_laplacian_norm':norm.str(90),'Y_lower_bound':lower.str(90),'necessary_residual_ceiling':ceiling.str(90),'ratio':(lower/ceiling).str(90) if beta>0 else None,'elapsed_seconds':time.monotonic()-tick}
        out['weights'].append(row);out['elapsed_seconds']=time.monotonic()-start
        (ROOT/f'verification/{name}_{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
        print('a',a,'weighted lap',norm.str(30),'Y_lower',lower.str(30),'ceiling',ceiling.str(20),'elapsed',time.monotonic()-start,flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--a',nargs='+',default=['0','1/4','1/2','3/4','1','5/4','3/2']);p.add_argument('--bits',type=int,default=2048);args=p.parse_args();run(args.candidate,args.a,args.bits)
