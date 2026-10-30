from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,hashlib,argparse,importlib.util
from flint import fmpq as Q, fmpq_poly as P, arb, ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('polar_norm_helper',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(name,weights,bits):
    ctx.prec=bits;start=time.monotonic();src=ROOT/f'data/{name}.json'
    c,delta,rho,stream=m.fields(json.loads(src.read_text()));F={};Z=P([]);U=P([1,-1])
    def add(ell,n,V):
        if not n or not V:return
        if n<0:n,V=-n,-V
        F[ell,n]=F.get((ell,n),Z)+V
        if not F[ell,n]:del F[ell,n]
    for (j,n),R in rho.items():add(j+1,n,c*m.td(R,(j+1)*delta/2,1)-R)
    for (j,mm),S in stream.items():
        DS=m.td(S,(j+1)*delta/2,2)
        for (i,n),R in rho.items():
            DR=m.td(R,(i+1)*delta/2,1)
            add(i+j+2,n+mm,(n*R*DS-mm*S*DR)/2)
            add(i+j+2,n-mm,(-n*R*DS-mm*S*DR)/2)
    bymode={};components=[];leading={};qmin=None
    for (ell,n),V in F.items():
        V=V(U);v=next(k for k,x in enumerate(V) if x);power=ell*delta/2+v
        components.append((ell,n,v,V));bymode.setdefault(n,[]).append((ell,V))
        if qmin is None or power<qmin:qmin=power;leading={n:V[v]}
        elif power==qmin:leading[n]=leading.get(n,Q(0))+V[v]
    lead_energy=sum((x*x for x in leading.values()),Q(0));assert lead_energy>0
    groups={}
    for terms in bymode.values():
        for j,(ell,V) in enumerate(terms):
            for k in range(j,len(terms)):
                ell2,W=terms[k];power=(ell+ell2)*delta/2-3
                groups[power]=groups.get(power,Z)+(1 if j==k else 2)*U*V*W
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'source_sha256':sha(src),
         'code_sha256':sha(Path(__file__)),'helper_sha256':sha(helper),'proof_sha256':sha(ROOT/'PROOF.md'),
         'precision_bits':bits,'residual_components':len(F),'angular_modes':len(bymode),'square_power_groups':len(groups),
         'leading_q':str(qmin),'sharp_weight_membership_a_greater_than':str(2-2*qmin),
         'leading_angular_energy_over_pi':str(lead_energy),'weights':[]}
    print('built',name,'components',len(F),'modes',len(bymode),'q',qmin,'seconds',time.monotonic()-start,flush=True)
    for aa in weights:
        tick=time.monotonic();a=Q(aa)
        if a<=2-2*qmin:
            row={'a':str(a),'member':False,'reason':'nonzero exact leading angular sector'}
            print('a',a,'diverges',flush=True)
        else:
            assert all(a-3+ell*delta+2*v>-1 for ell,n,v,V in components)
            E=Q(0)
            for e,V in groups.items():
                for k,x in enumerate(V):
                    if x:
                        den=a+e+k+1;assert den>0;E+=x/den
            assert E>0
            norm=(arb.pi()/2*m.ar(E)).sqrt()
            row={'a':str(a),'member':True,'exact_energy_over_pi_half':str(E),'norm':norm.str(100),'elapsed_seconds':time.monotonic()-tick}
            print('a',a,'norm',norm.str(40),'seconds',row['elapsed_seconds'],flush=True)
        out['weights'].append(row);out['elapsed_seconds']=time.monotonic()-start
        (ROOT/f'verification/{name}_{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate',default='state131',nargs='?');p.add_argument('--a',nargs='+',default=['1','11/10','221/200','6/5','13/10','7/5','3/2']);p.add_argument('--bits',type=int,default=1024);a=p.parse_args();run(a.candidate,a.a,a.bits)
