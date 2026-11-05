#!/usr/bin/env python3
"""Coarsen the completed independent join to simple exact rational constants."""
import hashlib,json
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):
    x=F(x);return arb(x.numerator)/arb(x.denominator)
def main():
    ctx.prec=512
    p=HERE/'ROOT_FINAL_LOCAL_Q_REPLAY.json';d=json.loads(p.read_text())
    assert d['status']=='ROOT_INDEPENDENT_FINAL_LOCAL_Q_NUMERICAL_PASS'
    assert d['program_sha256']==sha(HERE/'verify_final_local_Q_closure.py')
    assert d['consumer_result_sha256']==sha(HERE/d['consumer_result_path'])
    R=F(381377,10**12);M=F(3,10);beta2=F(2087491,10**6)
    beta=F(7,10);epsilon=F(3491,31250);C=F(28427625600);L=F(57,250);n=F(759,100000);f2=F(7961207,10**13)
    assert arb(d['values']['background_epsilon'])<aa(epsilon)
    assert arb(d['values']['background_weak_C'])<aa(C)
    assert arb(d['values']['nonlinear_loss'])<aa(L)
    b0=beta-epsilon;bprime=b0-L
    assert b0==F(9192,15625) and bprime==F(11259,31250)
    radius_margin=R*beta2-f2
    margin=bprime*M*M-n*M-C*R*R
    assert radius_margin>0 and margin>F(260141,10**7)
    pi_lower=F(157,50);contraction=F(123,1000)
    assert arb.pi()>aa(pi_lower)
    assert 25*M*M/(11*pi_lower*beta2*beta2)<contraction*contraction
    norm_path=HERE/'Q_to_inherited_N_at_M03.json';norm=json.loads(norm_path.read_text())
    assert norm['R']==str(R) and norm['auxiliary_M']==str(M) and norm['auxiliary_weight_slope']=='2'
    assert arb(norm['inherited_N2_upper'])<aa(F(355363,10**6))
    out={'status':'EXACT_RATIONAL_FIXED_PARAMETER_BALL_PASS',
         'finished_utc':datetime.now(timezone.utc).isoformat(),'program_sha256':sha(Path(__file__)),
         'input_sha256':{str(q.relative_to(HERE)):sha(q) for q in [p,norm_path]},
         'R':str(R),'M':str(M),'beta_L2':str(beta2),'forcing_L2':str(f2),'forcing_Q':str(n),
         'matrix_beta':str(beta),'background_epsilon':str(epsilon),'background_C':str(C),
         'background_strong_decay':str(b0),'nonlinear_loss_upper':str(L),'frozen_strong_decay':str(bprime),
         'exact_L2_radius_margin':str(radius_margin),'exact_selfmap_margin':str(margin),
         'selfmap_margin_arb':aa(margin).str(100),'contraction_upper':str(contraction),
         'inherited_N_upper':'355363/1000000',
         'scope':'Exact rational strict ball inequalities after the independently verified analytic/numerical rate bounds. The PDE proof and source certificates remain explicit dependencies.'}
    (HERE/'RATIONAL_FINAL_BALL.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
