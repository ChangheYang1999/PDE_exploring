# Interval, tail-decomposition and radial-section audit

Status: exact algebraic repairs are confirmed below; the specified code
snapshot still has defects. No new numerical margin, singular value or
off-basis norm is certified by this audit. File hashes are recorded in
`evidence/check.json`. The files were copied between02:34Z and02:39Z on
2026-10-28; the recorded hashes, rather than a mutable upstream filename,
define the audited objects.

## The spatial L2 norm and its angular Gram matrix are correct

For h=x squared y sum_m b_m(t) cos(2m theta), t=log r, the area element is
r squared dt dtheta and x squared y=r cubed cos squared(theta)sin(theta).
Thus

 ||h|| squared = integral exp(8t+mu(t))
     |sum_m b_m(t) Phi_m(theta)| squared dt dtheta,
 Phi_m=cos squared(theta)sin(theta)cos(2m theta).

The exact identity

 cos^4(theta)sin squared(theta)
    =(1+(1/2)cos(2theta)-cos(4theta)-(1/2)cos(6theta))/16

gives I_d=(1/pi) integral cos^4(theta)sin squared(theta)cos(2d theta)dtheta,
with I_0=1/8,I_{+-1}=1/32,I_{+-2}=-1/16,I_{+-3}=-1/32 and all others0.
Consequently the angular Gram entries divided by pi are

 (I_{m-m'}+I_{m+m'})/2.

These are exactly `angular_matrix` in `section_l2.py`. An independent
finite sine expansion of Phi_m verifies every entry for0<=m,m'<8 in exact
rationals. For a forcing g=r cubed sum_N G_N(t)sin((2N+1)theta), angular
orthogonality gives pi sum_N integral G_N squared exp(8t+mu(t))dt. Thus
the factors of pi in the rows and the test Gram are consistent.

`mu_at` integrates the specified slopes continuously, including at knots.
Independent rational integration checks negative t, zero, every type of
boundary and interior point, and the far linear region. `mu_prime_values_on`
includes both adjacent slopes at a knot. Its midpoint/radius construction
is exact here because every endpoint and half-difference is a small dyadic
rational. The knot-hull rule is valid for the direct Lipschitz theorem of
proof 28, whether or not the margin cells are split at each knot.

The spatial L2 assembly splits middle trial cells at the weight knots and
puts later knots among the outer cell boundaries. Coarse and test spline
pieces are re-expanded at the actual new cell left endpoint, so their
polynomial definitions remain unchanged. The background middle-cell
polynomials are likewise shifted by `sub_lo`. The partial Green formulas
in `BackgroundL2` are the variation-of-constants formulas for A'+2n A=
exp(4t)fhat and B'-2n B=-exp(4t)fhat. For middle cells fhat is a polynomial,
so the factor exp(4t_a) in the new A boundary and exp(4t_b) in the new B
boundary is correct. These structural checks do not replace a numerical
recomputation of the assembled entries.

The fixed-operator class uses plain B, no strain term, and no cM addition.
Its inherited unit far images are linear in A and B and do not themselves
include a strain term. Thus that reuse is algebraically consistent.
The J column is an ordinary spatial-L2 column in this section. All selected
columns and their fixed-operator images have the stated near and far
integrability. No KP or TAU tail belongs to this L2 realization.

A production certificate must use all integration cells. The optional
`cells_limit` path only sums a subset and therefore cannot certify the
full spatial norm. Coverage and hashes must be checked in an actual run.

## Margin code: interval multiplication is not interval squaring

The snapshot computes

 gr=(rr*rr+rt*rt).sqrt().

In the installed python-flint binding, with rr=rt=arb(0,1), multiplication
does not correlate the two occurrences of a ball. Each product contains
negative values, and the displayed square root is NaN. The independent
check reproduces this. `rr**2` also gives NaN for that ball in this binding,
so replacing multiplication by that expression is not a repair.

The issue occurs whenever both derivative enclosures straddle zero with
sufficient width. Boxes meeting an axis where both derivatives vanish
are particularly relevant. A rigorous upper bound needs only

 R=arb(rr.abs_upper()), T=arb(rt.abs_upper()),
 gr_up=sqrt(R*R+T*T).

Here R and T are the exact nonnegative upper endpoints of the absolute
value enclosures. This gives an upper bound for the true gradient norm;
using the lower endpoint of dy then bounds b_+=(|grad rho|-dy)/2 above,
which is sufficient for the lower margin. A full interval-square routine
could instead use the exact absolute lower and upper endpoints. Every
nonfinite intermediate or output must fail the certificate.

The radial `range_on_cell` argument itself is valid: on a finite cell,
|f(t)-f(mid)|<=sup|f'|h/2; on a half-line the exponent0 constant is separated
and the remaining terms are bounded symmetrically. `sup_bound` bounds each
monomial exponential by its explicit maximum. For example on a decaying
half-line, max_{u>=0}u^a exp(-lambda u)=(a/lambda)^a exp(-a), with the
constant case handled separately. All these expressions are computed
with Arb. The small multiplicative inflation of the converted radius
is adequate under finite ordinary round-to-nearest arithmetic: the
actual binary factor1+1e-15 is1+10u, u=2^-53, and two relative rounding
errors cannot exhaust that allowance. The positive1e-300 floor covers
subnormal-sized radial radii. Angular widths are ordinary positive
numbers and use the same multiplicative allowance. This observation
does not justify the uninflated final endpoint conversions below.

A uniform bound on a half-line does not by itself prove that the gradient
tends to zero there. The latter follows by separately checking that all
nonzero gradient exponential terms have strictly decaying exponents,
with any polynomial factor attached to them. Those exact exponent signs
and the absence of a constant term must be recorded when applying proof 28.

## Final endpoint conversions are not directed

For the exact positive number v=1+2^-54, `float(v.upper())` is1, strictly
below v. For a lower endpoint one can take1-2^-55, whose nearest float is1,
strictly above it. Thus the snapshot's stored `M_lo`, `BP_up`, `GR_up`,
`DU_up` and analogous range arrays need directed conversions if the JSON
or NPZ numbers themselves are to be certified bounds.

For a finite exact endpoint z, one safe scalar conversion is

 upper: nextafter(float(z),+infinity),
 lower: nextafter(float(z),-infinity).

The adjacent floating number beyond the nearest one brackets the exact
endpoint, including subnormal values. Infinite and NaN cases need explicit
handling; NaN is never a certified bound. Keeping exact dyadic endpoints
instead avoids a floating conversion entirely.

This defect does not imply that an actual large positive margin would
change sign. It does prevent the unqualified reporting of the nearest
floating endpoint as its exact certified lower bound. A smaller outward
rounded rational constant could still be certified after checking the
underlying balls.

## Off-basis code: the row maximum and tiny-positive branch remain wrong

The new t_of retains an Arb endpoint before taking the square root, which
repairs the earlier ordinary rounding example in V027. But its test
`float(v.upper())>0` discards a strictly positive endpoint such as2^-1200:
the nearest float is0 and t_of returns0. The branch must compare exact
endpoints, not their potentially underflowed floats.

More seriously, the maximum row sum is selected by comparing nearest
floats and retaining an entire row ball. For the exact diagonal matrix

 E=diag(1/2,1/2+2^-55),

both floating row endpoints are1/2. The strict comparison retains the
first, smaller row. Consequently nEb need not bound the infinity norm.
This can underestimate the quantitative factor1/sqrt(1-||E||). Arb's
maximum operation, or a maximum of exact upper endpoints, repairs this.
The final bound and per-column bounds still require directed conversion.

The separate positive-definiteness helper uses Arb.max in this installed
binding. Its strict boolean check `float(upper)<1` is safe: nearest rounding
of a number>=1 cannot produce a float<1. This audit does not refute that
boolean test. It distinguishes it from the quantitative norm factor.

The snapshot also opens `tailbound.json`, assigns its content to the unused
TB variable, and later actually reads `tailbound2.json`. A run directory
containing the documented required inputs but not the obsolete file will
raise FileNotFoundError before producing an off-basis bound. This is a
pipeline dependency defect, not a mathematical counterexample.

## The tail driver mixes the B and Bt decompositions

The aggregate Pcol correction in workerB is now correct: it uses the
column's actual sine coefficients and abs(pj).upper(). But part(c) calls
`colobj.green_on_cell`, which returns Bt_1=B_1-2c[h]exp(2t). Thus this
part uses

 U_tilde[h]=U[h]-c[h](-x,y),

rather than the physical U[h]. With this convention the normalized
operator is exactly

 (V.grad-1)h+U_tilde[h].grad rho+c[h]M,
 M=(-2x/3,4y/3).grad rho.

Equivalently, using plain B it is

 (V.grad-1)h+U[h].grad rho+(c[h]/3)X.grad rho.

The snapshot combines the first convention in part(c) with the second
convention in its joint part(d), which contains only (C/3)dR_rem and the
KP transport. It omits the term C(-x,y).grad rho. The difference is not
zero and not confined to retained angular modes.

For an exact local model rho=r cubed sin(29theta), direct differentiation
gives

 r^-3 (-x,y).grad rho=13 sin(31theta)-16 sin(27theta).

Both output modes are beyond the12 retained modes of S0. A smooth cutoff
can make this model compact in an annulus; on its constant region the
identity is unchanged. Thus the asserted term-by-term decomposition is
false independently of rounding or the magnitude of any final bound.

There is also a membership problem before any triangle estimate: on the
outer half-line Bt includes a linear-velocity term even for a compact
input. Against a leading density r^k Theta this creates an r^k image.
In the selected forcing norm with gamma<k, its squared radial integrand
is proportional to exp(2(k-gamma)t), which is not integrable. The required
cancellation is between this contribution and the missing part of cM.
Taking their norms separately is impermissible.

A consistent repair is to use canonical plain B for part(c) and retain
the radial-strain/KP cancellation already expressed in part(d). Plain B
should be produced by its canonical Green formula, as in ColumnFix,
rather than subtracting and then adding a ball constant, which can leave
a spurious nonintegrable exponent with a small interval coefficient.
Alternatively one must analytically combine all Bt and cM terms before
bounding or integrating. After either repair the full dropped-mode
bound needs a fresh audit.

The omission of ordinary transport-self terms from the dropped-mode
bound is harmless for the actual S0 dimensions because Mout>=Mh+1:
a column with angular label m has sine indices at most m+1. That dimension
condition must be imposed for any reuse of the driver. It is not a generic
identity for arbitrary Mh and Mout.

## Float tail inflation still needs a proved error budget

`up` in the tail driver is a nearest endpoint conversion. Some additions
use a multiplicative factor, `np.add.at` does not, and the final reduction
is multiplied by1+1e-8. A rigorous global allowance is possible if every
operation count and range is bounded. The snapshot gives only a comment,
not such a certificate. Relative-error reasoning also needs an underflow
analysis. For example a positive normal input2^-600 has a squared floating
value0; a subsequent finite multiplier leaves0 although the exact energy
is2^-1200>0. The independent check reproduces this.

This does not assert that the actual final S0 energy is underestimated by
that toy example. It refutes the unconditional claim that the implementation's
floats are outward upper bounds. Establish a complete range and count
bound, use directed operations including a positive subnormal allowance,
or retain interval arithmetic through the sums.

## Scope of a future finite certificate

The spatial L2 Gram formulas and the revised aggregate angular lookup
are confirmed. The exact inverse-Gram lower-bound identity and the
positive-definiteness test retain the scope proved in topics12 and17.
A finite singular-value certificate still needs fixed input/code hashes,
all-cell coverage, independent entry checks and successful guards. A
finite certificate supplies no quantitative control of the compact
remainder on the infinite complement and no closed physical strain
constraint. Those are distinct analytic questions, as topics28 and29
make explicit.
