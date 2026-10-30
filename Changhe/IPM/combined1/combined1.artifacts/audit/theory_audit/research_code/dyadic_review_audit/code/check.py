from pathlib import Path
from datetime import datetime,timezone
import json,sys,hashlib,time,importlib.util
from flint import fmpq as Q, fmpq_poly as P, arb, ctx
sys.set_int_max_str_digits(0)
ctx.prec=1024
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('dyadic_polar',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.monotonic()
src=ROOT.parent/'weighted_full_residual/data/state131.json'
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
leading={};small=None
for (ell,n),V in F.items():
    Qz=V(U);v=next(k for k,x in enumerate(Qz) if x);e=ell*delta/2+v
    if small is None or e<small:small=e;leading={n:Qz[v]}
    elif e==small:leading[n]=leading.get(n,Q(0))+Qz[v]
leading={n:x for n,x in leading.items() if x}
ff=json.loads((ROOT/'source/state131_farfield.json').read_text());entry=ff['residual_sectors_E']['1,0']
target={int(n):Q(v['exact']) for n,v in entry['series'].items() if Q(v['exact'])}
assert leading==target
b=1-2*small;assert b==Q(entry['exponent'])==2/c-1
E=sum((x*x for x in leading.values()),Q(0));D=sum((((b*b-n*n)*x)**2 for n,x in leading.items()),Q(0))
A=m.ar;pi=arb.pi();a=Q(221,200);beta=Q(2181481,10**8);CU=2/(2-a);Ylow=Q(25963000000)
Rchosen=(8*pi).sqrt()*A(beta/(CU+a));Mchosen=Rchosen/A(Ylow)
betamax=1+c-c*a;Runiv=(8*pi).sqrt()*A(betamax/(1+a));Muniv=Runiv/A(Ylow)
# Safe upper endpoints, not nearest-decimal formatting.
assert Mchosen<A(Q(12613,10**16))
assert Muniv<A(Q(74294,10**15))
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'source_sha256':sha(src),'code_sha256':sha(__file__),'helper_sha256':sha(helper),'proof_sha256':sha(ROOT/'PROOF.md'),'review_sha256':sha(ROOT/'source/T2_REVIEW_T4_058.md'),'leading_exponent':str(b),'exact_leading_coefficients_compared':len(leading),'leading_norm':(pi*A(E)).sqrt().str(90),'leading_laplacian_norm':(pi*A(D)).sqrt().str(90),'chosen_beta':str(beta),'chosen_CU':str(CU),'chosen_rate_R_ceiling':Rchosen.str(90),'chosen_rate_M_ceiling':Mchosen.str(90),'universal_beta_ceiling':str(betamax),'universal_R_ceiling':Runiv.str(90),'universal_M_ceiling':Muniv.str(90),'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n')
for k,v in out.items():print(k,v)
