"""Exact and Arb checks for the three-component L2 closure. No sampling."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, itertools
from flint import arb, ctx
ctx.prec = 256
ROOT=Path(__file__).resolve().parents[1]
def A(x):
    x=Q(x)
    return arb(x.numerator)/x.denominator
G=[[Q(1,4),Q(-347,10),Q(-5)],
   [Q(-347,10),Q(53048,5),Q(-49152)],
   [Q(-5),Q(-49152),Q(458752)]]
def det(M):
    ans=Q(0)
    for p in itertools.permutations(range(len(M))):
        sign=(-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        term=Q(sign)
        for i,j in enumerate(p):term*=M[i][j]
        ans+=term
    return ans
minors=[det([row[:n] for row in G[:n]]) for n in [1,2,3]]
assert all(m>0 for m in minors)
s=Q(1,2**17); r=Q(1,2**14); eta=Q(1,163840)
S=A(s);R=A(r)
beta=A(Q(1,4))-4800*S-5*R/S.sqrt()
c_s=1/(2*(arb.pi()*S*(1+S)).sqrt())
d=c_s*R; ratio=d/2
assert beta>A(Q(1,10))
assert A(eta)/beta<R
assert d<A(Q(3117,500000)) and ratio<A(Q(39,12500))
rows=[Q(19053,4),Q(17925,4),Q(4086)]
assert max(rows)<4800
As=Q(127,50)+Q(653,5)*Q(1,1024)
Bs=Q(9,5)*(1+Q(44,1024))
assert As+Bs<5
# Reconstruct HS from the independently reproduced exact rational integrals.
p=ROOT.parent/'background_norm_reproduction/verification/reproduction.json'
z=json.loads(p.read_text())
# Discover the named result mapping without embedding large fractions into output.
mapping=next(v for v in z.values() if isinstance(v,dict) and 'D_rho_x' in v)
qx=Q(mapping['D_rho_x']['rational_energy_over_pi_half'])
qy=Q(mapping['D_rho_y']['rational_energy_over_pi_half'])
# The energy convention is ||field||^2=(pi/2)*rational.
log2=arb(2).log()
kappa=(((log2-A(Q(1,2)))*A(qx)+(3*log2-2)*A(qy))/32).sqrt()
c=Q(4076476460239181,2251799813685248)
low=A(c)+1-A(Q(1,20))-kappa
assert low>2
result={
 'date_utc':datetime.now(timezone.utc).isoformat(),
 'precision_bits':ctx.prec,
 'gram_matrix':[[str(v) for v in row] for row in G],
 'positive_leading_minors':[str(x) for x in minors],
 'commutator_symmetric_row_sums':[str(x) for x in rows],
 'rough_As_plus_Bs_at_maximum_s':str(As+Bs),
 's':str(s),'r':str(r),'forcing_threshold':str(eta),
 'high_decay_beta':str(beta), 'selfmap_radius_upper':str(A(eta)/beta),
 'gradient_bound':str(d),'L2_contraction_ratio':str(ratio),
 'state131_gradient_HS':str(kappa),'state131_low_decay_lower':str(low),
 'background_exact_energy_file':str(p.relative_to(ROOT.parent.parent)),
 'background_exact_energy_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'scope':'Exact Gram calculation and Arb256 strict comparisons. Conditional closure requires all analytic hypotheses and a certified actual residual bound. No candidate existence is asserted.'}
out=ROOT/'verification/box.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
