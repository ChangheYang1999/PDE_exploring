# Exact quotient coordinates for the candidate007 generator span

## Statement

Fix c=4076476460239181/2251799813685248, gamma=1/c and
delta=1-gamma. For the2982 exact generators of candidate007, write

    G_i=H_m(1+r^2)^(p_j-m) P_i(t),
    p_j=(3+gamma-j delta)/2, H_m=Re(x+iy)^(2m),
    t=r^2/(1+r^2).

The supplied polynomials are t^w or t^w P_n(2t-1), with the usual
Legendre normalization P_n(1)=1. Every coefficient is variable.
The previously independently confirmed polynomial rank is1922, with
1060 exact zero-potential directions. This construction chooses1922
independent original generators, preferring Legendre columns when they
are available, and gives exact linear maps R:Q^2982->Q^1922 and
E:Q^1922->Q^2982 satisfying

    R E=I, chi(E R a)=chi(a), ker R=ker chi.

These identities hold for all real coefficient vectors too. The exact
reduced coefficients for007 therefore represent precisely the same
potential and density as the original snapshot. No optimization is
performed, and this is an unregistered coordinate artifact.

The preference for Legendre columns changes neither the rank nor the
span. It is not a condition-number guarantee. A binary64 rounding of the
new exact coefficients is a different function unless separately checked.
All original optimizer constraint matrices and their coordinate pivots
must be rebuilt for the selected generator list.

## Exact block elimination

Angular orthogonality separates m. Within a fixed(j,m), expand each
P_i in ordinary powers of t. The binomial identity

    P_n(2t-1)=sum_(k=0)^n (-1)^(n-k) binom(n,k)binom(n+k,k)t^k

is derived in ../basis_redundancy/PROOF.md. The code compares this with
the three-term Legendre recurrence. Order the columns with Legendre
columns first, then by degree and original index. Exact elimination
of the largest remaining polynomial degree either adds an independent
pivot polynomial or produces an identity

    G_j+sum_(i in P) r_(j,i)G_i=0

for a nonpivot index j. Every recorded relation is multiplied out and
checked coefficient by coefficient. It has coefficient1 in its own
nonpivot coordinate and no other nonpivot coordinate. Thus the1060
relations are linearly independent.

Set beta_i=a_i-sum_(j nonpivot) a_j r_(j,i), for each pivot i.
Substituting the relations into sum_i a_i G_i proves equality of the
potentials. Let E put beta in the pivot positions and zeros elsewhere.
The definition gives R E=I. The selected block polynomials are linearly
independent. Branches with different j cannot cancel because
(j-j')delta/2 is not an integer: after u=1-t, their finite radial sums
have disjoint exponent classes modulo integers. In any finite nonzero
sum, divide by its least u exponent and let u tend to zero; its leading
coefficient cannot vanish. This proves global independence, ker R=ker chi,
and the claimed rank1922. The arithmetic nonresonance is checked exactly.

All derivatives, background fields, residuals, weak rows and exact
normalization constraints are functions of chi, so equality of the
potential preserves them. The audited potential-to-density injectivity
T4-199/R1-024 further implies that these1922 coordinates give distinct
densities in the007 span. It gives no norm equivalence or inverse bound.

## Verification and use

The construction starts from the frozen raw007 generator file. It writes
a new generator file containing the selected original generator shapes
and their exact transformed rational coefficients. Source hashes,
selected original indices, complete kernel relations and every block
rank are retained. Rebuilding the potential polynomial map from both
the original and reduced lists must agree exactly with the previously
independently confirmed canonical007 JSON, coefficient by coefficient.
A second reduction must return the identical list and coefficients.

The helper supports a separate exact input only after checking its
format, absence of fixed coefficients, allowed generator specifications,
nonnegative integer indices and the required branch nonresonance.
The theorem's numerical dimension1922 refers specifically to007;
other input ranks are computed and reported, never copied. It writes to
an explicitly supplied directory and never imports optimizer code or
runs a floating matrix factorization.

This is a concrete exact coordinate reduction for a subsequent controlled
optimizer experiment. It cannot certify the finite Jacobian's smallest
singular value, the infinite-dimensional inverse, or nonlinear closure.
No improved residual or numerical stability is claimed from coordinate
reduction alone. The new choice of pivots and coefficient transformation
remain OPEN for an independent peer even though the underlying rank and
zero-potential dimension were already confirmed independently.
