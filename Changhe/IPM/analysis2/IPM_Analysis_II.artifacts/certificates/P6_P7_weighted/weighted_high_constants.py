from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
import json, sys
from flint import arb, ctx
ctx.prec = 384
HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
sys.path.insert(0, str(BASE/'02_energy/verification'))
from compact_matrix import A
D, Z = 8256, 16512
C3 = D*256 + 3*35 + 2*2**14 + 3*77*256 + 6*2**14*256 + 2*2**84*2048
assert C3 < 2**97 and Z < 2**15
assert 2**194 + 2**15 < 2**195
assert Q(2**195,20) - 2**195 >= -Q(3,2)*2**195
th, sig = Q(1,62), Q(1,5)
al = th/2
assert (1-th)/20-Q(3,2)*th == Q(1,40)
assert sig+th < Q(1,4)
cgrad = 1/(2*(arb.pi()*A(th)*(1+A(th))).sqrt())
chold = 2**(-A(al))/arb.pi().sqrt()*((2+A(al)).gamma()*(A(th)-A(al)).gamma()/(2+A(th)).gamma()).sqrt()
assert cgrad < 4 and chold < 9
# Smoothstep derivative bounds, radial to Cartesian tensor conversion.
assert Q(35,16) < 3
assert Q(420,16) < 27
assert 4*3 < 16 and 16*27 < 512 and 64*210 < 16384
assert 512+16*4 < 1024
assert 16384+2*(512*4+16*16) < 32768
# Bessel H^k cutoff multiplication, bounding sqrt(2),sqrt(3) by 2.
c0, c1, c2, c3 = 1, 16, 1024, 32768
H3coeff = [c0+2*c1+2*c2+c3, 2*c0+4*c1+3*c2, 2*c0+3*c1, c0]
H2coeff = [c0+2*c1+c2, 2*c0+2*c1, c0]
assert sum(H3coeff) < 2**16 and sum(H2coeff) < 2**16
assert arb(17)**A(Q(3,5)) < 6
assert arb(17)**A(Q(1,10)) < 2
assert arb(4)**A(Q(2,5)) < 2
assert 6*2**16 < 2**24
localgrad, localhold = 4*2**24, 9*2**24
# Nearby annuli and the central disk give the localhold constant. Far pairs
# satisfy d >= max(1,|X|,|Y|)/4 and use twice the gradient bound.
assert localhold < 2**30
assert 2*localgrad*arb(4)**A(al) < 2**30
# Density infinity + rescaled Holder seminorm: use sup <=1 and grad <=4.
assert 2**24 * (1+8) < 2**28
assert 2*2**28 < 2**30
p, kap = 256, 260
gap = p*(1+al)+2-kap
assert gap == Q(2,31)
cmom = (2*arb.pi()/A(gap))**(arb(1)/p)*A(Q(2**30,1))/(1+A(al))
assert cmom < 2**31
cc = A(Q(localgrad,4)) + 4*A(Q(2**30,1))/(arb.pi()*A(al)*(1+A(al))) + 2**A((1+sig)/2)/(2*arb.pi()*(1-A(sig))).sqrt()
assert cc < 2**39
assert 1+2**30+2**31+2**39 < 2**40
assert 40*2**40 < 2**46
out = {
    'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'theta': str(th), 'alpha': str(al), 'density_growth_bound': str(sig+th),
    'E3_E2_coefficient': str(2**195), 'E3_growth': '3/2',
    'interpolated_decay': '1/40', 'inverse': 40,
    'third_derivative_cross_coefficient': str(C3),
    'cutoff_H3_coefficient_bounds': H3coeff,
    'cutoff_rescaling_bound': str(2**24),
    'local_Sobolev_gradient_constant': cgrad.str(60),
    'local_Sobolev_gradient_holder_constant': chold.str(60),
    'gradient_bound': str(localgrad), 'gradient_holder_bound': str(2**30),
    'moment_p': p, 'moment_kappa': kap, 'moment_gap': str(gap),
    'moment_bound_before_rounding': cmom.str(60),
    'strain_bound_before_rounding': cc.str(60),
    'combined_inverse_bound': str(2**46),
    'arithmetic': 'all rational and Arb inequalities pass',
    'scope': 'Exact checkpoint131; relies on V036 and V037 complete continuum certificates. Linear theorem only.'
}
(HERE/'weighted_high_constants.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
