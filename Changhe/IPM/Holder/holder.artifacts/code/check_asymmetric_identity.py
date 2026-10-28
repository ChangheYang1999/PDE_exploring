"""Independent analytic constant evaluation and a diagnostic of the Holder lemma.
The random-pair checks are diagnostics only; the proof is in the topic PROOF.md.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import numpy as np
from flint import arb, ctx
ctx.prec = 192
pi = arb.pi()
base = arb(1)/2 + (arb(2).log()-1)/pi
gap = 2/pi*(pi/4).cosh().log()
t = (pi/4).tanh()/2
A = arb(1)/2+t
B = 1-A
entropy = -A*A.log()-B*B.log()
residual = 2/pi*(entropy-arb(2).log())+t-gap
rng = np.random.default_rng(28411)
xs = np.r_[0.0, rng.uniform(-3,3,1200), np.sign(rng.normal(size=500))*10.0**rng.uniform(-15,1,500)]
reports=[]
for alpha in [.001,.01,.1,.5,.9,.99]:
 a=float(A.mid()); b=1-a; p=1/(1-alpha)
 m=np.exp(-np.logaddexp(p*np.log(a),p*np.log(b))/p)
 val=m*(a*np.maximum(xs,0)**alpha-b*np.maximum(-xs,0)**alpha)
 i=rng.integers(0,len(xs),200000); j=rng.integers(0,len(xs),200000)
 ok=i!=j
 ratios=np.abs(val[i[ok]]-val[j[ok]])/np.abs(xs[i[ok]]-xs[j[ok]])**alpha
 # The exact equality case for opposite-sign inputs has s/t=(A/B)^p.
 logratio=p*np.log(a/b)
 r=np.exp(-logratio)
 exact_pair_ratio=m*(a+b*r**alpha)/(1+r)**alpha
 reports.append(dict(alpha=alpha,max_random_ratio=float(ratios.max()),equality_pair_ratio=float(exact_pair_ratio)))
out=dict(time_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), precision_bits=ctx.prec,
         C0=base.str(45), extra_gap=gap.str(45), D0_lower=(base+gap).str(45),
         A=A.str(45), B=B.str(45), pole_magnitude=t.str(45), optimization_identity_residual=residual.str(8),
         diagnostic_random_pairs=reports)
Path('data/asymmetric_identity_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
