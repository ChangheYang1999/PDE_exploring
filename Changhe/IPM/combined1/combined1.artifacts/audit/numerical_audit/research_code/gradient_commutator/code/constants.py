from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import mpmath as mp
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3]
start=time.monotonic();mp.mp.dps=60;ctx.prec=384

def integral(p):
    def f(v):
        if v==0:return mp.mpf(0)
        return 8*v**(2*p)/(1+v*v)**3*(mp.log1p(1/(v*v))-1/(1+v*v))
    return mp.quad(f,[0,mp.mpf(1)/8,mp.mpf(1)/2,1,2,8,mp.inf])
A=integral(1);B=integral(2)
exactA=mp.pi*(mp.log(2)-mp.mpf(1)/2);exactB=mp.pi*(3*mp.log(2)-2)
assert abs(A-exactA)<mp.mpf('1e-55') and abs(B-exactB)<mp.mpf('1e-55')
a=arb.pi()*(arb(2).log()-arb(1)/2);b=arb.pi()*(3*arb(2).log()-2)
k=((arb(2).log()-arb(1)/2)/(16*arb.pi())).sqrt()
old=((4*arb(2).log()-1)/(8*arb.pi())).sqrt()
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
     'proof_sha256':hashlib.sha256((ROOT/'research/gradient_commutator/PROOF.md').read_bytes()).hexdigest(),
     'A_arb':a.str(70),'B_arb':b.str(70),'new_uniform_constant':k.str(70),'T4_generic_constant':old.str(70),
     'constant_ratio':(old/k).str(50),'A_floating_quadrature':str(A),'B_floating_quadrature':str(B),
     'A_error':str(abs(A-exactA)),'B_error':str(abs(B-exactB)),
     'quadrature_status':'FLOAT sanity check, no rigorous integration error claimed',
     'elapsed_seconds':time.monotonic()-start}
(ROOT/'research/gradient_commutator/verification/constants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
