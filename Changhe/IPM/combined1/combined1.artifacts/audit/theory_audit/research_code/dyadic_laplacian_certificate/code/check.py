from pathlib import Path
from datetime import datetime,timezone
import json,sys,hashlib,time,importlib.util
from flint import fmpq as Q, fmpq_poly as P, arb, ctx
sys.set_int_max_str_digits(0);ctx.prec=1024
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('lap_polar',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.monotonic();src=ROOT/'data/state131.json'
c,delta,rho,stream=m.fields(json.loads(src.read_text()));F={};Z=P([]);U=P([1,-1])
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
coeff={}
for (ell,n),V in F.items():
    d=ell*delta/2;K=(m.td(m.td(V,d,1),d,1)-n*n*V)(U)
    for k,x in enumerate(K):
        if not x:continue
        e=d-delta+k;assert e>=0
        row=coeff.setdefault(e,{})
        row[n]=row.get(n,Q(0))+x
coeff={e:{n:x for n,x in row.items() if x} for e,row in coeff.items()}
coeff={e:row for e,row in coeff.items() if row}
energies={e:sum((x*x for x in row.values()),Q(0)) for e,row in coeff.items()}
A=m.ar;pi=arb.pi();D=(pi*A(energies[Q(0)])).sqrt();norms={e:(pi*A(E)).sqrt() for e,E in energies.items() if e>0}
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(src),'code_sha256':sha(__file__),'helper_sha256':sha(helper),'proof_sha256':sha(ROOT/'PROOF.md'),'precision_bits':ctx.prec,'c':str(c),'delta':str(delta),'b':str(1-2*delta),'coefficient_groups':len(coeff),'residual_components':len(F),'angular_squared_norms_over_pi':{str(e):str(E) for e,E in sorted(energies.items())},'leading_laplacian_norm':D.str(90),'tail_tests':[]}
for j in range(10,21):
    z=Q(1,1+2**(2*j));t=1-z
    rem=(1-A(t)**A(delta))*D+sum((A(z)**A(e)*v for e,v in norms.items()),arb(0))
    ratio=rem/D
    out['tail_tests'].append({'J':j,'R0':str(2**j),'z0':str(z),'relative_remainder_upper':ratio.str(90),'below_half':bool(ratio<arb(1)/2),'below_quarter':bool(ratio<arb(1)/4)})
    print('J',j,'relative full remainder',ratio.str(30),flush=True)
out['elapsed_seconds']=time.monotonic()-start
(ROOT/'verification/tail_results.json').write_text(json.dumps(out,indent=2)+'\n')
print('groups',len(coeff),'D',D.str(40),'elapsed',out['elapsed_seconds'],flush=True)
