# Independent whole-plane norms for the exact scale-25 candidate

Written 2026-10-29T10:29:46.611611+00:00, before this topic's comparison code. The
numerical assertions remain OPEN until the specified checks finish.
This proof defines what an accepted comparison establishes.

## Statement, reference and spaces

Fix

    c = 4076476460239181 / 2251799813685248,
    delta = 1 - 1/c = 1824676646553933 / 4076476460239181.

Let chi be the finite exact generator sum in the immutable candidate
C1-N1-016-legqs25-quot013. Its raw JSON has SHA256
 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Every coefficient and scale is interpreted as the exact rational number
in that file. Define on the full plane

    rho = -partial_y Delta chi,
    psi = partial_x partial_y chi,
    u = (-partial_y psi, partial_x psi),
    F = (c X + u) dot grad rho - rho.

All functions are the smooth extensions of these finite generators to
the origin. The unweighted norms use Lebesgue measure dx dy. The four
quantities to be enclosed are

    G0 = ||F||_2,
    rF = || |X| F ||_2,
    G1 = (||partial_x F||_2^2 + ||partial_y F||_2^2)^(1/2),
    P2 = ||(1 + 4|X|^2)^(2/5) D^2 F||_2.

Here D^2 F is the full ordered Cartesian Hessian. Thus its squared
pointwise norm is F_xx^2 + 2 F_xy^2 + F_yy^2. The symbol rF names a
norm; it is not a new residual. These claims require no inverse theorem
and imply neither residual smallness nor existence of a solution.

For each completed norm, the algorithm below produces an outward real
interval containing that quantity, provided all its exact identities,
integrability tests and finite-ball operations pass. The final
comparison only accepts norms for which both actual computations are
complete. A running record is not evidence for unfinished norms.

## Exact fields, angular products and derivatives

Put t=r^2/(1+r^2), v=1-t and w=v^(delta/2). For a derivative of order d,
use the representation

    H_d = R_d sum_(ell,k,n) w^ell A_(ell,k,n)(t) T_(k,n)(theta),
    R_d = r v^(d/2) if d is even,
    R_d = v^((d-1)/2) if d is odd,
    T_(c,n)=cos(n theta), T_(s,n)=sin(n theta).

The coefficients A are rational functions P(t)/D(t) with exact
rational-polynomial numerators and

    D(t) = product_a (1+a(1-t))^N_a,   a>0, N_a>=0.

For this reference only a=624 occurs, apart from absent factors. The
generic implementation also supports the other positive scales stated
in its dependency proof. Every denominator is positive on [0,1].
Consequently exact common-denominator addition preserves the function
without introducing a pole on the integration interval.

The generator-jet formulas, compact derivative formulas and Laurent
product theorem in ../scaled_product_norms/PROOF.md apply to these
exact generators. For completeness, in a cosine-times-sine product,
encode cos(n theta) by (z^n+z^-n)/2 and sin(n theta) by
(z^n-z^-n)/(2i). After clearing negative powers, their product is
antisymmetric about the sum of the two angular centers. If its positive
coefficient polynomial is H_n, the sine coefficient is H_n/2 after
restoring the two common radial denominators. The central coefficient
must vanish, and the negative coefficient must be -H_n. Packing
z^j t^k as Z^(s j+k) is exact if the stride s exceeds the sum of the two
maximum radial degrees. This strict inequality prevents carries between
angular blocks in multiplication. The implementation tests the stride,
central zero and every negative-positive coefficient identity.

Apply this product to u_1 rho_x and u_2 rho_y. The linear term follows
from r partial_r t=2tv and r partial_r w=-delta t w:

    (c r partial_r - 1)(r w^ell A)
      = r w^ell {c[(1-ell delta t)A+2tv A']-A}.

The prime differentiates the complete rational function. Thus the
constructed field is precisely F above. The derivative recurrence in
the dependency proof follows from the same identities and
partial_x=cos(theta) partial_r-sin(theta) r^-1 partial_theta,
partial_y=sin(theta) partial_r+cos(theta) r^-1 partial_theta.
It includes derivatives of every scale factor. Any division by t in an
odd-order angular term must have exact zero remainder; otherwise the
computation fails. Two routes to F_xy must agree exactly.

Independent Cartesian jets of chi through order six provide 33 value
comparisons: F and its five first/second derivatives, together with
rho,u_1,u_2,rho_x,rho_y, at each of (3/7,-2/5), (21,-9), (3/10,70).
These values detect implementation errors; isolated value agreement is
not substituted for the exact algebraic derivation above.

## Whole-plane radial integrals

Different Fourier modes and sine/cosine kinds are orthogonal. A
nonconstant sine or cosine square integrates to pi, while the constant
cosine square integrates to 2pi. Expand every ordered branch pair of
each fixed mode and kind. For the d-th derivative tensor, multiply the
component partial_x^a partial_y^(d-a) by binomial(d,a) in the squared
norm. This gives the factor two for F_xy in the Hessian.

Let Q_E(t) be the complete rational coefficient of the angular square
sum at branch sum E, with the constant-cosine factor already included.
The contribution before radial integration is not asserted positive
for each E separately. Their total is the nonnegative tensor square.
Since r dr=dt/(2v^2), R_d^2=t^epsilon v^(d-1), where epsilon is one for
even d and zero for odd d, the unweighted squared norm is

    (pi/2) sum_E integral_0^1
       v^(d-3+E delta/2) (1-v)^epsilon Q_E(1-v) dv.

For rF add the weight r^2=t/v. It increases the numerator t power by
one and decreases the exponent of v by one. For P2 add

    (1+4r^2)^(4/5) = (1+3t)^(4/5) v^(-4/5).

For each complete Q_E multiply the indicated numerator factors, replace
t by 1-v, and factor out every exact power v^q from its numerator. The
remaining integral is

    integral_0^1 v^b P(v) / product_a(1+a v)^N_a dv,
    b = d-3+E delta/2 + shift + q.

The computation must prove b>-1 for every nonzero group. The remaining
numerator is polynomial and every denominator is bounded away from
zero; this proves absolute integrability of that group at both ends.
There are finitely many groups, so termwise integration is legitimate.
This sufficient group test makes no claim about a failed case in which
further cancellation could restore integrability.

The exact partial-fraction and moment theorem in
../rational_pole_moments/PROOF.md evaluates each proper integral by
rational arithmetic and Arb enclosures of Euler hypergeometric
integrals. Its hypotheses include positive scales and b>-1. Every
recorded decomposition identity must pass; all balls and sums must be
finite. No analytic continuation is assigned an integral meaning.
There is no radial or angular quadrature, cutoff radius or omitted tail.

For the P2 factor put z=(3t-3/2)/(5/2), so |z|<=3/5, and write

    (1+3t)^(4/5) = (5/2)^(4/5) (1+z)^(4/5).

Let W=sum_(j=0)^56 binomial(4/5,j) z^j. The binomial series converges
absolutely on this interval. Starting at j=57, the ratio of successive
absolute terms is at most 3/5, because |(4/5-j)/(j+1)|<1. Therefore

    |(1+z)^(4/5)-W| <= eps,
    eps = |binomial(4/5,57)| (3/5)^57 / (2/5).

Multiply W-eps <= (1+z)^(4/5) <= W+eps by the full nonnegative Hessian
square density, including v^(-4/5), then integrate. If S is the complete
radial integral of that density and T includes W, then

    P2^2 belongs to (pi/2)(5/2)^(4/5)[T-eps S, T+eps S].

Computing S and T via signed groups is legitimate because the pointwise
inequality was applied to their total. The final S and both squared
bounds must be strictly positive. Monotonicity of the square root then
provides the norm bounds. Unweighted norms use the same rule with
eps=0 and T=S.

## N3 representation, source audit and calibration scope

N3's canonical tuple-key representation is the same rational Fourier
field, with the scale powers in the tuple rather than a coefficient
object. Its unordered angular pairs carry multiplicity two off the
diagonal and a factor 1/2 for the radial Jacobian. Thus N3's final pi
factor and N4's final pi/2 factor represent the same integral. N3
extracts endpoint zeros from each canonical field before squaring;
N4 extracts them after combining a complete branch-sum group. The
numbers of groups and denominator powers may therefore differ.
Neither equality of their group counts nor equality of unreduced
polynomial fingerprints is required.

The actual N3 production file is frozen under
source/legqs_norms.py, SHA256
17bfbf4ae96e9db94adb34a220137d38c4da92ae7612ff73c053e9b259c97ca8.
It is older than the source used by the subsequent admissible
calibration N4-302. Three other production modules are byte-identical
to that calibration. The saved complete diff identifies these changes:

* The old I0 cache key omits precision. The actual production run uses
  the same precision, 1024 bits, for every call sharing this cache, so
  this omission causes no precision mix in that run.
* The old accumulator adds the rational R1 from each class as an Arb
  ball. The newer source first combines all these rational constants
  exactly. Both operations enclose the exact sum; the old description
  that every cancellation is exact is too strong across classes.
* The newer source adds finiteness assertions and radius diagnostics.
  Absence of those assertions in the older file is not evidence that
  its output is finite. The comparison must explicitly check that.

N4-300 found inadmissible exponents and divergent examples in the old
calibration test, not a missing b>-1 guard in production's accumulator.
N4-301 found a duplicated panel in a quadrature calibration. Actual
production uses no quadrature. Its source has not been called a repaired
quadrature run. The relevant replacement evidence is N4-302's 2383
admissible moment/small-field checks, N4-305's complete six-generator
field/norm fixture, N4-308's exact packed-product fixture, and the actual
independent reconstruction and completed norms required here.

## Comparison and accepted precision

Bind both records to the identical raw SHA256 and exact c and delta,
and bind each record's complete source dependency graph. Audit the
actual completed norm's label, weights, derivative order and precision.
All own Cartesian comparisons, positive denominators, endpoint tests,
partial-fraction identities and finite sums must pass.

For an own completed norm, let L and U be the recorded outward balls
for its lower and upper bounds. The true norm lies between the lower
endpoint of L and the upper endpoint of U. Select rational decimal
endpoints l,u strictly outside those endpoints; this yields an explicit
accepted interval [l,u]. Require also that N3's displayed outward norm
balls are finite and consistent with this accepted interval and with
the own bounds. For unweighted norms the full own interval must lie
inside the hull of N3's displayed lower and upper norm balls. For P2,
compare the lower and upper bound balls separately, since the binomial
remainder intentionally leaves a gap between the two bounds.

The printed 40-digit N3 balls are wider than its internal 1024-bit
endpoints. The own saved 100-digit balls are wider than its internal
2048-bit endpoints. Overlap of printed balls does not reproduce all
internal bits and is not alone an interval proof. The proof of the
accepted decimal enclosure comes from the complete independent own
calculation and outward comparisons. Claims will use the explicit
accepted interval, not unverified extra digits of either internal
endpoint. Full 1024-bit endpoint reproduction remains OPEN unless
separately performed at sufficient retained precision.

## Dependencies and limits

Required dependencies are the exact generator and product theorem in
../scaled_product_norms/PROOF.md, the positive-pole integral theorem in
../rational_pole_moments/PROOF.md, the Cartesian jet derivation in
../multiscale_generators, and the exact fixtures and input hashes
recorded with N4-302, N4-305 and N4-308. These are local exact-code and
Arb verifications, not a Lean formalization.

A passed G0 comparison certifies G0 only. The same applies separately
to rF, G1 and P2. This topic does not compute the homogeneous negative
Sobolev norm H or an E2 closure constant, and rF is not substituted for
H. No result here changes the fixed-c distance exclusions or establishes
an inverse estimate, contraction, existence or an exact solution.
