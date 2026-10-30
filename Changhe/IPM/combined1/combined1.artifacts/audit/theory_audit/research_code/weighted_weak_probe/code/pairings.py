"""Independent weak-equation pairings for a finite polar background."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, importlib.util, json, hashlib, time
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'localized_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('local_pairing_helper',helper)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(name,ks,bits):
    ctx.prec=bits;start=time.monotonic();src=ROOT/f'data/{name}_canonical.json'
    c,delta,rho,stream=m.fields(json.loads(src.read_text()));T,W,Z=m.T,m.W,m.ZERO
    n0={};n1={}
    for (j,mode),ss in stream.items():
        ds=m.td(ss,(j+1)*delta/2,2)
        for (i,n),rr in rho.items():
            if abs(n-mode)!=1:continue
            sign=1 if n>mode else -1
            n0[j+i]=n0.get(j+i,Z)+rr*(sign*mode*ss*(1-4*T)-ds)
            n1[j+i]=n1.get(j+i,Z)+2*sign*mode*rr*ss*W
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,
         'canonical_sha256':sha(src),'precision_bits':bits,'code_sha256':sha(Path(__file__)),
         'helper_sha256':sha(helper),'proof_sha256':sha(ROOT/'PROOF.md'),
         'method':'polar weak background equation; exact polynomial interactions; outward beta recurrences',
         'scope':'pairings only; no unweighted residual or correction membership asserted','rows':[]}
    print('prepared',name,'seconds',time.monotonic()-start,flush=True)
    for k in ks:
        tick=time.monotonic();lk=3*c+1+2*c*k*W-4*c*T
        lin=-arb.pi()/2*sum((m.integral(rr*lk,(j+1)*delta/2-1,k+1)
                            for (j,n),rr in rho.items() if n==1),arb(0))
        nonlin=arb.pi()/4*sum((m.integral(v+k*n1[j],(j+2)*delta/2-1,k+1)
                              for j,v in n0.items()),arb(0))
        value=lin+nonlin
        out['rows'].append({'k':k,'pairing':value.str(100),
                            'linear_pairing':lin.str(100),'nonlinear_pairing':nonlin.str(100),
                            'elapsed_seconds':time.monotonic()-tick})
        out['elapsed_seconds']=time.monotonic()-start
        (ROOT/f'data/{name}_pairings.json').write_text(json.dumps(out,indent=2)+'\n')
        print('k',k,'pairing',value.str(32),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--k',type=int,nargs='+',required=True)
    p.add_argument('--bits',type=int,default=2048);a=p.parse_args();run(a.candidate,a.k,a.bits)
