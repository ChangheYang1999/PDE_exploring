# Exact membership in a finite analytic probe span

## Statement, notation and scope

For each positive odd integer n and integer K >= (n-1)/2, define on R2

 phi_(n,K)(r,theta) = r(1+r^2)^(-2) t^K sin(n theta),
 t=r^2/(1+r^2).

Let A be any finite set of distinct admissible pairs (n,K), and let W_A
be the real linear span of their analytic functions. Then all listed
functions are linearly independent. For any admissible (n0,K0),

 phi_(n0,K0) belongs to W_A if and only if (n0,K0) belongs to A.

The equality may be interpreted pointwise, almost everywhere, or as an
identity of distributions. This statement concerns the exact analytic
weak rows only. It does not assert statistical independence, independence
from sampled residuals or derivatives, a numerical condition number,
independence from other unrecorded optimizer information, or a bound on
the maximum of uncomputed tests.

The concrete proposed021 objective contains the67 rows accepted for016,
plus14 rows (n,(n-1)/2+s), n=19,21,...,31 and s=128,512. Conditional on
that exact recorded objective list and its inherited history, all25
previously registered pairs n in {19,23,25,29,31}, K in
{600,900,1200,1800,2400} are outside its span. Each of the21 diagnostic
pairs n=19,21,...,31, K=(n-1)/2+s, s=0,8,32 also lies outside. The
previous diagnostic (21,522) is now an objective row and is not held out.
No actual021 snapshot is bound by this preparatory theorem.

## Complete proof

For r>0 the factor b(r)=r(1+r^2)^(-2) is positive and t maps (0,infinity)
bijectively to (0,1). Consider a finite relation sum a_(n,K) phi_(n,K)=0.
Divide by b(r), multiply by sin(n0 theta), and integrate over one full
circle. Sine orthogonality gives

 sum_{K:(n0,K) in A} a_(n0,K) t^K = 0, 0<t<1.

A polynomial that vanishes on this interval is identically zero. For
completeness, if it were nonzero, factor its least nonzero power t^j.
The remaining polynomial has a nonzero limit at zero, contradicting
its vanishing for every positive t. Removing its least coefficient and
repeating proves every coefficient zero. Applying this separately to
each of the finitely many angular frequencies proves independence.
Appending a proposed probe whose pair is absent gives another independent
finite set, proving it cannot belong to W_A. The converse is its definition.

Each function is smooth at the origin: r^(2K+1) sin(n theta) equals
the degree-n harmonic polynomial Im(x+iy)^n multiplied by
(x^2+y^2)^(K-(n-1)/2), and the denominator (1+r^2)^(K+2) is positive
and smooth. Finite linear combinations are continuous. If such a
combination vanishes almost everywhere, continuity makes it vanish
everywhere. The same holds for a zero distribution represented by a
continuous function: a nonzero value has a neighborhood of constant
sign, where a nonnegative smooth test gives a nonzero pairing. Thus
all three meanings of equality yield the same conclusion.

For the proposed021 row set, the objective exponents in each mode
n=19,...,31 are exactly (n-1)/2+128 and (n-1)/2+512, lying respectively
in[137,143] and[521,527]. Every registered exponent is at least600.
The additional diagnostic exponents lie in[9,47], disjoint from both
ranges. The finite-set theorem proves all46 stated separations even
though the angular modes now overlap objective modes. In contrast,
(21,522) equals (21,(21-1)/2+512) and is a row. Earlier recorded
ancestor stages used only a subset of the67 old rows, so adding those
histories does not enlarge the81-row span. An actual run must still be
checked against this exact history, row set and source hashes.

## Exact verification and dependencies

The checker freezes the accepted016 objective result and every bound
input, the public25-pair register, and current N1 launch scripts and
notes as text. It parses the actual proposed launch arguments without
executing publisher code. Check81 distinct admissible rows, the exact
14-row difference, all46 pairwise separations and the newly included
(21,522). For comparison the proposed022 script still has the67 old
rows, so its25 registered and35 original high-mode probes are separated
by angular frequency. A launcher or note does not certify the actual
completed candidate. Its immutable coefficient metadata and finished
log must be bound in the subsequent candidate audit.

The polynomial and Fourier arguments above are complete informal proofs.
The finite checker validates the stated row lists and exact arithmetic;
it does not infer historical bytes from a current source timestamp.
The public25-pair register predates both proposed runs. The new N1 note
is dated08:33Z and describes launches at08:32Z, so this theorem does not
call that note a record predating launch. It supplies no residual norm,
PDE inverse or existence result. Full weak-distance hypotheses are in
../joint_scaled_factored_weak/PROOF.md.
