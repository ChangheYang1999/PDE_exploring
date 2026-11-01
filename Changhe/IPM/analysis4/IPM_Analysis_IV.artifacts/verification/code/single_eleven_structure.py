"""Exact common-potential reconstruction and necessary top-mode radius for sin11."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from high_harmonic_tuning import Chain,coefficient,L,Q,Poly,parse
from certified_initial_majorants import pack
ROOT=Path('research/228_single_eleven_structure')
def main():
    started=time.monotonic();chain=Chain(11);chain.initialize();f=chain.F[9];maxk=(f.M-1)//2;D={maxk+1:Q(0)}
    for k in range(maxk,0,-1):D[k]=(coefficient(f,2*k+1)-k*D[k+1])/(k+1)
    M=2*maxk;coeffs=[Q(0)]*(2*M+1)
    for k,v in D.items():
        if v:
            a=-v/(4*k*k);coeffs[M+2*k]+=a/2;coeffs[M-2*k]+=a/2
    pure=L(Q(0),M,[Poly(coeffs)]);pure_stream=pure.X().Y().scale(-1);beta=coefficient(pure_stream,2)
    assert beta==D[2]/8 and ((pure.X().X()-pure.Y().Y()).Y()-f).zero()
    original=Path('research/36_free_multipole_compatibility/verification/sin11_pure_chi.json');old=json.loads(original.read_text());assert beta==Q(old['pure_potential_beta_exact'])
    tuning=Path('research/197_high_harmonic_tuning/verification/sin11_block1.json');row=json.loads(tuning.read_text());H=Q(row['tuned_harmonic_exact']);lam=beta-H;assert lam>0
    target=chain.G[9]+parse(Q(-2),{'2':[str(H)]});potential=pure+L(Q(0),0,[Poly([Q(0)]),Poly([lam])])
    assert ((potential.X().X()-potential.Y().Y()).Y()-f).zero()
    assert (potential.X().Y().scale(-1)-target).zero()
    hs=[Q(0),Q(1)];eta=Q(104,9);d=Q(4,5);top=[]
    for n in range(2,10):
        h=sum(((24*(n-i)/(eta*i+2)-1)*hs[i]*hs[n-i] for i in range(1,n)),Q(0))/(4*d*(n-1));hs.append(h)
        assert h>0 and coefficient(chain.F[n],12*n-1)==(-1)**(n-1)*h
        top.append(dict(n=n,top_coefficient=str(coefficient(chain.F[n],12*n-1)),scalar=str(h)))
    ctx.prec=512;a=arb(9)/52;b=arb(99)/52;RH=arb(16)/5*((a*a.gamma()*b.gamma()/(a+b).gamma()).log()*arb(52)/9).exp();radius=(-RH.log()*arb(9)/4).exp()
    lower_integer=int((radius.lower()*10**12).floor().unique_fmpz());assert arb(lower_integer)/10**12<radius
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,bits=512,
        beta_pure_exact=str(beta),H9_exact=str(H),lambda_exact=str(lam),lambda_positive=True,
        exact_full_density_reconstruction=True,exact_full_stream_reconstruction=True,top_checks=top,
        R_H=RH.str(60,radius=True),R_H_ball=pack(RH),necessary_radius=radius.str(60,radius=True),necessary_radius_ball=pack(radius),
        safe_decimal_lower_bound=f'{lower_integer//10**12}.{lower_integer%10**12:012d}',
        sources=[dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest()) for p in [original,tuning]],actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['single_eleven_structure.py','high_harmonic_tuning.py','laurent_log_audit.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k not in ['top_checks','lambda_exact','H9_exact','beta_pure_exact','R_H_ball','necessary_radius_ball']}),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(json.dumps(failure),flush=True);raise SystemExit(1)
